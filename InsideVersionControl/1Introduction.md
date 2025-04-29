
#  Version Control

##  What is Version Control?
Version Control is a **system that records changes** to files over time so developers can:
- Track changes
- Revert to previous versions
- Collaborate with others
- Identify who made specific changes

Also known as **Source Control** or **Source Code Management (SCM)**.

---

##  Key Features
- **Revision History**: Full record of changes to files and code
- **Identity**: Tracks *who* made each change
- **Collaboration**: Multiple developers can work together efficiently
- **Automation**: Integrates with CI/CD for deployments
- **Efficiency**: Enables agile, test-driven, and iterative workflows

---

##  Benefits
- Rollback faulty changes easily
- Review and understand changes via peer reviews
- Enhances team collaboration in Agile and DevOps workflows
- Maintains a “source of truth” for the entire project

---

##  Real-World Example (Meta)
- Uses a **monolithic repository** (all backend code in one place)
- Any engineer can edit or improve any part of the codebase
- Heavy use of **peer reviews** and **automated tests**
- Tools like `git blame` help trace the origin and reason behind code changes
- Emphasis on **small, reversible changes** and **gatekeepers** for safe production releases
- Collaboration extends across departments and includes non-engineers

---

##  Tips for Teams
- Use messaging and meetings to unblock each other
- Document changes clearly in commit messages
- Test thoroughly to avoid breaking shared services
- Encourage peer feedback to improve code quality
- Embrace diverse perspectives for better outcomes

---

##  DevOps & Agile Integration
- Version control supports Agile sprints and iterations
- Integral to CI/CD pipelines and deployment automation
- Helps in maintaining high-quality, fast-paced delivery cycles

---

##  Popular Version Control Systems
- Git (most common)
- Subversion (SVN)
- Mercurial

---

##  Commands to Remember (Git)
```bash
git init             # Initialize a repository
git status           # Show current status
git add .            # Stage all changes
git commit -m "msg"  # Commit staged changes
git log              # View commit history
git diff             # Show changes
git blame <file>     # Show who last modified each line
```

---

