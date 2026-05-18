Title: Understanding Manus sandbox - your cloud computer

URL Source: https://manus.im/blog/manus-sandbox

Markdown Content:
[Product](https://manus.im/blog?kind=PRODUCT)·Wednesday, January 14

## Understanding Manus sandbox - your cloud computer

As the origin of Manus's name "Mens et Manus" (Mind and Hand) suggests, Manus aims to enable AI models not just to think, but to take action on your behalf. Among the "hands" we've given to AI models, the most powerful is a real cloud computer — the Manus Sandbox.

## What is Manus Sandbox?

Manus Sandbox is a fully isolated cloud virtual machine that Manus allocates for each task. Each Sandbox runs in its own environment, does not affect other tasks, and can execute in parallel.

The power of Sandbox lies in its completeness—just like the personal computer you use, it has full capabilities: networking, file system, browser, various software tools. Our AI Agent has been designed and trained to effectively choose and correctly use these tools to help you complete tasks. Moreover, with this computer, the AI can solve problems through what it does best—writing code—and can even help you create complete websites and mobile apps. All of this happens on the virtualization platform behind Manus. These Sandboxes can work 24/7 to complete the tasks you assign without consuming your local resources.


## Manus Sandbox Features

### What's in Your Sandbox

Your Manus Sandbox stores the files needed during task execution, including:

1.Attachments uploaded by you

2.Files and artifacts created and written by Manus during execution

3.Configurations needed by Manus to execute specific tasks (such as tokens uploaded by users, or tokens assigned by Manus to users for calling related APIs)

You can view all artifact files in the Sandbox via the "View all files in this task" entry in the top-right corner.


You can also simply ask Manus about the current Sandbox status and contents—for example, "Zip up all the code you've written so far and send it to me"—and Manus will access the Sandbox to fulfill your request.

### Sandbox Lifecycle

The Sandbox follows a predictable lifecycle that balances resource efficiency with persistence:

•Create: A Sandbox is created on demand in a new session

•Sleep/Awake: When the Sandbox is inactive (no operations, file edits, etc.), it will automatically go to sleep. When you return to the task and Manus needs to operate the Sandbox, it will be automatically woken up. During the sleep/wake cycle, the files and data in the Sandbox remain unchanged

•Recycle/Recreate: A continuously sleeping Sandbox may be recycled (Free users: 7 days; Manus Pro: 21 days). When you reopen the task after it has been recycled, a new Sandbox will be created automatically. Manus will also restore some files from the previous Sandbox into the new one: Manus artifacts, uploaded attachments, and important files such as Slides/WebDev will be restored automatically; intermediate code and temporary files created during execution will not be restored


Because Sandboxes can sleep, if you need to deploy a long-running backend service, you can use Manus's web development capability to build the frontend/backend and deploy it to the public internet.

### Sandbox Security

Our Manus Sandbox follows the [Zero Trust](https://en.wikipedia.org/wiki/Zero_trust_architecture) principle. Like a cloud VM you purchase from a cloud provider, you and Manus have full control over this computer—you can perform unrestricted operations (for example, gaining root access, modifying system files, or even formatting the entire disk). This allows Manus to complete tasks with minimal permission constraints.

Don't worry: any operations inside a Sandbox only affect that Sandbox. They do not impact the security or stability of the Manus service, and your session/account data cannot be accessed from the Sandbox. If an unrecoverable error occurs, Manus will automatically create a new Sandbox to replace it so the task can continue.

## Avoiding Accidental Sharing of Sensitive Data in Sandbox

As your private computer, the Sandbox may contain your personal sensitive information and data. Manus has strict privacy protection policies and measures in place and will not read or share any user data without user authorization. However, you still need to take measures to avoid accidental sharing of data in the Sandbox.

It's important to distinguish between two scenarios: "sharing" and "collaboration."

### Sharing

For task sharing (through the "Share" button in the upper right corner of Manus), the recipient will only see the messages in the task conversation and the output artifacts. The Sandbox is completely invisible to them. Therefore, you only need to be concerned about whether the conversation contains sensitive information, without worrying about the contents of the Sandbox being leaked.

### Collaboration

For task collaboration (through the collaboration button in the upper right corner of Manus, inviting specific users to participate), once a collaborator joins the session, they gain permission to participate in the task. This means collaborators can send instructions to the AI and control task execution. At this point, the Sandbox is also open to collaborators—they can access or modify files and data in the Sandbox through the AI, which may cause unexpected data leakage.

Additionally, Connectors will be automatically disabled once collaboration is enabled, so you don't need to worry about collaborators accessing your Connectors.


You can use the table above to understand the accessibility of task content to other users in different scenarios, and confirm that your private data will not be leaked before sharing or collaborating.

## Privacy Best Practices

•Since the Sandbox is essentially your private computer, double-check whether it contains sensitive content you don't want collaborators to access before adding collaborators

•If the task already contains sensitive content, create a new task, copy only the necessary content and artifacts, and then invite collaborators to that task

•Avoid sending personal sensitive information in a collaboration session

## Availability

The Manus Sandbox is a core component of our platform and is available to all users across all subscription tiers.

## Common Questions

Q: What happens to my files when a Sandbox is recycled?

A: Manus automatically restores your most important files—artifacts, uploaded attachments, and project files like Slides/WebDev—to the new Sandbox. Intermediate code and temporary files are not restored.

Q: How long before my Sandbox is recycled?

A: Free users have a 7-day retention period, while Manus Pro users have 21 days of retention before an inactive Sandbox is recycled.

Q: Can collaborators access my Connectors through the Sandbox?

A: No. Connectors are automatically disabled when collaboration is enabled, ensuring collaborators cannot access your connected services.

The Manus Sandbox represents the foundation of how Manus takes action on your behalf. By providing a persistent, secure, and fully-featured cloud computing environment, we're enabling a new class of AI-powered work that goes beyond conversation into real execution.

## References

### Download desktop & mobile app

Access Manus anytime, anywhere.
