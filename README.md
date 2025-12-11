# 202512WeekOne - Developer Environment Assessment

This repository serves as a practical assessment of your understanding of essential developer tools and workflows. Over the course of five days, you will build a simple command-line calculator while demonstrating competency in the following areas:

- Git and GitHub workflows
- Linux command line operations
- Python programming fundamentals
- Docker container basics

## Structure

This assessment is organized across five branches, each building upon the previous one:

| Branch | Focus Area | Description |
|--------|-----------|-------------|
| `day1-environment` | Git and Linux | Environment validation and initial file creation |
| `day2-github` | GitHub and Branching | Branch workflows and documentation |
| `day3-python` | Python Basics | Calculator function implementation |
| `day4-docker` | Docker Fundamentals | Container operations and concepts |
| `day5-final` | Integration | Complete CLI application and reflection |

## Getting Started

### Step 1: Clone This Repository
```bash
git clone <this-repo-url>
cd 202512WeekOne
```

### Step 2: Create Your Own Repository
Create a new repository on your GitHub account named `202512WeekOne`, then update your local remote:
```bash
git remote remove origin
git remote add origin git@github.com:YOUR_USERNAME/202512WeekOne.git
```

### Step 3: Begin Day 1
```bash
git checkout day1-environment
```

Each branch contains a `TASKS.md` file with detailed instructions for that day's work.

## Completion Criteria

Each branch includes automated tests that verify your work. When you push your changes, these tests run automatically via GitHub Actions. You can view the results in the Actions tab of your repository.

Your final submission must include:
- All five branches completed and pushed to your repository
- A working command-line calculator application
- A `LEARNING_LOG.md` file documenting your learning process

## Branch Progression

Complete the branches in order. Each branch builds on the work from the previous day:

```
main
  └── day1-environment
        └── day2-github
              └── day3-python
                    └── day4-docker
                          └── day5-final
```

After completing each day's tasks:
1. Commit your changes with a descriptive message
2. Push the branch to your repository
3. Proceed to the next branch

## Extra Credit

The following extensions are optional but encouraged:
- Dockerize your final calculator application
- Implement additional calculator operations
- Add robust error handling for edge cases

## Resources

If you encounter difficulties:
- Review the original 5-Day Pre-Op Plan document
- Consult the `TASKS.md` file in each branch for detailed guidance
- Use `git log` and `git status` to understand your repository state
