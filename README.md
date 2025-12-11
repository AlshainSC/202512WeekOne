# 202512WeekOne - Developer Environment Challenge

Welcome to your first week challenge! This repository is designed to test and validate your understanding of essential developer tools and workflows.

## 🎯 Objective

Build a simple **command-line calculator** while demonstrating proficiency in:
- Git & GitHub workflows
- Linux command line basics
- Python programming fundamentals
- Docker basics

## 📋 How This Works

This challenge is structured across **5 branches**, each building on the previous one:

| Branch | Focus Area | What You'll Do |
|--------|-----------|----------------|
| `day1-environment` | Git & Linux | Validate your environment, create initial files |
| `day2-github` | GitHub & Branching | Practice branching, update documentation |
| `day3-python` | Python Basics | Write calculator functions |
| `day4-docker` | Docker Fundamentals | Demonstrate container knowledge |
| `day5-final` | Integration | Complete the CLI app, document your learning |

## 🚀 Getting Started

### 1. Clone This Repository
```bash
git clone <this-repo-url>
cd 202512WeekOne
```

### 2. Create Your Own Repository
- Create a **new repository** on your GitHub account named `202512WeekOne`
- Change the remote to point to YOUR repository:
```bash
git remote remove origin
git remote add origin git@github.com:YOUR_USERNAME/202512WeekOne.git
```

### 3. Start with Day 1
```bash
git checkout day1-environment
```

Each branch contains a `TASKS.md` file with specific instructions for that day.

## ✅ Completion Criteria

Each branch has automated tests that verify your work. When you push your changes, the tests will run automatically via GitHub Actions.

**Your final submission should include:**
- All 5 branches completed and pushed
- A working command-line calculator
- A `LEARNING_LOG.md` documenting your journey

## 📝 Branch Progression

Complete the branches **in order**. Each branch builds on the previous:

```
main
  └── day1-environment
        └── day2-github
              └── day3-python
                    └── day4-docker
                          └── day5-final
```

After completing each day's tasks:
1. Commit your changes
2. Push the branch to your repository
3. Move to the next branch

## 🏆 Extra Credit

- Dockerize your final calculator application
- Add additional calculator operations
- Implement error handling for edge cases

## ❓ Need Help?

- Review the original 5-Day Pre-Op Plan document
- Check the `TASKS.md` file in each branch for detailed instructions
- Use `git log` and `git status` to understand your current state

Good luck! 🍀
