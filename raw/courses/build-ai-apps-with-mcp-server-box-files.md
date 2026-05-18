Title: Build AI Apps with MCP Server: Working with Box Files

URL Source: https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/information

Markdown Content:
# Build AI Apps with MCP Server: Working with Box Files - DeepLearning.AI

✨ New course! Enroll in [Transformers in Practice](https://bit.ly/4nGXQoF)

[![Image 2: DeepLearning.AI](https://dlai-learn.deeplearning.ai/_next/image?url=%2Fdlai%2Fassets%2Fdlai-logo.png&w=640&q=75&dpl=dpl_WW5rMdym78ZyVbHzEGs4bw3Cmidc)](https://www.deeplearning.ai/)

[Explore Courses](https://learn.deeplearning.ai/courses)

AI Newsletter

*   [The Batch](https://www.deeplearning.ai/the-batch/)
*   [Andrew's Letter](https://www.deeplearning.ai/the-batch/tag/letters/)
*   [Data Points](https://www.deeplearning.ai/the-batch/tag/data-points/)
*   [ML Research](https://www.deeplearning.ai/the-batch/tag/research/)
*   [Blog](https://www.deeplearning.ai/blog/)

Community

*   [Forum](https://community.deeplearning.ai/)
*   [Events](https://www.deeplearning.ai/events/)
*   [Ambassadors](https://www.deeplearning.ai/ambassador/)
*   [Ambassador Spotlight](https://www.deeplearning.ai/blog/category/ambassador-spotlight/)
*   [Resources](https://www.deeplearning.ai/resources/)

[Membership](https://learn.deeplearning.ai/membership)[Start Learning](https://learn.deeplearning.ai/my/learning)

*   [Explore Courses](https://learn.deeplearning.ai/courses)
*   
AI Newsletter
    *   [The Batch](https://www.deeplearning.ai/the-batch/)
    *   [Andrew's Letter](https://www.deeplearning.ai/the-batch/tag/letters/)
    *   [Data Points](https://www.deeplearning.ai/the-batch/tag/data-points/)
    *   [ML Research](https://www.deeplearning.ai/the-batch/tag/research/)
    *   [Blog](https://www.deeplearning.ai/blog/)

*   
Community
    *   [Forum](https://community.deeplearning.ai/)
    *   [Events](https://www.deeplearning.ai/events/)
    *   [Ambassadors](https://www.deeplearning.ai/ambassador/)
    *   [Ambassador Spotlight](https://www.deeplearning.ai/blog/category/ambassador-spotlight/)
    *   [Resources](https://www.deeplearning.ai/resources/)

*   [Membership](https://learn.deeplearning.ai/membership)
*   [Start Learning](https://learn.deeplearning.ai/my/learning)

*   [Overview](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/information#overview)
*   [Course Outline](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/information#course-outline)
*   [Instructors](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/information#instructors)


1.   [All Courses](https://learn.deeplearning.ai/courses)
2.   [Short Course](https://learn.deeplearning.ai/courses?types=short_course)
3.   Build AI Apps with MCP Server: Working with Box Files

1.   [All Courses](https://learn.deeplearning.ai/courses)
2.   [Short Course](https://learn.deeplearning.ai/courses?types=short_course)
3.   Build AI Apps with MCP Server: Working with Box Files

Short Course Intermediate 36 mins

# Build AI Apps with MCP Server: Working with Box Files

Instructor:Ben Kus

[![Image 4: Box logo](https://dlai-learn.deeplearning.ai/_next/image?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2025%2F09%2FBox-Logo-01.png&w=384&q=75)](https://box.com/)

Earn an accomplishment with[PRO](https://learn.deeplearning.ai/membership)

[Enroll for Free](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files?utm_source=home&utm_medium=course-landing-page&utm_campaign=summary-cta-button)

[Video 2](https://www.youtube.com/watch?v=sFZZqsgBxiE)


*   Intermediate
*   36 mins
*   7 Video Lessons
*   3 Code Examples
*   1 Graded Assignment PRO
*   Earn an accomplishment with PRO
*   Instructor: Ben Kus
*   ![Image 6: Box](https://dlai-learn.deeplearning.ai/_next/image?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2025%2F09%2FBox-Square-Logo.png&w=48&q=75)Box
*   Learn more about[Membership PRO Plan](https://learn.deeplearning.ai/membership)

[Start Learning](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files?utm_source=home&utm_medium=course-landing-page&utm_campaign=summary-cta-button)

## What you'll learn

*   Build an LLM-powered app that processes invoice files, and extracts fields such as client name, total amount and purchased products, and generates a summary report for each client.

*   Connect the app to the Box MCP server to access tools such as folder and files listing, and text extraction, to avoid manual downloads and remove custom text extraction.

*   Orchestrate a three-agent system consisting of files agent, extraction agent and an orchestrator, built using Google’s ADK and communicating using the A2A (Agent2Agent) protocol.

## About this course

Join **Build AI Apps with MCP servers: Working with Box files**, built in partnership with Box, and taught by Ben Kus, its Chief Technology Officer.

You’ll begin with an AI application that processes files manually downloaded from a Box folder and locally stored. You’ll then refactor the application to make it MCP-compliant and connect it to the Box MCP server. The server will provide the application with the required tools to process the files directly in Box. You’ll finally evolve your solution into a multi-agent system that coordinates via the A2A protocol.

MCP or Model Context Protocol standardizes how context, in terms of tools and resources, is provided to LLMs. Instead of writing custom code inside your application for file search, file downloads, and text extraction, you can offload these tasks to an MCP server. An MCP client within your application can communicate with the MCP server to discover the tools and send requests to execute a certain tool. In this course, you’ll use the Box MCP server and learn how to connect it to your application to process files from a Box folder. You’ll also build a multi-agent system using Google’s Agent Development Kit. The agents will use A2A to communicate with each other, and the Box MCP server to access file and text extraction tools.

In detail, you’ll:

*   Build an LLM-powered invoice app that processes local PDF invoices to extract fields such as client name, total amount, and purchased product, and generates per-client reports.
*   Transform your application into an MCP-compliant app and use the tools of the Box MCP server to list the invoices within a Box folder and extract texts from each invoice, without manually downloading the files.
*   Move from a single agent to a multi-agent design: use an orchestrator to coordinate the tasks among sub-agents that use the Box MCP server and are specialized in files listing, text extraction, and reporting.
*   Design the orchestrator and subagents as A2A servers, and use an A2A client to send the user’s request to the orchestrator.

By the end, you’ll know how to build an AI application and AI agents that use the MCP server to process Box content securely, without manual downloads, and that support several file types and scale better with the number of files.

## Who should join?

This course is great for AI builders who work with documents and want a practical way to extract fields and build small agent-based workflows. Basic Python knowledge is recommended. No prior MCP, A2A, or Box API experience required.

## Course Outline

7 Lessons・3 Code Examples

*   [Introduction Video ・ 2 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/hl2xjv/introduction)
*   [Simple Invoice Processing App Video with Code Example ・ 3 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/8bp30g/simple-invoice-processing-app)
*   [Introduction to Box MCP Server Video ・ 3 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/dew9nq/introduction-to-box-mcp-server)
*   [Processing Invoices Using Box MCP Server Video with Code Example ・ 5 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/79cerh/processing-invoices-using-box-mcp-server)
*   [From a Single-Agent to a Multi-Agent Architecture Video ・ 3 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/jclw7p/from-a-single-agent-to-a-multi-agent-architecture)
*   [Processing Invoices Using A Multi-Agent System Video with Code Example ・ 6 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/vtzh22/processing-invoices-using-a-multi-agent-system)
*   [Conclusion Video ・ 1 min](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/536buk/conclusion)
*   [Quiz Graded・Quiz ・ 10 mins](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files/lesson/jclw7m/quiz)


#### Elevate your learning experience with Pro

Upgrade to Pro and gain unlimited accomplishments on your resume

[Learn More](https://learn.deeplearning.ai/membership)

## Instructor


### Ben Kus

Chief Technology Officer of [Box](https://www.box.com/)

*   [](https://www.linkedin.com/in/benkus)

## Build AI Apps with MCP Server: Working with Box Files

*   Intermediate
*   36 mins
*   7 Video Lessons
*   3 Code Examples
*   1 Graded Assignment PRO
*   Earn an accomplishment with PRO
*   Instructor: Ben Kus
*   ![Image 9: Box](https://dlai-learn.deeplearning.ai/_next/image?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2025%2F09%2FBox-Square-Logo.png&w=48&q=75)Box
*   Learn more about[Membership PRO Plan](https://learn.deeplearning.ai/membership)

[Start Learning](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files?utm_source=home&utm_medium=course-landing-page&utm_campaign=summary-cta-button)


Course access is free for a limited time during the DeepLearning.AI learning platform beta!

[Enroll for Free](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files?utm_source=home&utm_medium=course-landing-page&utm_campaign=summary-cta-button)

## Want to learn more about Generative AI?

Keep learning with updates on curated AI news, courses, and events, as well as Andrew’s thoughts from DeepLearning.AI!

First name* 

Last name* 

Email* 

Where do you live?* 

*   - [x] I want to get the latest news, courses, and workshops and events announcements* 

[Start Learning](https://learn.deeplearning.ai/courses/build-ai-apps-with-mcp-server-working-with-box-files?utm_source=home&utm_medium=course-landing-page&utm_campaign=summary-cta-button)

[![Image 11: DeepLearning.AI](https://dlai-learn.deeplearning.ai/_next/image?url=%2Fdlai%2Fassets%2Fdlai-logo.png&w=640&q=75&dpl=dpl_WW5rMdym78ZyVbHzEGs4bw3Cmidc)](https://www.deeplearning.ai/)
*   [Courses](https://learn.deeplearning.ai/courses)
*   [The Batch](https://www.deeplearning.ai/the-batch/)
*   [Community](https://www.deeplearning.ai/community)
*   [Careers](https://www.deeplearning.ai/careers/)
*   [About](https://www.deeplearning.ai/about/)
*   [Contact](https://www.deeplearning.ai/contact/)
*   [Help](https://info.deeplearning.ai/knowledge-base)

[](https://www.facebook.com/1027125564106325)[](https://www.instagram.com/deeplearningai)[](https://x.com/deeplearningai)[](https://www.linkedin.com/company/18246783)[](https://www.youtube.com/c/Deeplearningai)

[Terms of Use](https://www.deeplearning.ai/terms-of-use/)│[Privacy Policy](https://www.deeplearning.ai/privacy/)
