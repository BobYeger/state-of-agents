## Introduction

When working on complex software projects, you often need to handle multiple tasks simultaneously, perhaps fixing a critical bug while also implementing a new feature. Traditional Git workflows might have you stashing changes or creating multiple clones of your repository, both of which have drawbacks. This is where Git worktrees shine, especially when paired with Claude Code's AI-powered assistance.

Git worktrees allow you to check out multiple branches from the same repository into separate directories, giving you isolated working environments while sharing the same Git history. When combined with Claude Code, you can run parallel AI-assisted coding sessions, each focused on different tasks without interference between them.

![Git Worktrees Workflow with Claude Code](https://nateross.dev/content/claude-code-tutorials/diagrams/git-worktrees-workflow.svg)

## Tutorial Overview

In this tutorial, we'll dive deep into using Git worktrees with Claude Code to manage parallel development tasks efficiently. We'll go beyond the basics to show you how to set up a sophisticated workflow that maximizes productivity across multiple features or bug fixes simultaneously.

#### What You'll Learn

- Setting up Git worktrees for isolated coding environments
- Running Claude Code in parallel across multiple worktrees
- Managing shared dependencies between worktrees
- Coordinating changes across feature branches
- Advanced worktree workflows for team coordination

#### Requirements

- Git installed (v2.17+)
- Claude Code CLI
- A Git repository to work with
- Basic familiarity with Git branching

## Understanding Git Worktrees

Before we dive into our custom examples, let's make sure we have a solid grasp of what Git worktrees are and how they work.

### What Are Git Worktrees?

A Git worktree is an additional working tree connected to your repository. While a traditional Git repository has one working directory, worktrees allow you to check out multiple branches into separate directories simultaneously, all connected to the same repository and sharing the same Git history.

### Why Use Worktrees Instead of Alternatives?

#### Worktrees vs. Stashing Changes

- No need to stash and unstash changes when switching contexts
- Multiple tasks remain accessible simultaneously
- Lower risk of stash conflicts or lost changes
- Cleaner separation of work in progress

#### Worktrees vs. Multiple Clones

- Single.git directory saves disk space
- Shared Git history and references
- Easier coordination between branches
- No need to push/pull between local clones
- Simplified management of related work

## Basic Worktree Setup

Let's start with setting up worktrees for a typical development scenario. Imagine you're working on a React application and need to simultaneously fix a critical bug while continuing development on a new feature.

### Creating Your First Worktree

First, let's create a new branch for our bug fix and set up a worktree for it:

```bash
# Create a new branch for the bug fix
git checkout -b bugfix/auth-issue

# Create a new worktree with this branch
git worktree add ../project-bugfix bugfix/auth-issue
```

This creates a new directory called `project-bugfix` in the parent directory of your current repository, with the `bugfix/auth-issue` branch checked out. Your original directory still has your previous branch checked out.

### Creating a Second Worktree for a Feature

Now, let's create another worktree for our feature development:

```bash
# Create a new branch for the feature
git checkout -b feature/user-profile

# Create a new worktree with this branch
git worktree add ../project-feature feature/user-profile
```

You now have three working directories, each with a different branch checked out:

- Original directory - your original branch (perhaps `main` or `develop`)
- `../project-bugfix` - the `bugfix/auth-issue` branch
- `../project-feature` - the `feature/user-profile` branch

## Running Claude Code in Multiple Worktrees

Now that we have separate worktrees set up, let's see how we can use Claude Code in each of them to work on different tasks simultaneously.

### Launching Claude Code in Your Bug Fix Worktree

```bash
# Navigate to your bug fix worktree
cd ../project-bugfix

# Launch Claude Code
claude

# In the Claude Code session:
# Ask Claude to help find and fix the authentication issue
Human: Please help me identify and fix authentication issues in our React application.
Users are sometimes getting logged out unexpectedly when navigating between pages.
Can you examine our auth provider implementation and token refresh logic?
```

### Simultaneously Running Claude Code in Your Feature Worktree

Open a new terminal window and run:

```bash
# Navigate to your feature worktree
cd ../project-feature

# Launch a separate Claude Code session
claude

# In this Claude Code session:
# Ask Claude to help with your feature development
Human: I'm implementing a new user profile page in our React app.
Can you help me create a component that allows users to update their profile information?
We need to include fields for name, bio, profile picture, and account preferences.
```

Now you have two Claude Code sessions running simultaneously, each focused on a different task and working with completely isolated code environments to prevent any interference between them.

### Benefits of Isolated Claude Code Sessions

Having separate Claude Code sessions in different worktrees provides several advantages:

- **Focused Context:** Each Claude instance has a clean, task-specific context, making its assistance more precise
- **No Confusion:** Claude doesn't mix up different tasks or branches in its understanding of your code
- **Conversation History:** Each session maintains its own conversation history relevant to its specific task
- **Independent Workflow:** You can pause or continue work on each task independently without affecting the other

## Custom Example: Coordinated Feature Development with Shared Components

Let's explore a more advanced real-world scenario: imagine you're working on a large-scale application where you need to develop two related features that will both use some shared components, but you want to develop them in parallel.

### Scenario Description

You're building an e-commerce platform and need to develop both a product recommendation system and a user preference settings page. Both features will share some UI components and utility functions, but you want to develop and test them independently before combining them.

### Implementation Steps

1. **Step 1: Create a shared components branch**
	First, we'll create a branch for our shared components:
	```bash
	# Start from your main development branch
	git checkout develop
	# Create a branch for shared components
	git checkout -b feature/shared-components
	# Create a worktree for this branch
	git worktree add ../ecommerce-shared feature/shared-components
	```
2. **Step 2: Create feature-specific branches and worktrees**
	```bash
	# Create recommendation feature branch from shared components
	git checkout -b feature/product-recommendations feature/shared-components
	# Create worktree for recommendations
	git worktree add ../ecommerce-recommendations feature/product-recommendations
	# Create preferences feature branch from shared components
	git checkout -b feature/user-preferences feature/shared-components
	# Create worktree for preferences
	git worktree add ../ecommerce-preferences feature/user-preferences
	```
3. **Step 3: Develop shared components with Claude Code**
	Navigate to the shared components worktree and use Claude Code to develop the common elements:
	```bash
	cd ../ecommerce-shared
	claude
	# In Claude Code session:
	Human: I need to create reusable UI components for our e-commerce app.
	Specifically, I need:
	1. A PreferenceToggle component that can be used for user settings
	2. A ProductCard component that can display product information
	3. A shared utility function for formatting pricing information
	Please help me implement these components in React with TypeScript.
	```
4. **Step 4: Start parallel development on both features**
	After implementing the shared components, commit and push your changes:
	```bash
	# In the shared components directory
	git add .
	git commit -m "Add shared UI components and utilities"
	git push -u origin feature/shared-components
	```
	Now update both feature branches with the shared components:
	```bash
	# Update the recommendations worktree
	cd ../ecommerce-recommendations
	git pull origin feature/shared-components
	# Update the preferences worktree
	cd ../ecommerce-preferences
	git pull origin feature/shared-components
	```
5. **Step 5: Use Claude Code to develop both features simultaneously**
	Open two terminal windows and run Claude Code in each worktree:
	In the first terminal (recommendations):
	```bash
	cd ../ecommerce-recommendations
	claude
	# In this Claude Code session:
	Human: Using our shared components (ProductCard and pricing utils),
	help me implement a product recommendation system that shows
	personalized product suggestions based on browsing history.
	```
	In the second terminal (preferences):
	```bash
	cd ../ecommerce-preferences
	claude
	# In this Claude Code session:
	Human: Using our shared PreferenceToggle component,
	help me create a user preferences page that allows
	users to set their notification settings, theme preferences, and privacy options.
	```
6. **Step 6: Periodically update shared components**
	If you need to make changes to shared components during development:
	```bash
	# Make changes in the shared components worktree
	cd ../ecommerce-shared
	# Make changes with Claude's help
	git commit -am "Update shared components with new features"
	git push
	# Update each feature branch
	cd ../ecommerce-recommendations
	git merge origin/feature/shared-components
	cd ../ecommerce-preferences
	git merge origin/feature/shared-components
	```

### Results and Benefits

This workflow provides several significant advantages:

- **Parallelized development:** You can work on multiple features simultaneously without context switching
- **Isolated environments:** Claude Code can focus on specific tasks without getting confused by unrelated code
- **Shared components:** You maintain centralized components while preventing feature branches from interfering with each other
- **Efficient merging:** When features are ready, they can be merged independently
- **Collaborative potential:** Different team members can work in different worktrees simultaneously

## Advanced Example: Implementing a Full-Stack Feature with Microservices

Let's explore an even more sophisticated example where Git worktrees and Claude Code help you implement a complex full-stack feature across multiple microservices, allowing you to context-switch between codebases with different languages and frameworks while maintaining a coherent mental model.

### Scenario Overview

Imagine you're working on a microservices-based application with:

- A frontend React application
- An authentication service (Node.js)
- A user data service (Python)
- A notification service (Go)

You need to implement a complex "password reset" feature that spans all these services. Using Git worktrees and Claude Code, you can tackle each service component in parallel without constantly switching mental contexts between programming languages and frameworks.

### Step-By-Step Implementation

1. **Step 1: Create a coordinated project setup with worktrees**
	First, create a project directory to organize your work:
	```bash
	# Create a project-specific directory
	mkdir -p ~/projects/password-reset-feature
	cd ~/projects/password-reset-feature
	# Create a project coordination document
	echo "# Password Reset Feature Implementation" > README.md
	echo "Coordinated implementation across microservices" >> README.md
	echo "- [ ] Frontend UI components (React)" >> README.md
	echo "- [ ] Authentication service endpoints (Node.js)" >> README.md
	echo "- [ ] User data service updates (Python)" >> README.md
	echo "- [ ] Notification service integration (Go)" >> README.md
	# Initialize Git repository for coordination
	git init
	git add README.md
	git commit -m "Initial project coordination setup"
	```
2. **Step 2: Set up worktrees for each service**
	Create a feature branch and worktree for each service repository:
	```bash
	# For the frontend repo
	cd ~/projects/frontend
	git checkout -b feature/password-reset
	git worktree add ~/projects/password-reset-feature/frontend feature/password-reset
	# For the auth service repo
	cd ~/projects/auth-service
	git checkout -b feature/password-reset
	git worktree add ~/projects/password-reset-feature/auth-service feature/password-reset
	# For the user data service repo
	cd ~/projects/user-data-service
	git checkout -b feature/password-reset
	git worktree add ~/projects/password-reset-feature/user-data-service feature/password-reset
	# For the notification service repo
	cd ~/projects/notification-service
	git checkout -b feature/password-reset
	git worktree add ~/projects/password-reset-feature/notification-service feature/password-reset
	```
3. **Step 3: Launch Claude Code sessions for parallel development**
	Now, open multiple terminal windows and launch Claude Code in each worktree to get specialized assistance tailored to each service's language and framework:
	#### Frontend (React) implementation with Claude Code
	```bash
	cd ~/projects/password-reset-feature/frontend
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET FRONTEND] I need to implement a password reset flow in our React application with the following screens:
	1. A "Forgot Password" form that asks for email
	2. A verification code entry screen
	3. A new password & confirmation screen
	4. A success confirmation screen
	Please help me create these components using our design system's elements and React Router.
	```
	#### Authentication Service (Node.js) implementation with Claude Code
	```bash
	cd ~/projects/password-reset-feature/auth-service
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET AUTH SERVICE] I need to implement new endpoints in our Node.js Express authentication service to handle password reset:
	1. POST /auth/forgot-password - Request a reset code
	2. POST /auth/verify-reset-code - Verify the code is valid
	3. POST /auth/reset-password - Update password with the verified code
	The service should handle token generation, verification, expiration, and communicate with the user service via gRPC.
	```
	#### User Data Service (Python) implementation with Claude Code
	```bash
	cd ~/projects/password-reset-feature/user-data-service
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET USER SERVICE] Help me implement the necessary changes in our Python Flask user data service to:
	1. Store and validate password reset codes
	2. Add methods to update user credentials securely
	3. Implement proper password hashing with modern best practices
	4. Update our database schemas with appropriate indices and constraints
	5. Implement input validation and error handling for reset requests
	```
	#### Notification Service (Go) implementation with Claude Code
	```bash
	cd ~/projects/password-reset-feature/notification-service
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET NOTIFICATION SERVICE] I need to enhance our Go notification service to:
	1. Send password reset emails with verification codes
	2. Create templates for the reset emails using our company branding
	3. Implement rate limiting for reset email requests
	4. Add metrics collection for successful/failed password resets
	5. Create appropriate logging for security audit purposes
	```
4. **Step 4: Coordinate implementations and test integrations**
	With all services being developed in parallel, you can use your project coordination directory to keep track of progress and test the integration:
	```bash
	cd ~/projects/password-reset-feature

	# Create a docker-compose file to run all services locally
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET INTEGRATION] I'm working on a password reset feature across multiple microservices. Help me create a docker-compose.yml file to run all these services locally for testing:
	1. React frontend on port 3000
	2. Node.js authentication service on port 3001
	3. Python user data service on port 3002
	4. Go notification service on port 3003
	Include configurations for:
	- A shared Redis instance for cross-service communication
	- A PostgreSQL database for persistent storage
	- A MailHog instance for testing email delivery
	```
5. **Step 5: Track implementation progress in the coordination repository**
	As you complete components of the feature, update your coordination repository:
	```bash
	cd ~/projects/password-reset-feature

	# Update the README with progress
	sed -i 's/- [ ] Frontend UI components (React)/- [x] Frontend UI components (React)/' README.md
	git commit -am "Complete frontend implementation for password reset"
	# Add integration test scripts and documentation
	mkdir -p integration-tests
	cd integration-tests
	# Use Claude Code to help create integration tests
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET INTEGRATION TESTS] Help me create integration tests for our password reset flow across multiple services:
	1. End-to-end user flow test using Cypress
	2. API integration tests with Jest for the authentication endpoints
	3. Email delivery verification tests for the notification service
	4. Load testing scripts to validate our rate limiting
	```
6. **Step 6: Finalize and prepare for review**
	Once all services are implemented and tested, prepare the changes for review:
	```bash
	# Commit and push all changes in each service
	cd ~/projects/password-reset-feature/frontend
	git commit -am "Complete password reset UI implementation"
	git push -u origin feature/password-reset
	cd ~/projects/password-reset-feature/auth-service
	git commit -am "Implement password reset endpoints and validation"
	git push -u origin feature/password-reset
	cd ~/projects/password-reset-feature/user-data-service
	git commit -am "Add password reset data storage and security features"
	git push -u origin feature/password-reset
	cd ~/projects/password-reset-feature/notification-service
	git commit -am "Implement password reset email notifications"
	git push -u origin feature/password-reset
	# Create pull requests for each service
	cd ~/projects/password-reset-feature
	claude
	# In Claude Code session:
	Human: [PASSWORD RESET PULL REQUESTS] Help me draft consistent pull request descriptions for each of our services implementing the password reset feature. Include:
	1. Feature overview that's consistent across all PRs
	2. Service-specific implementation details
	3. Testing instructions for reviewers
	4. Security considerations specific to each service
	5. Deployment notes and database migration steps where applicable
	```

### Benefits of This Approach

This sophisticated workflow using Git worktrees and Claude Code offers several powerful advantages for complex, cross-service feature development:

- **Language-specific assistance:** Each Claude Code session can focus on a specific programming language and framework
- **Simultaneous development:** Work on multiple services in parallel without mentally context-switching between languages
- **Coordinated implementation:** Maintain a central coordination point for the feature across services
- **Efficient organization:** Keep all feature-related code in a single directory structure
- **Integration testing:** More easily test the complete feature across services
- **Clear mental separation:** Each worktree gives you a clean slate for focused work
- **Enhanced productivity:** Leverage Claude's specialized knowledge across different tech stacks

This pattern is particularly valuable for developers who work in polyglot environments with microservices or need to maintain multiple versions of the same codebase. Git worktrees combined with Claude Code's assistance create a development environment that adapts to your complex workflow needs.

## Best Practices and Tips

- **Name worktrees descriptively:** Use meaningful names that indicate the branch or feature they contain
- **Clean up worktrees when done:** Use `git worktree remove <path>` to clean up worktrees you no longer need
- **Use absolute paths:** Specify absolute paths when creating worktrees to avoid confusion
- **Organize worktrees by feature:** Group related worktrees in a feature-specific parent directory
- **Combine with git aliases:** Create aliases for common worktree operations to streamline your workflow
	```bash
	# Add these to your ~/.gitconfig
	[alias]
	  wt = worktree
	  wta = worktree add
	  wtls = worktree list
	  wtmv = worktree move
	  wtrm = worktree remove
	```
- **Use consistent Claude Code prompts:** Start each Claude Code session with consistent identifiers to maintain context across worktrees

## Common Issues and Solutions

### Issue 1: Dependencies getting out of sync across worktrees

When working with multiple worktrees, especially in JavaScript/TypeScript projects, dependencies can get out of sync.

#### Solution:

Use symbolic links for node\_modules or use a tool like yarn workspaces:

```bash
# Create a shared node_modules directory
mkdir -p ~/shared/node_modules

# Remove existing node_modules and link to shared one
cd ~/projects/project-worktree-1
rm -rf node_modules
ln -s ~/shared/node_modules ./node_modules

# Do the same for other worktrees
cd ~/projects/project-worktree-2
rm -rf node_modules
ln -s ~/shared/node_modules ./node_modules

# Install dependencies in one location
cd ~/shared
npm install
```

### Issue 2: Conflicting Claude Code sessions and context confusion

Working with multiple Claude Code sessions can sometimes lead to context confusion.

#### Solution:

Clearly label your Claude Code sessions and use prefix tags in your prompts:

```bash
# Start Claude with a clear session identifier
claude

# Always start your prompts with a clear context tag
Human: [FEATURE-A] Let's continue working on the authentication implementation.

# Or use terminal titles to keep track of sessions
echo -e "\033]0;Claude: Feature A\007"
claude
```

### Issue 3: Forgetting which worktree you're in

When working with multiple worktrees, it's easy to forget which branch you're working on.

#### Solution:

Add branch information to your shell prompt and use different terminal colors:

```bash
# For bash users, add to ~/.bashrc
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export PS1="[e[36m]\w[e[91m]\$(parse_git_branch)[e[00m] $ "

# For zsh users with oh-my-zsh
# Edit your theme or .zshrc to include git branch information

# Use different terminal colors for different worktrees
# For example in iTerm or other terminal emulators
```

## Conclusion

Git worktrees transform how you manage parallel development tasks by providing isolated working environments that share a common Git history. When combined with Claude Code, this powerful workflow enables you to work on multiple features or services simultaneously with specialized AI assistance for each context.

This approach is particularly valuable for complex projects with microservices, polyglot environments, or situations where you need to maintain multiple versions of your code. By setting up dedicated worktrees for each task and launching Claude Code sessions in each environment, you can achieve a remarkable level of organization and productivity.

In the next tutorial, we'll explore how to leverage Claude Code's conversation resumption features to maintain context across multiple development sessions, building on the parallel workflow capabilities we've established here.

## Further Resources

Additional resources to deepen your understanding of Git worktrees and parallel development:

### Key Resources

[Claude Code Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#run-parallel-claude-code-sessions-with-git-worktrees)

Official Anthropic documentation for Git worktrees with Claude Code

[Git Worktrees Documentation](https://git-scm.com/docs/git-worktree)

Official Git documentation for managing multiple working trees

[Advanced Git Techniques](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)

Official Git documentation on advanced Git tools and techniques

[Git Worktree Tutorial](https://www.atlassian.com/git/tutorials/git-worktree)

Atlassian's detailed tutorial on Git worktrees for parallel workflows

[Managing Complex Git Workflows](https://gitbetter.substack.com/p/git-worktrees-the-best-git-feature)

In-depth exploration of Git worktrees as a productivity tool

[Git Worktrees in Practice](https://levelup.gitconnected.com/git-worktrees-the-best-git-feature-youve-never-heard-of-9cd21df67baf)

Real-world examples of Git worktrees in development teams

[Advanced Git Techniques](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)

Official Git documentation on advanced Git tools and techniques

[Managing Microservices Development](https://microservices.io/patterns/index.html)

Patterns and practices for effective microservices development

[Git Worktree Tutorial](https://www.atlassian.com/git/tutorials/git-worktree)

Atlassian's detailed tutorial on Git worktrees for parallel workflows