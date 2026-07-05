Title: You Cannot Have Exactly-Once Delivery

URL Source: https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/

Published Time: 2015-03-25T23:14:57+00:00

Markdown Content:
[Skip to content](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#content)

[Brave New Geek](https://bravenewgeek.com/)

Introspections of a software engineer

Menu 

*   [Home](https://bravenewgeek.com/)
*   [About Me](https://bravenewgeek.com/about-me/)
*   [Archive](https://bravenewgeek.com/archive/)
*   [Real Kinetic](https://realkinetic.com/)
*   [RSS](https://bravenewgeek.com/feed/)

Posted on[March 25, 2015 April 4, 2017](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/) by [Tyler Treat](https://bravenewgeek.com/author/tyler/)

# You Cannot Have Exactly-Once Delivery

I’m often surprised that people continually have fundamental misconceptions about how distributed systems behave. I myself shared many of these misconceptions, so I try not to demean or dismiss but rather educate and enlighten, hopefully while sounding less preachy than that just did. I continue to learn only by following in the footsteps of others. In retrospect, it shouldn’t be surprising that folks buy into these fallacies as I once did, but it can be frustrating when trying to communicate certain design decisions and constraints.

Within the context of a distributed system,**you cannot have exactly-once message delivery**. Web browser and server? Distributed. Server and database? Distributed. Server and message queue? Distributed. You cannot have exactly-once delivery semantics in any of these situations.

As I’ve [described in the past](http://www.slideshare.net/TylerTreat/from-mainframe-to-microservice-an-introduction-to-distributed-systems-41004778/23), **distributed systems are all about trade-offs**. This is one of them. There are essentially three types of delivery semantics: at-most-once, at-least-once, and exactly-once. Of the three, the first two are feasible and widely used. If you want to be super anal, you might say at-least-once delivery is also impossible because, technically speaking, network partitions are not strictly time-bound. If the connection from you to the server is interrupted indefinitely, you can’t deliver _anything._ Practically speaking, you have bigger fish to fry at that point—like calling your ISP—so we consider at-least-once delivery, for all intents and purposes, possible. With this model of thinking, network partitions are finitely bounded in time, however arbitrary this may be.

So where does the trade-off come into play, and why is exactly-once delivery impossible? The answer lies in the Two Generals thought experiment or the more generalized Byzantine Generals Problem, which I’ve [looked at extensively](https://bravenewgeek.com/understanding-consensus/). We must also consider the [FLP result](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf), which basically says, given the possibility of a faulty process, it’s _impossible_ for a system of processes to agree on a decision.

In the letter I mail you, I ask you to call me once you receive it. You never do. Either you really didn’t care for my letter or it got lost in the mail._That’s the cost of doing business._ I can send the one letter and hope you get it, or I can send 10 letters and assume you’ll get at least one of them. The trade-off here is quite clear (postage is expensive!), but sending 10 letters doesn’t really provide any additional guarantees. In a distributed system, we try to guarantee the delivery of a message by waiting for an acknowledgement that it was received, but all sorts of things can go wrong. Did the message get dropped? Did the ack get dropped? Did the receiver crash? Are they just slow? Is the network slow? Am _I_ slow? **FLP and the Two Generals Problem are not design complexities, they are _impossibility results_.**

People often bend the meaning of “delivery” in order to make their system fit the semantics of exactly-once, or in other cases, the term is overloaded to mean something entirely different. State-machine replication is a good example of this. Atomic broadcast protocols ensure messages are delivered reliably and in order. The truth is, we _can’t_ deliver messages reliably and in order in the face of network partitions and crashes without a high degree of coordination. This coordination, of course, comes at a cost (latency and availability), while still relying on at-least-once semantics. [Zab](http://web.stanford.edu/class/cs347/reading/zab.pdf), the atomic broadcast protocol which lays the foundation for ZooKeeper, enforces idempotent operations.

> State changes are idempotent and applying the same state change multiple times does not lead to inconsistencies as long as the application order is consistent with the delivery order. Consequently, guaranteeing at-least once semantics is sufficient and simplifies the implementation.

“Simplifies the implementation” is the authors’ attempt at subtlety. State-machine replication is just that, replicating state. If our messages have side effects, all of this goes out the window.

We’re left with a few options, all equally tenuous. When a message is delivered, it’s acknowledged immediately before processing. The sender receives the ack and calls it a day. However, if the receiver crashes before or during its processing, that data is lost forever. Customer transaction? Sorry, looks like you’re not getting your order. This is the worldview of at-most-once delivery. To be honest, implementing at-most-once semantics is more complicated than this depending on the situation. If there are multiple workers processing tasks or the work queues are replicated, the broker must be strongly consistent (or CP in CAP theorem parlance) so as to ensure a task is not delivered to any other workers once it’s been acked. Apache Kafka uses ZooKeeper to handle this coordination.

On the other hand, we can acknowledge messages after they are processed. If the process crashes after handling a message but before acking (or the ack isn’t delivered), the sender will redeliver.Hello,at-least-once delivery. Furthermore, if you want to deliver messages in order to more than one site, you need an atomic broadcast which is a _huge_ burden on throughput. Fast or consistent. Welcome to the world of distributed systems.

Every major message queue in existence which provides any guarantees will market itself as at-least-once delivery. If it [claims exactly-once](http://datasys.cs.iit.edu/publications/2014_SCRAMBL14_HDMQ.pdf), it’s because they are lying to your face in hopes that you will buy it or they themselves do not understand distributed systems. Either way, it’s not a good indicator.

RabbitMQ attempts to provide [guarantees](https://www.rabbitmq.com/reliability.html) along these lines:

> When using confirms, producers recovering from a channel or connection failure should retransmit any messages for which an acknowledgement has not been received from the broker. There is a possibility of message duplication here, because the broker might have sent a confirmation that never reached the producer (due to network failures, etc). Therefore consumer applications will need to perform deduplication or handle incoming messages in an idempotent manner.

The way we achieve exactly-once delivery in practice is by faking it. Either the messages themselves should be idempotent, meaning they can be applied more than once without adverse effects, or we remove the need for idempotency through deduplication. Ideally, our messages don’t require strict ordering and are commutative instead. There are design implications and trade-offs involved with whichever route you take, but this is the reality in which we must live.

Rethinking operations as idempotent actions might be easier said than done, but it mostly requires a change in the way we think about state. This is best described by revisiting the replicated state machine. Rather than distributing operations to apply at various nodes, what if we just distribute the state changes themselves? Rather than mutating state, let’s just report _facts_ at various points in time. This is effectively how Zab works.

Imagine we want to tell a friend to come pick us up. We send him a series of text messages with turn-by-turn directions, but one of the messages is delivered twice! Our friend isn’t too happy when he finds himself in the bad part of town. Instead, let’s just tell him _where_ we are and let him figure it out. If the message gets delivered more than once, it won’t matter. The implications are wider reaching than this, since we’re still concerned with the _ordering_ of messages, which is why solutions like commutative and convergent replicated data types are becoming more popular. That said, we can typically solve this problem through extrinsic means like sequencing, vector clocks, or other partial-ordering mechanisms. **It’s usually causal ordering that we’re after anyway. People who say otherwise don’t quite realize that _[there is no now](https://queue.acm.org/detail.cfm?id=2745385)in a distributed system_.**

To reiterate, there is no such thing as exactly-once delivery. We must choose between the lesser of two evils, which is at-least-once delivery in most cases. This can be used to simulate exactly-once semantics by ensuring idempotency or otherwise eliminating side effects from operations. Once again, it’s important to understand the trade-offs involved when designing distributed systems. There is asynchrony abound, which means you _cannot_ expect synchronous, guaranteed behavior. Design for failure and resiliency against this asynchronous nature.

[Follow @tyler_treat](https://twitter.com/tyler_treat?ref_src=twsrc%5Etfw)

### Share this:

*   [Pocket](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?share=pocket "Click to share on Pocket")
*   [Twitter](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?share=twitter "Click to share on Twitter")
*   [LinkedIn](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?share=linkedin "Click to share on LinkedIn")
*   [Reddit](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?share=reddit "Click to share on Reddit")
*   [Facebook](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?share=facebook "Click to share on Facebook")

### _Related_

Categories[Distributed Systems](https://bravenewgeek.com/category/distributed-systems-2/)Tags[cap theorem](https://bravenewgeek.com/tag/cap-theorem/), [consensus](https://bravenewgeek.com/tag/consensus/), [crdts](https://bravenewgeek.com/tag/crdts/), [distributed systems](https://bravenewgeek.com/tag/distributed-systems/), [flp result](https://bravenewgeek.com/tag/flp-result/), [message queues](https://bravenewgeek.com/tag/message-queues/), [messaging](https://bravenewgeek.com/tag/messaging/), [zab](https://bravenewgeek.com/tag/zab/), [zookeeper](https://bravenewgeek.com/tag/zookeeper/)

## 66 Replies to “You Cannot Have Exactly-Once Delivery”

1.   ![Image 1](https://secure.gravatar.com/avatar/5c4cb9a7a1f02a026bbe2663c935de100719f1a8b3f62f626183538e9ad3bc77?s=100&d=mm&r=g)**Confused**says: [March 25, 2015 at 6:57 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-123) “I can send 10 letters and assume you’ll get at least one of them (at-least-once).”

How is it you can assume 1 of 10 gets through? Isn’t this really “at most 10”?

If you can assume 1-of-N will get through, then why not just take N=1 and call it exactly-once? [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=123#respond) 
    1.   ![Image 2](https://secure.gravatar.com/avatar/ed3b7dbdc172efc254683c3c301813371eba0395569dcf77400a8b52ccc238de?s=100&d=mm&r=g)**Tyler Treat**says: [March 25, 2015 at 7:27 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-124) Yes, you’re correct. It’s not really an example of at-least-once delivery which requires an acknowledgement. Unintentionally misleading :)

Updated the wording to hopefully make it clear (and correct). [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=124#respond) 

2.   ![Image 3](https://secure.gravatar.com/avatar/ebd25f533064de7f5234ceb9f30360b4630818f536a39445dc6825a9ee4828ec?s=100&d=mm&r=g)**Jason Dusek**says: [March 26, 2015 at 2:32 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-127) The FLP result comes with a caveat — it applies to a “completely asynchronous” protocol.

> In this paper, we show the surprising result that no completely asynchronous consensus protocol can tolerate even a single unannounced process death.

With tightly bounded clock drift (hard to bound in practice), it seems reasonable that we can guarantee once-and-only-once delivery, because we can perform consensus. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=127#respond) 
    1.   ![Image 4](https://secure.gravatar.com/avatar/e796097276fbee20a6e78e1f8d49ad327fea535cffb499bf6c34d7ecbf57b03e?s=100&d=mm&r=g)**Joubin Houshyar**says: [March 26, 2015 at 1:59 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-142) It seems the conceptual root cause is subscription to the illusion of continuums and a stubborn belief in the fairy dust of (meaningful) instantaneity. We need to accept the reality of a discreet view of the world– which naturally promotes to first-class design concerns the notions of ‘precision’ & (time) ‘granularities’.

The fact of the matter is that all of our computational systems are operating on data from ‘the past’.

(re. clock bounds: Google has done it with Spanner — someone needs to commoditize the necessary h/w.) [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=142#respond) 
        1.   ![Image 5](https://secure.gravatar.com/avatar/23bbd020645431f6341edf912e04234133f53ff59211295aa7e75e25d3fdcdad?s=100&d=mm&r=g)**Nicolas Correard**says: [February 24, 2016 at 4:30 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-14063) CockroachDB do the equivalent of spanner without the hardware. Look for the blog post containing “CockroachDB was designed to work without atomic clocks or GPS clocks. It’s an open source database intended to be run on arbitrary collections of nodes: from physical servers in a corp development cluster to public cloud infrastructure using the flavor-of-the-month virtualization layer. It’d be a showstopper to require an external dependency on specialized hardware for clock synchronization.” [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=14063#respond) 

3.   ![Image 6](https://secure.gravatar.com/avatar/71bac479b95da386294e070ddd7cfdaed68f9b6f763e8d844761ec413d1f7ba1?s=100&d=mm&r=g)**lmm**says: [March 26, 2015 at 3:43 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-128) Doesn’t the existence of three-phase commit contradict this? If I make a change and commit it with 3PC, retrying until it does, how is that not exactly-once delivery? [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=128#respond) 
    1.   ![Image 7](https://secure.gravatar.com/avatar/9c2dfc5c9f3cb76c26cc09566999106404b3894716181cca23718a998877290b?s=100&d=mm&r=g)**J W**says: [November 5, 2021 at 11:32 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-42809) FLP literally does not apply to message passing lol. It important for writers to actually understand the proof of the theorem they’re talking about before they make wild claims like those in this article. In fact, FLP assumes reliable links! You read that right–*it literally assumes the existence of exactly-once delivery between correct nodes*, but proceeds to show that this doesn’t affect its main result. If you are claiming that one of the core system assumptions of FLP (the existence of reliable links) is disproved by FLP, you *might* just not understand distributed systems as well as you think you do.

But what about in practice? Well, in practice it’s really easy to get exactly-once delivery between nodes, as long as you’re in a system strong enough to eventually solve consensus. In most contexts in which people want exactly-once delivery (such as between managed nodes in datacenters) this is a completely reasonable assumption. So this is a dumb post in practice, too. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=42809#respond) 
        1.   ![Image 8](https://secure.gravatar.com/avatar/0ac3121cd5bd30a628f2fdcbbc8f1882bcf3b5218c60aaa218a153d76effc951?s=100&d=mm&r=g)**haha**says: [November 6, 2024 at 11:10 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-58976) So true… I was shocked to see so many blogs claiming exactly-once is impossible, citing the two-general problem and the FLP paper.

Those impossibility resutls only say that algorithms guaranteeing liveness (i.e., terminate within bounded number of steps) do not exist; there can still be algorithms that guarantee safety (i.e., produce correct consensus outcomes once terminated). Paxos and 2PC are such algorithms and they work just fine in practice. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=58976#respond) 

4.   ![Image 9](https://secure.gravatar.com/avatar/9a8cd62ebf613ac5a3e292c79c124c9a9b6f736c0e4a401c847d5cddf3e12ade?s=100&d=mm&r=g)**Webhiker**says: [March 26, 2015 at 4:01 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-129) All your objections to Exactly-once also apply to AtLeastOnce.

 And ExactlyOnce is possible…all your objections are based on the current design flay of messaing systems which decouple delivery into a message queue.

If you don’t decouple, the act of the recipient “reading” the message can be easily detected, including it’s failure. But then all the investment in expensive message queues looks stupid, so no-one will be able sell their superior knowledge of straw man arguments on why message delivery cannot be guaranteed. :) [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=129#respond) 
    1.   ![Image 10](https://secure.gravatar.com/avatar/e833b14d190e837b6bba61ca94a072391cc8bf851139bf8b9650ee712e950235?s=100&d=mm&r=g)**MC**says: [April 18, 2022 at 10:37 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-47957) You have absolutely no clue what you’re babbling about. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=47957#respond) 

5.   ![Image 11](https://secure.gravatar.com/avatar/046025e704e95e0e79352df7cbb69e34cf158e385d79459868b0fc7c3cbdf957?s=100&d=mm&r=g)**[Michael Chermside](http://mcherm.com/)**says: [March 26, 2015 at 8:58 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-136) Although it is impossible to create a system that guarantees “exactly once” delivery, it *is* possible to create a system that guarantees that EITHER (1) it will deliver exactly once, OR (2) it will report an error to a human being. This is also the technique best used for attempts at “at least once” delivery which fail over an extended period of time.

None of this invalidates anything you said about the usefulness of idempotency, but I like to point it out because it emphasizes two things: the impossibility of perfect message delivery (like “exactly once” being impossible) and the need to have someone monitor the error queues of your messaging system. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=136#respond) 
    1.   ![Image 12](https://secure.gravatar.com/avatar/e72d0e8394554f16540cfd084df9ed49551079dcc1da8baa4823581187519865?s=100&d=mm&r=g)**sumit**says: [March 27, 2015 at 2:43 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-147) Hey Michael,

It would be really helpful if you could point out some simple and relevant article(s) that supports the guarantee you mentioned. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=147#respond) 
    2.   ![Image 13](https://secure.gravatar.com/avatar/26c4e71c2fe397bd31e6cf933a901f2438a014e7d5f8778ce43277650b959814?s=100&d=mm&r=g)**Michael Ho**says: [June 5, 2015 at 11:05 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-777) Fancy meeting you here, MCherm! [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=777#respond) 

6.   ![Image 14](https://secure.gravatar.com/avatar/2d2c31234a805bdf04546faf7c51fd6eec3834d5c084d2e3ae398824340290f2?s=100&d=mm&r=g)**Stu**says: [March 26, 2015 at 9:16 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-137) You’re right, but I’m not sure about the melodrama. Accusing folks like IBM or BEA/Oracle of lying for 20 years is a reach, it’s more like you weren’t there when they coined the term.

“Exactly once” has *always* meant “at least once but dupe-detected”. Mainly because we couldn’t convince customers to send idempotent and communitative state changes. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=137#respond) 
    1.   ![Image 15](https://secure.gravatar.com/avatar/47a15b06f753cdaceb83602ffac3402b1ebf32bd073b5a4dd1b20734f8282f9a?s=100&d=mm&r=g)**Sebastien Lorber**says: [April 5, 2015 at 7:10 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-260) +1

With event-sourcing/stream processing for example you would version every event/message so that it’s easy to dedup. If your friend receive 2 messages with id=456 telling him to turn left them it is easy for him to ignore one of them.

Another problem is about message ordering. If you have multiple datacenters and want to keep allow local writes during a network partition it seems impossible to guarantee global event ordering.

 Kafka does only guarantee ordering across a single Kafka partition for example.

 See how Eventuate is trying to solve this with causal consistency: [https://github.com/RBMHTechnology/eventuate](https://github.com/RBMHTechnology/eventuate) [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=260#respond) 

7.    Pingback: [Process Focus vs. System Architecture | Thinking Matters](http://social-biz.org/2015/04/23/process-focus-vs-system-architecture/) 
8.    Pingback: [Endnu en god artikel om udvikling | Hennings blog](https://henningjust.wordpress.com/2015/04/27/endnu-en-god-artikel-om-udvikling/) 
9.    Pingback: [Service-Disoriented Architecture | Brave New Geek](https://bravenewgeek.com/service-disoriented-architecture/) 
10.   ![Image 16](https://secure.gravatar.com/avatar/77b307bbf0f7e05ae4cc479b6101251ec3900d10ac044e518fe7213df68bf6ba?s=100&d=mm&r=g)**[Mike Spooner](http://mbus.sunhelp.org/)**says: [June 8, 2015 at 3:11 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-796) Well said, nice article. But this has been well-understood since at least 1986… sigh [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=796#respond) 
    1.   ![Image 17](https://secure.gravatar.com/avatar/eae884dff9f5ffc82b63c870e5d13957f3c99d3510b19a483693fee52689aa90?s=100&d=mm&r=g)**John B**says: [September 9, 2015 at 9:06 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-2562) yes, it has been well understood by certain people for a long time, but there’s been an entire new generation of software developers since 1986.

While it may be tedious for those of us who have been around for a long time, re-introducing key concepts to young developers is incredibly valuable work. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=2562#respond) 

11.   ![Image 18](https://secure.gravatar.com/avatar/d216588475a336c5552d40574e1954820c70c9594f4e3bc66b4bd4d37b361e92?s=100&d=mm&r=g)**[Abhinav Singh](http://abhinavsingh.com/)**says: [September 6, 2015 at 2:05 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-2474) Great post as always. Wanted to leave my 2 cents here.

Let’s forget engineering and take a real world example like you did. Assume a distributed system of 2 nodes, me and my wife sitting in next room. If I want to communicate with her, I shout out her name and wait for response. Well, if I don’t hear back from her, we can assume:

– probably she didn’t hear me (partitioned by walls)

 – simply ignored my message coz she is busy

 – received my message but it wasn’t clear to her what to do with it

 – received and she did shout back, but I just couldn’t hear her due to partition caused by walls and due to her soft voice

 – may be I did likely heard her, but I am not sure

 – may be I was too busy when she called out to me

 – ….. We can go on here

Now, if I seriously want her attention and mean business, I will have to move past this “exactly-once” melodrama and shout out to her again. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=2474#respond) 
12.    Pingback: [You cannot have at-least-once broadcast - 250bpm](http://250bpm.com/blog:61) 
13.    Pingback: [» Reportáž z GeeCON Praha 2015 Myšlenky dne otce Fura](http://blog.novoj.net/2015/10/26/reportaz-z-geecon-praha-2015/) 
14.    Pingback: [Use Cases für Apache Kafka: "Viele Data-Probleme sind gar nicht so big" - JAXenter](https://jaxenter.de/use-cases-fuer-apache-kafka-viele-data-probleme-sind-gar-nicht-so-big-38862) 
15.    Pingback: [Exactly Once Stream Processing Semantics ? Not Exactly | Mawazo](https://pkghosh.wordpress.com/2016/05/18/exactly-once-stream-processing-semantics-not-exactly/) 
16.    Pingback: [分布式系统互斥性与幂等性问题的分析与解决 – 大耳狐](http://blog.daerhu.com/?p=108) 
17.    Pingback: [分布式系统互斥性与幂等性问题的分析与解决 | 九悦](http://www.ixfun.cn/11641.html) 
18.    Pingback: [Monzo是如何从0开始构建7*24小时不停歇的银行后台系统的？ - 莹莹之色](http://hack.hk.cn/2016/11/30/monzo%e6%98%af%e5%a6%82%e4%bd%95%e4%bb%8e0%e5%bc%80%e5%a7%8b%e6%9e%84%e5%bb%ba724%e5%b0%8f%e6%97%b6%e4%b8%8d%e5%81%9c%e6%ad%87%e7%9a%84%e9%93%b6%e8%a1%8c%e5%90%8e%e5%8f%b0) 
19.    Pingback: [Monzo是如何从0开始构建7*24小时不停歇的银行后台系统的？-zoues](http://www.zoues.com/2016/12/08/monzo%e6%98%af%e5%a6%82%e4%bd%95%e4%bb%8e0%e5%bc%80%e5%a7%8b%e6%9e%84%e5%bb%ba724%e5%b0%8f%e6%97%b6%e4%b8%8d%e5%81%9c%e6%ad%87%e7%9a%84%e9%93%b6%e8%a1%8c%e5%90%8e%e5%8f) 
20.    Pingback: [performance tuning kafka – Technology Musings](https://phisymmetry.wordpress.com/2016/04/11/performance-tuning-kafka/) 
21.   ![Image 19](https://secure.gravatar.com/avatar/baa998c06758f2e08f9365d4285dff5663152b3999ecc75d87543a75ffa18e58?s=100&d=mm&r=g)**Kunal**says: [December 12, 2016 at 1:22 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-17089) You can achieve the intent of “exactly-once” i.e. no duplicates and no data-loss on failures by making the receiver (client) state aware (i.e. offset, IDs); the client de-dupes.

There is business intent to building technology always. Religiously speaking, it is correct that exactly-once is not possible on the network protocol level in a distributed system; I don’t think anyone will argue that. When people say we need exactly once, they really are speaking from a business or application intent. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=17089#respond) 
    1.   ![Image 20](https://secure.gravatar.com/avatar/77b307bbf0f7e05ae4cc479b6101251ec3900d10ac044e518fe7213df68bf6ba?s=100&d=mm&r=g)**[Mike Spooner](http://mbus.sunhelp.org/)**says: [December 12, 2016 at 6:12 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-17106) Although sequence-numbers/IDs does mean that, like the 787 Dreamliner, you have to poweroff or restart the entire system-universe every so often, at least until we get systems that really can count to infinity (at least “A0”, not necessarily as far as Cantors number). [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=17106#respond) 

22.    Pingback: [Tuning Kafka – Technology Musings](https://phisymmetry.wordpress.com/2016/02/11/performance-tuning-kafka/) 
23.    Pingback: [Building a modern bank backend – At Monzo – Advance](http://www.advancedemos.co.za/advance/?p=75) 
24.    Pingback: [Delivering Billions of Messages Exactly Once · Segment Blog | Artificia Intelligence](http://www.aboromedia.com/ai/2017/06/30/delivering-billions-of-messages-exactly-once-%c2%b7-segment-blog/) 
25.    Pingback: [如何做到“恰好一次”地传递数十亿条消息 - 莹莹之色](http://hack.hk.cn/2017/07/07/%e5%a6%82%e4%bd%95%e5%81%9a%e5%88%b0%e6%81%b0%e5%a5%bd%e4%b8%80%e6%ac%a1%e5%9c%b0%e4%bc%a0%e9%80%92%e6%95%b0%e5%8d%81%e4%ba%bf%e6%9d%a1%e6%b6%88%e6%81%af/) 
26.    Pingback: [转：分布式系统互斥性与幂等性问题的分析与解决 – 东京钱爷的博客](https://blog.uenta.cn/2017/08/15/%e8%bd%ac%ef%bc%9a%e5%88%86%e5%b8%83%e5%bc%8f%e7%b3%bb%e7%bb%9f%e4%ba%92%e6%96%a5%e6%80%a7%e4%b8%8e%e5%b9%82%e7%ad%89%e6%80%a7%e9%97%ae%e9%a2%98%e7%9a%84%e5%88%86%e6%9) 
27.    Pingback: [Apache Kafka gets 'exactly-once' message delivery - and that's a big deal - SiliconANGLE](https://siliconangle.com/blog/2017/08/25/apache-kafka-gets-exactly-message-delivery-thats-big-deal/) 
28.    Pingback: [Apache Kafka 1.0 Released Exactly Once – IoT up2date](http://observatorios.eversusi.com/iot/apache-kafka-1-0-released-exactly-once/) 
29.    Pingback: [Apache Kafka](https://datahub.packtpub.com/analytics/apache-kafka-1-0-streaming-platform/) 
30.   ![Image 21](https://secure.gravatar.com/avatar/cc4c7a4beed6f72aaba994a119ee1085f7eff49f8f69775cbd6346174857425a?s=100&d=mm&r=g)**Homesh Rawat**says: [February 17, 2018 at 4:12 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-21329) Great read! [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=21329#respond) 
31.   ![Image 22](https://secure.gravatar.com/avatar/5f5cc9d79ba5ae36e7a83ff2aa9df8c3210157e3bd25639dd4be43ac2d4b0261?s=100&d=mm&r=g)**[mark](http://bestical.rocks/)**says: [June 18, 2018 at 5:45 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-22129) I thinks these works like deduplication and… must execute on consumer side [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=22129#respond) 
32.    Pingback: [Reliable notifications between two apps or microservices](http://mimilele.com/index.php/192.html) 
33.    Pingback: [1 – A victim of its own popularity: Scaling our CloudWatch integration | Traffic.Ventures Social](http://blog.traffic.ventures/?p=166930) 
34.    Pingback: [1 – Nancy Lynch – Distributed Systems Pioneer | Traffic.Ventures Social](http://blog.traffic.ventures/?p=176049) 
35.    Pingback: [Reliable notifications between two apps or microservices – NICE CODE](http://surgicalcity.us/index.php/2019/01/10/reliable-notifications-between-two-apps-or-microservices/) 
36.   ![Image 23](https://secure.gravatar.com/avatar/72e541e3758162714e9ab47655a58101ef94f4acf57776c182231a6c1a45e783?s=100&d=mm&r=g)**Nicholas**says: [February 11, 2019 at 12:11 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-25107) “The way we achieve exactly-once delivery in practice is by faking it. Either the messages themselves should be idempotent, meaning they can be applied more than once without adverse effects, or we remove the need for idempotency through deduplication.”

If the message only writes exactly once then that’s successful exactly-once semantics. Back when this article was written it was a hard problem a lot of people struggled with, but today Kafka has a system for exactly-once, and I work at a different company that does it in a different way. You can call it “fake” but in that case we have stable, well-functioning “fake” exactly-once semantics, and a lot of customers use that “fake” system successfully to solve real problems. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=25107#respond) 
37.    Pingback: [A Game of Snakes & Ladders Called Microservices | APIscene](https://www.apiscene.io/lifecycle/a-game-of-snakes-ladders-called-microservices/) 
38.    Pingback: [Stream Deduplication with Hazelcast Jet | Hazelcast](https://hazelcast.com/blog/stream-deduplication-with-hazelcast-jet/) 
39.    Pingback: [Stream Deduplication with Hazelcast Jet - Hazelcast Hazelcast the Leading In-Memory Data Grid](https://hazelcastorg2.wpengine.com/blog/stream-deduplication-with-hazelcast-jet/) 
40.   ![Image 24](https://secure.gravatar.com/avatar/32e27a41ff5e9c865de49b28e294346dfb313ee07fdc7d3cb7066c6af1a1c19c?s=100&d=mm&r=g)**Mehedi**says: [May 22, 2020 at 7:14 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-31313) How Gmail ensure only one email? [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=31313#respond) 
41.    Pingback: [Cassandra: difference between exactly-once and at-least-once guarantees - IZZIDB](https://izzidb.com/cassandra-difference-between-exactly-once-and-at-least-once-guarantees/) 
42.    Pingback: [Handling access token expiry when internet is unstable - Tutorial Guruji](https://www.tutorialguruji.com/android/handling-access-token-expiry-when-internet-is-unstable/) 
43.    Pingback: [Exactly-Once Delivery，這個需求做不了 - 水源一二三](https://theweidi.net/posts/exactly-once-delivery%ef%bc%8c%e9%80%99%e5%80%8b%e9%9c%80%e6%b1%82%e5%81%9a%e4%b8%8d%e4%ba%86/) 
44.    Pingback: [Exactly-Once Delivery，這個需求做不了 - 水源一二三](https://theweidi.net/posts/you-cannot-have-exactly-once-delivery/) 
45.   ![Image 25](https://secure.gravatar.com/avatar/7b81aa642da7fe3aaeed79ab725dc2f5e6db829b59aeb5ff915403af87bb1bd4?s=100&d=mm&r=g)**temporal user**says: [January 13, 2022 at 9:05 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-45732) temporal does exactly once delivery [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=45732#respond) 
46.    Pingback: [高并发-业务-如何构建幂等性接口 - 算法网](https://itpcb.com/a/2282896) 
47.    Pingback: [分布式系统互斥性与幂等性问题的分析与解决 – 源码巴士](https://code84.com/577379.html) 
48.    Pingback: [Part 3: Processing Payments – Ethereum Payment | Code Capsule](https://codecapsule.com/2022/11/29/ethereum-payment-part-3-processing-payments/) 
49.   ![Image 26](https://secure.gravatar.com/avatar/79c50a40bf4c2cd1709e2217bc6eedd852957c53ddf14b6437f2e93415e1e56d?s=100&d=mm&r=g)**Alexey Stogny**says: [February 23, 2023 at 10:15 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-51403) Nice post! Thanks! Wouldn’t post useless comment, but there’s no other way to subscribe to new posts ;) [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=51403#respond) 
50.   ![Image 27](https://secure.gravatar.com/avatar/8e41bb81bd39d7cefccf82ca217fa71d44f4f6b6c560778da0fb956c30e50c32?s=100&d=mm&r=g)**Simon Boddy**says: [March 2, 2023 at 2:07 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-51460) Absolutely. Of course. And there’s a simple pattern for dealing with this… use a request/response protocol rather than messages, then make sure all unsafe requests have an application-level id. The receiving process, the server application, should store all responses. If it sees a request for the first time it does the work, then sends and stores the response. If it sees a request for which it has a stored response, it just replays the response. Reliability is an application level responsibility, and uniquely identified requests can be linked to uniqueness in the application context (1 shopping cart can have 1 payment request that the shopping cart app can repeat endlessly until it gets a response) [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=51460#respond) 
51.   ![Image 28](https://secure.gravatar.com/avatar/2bd621dd95b7dadd1275169c1441fd1c07776ee1f604a0439c22ab2717aa25e0?s=100&d=mm&r=g)**Rody**says: [April 18, 2023 at 9:10 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-51813) What about modern day chat applications, they use sockets and messages are delivered once and they come under distributed systems right?

 isnt exactly once not achieved, or is it with the sender and receiver being the same services giving an edge? [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=51813#respond) 
52.   ![Image 29](https://secure.gravatar.com/avatar/148463dba0ba20773cc5fb66987dd80d0857e0c4e06c3a2da45ed62cb8258ed3?s=100&d=mm&r=g)**[abc123](http://abc123/)**says: [September 18, 2023 at 9:48 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-52785)  [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=52785#respond) 
53.   ![Image 30](https://secure.gravatar.com/avatar/bd31392884b5776bee50515d246d871b71da346ed53f23dda41040dc3118dd33?s=100&d=mm&r=g)**Gyula Csom**says: [February 7, 2025 at 6:38 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-60669) I think the reasoning here is not totally precise. From FLP it follows that “Exactly once” is impossible in network (where partitions can occur). However it does not seem to be impossible at the application level (if we assume the machine reliable where partition cannot occur). How? Through idempotency:

— Draft protocol

Here is a simple protocol using shared message log. Lets say the message broker is Kafka, which BTW also states it can do “Exactly once”:

Step 1. Kafka server->client: Server sends, client Receives new message

 Step 2. Kafka client: Logs message as being processed

 Step 3. Kafka client->Application: Client sends, Application receives new message

 Step 4. Application: Process message

 Step 5. Application: Logs message as processed

— Case of network failure:

Step 2. Check log before forwarding and only forward message to application iff it is not yet processed.

— Case of process failure of Kafka client (after the message is already processed):

Restart Kafka client: Consult log and only forward messages which are not marked as processed

Case of process failure of Application:

Restart Application: Consult log and process messages which are not marked as processed

— Case of process failure of Kafka client (while message is being processed by the application):

No need nothing (single threaded Application) or some intra-app coordination (multi threaded)

— Case of process failure of both Kafka client and Application:

No need nothing.

A thing which seems to be interesting here, in case of business applications (DB): what happens with the transaction? Then idempotency should be solved at that side as well, such as recording a version (such as e.g. optimistic lock) both at the local log and the DB.

Then the only problem remains when Application crashes during transaction, after transaction started but but before commited. To my understanding client-crash-survival DB sessions might be theoretically possible, but I am not aware of any RDBMS implementing it. Someone else? :-)

As always I can be wrong – these are just rough thoughts. Any feedback is more then welcome. :-) [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=60669#respond) 
54.   ![Image 31](https://secure.gravatar.com/avatar/bd31392884b5776bee50515d246d871b71da346ed53f23dda41040dc3118dd33?s=100&d=mm&r=g)**Gyula Csom**says: [February 9, 2025 at 5:40 am](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-60691) So to clarify… the above protocol is still not “Exactly once” at the network level. That is impossible due to FLP. However a smart protocol may hide this from the Application and present itself as “Exactly once”.

Bottom line: If network partitions (resending lost messages) is an issue than “Exactly once” can be missleading, someone shall not forget about the physical level. However if partitions are not a big issue (network is robust enough, fast, etc.) then someone may forget about the physical level (network) and just think that at the Application level (i.e. logically) it is “Exactly once”. Question here: what is the added value here in comparison with “Idempotency” which sometimes can still be an issue at the Application level as well, such as when an impatient user resends the message that cannot be (easily) handled by infrastructure. What are your experiences in this regard? [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=60691#respond) 
55.   ![Image 32](https://secure.gravatar.com/avatar/f189fa33c843109676d61dc2e19d72bbdd0a3a038cfa8ead48c3a8a416156b56?s=100&d=mm&r=g)**Heth Gala**says: [January 14, 2026 at 7:47 pm](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#comment-66177) This article was just a rant. Nothing useful came out of it. I was expecting how to achieve at-least once in notification systems here but its total rant. [Reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/?replytocom=66177#respond) 

### Leave a Reply [Cancel reply](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/#respond)

Your email address will not be published.Required fields are marked *

Comment *

Name *

Email *

Website

- [x] Notify me of follow-up comments by email.

- [x] Notify me of new posts by email.

Δ

## Post navigation

[Previous Post Previous If State Is Hell, SOA Is Satan](https://bravenewgeek.com/if-state-is-hell-soa-is-satan/)

[Next Post Next Writing Good Code](https://bravenewgeek.com/writing-good-code/)

## Popular

*   [You Cannot Have Exactly-Once Delivery](https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/)
*   [Everything You Know About Latency Is Wrong](https://bravenewgeek.com/everything-you-know-about-latency-is-wrong/)
*   [So You Wanna Go Fast?](https://bravenewgeek.com/so-you-wanna-go-fast/)
*   [Abstraction Considered Harmful](https://bravenewgeek.com/abstraction-considered-harmful/)
*   [Dissecting Message Queues](https://bravenewgeek.com/dissecting-message-queues/)

## Recent

*   [What is Koreo?](https://bravenewgeek.com/what-is-koreo/)
*   [Controller-Driven Infrastructure as Code](https://bravenewgeek.com/controller-driven-infrastructure-as-code/)
*   [Platform Engineering as a Service](https://bravenewgeek.com/platform-engineering-as-a-service/)
*   [Deployment-Driven Development](https://bravenewgeek.com/deployment-driven-development/)
*   [Automating Infrastructure as Code with Vertex AI](https://bravenewgeek.com/automating-infrastructure-as-code-with-vertex-ai/)

## Categories

*   [AI](https://bravenewgeek.com/category/ai/)
*   [Algorithms](https://bravenewgeek.com/category/algorithms/)
*   [Analytics](https://bravenewgeek.com/category/analytics/)
*   [Android](https://bravenewgeek.com/category/android/)
*   [AWS](https://bravenewgeek.com/category/aws/)
*   [Bash](https://bravenewgeek.com/category/bash/)
*   [Benchmarking](https://bravenewgeek.com/category/benchmarking/)
*   [Business](https://bravenewgeek.com/category/business-2/)
*   [Cloud](https://bravenewgeek.com/category/cloud/)
*   [Computer Science](https://bravenewgeek.com/category/computer-science/)
*   [Concurrency](https://bravenewgeek.com/category/concurrency-2/)
*   [Consulting](https://bravenewgeek.com/category/consulting/)
*   [Culture](https://bravenewgeek.com/category/culture/)
*   [Data Structures](https://bravenewgeek.com/category/data-structures/)
*   [Databases](https://bravenewgeek.com/category/databases-2/)
*   [Design Patterns](https://bravenewgeek.com/category/design-patterns/)
*   [DevOps](https://bravenewgeek.com/category/devops/)
*   [Distributed Systems](https://bravenewgeek.com/category/distributed-systems-2/)
*   [Economics](https://bravenewgeek.com/category/economics-2/)
*   [GCP](https://bravenewgeek.com/category/gcp/)
*   [GitLab](https://bravenewgeek.com/category/gitlab/)
*   [Go](https://bravenewgeek.com/category/go-2/)
*   [Infinitum](https://bravenewgeek.com/category/infinitum/)
*   [Java](https://bravenewgeek.com/category/java/)
*   [JavaScript](https://bravenewgeek.com/category/javascript/)
*   [Konfigurate](https://bravenewgeek.com/category/konfig/)
*   [Koreo](https://bravenewgeek.com/category/koreo/)
*   [Kubernetes](https://bravenewgeek.com/category/kubernetes/)
*   [Liftbridge](https://bravenewgeek.com/category/liftbridge/)
*   [Management](https://bravenewgeek.com/category/management/)
*   [Mathematics](https://bravenewgeek.com/category/mathematics/)
*   [Messaging](https://bravenewgeek.com/category/messaging/)
*   [Operations](https://bravenewgeek.com/category/operations/)
*   [Platform Engineering](https://bravenewgeek.com/category/platform-engineering/)
*   [Postmortem](https://bravenewgeek.com/category/postmortem/)
*   [Python](https://bravenewgeek.com/category/python/)
*   [Real Kinetic](https://bravenewgeek.com/category/real-kinetic/)
*   [Security](https://bravenewgeek.com/category/security/)
*   [Software Architecture](https://bravenewgeek.com/category/software-architecture/)
*   [Software Engineering](https://bravenewgeek.com/category/software-engineering/)
*   [Spring](https://bravenewgeek.com/category/spring/)
*   [Systems Theory](https://bravenewgeek.com/category/systems-theory/)
*   [Unix](https://bravenewgeek.com/category/unix/)

## Archives

*   [May 2025](https://bravenewgeek.com/2025/05/)
*   [March 2025](https://bravenewgeek.com/2025/03/)
*   [November 2024](https://bravenewgeek.com/2024/11/)
*   [June 2024](https://bravenewgeek.com/2024/06/)
*   [May 2024](https://bravenewgeek.com/2024/05/)
*   [April 2024](https://bravenewgeek.com/2024/04/)
*   [February 2024](https://bravenewgeek.com/2024/02/)
*   [June 2022](https://bravenewgeek.com/2022/06/)
*   [October 2021](https://bravenewgeek.com/2021/10/)
*   [December 2020](https://bravenewgeek.com/2020/12/)
*   [November 2020](https://bravenewgeek.com/2020/11/)
*   [October 2020](https://bravenewgeek.com/2020/10/)
*   [July 2020](https://bravenewgeek.com/2020/07/)
*   [June 2020](https://bravenewgeek.com/2020/06/)
*   [April 2020](https://bravenewgeek.com/2020/04/)
*   [February 2020](https://bravenewgeek.com/2020/02/)
*   [January 2020](https://bravenewgeek.com/2020/01/)
*   [October 2019](https://bravenewgeek.com/2019/10/)
*   [September 2019](https://bravenewgeek.com/2019/09/)
*   [August 2019](https://bravenewgeek.com/2019/08/)
*   [April 2019](https://bravenewgeek.com/2019/04/)
*   [March 2019](https://bravenewgeek.com/2019/03/)
*   [January 2019](https://bravenewgeek.com/2019/01/)
*   [September 2018](https://bravenewgeek.com/2018/09/)
*   [July 2018](https://bravenewgeek.com/2018/07/)
*   [April 2018](https://bravenewgeek.com/2018/04/)
*   [February 2018](https://bravenewgeek.com/2018/02/)
*   [January 2018](https://bravenewgeek.com/2018/01/)
*   [December 2017](https://bravenewgeek.com/2017/12/)
*   [November 2017](https://bravenewgeek.com/2017/11/)
*   [October 2017](https://bravenewgeek.com/2017/10/)
*   [August 2017](https://bravenewgeek.com/2017/08/)
*   [July 2017](https://bravenewgeek.com/2017/07/)
*   [June 2017](https://bravenewgeek.com/2017/06/)
*   [May 2017](https://bravenewgeek.com/2017/05/)
*   [April 2017](https://bravenewgeek.com/2017/04/)
*   [December 2016](https://bravenewgeek.com/2016/12/)
*   [November 2016](https://bravenewgeek.com/2016/11/)
*   [April 2016](https://bravenewgeek.com/2016/04/)
*   [February 2016](https://bravenewgeek.com/2016/02/)
*   [January 2016](https://bravenewgeek.com/2016/01/)
*   [December 2015](https://bravenewgeek.com/2015/12/)
*   [September 2015](https://bravenewgeek.com/2015/09/)
*   [August 2015](https://bravenewgeek.com/2015/08/)
*   [July 2015](https://bravenewgeek.com/2015/07/)
*   [June 2015](https://bravenewgeek.com/2015/06/)
*   [May 2015](https://bravenewgeek.com/2015/05/)
*   [April 2015](https://bravenewgeek.com/2015/04/)
*   [March 2015](https://bravenewgeek.com/2015/03/)
*   [February 2015](https://bravenewgeek.com/2015/02/)
*   [January 2015](https://bravenewgeek.com/2015/01/)
*   [December 2014](https://bravenewgeek.com/2014/12/)
*   [November 2014](https://bravenewgeek.com/2014/11/)
*   [October 2014](https://bravenewgeek.com/2014/10/)
*   [September 2014](https://bravenewgeek.com/2014/09/)
*   [August 2014](https://bravenewgeek.com/2014/08/)
*   [July 2014](https://bravenewgeek.com/2014/07/)
*   [June 2014](https://bravenewgeek.com/2014/06/)
*   [May 2014](https://bravenewgeek.com/2014/05/)
*   [March 2014](https://bravenewgeek.com/2014/03/)
*   [December 2013](https://bravenewgeek.com/2013/12/)
*   [September 2013](https://bravenewgeek.com/2013/09/)
*   [June 2013](https://bravenewgeek.com/2013/06/)
*   [March 2013](https://bravenewgeek.com/2013/03/)
*   [January 2013](https://bravenewgeek.com/2013/01/)
*   [December 2012](https://bravenewgeek.com/2012/12/)

## Tags

*   [agile](https://bravenewgeek.com/tag/agile/)
*   [algorithms](https://bravenewgeek.com/tag/algorithms-2/)
*   [android](https://bravenewgeek.com/tag/android-2/)
*   [app engine](https://bravenewgeek.com/tag/app-engine/)
*   [architecture](https://bravenewgeek.com/tag/architecture/)
*   [cap theorem](https://bravenewgeek.com/tag/cap-theorem/)
*   [cloud](https://bravenewgeek.com/tag/cloud/)
*   [cloud-native](https://bravenewgeek.com/tag/cloud-native/)
*   [consulting](https://bravenewgeek.com/tag/consulting-2/)
*   [culture](https://bravenewgeek.com/tag/culture/)
*   [databases](https://bravenewgeek.com/tag/databases/)
*   [design patterns](https://bravenewgeek.com/tag/design-patterns-2/)
*   [devops](https://bravenewgeek.com/tag/devops/)
*   [distributed log](https://bravenewgeek.com/tag/distributed-log/)
*   [distributed systems](https://bravenewgeek.com/tag/distributed-systems/)
*   [engineering culture](https://bravenewgeek.com/tag/engineering-culture/)
*   [engineering empathy](https://bravenewgeek.com/tag/engineering-empathy/)
*   [fault tolerance](https://bravenewgeek.com/tag/fault-tolerance/)
*   [gcp](https://bravenewgeek.com/tag/gcp/)
*   [go](https://bravenewgeek.com/tag/go/)
*   [infinitum](https://bravenewgeek.com/tag/infinitum-2/)
*   [java](https://bravenewgeek.com/tag/java-2/)
*   [kafka](https://bravenewgeek.com/tag/kafka/)
*   [konfigurate](https://bravenewgeek.com/tag/konfig/)
*   [kubernetes](https://bravenewgeek.com/tag/kubernetes/)
*   [message-oriented middleware](https://bravenewgeek.com/tag/message-oriented-middleware/)
*   [message queues](https://bravenewgeek.com/tag/message-queues/)
*   [messaging](https://bravenewgeek.com/tag/messaging/)
*   [microservices](https://bravenewgeek.com/tag/microservices/)
*   [nats](https://bravenewgeek.com/tag/nats/)
*   [nats streaming](https://bravenewgeek.com/tag/nats-streaming/)
*   [ops](https://bravenewgeek.com/tag/ops/)
*   [performance](https://bravenewgeek.com/tag/performance/)
*   [platform engineering](https://bravenewgeek.com/tag/platform-engineering/)
*   [process](https://bravenewgeek.com/tag/process/)
*   [product development](https://bravenewgeek.com/tag/product-development/)
*   [productivity](https://bravenewgeek.com/tag/productivity/)
*   [raft](https://bravenewgeek.com/tag/raft/)
*   [scalability](https://bravenewgeek.com/tag/scalability/)
*   [security](https://bravenewgeek.com/tag/security/)
*   [serverless](https://bravenewgeek.com/tag/serverless/)
*   [soa](https://bravenewgeek.com/tag/soa/)
*   [software engineering](https://bravenewgeek.com/tag/software-engineering-2/)
*   [stream processing](https://bravenewgeek.com/tag/stream-processing/)
*   [systems](https://bravenewgeek.com/tag/systems/)

[Proudly powered by WordPress](https://wordpress.org/)
