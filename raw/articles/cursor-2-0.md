Today, we’re releasing two big updates that make Cursor the best place to work with agents: our first coding model, Composer, and a new interface for working with many agents in parallel.

## Introducing Composer

Composer is a frontier model that is 4x faster than similarly intelligent models.

The model is built for low-latency agentic coding in Cursor, completing most turns in under 30 seconds. Early testers found the ability to iterate quickly with the model delightful and trust the model for multi-step coding tasks.

Composer was [trained](https://cursor.com/blog/composer) with a set of powerful tools including codebase-wide semantic search, making it much better at understanding and working in large codebases.

![](https://cursor.com/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2F2-0-0.png&w=1920&q=70)

## The multi-agent interface

The first thing you’ll notice when you open Cursor is our new interface.

It’s more focused and designed from the ground up to be centered around agents rather than files. So you can focus on the outcomes you want while agents take care of the details. When you need to dive deep into the code, you can still easily open files in the new layout or switch back to the classic IDE.

![](https://cursor.com/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2F2-0-1.jpg&w=1920&q=70)

Cursor 2.0 makes it easy to run many agents in parallel without them interfering with one another, powered by git worktrees or remote machines. We’ve even found that having multiple models attempt the same problem and picking the best result significantly improves the final output, especially for harder tasks.

As we use agents more for coding, we’ve seen two new bottlenecks emerge: reviewing code and testing the changes. With Cursor 2.0, we’re also starting to solve both of these. We’ve made it much easier to quickly review the changes an agent has made and dive deeper into the code when you need to. We’ve also built a native browser tool that allows Cursor to test its work and iterate until it has produced the correct final result.

## Start building

Cursor 2.0 is now available: [cursor.com/download](http://cursor.com/download).

View the full [changelog](https://cursor.com/changelog/2-0) to see all features.