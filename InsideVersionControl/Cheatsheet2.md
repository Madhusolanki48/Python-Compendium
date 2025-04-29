### **Unix & Bash Commands CheatSheet**

---

### **Useful Concepts**
| Concept | Use |
|---------|-----|
| `man [command]` | Show manual/help for a command |
| **Flags** | Modify command behavior (e.g., `-a`, `-l`) |

---

### **Common Unix Commands**
| Command | Description |
|---------|-------------|
| `cd` | Change directory |
| `ls` | List directory contents |
| `ls -l` | Long format with details |
| `ls -a` | Include hidden files |
| `pwd` | Show current directory path |
| `mkdir` | Make a new directory |
| `cp` | Copy files/directories |
| `mv` | Move/rename files |
| `rm` | Remove files |
| `rmdir` | Remove empty directories |
| `touch` | Create a new empty file |
| `cat` | View content of a file |
| `clear` | Clear the terminal screen |
| `exit` | Exit the terminal |
| `echo` | Print text to the terminal |

---

### **Pipes, Grep, and Redirection**

| **Command**                       | **Description**                                                           | **Example**                                          |
|------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------|
| **Pipes (`|`)**                    | Pass output of one command to another command.                            | `ls | wc -w` (Counts files in current directory)      |
| **Multiple Files Word Count**     | Use pipe for word count across multiple files.                            | `cat file1.txt file2.txt | wc -w`                    |
| **Grep (Search for Patterns)**     | Search for patterns in files.                                             | `grep "Sam" names.txt`                              |
| **Grep (Case-Insensitive)**        | Search ignoring case sensitivity.                                          | `grep -i "sam" names.txt`                           |
| **Grep (Exact Word Match)**        | Match the exact word, no partial matches.                                 | `grep -w "Sam" names.txt`                           |
| **Grep with Pipe**                 | Combine pipe with `grep` for filtering results.                           | `ls /bin | grep "zip"`                               |
| **Redirection (Standard Input `<`)** | Redirect input from a file.                                               | `cat < input.txt`                                    |
| **Redirection (Standard Output `>`)** | Redirect output to a file.                                                | `ls -l > output.txt`                                 |
| **Redirection (Standard Error `2>`)** | Redirect error messages to a file.                                        | `ls /nonexistentdir 2> error.txt`                   |
| **Redirection (Combine Output and Error `&>`)** | Redirect both output and errors to a file.                               | `ls /bin > output.txt 2>&1`                          |

---

### **Basic Navigation & Listing**
| Command | Description |
|--------|-------------|
| `cd ~` | Navigate to home directory |
| `ls -la` | List all files (including hidden ones) in long format |
| `less .bashrc` | View `.bashrc` config file (shell behavior) |
| `less .profile` | View `.profile` (used for environment variables) |
| `q` | Quit `less` viewer |

---

### **File and Directory Management**
| **Action**                     | **Command**                                  | **Description**                                                      |
|---------------------------------|----------------------------------------------|----------------------------------------------------------------------|
| **Check Current Directory**     | `pwd`                                        | Shows current directory (e.g., `/root`)                               |
| **List Directory Contents**     | `ls -l`                                      | Lists directory contents with details                                 |
| **Create a Directory**          | `mkdir submissions`                          | Creates a new directory named `submissions`                           |
| **Check if Created**            | `ls -l`                                      | You should now see `submissions/`                                     |
| **Enter the Directory**         | `cd submissions`<br> `ls`                    | Navigates into `submissions` and checks contents (should be empty)    |
| **Create Text Files**           | `touch test1.txt`<br> `touch test2.txt`<br> `ls -l` | Creates `test1.txt` and `test2.txt`, confirms they're created       |
| **Go Back to Parent Directory** | `cd ..`<br> `ls -l`                          | Navigates back and lists directories (`projects/`, `submissions/`)   |
| **Create Another Directory**    | `mkdir archive`<br> `ls -l`                  | Creates `archive/`, now three dirs: `projects/`, `submissions/`, `archive/` |
| **Move a Directory**            | `mv submissions archive`<br> `ls -l`         | Moves `submissions/` inside `archive/`                                |
| **Check If Moved**              | `cd archive`<br> `ls -l`                     | Confirms `submissions/` is now inside `archive/`                      |
| **Check Files Were Moved Too**  | `cd submissions`<br> `ls -l`                 | Both `test1.txt` and `test2.txt` should still be inside              |
| **Create a Shell Script**       | `vim testshell.sh`<br> Press `i`<br> `#!/bin/bash`<br> `echo "Hello World"`<br> Press `Esc`<br> `:wq!` | Open vim editor, write script, save and exit                           |
| **Make Script Executable**      | `chmod 755 testshell.sh`<br> `./testshell.sh` | Make script executable and run it                                     |

---
