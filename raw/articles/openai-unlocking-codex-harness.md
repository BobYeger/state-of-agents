Title: Membuka harness Codex: bagaimana kami membangun App Server

URL Source: https://openai.com/id-ID/index/unlocking-the-codex-harness/

Markdown Content:
Dalam postingan ini, kami akan memperkenalkan Codex App Server; kami juga akan membagikan pembelajaran kami sejauh ini tentang cara terbaik menghadirkan kemampuan Codex ke dalam produk Anda guna membantu para pengguna meningkatkan alur kerja mereka secara signifikan. Kami akan membahas arsitektur dan protokol App Server serta bagaimana integrasinya dengan berbagai permukaan Codex, sekaligus memberikan kiat untuk memanfaatkan Codex—baik jika Anda ingin menjadikannya peninjau kode, agen SRE, maupun asisten pengodean.

## Asal Server Aplikasi

Sebelum mendalami arsitektur, akan sangat membantu untuk memahami latar belakang App Server. Pada awalnya, App Server merupakan cara praktis untuk menggunakan kembali harness Codex di berbagai produk, yang kemudian secara bertahap berkembang menjadi protokol standar kami.

Codex CLI dimulai sebagai TUI (antarmuka pengguna terminal), yang berarti Codex diakses melalui terminal. Ketika kami membangun ekstensi VS Code (cara yang lebih ramah IDE untuk berinteraksi dengan agen Codex), kami memerlukan cara untuk menggunakan harness yang sama agar dapat menjalankan loop agen yang identik dari antarmuka pengguna IDE tanpa perlu mengimplementasikannya ulang. Hal ini menuntut dukungan pola interaksi yang kaya di luar request/response, seperti menjelajahi workspace, menyiarkan kemajuan saat agen bernalar, dan mengeluarkan perbedaan. Kami pertama kali bereksperimen dengan mengekspos [Codex sebagai server MCP⁠(terbuka di jendela baru)](https://github.com/openai/codex/pull/2264), tetapi mempertahankan semantik MCP dengan cara yang masuk akal untuk VS Code terbukti sulit. Sebagai gantinya, kami memperkenalkan protokol JSON-RPC yang mencerminkan loop TUI, yang kemudian menjadi [versi pertama tidak resmi⁠(terbuka di jendela baru)](https://github.com/openai/codex/pull/4471) dari App Server. Pada saat itu, kami tidak mengharapkan klien lain bergantung pada App Server, sehingga App Server belum dirancang sebagai API yang stabil.

Seiring adopsi Codex meningkat dalam beberapa bulan berikutnya, tim internal maupun mitra eksternal menginginkan kemampuan untuk menyematkan harness yang sama ke dalam produk mereka sendiri guna mempercepat alur kerja pengembangan perangkat lunak para pengguna. Sebagai contoh, JetBrains dan Xcode menginginkan pengalaman agen setingkat IDE, sementara aplikasi desktop Codex perlu mengorkestrasi banyak agen Codex secara paralel. Kebutuhan tersebut mendorong kami untuk merancang permukaan platform yang dapat diandalkan oleh produk kami dan integrasi mitra secara aman dari waktu ke waktu. Permukaan ini harus mudah diintegrasikan dan kompatibel ke belakang, sehingga kami dapat mengembangkan protokol tanpa merusak klien yang sudah ada.

Selanjutnya, kami akan memandu Anda melalui cara kami merancang arsitektur dan protokol agar klien yang berbeda dapat menggunakan harness yang sama.

## Di dalam harness Codex

Pertama, mari kita fokus pada apa saja yang terdapat di dalam harness Codex dan bagaimana Codex App Server mengeksposnya kepada klien. Dalam [blog](https://openai.com/id-ID/index/unrolling-the-codex-agent-loop/) Codex terbaru kami, kami menguraikan loop agen inti yang mengorkestrasi interaksi antara pengguna, model, dan alat-alat. Ini merupakan logika inti dari harness Codex, namun masih ada lebih banyak komponen yang diperlukan untuk menghadirkan pengalaman agen yang lengkap:

**1. Siklus hidup dan ketahanan thread**. Sebuah utas adalah percakapan Codex antara pengguna dan agen Codex. Codex dapat membuat, melanjutkan, melakukan fork, dan mengarsipkan utas, serta menyimpan riwayat peristiwa agar klien dapat tersambung kembali dan merender linimasa yang konsisten.

**2. Konfigurasi dan autentikasi**. Codex memuat konfigurasi, mengelola pengaturan default, dan menjalankan alur autentikasi seperti “Masuk dengan ChatGPT,” termasuk status kredensial.

**3. Pelaksanaan alat dan ekstensi**. Codex mengeksekusi alat shell/file di dalam sandbox dan menghubungkan integrasi seperti server MCP serta keterampilan agar dapat berpartisipasi dalam loop agen di bawah model kebijakan yang konsisten.

Seluruh logika agen yang kami sebutkan di sini, termasuk loop agen inti, berada pada bagian codebase Codex CLI yang disebut “[Codex core⁠(terbuka di jendela baru)](https://github.com/openai/codex/tree/main/codex-rs/core).” Codex core merupakan sebuah library tempat seluruh kode agen berada, sekaligus sebuah runtime yang dapat diaktifkan untuk menjalankan loop agen dan mengelola persistensi satu thread Codex (percakapan).

Agar dapat digunakan secara efektif, harness Codex perlu dapat diakses oleh klien. Di sinilah App Server berperan.

App Server adalah protokol JSON-RPC antara klien dan server, sekaligus sebuah proses jangka panjang yang mengelola thread inti Codex. Seperti yang terlihat pada diagram di atas, sebuah proses App Server memiliki empat komponen utama: pembaca stdio, pemroses pesan Codex, pengelola utas, dan utas inti. Pengelola utas memulai satu sesi inti untuk setiap utas, lalu pemroses pesan Codex berkomunikasi langsung dengan setiap sesi inti untuk mengirimkan permintaan klien dan menerima pembaruan.

Satu permintaan klien dapat menghasilkan banyak pembaruan peristiwa, dan peristiwa terperinci inilah yang memungkinkan kami membangun antarmuka pengguna yang kaya di atas App Server. Selain itu, pembaca stdio dan pemroses pesan Codex berfungsi sebagai lapisan penerjemahan antara klien dan thread inti Codex. Keduanya menerjemahkan permintaan JSON-RPC klien menjadi operasi inti Codex, mendengarkan aliran peristiwa internal inti Codex, lalu mengubah peristiwa tingkat rendah tersebut menjadi sekumpulan kecil notifikasi JSON-RPC yang stabil dan siap digunakan oleh antarmuka pengguna.

Protokol JSON-RPC antara klien dan App Server sepenuhnya bersifat dua arah. Sebuah utas yang khas mencakup permintaan klien dan banyak notifikasi dari server. Selain itu, server dapat memulai permintaan ketika agen memerlukan input, seperti persetujuan, lalu menjeda giliran hingga klien memberikan respons.

## Prinsip dasar percakapan

Selanjutnya, kami akan menguraikan primitif percakapan, yaitu elemen dasar dari protokol App Server. Merancang API untuk loop agen memang rumit karena interaksi pengguna/agen bukanlah permintaan–respons yang sederhana. Satu permintaan pengguna dapat berkembang menjadi urutan tindakan terstruktur yang perlu direpresentasikan secara setia oleh klien, termasuk masukan pengguna, kemajuan bertahap agen, serta artefak yang dihasilkan sepanjang proses (misalnya, perbedaan). Untuk membuat aliran interaksi tersebut mudah diintegrasikan dan tangguh di berbagai antarmuka pengguna, kami menetapkan tiga primitif inti dengan batasan dan siklus hidup yang jelas:

**1. Item:**Item adalah unit atomik dari masukan/keluaran di Codex. Item dikategorikan (misalnya, pesan pengguna, pesan agen, eksekusi alat, permintaan persetujuan, diff) dan masing-masing memiliki siklus hidup yang jelas:

*   `item/started` ketika item dimulai
*   peristiwa `item/*/delta` opsional sebagai aliran konten (untuk jenis item streaming)
*   `item/completed` ketika item diselesaikan dengan payload terminalnya

Siklus ini memungkinkan klien untuk mulai merender segera pada `started`, melakukan streaming pembaruan secara bertahap pada `delta`, dan menyelesaikannya pada `completed`.

**2. Giliran**: Satu giliran adalah satu unit kerja agen yang dimulai oleh input pengguna. Proses dimulai ketika klien mengirimkan input (misalnya, “jalankan pengujian dan rangkum kegagalan”) dan berakhir ketika agen selesai menghasilkan output untuk input tersebut. Satu giliran berisi serangkaian item yang merepresentasikan langkah-langkah antara serta output yang dihasilkan sepanjang proses.

**3. Utas**: Utas adalah wadah yang tahan lama untuk sesi Codex yang sedang berlangsung antara pengguna dan agen. Utas berisi beberapa giliran. Utas dapat dibuat, dilanjutkan, dipecah, dan diarsipkan. Riwayat utas disimpan sehingga klien dapat terhubung kembali dan menampilkan linimasa yang konsisten.

Sekarang, kami akan melihat percakapan yang disederhanakan antara klien dan agen, di mana percakapan tersebut direpresentasikan oleh primitif-primitif berikut:

Pada awal percakapan, klien dan server perlu memulai jabat tangan `initialize`. Klien harus mengirimkan satu permintaan `initialize` sebelum metode lainnya, dan server akan mengakuinya dengan sebuah respons. Ini memberi server kesempatan untuk mengiklankan kapabilitas serta memungkinkan kedua belah pihak menyepakati versi protokol, bendera fitur, dan pengaturan default sebelum pekerjaan sebenarnya dimulai. Berikut adalah contoh payload dari ekstensi VS Code OpenAI:

Inilah yang dikembalikan oleh server:

Ketika klien membuat permintaan baru, sistem akan terlebih dahulu membuat thread lalu membuat giliran. Server kemudian akan mengirimkan notifikasi kemajuan (`thread/started` dan `turn/started`). Server juga akan mengirimkan kembali masukan yang didaftarkannya sebagai item, seperti pesan pengguna pada contoh ini.

Pemanggilan alat juga dikirimkan kembali kepada klien sebagai item. Selain itu, server dapat meminta persetujuan klien sebelum dapat menjalankan suatu tindakan dengan mengirimkan permintaan dari server. Proses persetujuan akan menunda giliran hingga klien membalas dengan “izinkan” atau “tolak.” Berikut adalah tampilan alur persetujuan di ekstensi VS Code:


Pada akhirnya, server mengirimkan pesan agen lalu mengakhiri giliran dengan `turn/completed`. Peristiwa delta pada pesan agen mengalirkan potongan-potongan pesan kembali hingga pesan tersebut diselesaikan dengan `item/completed`.

Pesan-pesan dalam diagram disederhanakan supaya lebih mudah dibaca. Jika Anda ingin melihat JSON untuk satu giliran penuh, Anda dapat menjalankan klien pengujian dari repositori Codex CLI:

## Mengintegrasikan dengan klien

Sekarang, mari kita lihat bagaimana berbagai antarmuka klien menyematkan Codex melalui App Server. Kami akan membahas tiga pola: aplikasi lokal dan IDE, runtime web Codex, serta TUI.

Di ketiganya, transport yang digunakan adalah JSON-RPC melalui stdio (JSONL). JSON-RPC memudahkan pembangunan binding klien dalam bahasa pilihan Anda. Permukaan Codex dan integrasi mitra telah mengimplementasikan klien App Server dalam berbagai bahasa, termasuk Go, Python, TypeScript, Swift, dan Kotlin. Untuk TypeScript, Anda dapat menghasilkan definisi langsung dari protokol Rust dengan menjalankan:

Untuk bahasa lain, Anda dapat membuat bundel Skema JSON dan memasukkannya ke dalam generator kode pilihan Anda dengan menjalankan:


Klien lokal biasanya membundel atau mengambil biner App Server khusus platform, meluncurkannya sebagai proses anak yang berjalan lama, dan menjaga saluran stdio dua arah tetap terbuka untuk JSON-RPC. Dalam ekstensi VS Code dan Aplikasi Desktop kami, misalnya, artefak yang dikirimkan mencakup biner Codex khusus platform yang dipatok ke versi yang telah diuji, sehingga klien selalu menjalankan bit yang persis sama dengan yang telah kami validasi.

Tidak semua integrasi dapat mengirimkan pembaruan klien dengan frekuensi tinggi. Beberapa mitra, seperti Xcode, memisahkan siklus rilis dengan menjaga klien tetap stabil dan memungkinkannya untuk menunjuk ke biner App Server yang lebih baru saat diperlukan. Dengan pendekatan ini, mereka dapat mengadopsi peningkatan di sisi server (misalnya, auto-compaction yang lebih baik di inti Codex atau kunci konfigurasi yang baru didukung) serta meluncurkan perbaikan bug tanpa harus menunggu rilis klien. Permukaan JSON-RPC App Server dirancang agar kompatibel ke belakang, sehingga klien lama dapat berkomunikasi dengan server baru secara aman.


Codex Web menggunakan harness Codex, tetapi menjalankannya dalam lingkungan kontainer. Seorang pekerja menyediakan sebuah kontainer dengan workspace yang telah di-check out, meluncurkan biner App Server di dalamnya, dan mempertahankan saluran JSON-RPC berumur panjang melalui stdio[2](https://openai.com/id-ID/index/unlocking-the-codex-harness/#citation-bottom-2). Aplikasi web (yang berjalan di tab browser pengguna) berkomunikasi dengan backend Codex melalui HTTP dan SSE, yang mengalirkan peristiwa tugas yang dihasilkan oleh pekerja. Pendekatan ini menjaga antarmuka pengguna sisi browser tetap ringan sekaligus menyediakan runtime yang konsisten di seluruh desktop dan web.

Karena sesi web bersifat sementara (misalnya tab ditutup atau jaringan terputus), aplikasi web tidak dapat menjadi sumber kebenaran untuk tugas yang berlangsung lama. Dengan menyimpan status dan kemajuan di server, pekerjaan dapat terus berjalan meskipun tab menghilang. Protokol streaming serta sesi thread yang disimpan memudahkan sesi baru untuk tersambung kembali, melanjutkan dari titik terakhir, dan mengejar ketertinggalan tanpa harus membangun ulang status di sisi klien.


Secara historis, TUI merupakan klien “native” yang berjalan dalam proses yang sama dengan loop agen dan berkomunikasi langsung dengan tipe inti Rust, alih-alih melalui protokol app-server. Pendekatan ini membuat iterasi awal menjadi cepat, tetapi juga menjadikan TUI sebagai permukaan dengan kasus khusus.

Sekarang setelah App Server tersedia, kami berencana untuk [memfaktorkan ulang TUI⁠(terbuka di jendela baru)](https://github.com/openai/codex/pull/10192) agar menggunakannya sehingga TUI berperilaku seperti klien lainnya: meluncurkan proses anak App Server, berkomunikasi menggunakan JSON-RPC melalui stdio, serta merender peristiwa streaming dan alur persetujuan yang sama. Hal ini membuka alur kerja di mana TUI dapat terhubung ke server Codex yang berjalan di mesin jarak jauh, menjaga agen tetap dekat dengan sumber komputasi dan memungkinkan pekerjaan berlanjut meskipun laptop dalam keadaan tidur atau terputus, sambil tetap menyediakan pembaruan langsung dan kontrol secara lokal.

## Memilih protokol yang tepat

Codex App Server akan menjadi metode integrasi kelas satu yang akan kami pertahankan ke depannya, namun terdapat juga metode lain dengan fungsionalitas yang lebih terbatas. Secara default, kami merekomendasikan agar klien menggunakan Codex App Server untuk berintegrasi dengan Codex, tetapi penting untuk meninjau berbagai metode integrasi dan memahami kelebihan serta kekurangannya. Berikut adalah cara paling umum untuk menjalankan Codex dan kapan masing-masing pendekatan mungkin sesuai.

Jalankan [`codex mcp-server`⁠(terbuka di jendela baru)](https://developers.openai.com/codex/guides/agents-sdk/) dan hubungkan dari klien MCP mana pun yang mendukung server stdio (misalnya, [OpenAI Agents SDK⁠(terbuka di jendela baru)](https://openai.github.io/openai-agents-js/)). Ini merupakan pilihan yang baik jika Anda sudah memiliki alur kerja berbasis MCP dan ingin menggunakan Codex sebagai alat yang dapat dipanggil. Kekurangannya adalah Anda hanya mendapatkan apa yang diekspos oleh MCP, sehingga interaksi khusus Codex yang bergantung pada semantik sesi yang lebih kaya (misalnya, pembaruan perbedaan) mungkin tidak dapat dipetakan secara rapi melalui endpoint MCP.

Beberapa ekosistem menawarkan antarmuka portabel yang dapat menargetkan berbagai penyedia model dan runtime. Ini dapat menjadi pilihan yang baik jika Anda menginginkan satu abstraksi untuk mengoordinasikan beberapa agen. Komprominya adalah bahwa protokol-protokol ini sering kali berkonvergensi pada subset kapabilitas yang umum, sehingga interaksi yang lebih kaya menjadi lebih sulit direpresentasikan, terutama ketika semantik alat dan sesi yang spesifik per penyedia menjadi penting. Ruang ini berkembang dengan cepat, dan kami memperkirakan lebih banyak standar umum akan muncul seiring kami terus mencari primitif terbaik untuk merepresentasikan alur kerja agen di dunia nyata ([skills⁠(terbuka di jendela baru)](https://agentskills.io/home) adalah contoh yang baik untuk hal ini).

Pilih App Server ketika Anda menginginkan harness Codex lengkap diekspos sebagai aliran peristiwa yang stabil dan ramah bagi antarmuka pengguna. Dengan pendekatan ini, Anda memperoleh fungsionalitas penuh dari loop agen serta fitur pendukung lainnya, seperti Masuk dengan ChatGPT, penemuan model, dan manajemen konfigurasi. Biaya utamanya adalah pekerjaan integrasi, karena Anda perlu membangun binding JSON-RPC di sisi klien dalam bahasa yang Anda gunakan. Namun, dalam praktiknya, Codex mampu menangani banyak pekerjaan berat jika Anda menyediakan skema JSON dan dokumentasi. Banyak tim yang bekerja sama dengan kami dapat dengan cepat membangun integrasi yang berfungsi menggunakan Codex.

Mode CLI yang ringan dan dapat diprogram untuk tugas satu kali serta eksekusi CI. Mode ini sangat cocok untuk otomatisasi dan pipeline, di mana Anda menginginkan satu perintah yang dijalankan hingga selesai secara non-interaktif, mengalirkan output terstruktur untuk log, dan keluar dengan sinyal keberhasilan atau kegagalan yang jelas.

Pustaka TypeScript untuk mengontrol agen Codex lokal secara terprogram dari dalam aplikasi Anda sendiri. Ini paling sesuai ketika Anda menginginkan antarmuka pustaka native untuk alat dan alur kerja sisi server tanpa perlu membangun klien JSON-RPC terpisah. Karena dirilis lebih awal daripada App Server, saat ini pustaka ini mendukung lebih sedikit bahasa dan memiliki cakupan yang lebih terbatas. Jika terdapat minat dari pengembang, kami mungkin akan menambahkan SDK tambahan yang membungkus protokol App Server sehingga tim dapat menjangkau lebih banyak permukaan harness tanpa harus menulis binding JSON-RPC.

## Melanjutkan ini

Dalam postingan ini, kami membagikan pendekatan kami dalam merancang standar baru untuk berinteraksi dengan agen serta cara mengubah harness Codex menjadi protokol yang stabil dan ramah klien. Kami membahas bagaimana App Server mengekspos inti Codex, memungkinkan klien mengendalikan loop agen secara penuh, dan mendukung beragam antarmuka, termasuk TUI, integrasi IDE lokal, serta runtime web.

Jika hal ini memunculkan ide untuk mengintegrasikan Codex ke dalam alur kerja Anda sendiri, ada baiknya mencoba App Server. Seluruh kode sumber tersedia di repo open-source Codex CLI [repo⁠(terbuka di jendela baru)](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md). Silakan bagikan masukan dan permintaan fitur Anda. Kami sangat antusias mendengar dari Anda dan terus berupaya membuat agen lebih mudah diakses oleh semua orang.
