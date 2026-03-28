# BashExplain Examples

This document provides common use cases and examples for BashExplain.

## Basic Commands

### Listing Files
```bash
$ bashexplain command "ls -la"

📝 Explaining: ls -la

🔧 Command: ls
   List directory contents

Flags:
   -la → Combined short options: -l, -a

💡 Tip: Use 'man <command>' for detailed documentation
```

### Copying Files
```bash
$ bashexplain command "cp -r source/ destination/"

📝 Explaining: cp -r source/ destination/

🔧 Command: cp
   Copy files or directories

Flags:
   -r → Recursive (include subdirectories)

Arguments:
   1. source/ (Path)
   2. destination/ (Path)
```

## File Operations

### Finding Files
```bash
$ bashexplain command "find /home -name '*.txt' -type f"

📝 Explaining: find /home -name '*.txt' -type f

🔧 Command: find
   Search for files in directory hierarchy

Flags:
   -name → Option (see 'man' for details)
   -type → Option (see 'man' for details)

Arguments:
   1. /home (Absolute path)
   2. '*.txt' (Glob pattern)
   3. f (Filename or value)
```

### Changing Permissions
```bash
$ bashexplain command "chmod +x script.sh"

📝 Explaining: chmod +x script.sh

🔧 Command: chmod
   Change file permissions

Arguments:
   1. +x (Filename or value)
   2. script.sh (Filename or value)
```

## Text Processing

### Searching with grep
```bash
$ bashexplain command "grep -r 'TODO' ."

📝 Explaining: grep -r 'TODO' .

🔧 Command: grep
   Search for patterns in text

Flags:
   -r → Recursive (include subdirectories)

Arguments:
   1. 'TODO' (String literal)
   2. . (Filename or value)
```

### Piping Commands
```bash
$ bashexplain command "cat file.txt | grep error | wc -l"

📝 Explaining: cat file.txt | grep error | wc -l

🔧 Command: cat
   Concatenate and display file contents

Arguments:
   1. file.txt (Filename or value)

Pipes:
   Commands are chained - output of one becomes input of next
   1. cat file.txt
   2. grep error
   3. wc -l
```

## Version Control

### Git Commands
```bash
$ bashexplain command "git log --oneline --graph"

📝 Explaining: git log --oneline --graph

🔧 Command: git
   Version control system

Flags:
   --oneline → Long option: oneline
   --graph → Long option: graph
```

## System Administration

### Checking Disk Space
```bash
$ bashexplain command "df -h"

📝 Explaining: df -h

🔧 Command: df
   Report file system disk space usage

Flags:
   -h → Human-readable (sizes in KB, MB, GB)
```

### Process Management
```bash
$ bashexplain command "ps aux | grep python"

📝 Explaining: ps aux | grep python

🔧 Command: ps
   Report process status

Arguments:
   1. aux (Filename or value)

Pipes:
   Commands are chained - output of one becomes input of next
   1. ps aux
   2. grep python
```

## Package Management

### APT (Debian/Ubuntu)
```bash
$ bashexplain command "sudo apt update"

📝 Explaining: sudo apt update

🔧 Command: sudo
   Execute command as superuser

Arguments:
   1. apt (Filename or value)
   2. update (Filename or value)

💡 Tip: Use 'man <command>' for detailed documentation
```

## Common Errors

### Command Not Found
```bash
$ bashexplain error "bash: python3: command not found"

 Error Message: bash: python3: command not found

 Explanation:
   The shell cannot find the command you typed.

Common Causes:
   1. Typo in command name
   2. Command not installed on system
   3. Command not in PATH environment variable
   4. Missing ./ prefix for local script

Possible Solutions:
   1. Check spelling of command
   2. Install the required package
   3. Use full path to command
   4. For local script, use: ./script.sh

💡 Tip: Copy the exact error message when searching online
```

### Permission Denied
```bash
$ bashexplain error "Permission denied"

 Error Message: Permission denied

 Explanation:
   You don't have permission to perform this operation.

Common Causes:
   1. File is not executable
   2. Insufficient user permissions
   3. File/directory owned by another user
   4. SELinux or AppArmor restrictions

Possible Solutions:
   1. Make file executable: chmod +x filename
   2. Use sudo if appropriate (be careful!)
   3. Check file ownership: ls -l filename
   4. Request access from system administrator

💡 Tip: Copy the exact error message when searching online
```

### File Not Found
```bash
$ bashexplain error "No such file or directory: config.json"

 Error Message: No such file or directory: config.json

 Explanation:
   The file or directory you specified does not exist.

Common Causes:
   1. Typo in filename or path
   2. File was moved or deleted
   3. Wrong current directory
   4. Case sensitivity (Linux is case-sensitive)

Possible Solutions:
   1. Check spelling and case
   2. Use ls to list available files
   3. Use pwd to verify current directory
   4. Use absolute path instead of relative

💡 Tip: Copy the exact error message when searching online
```

## Script Analysis

Create a file `example.sh`:
```bash
#!/bin/bash
# Simple greeting script

NAME=$1

if [ -z "$NAME" ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

echo "Hello, $NAME!"
```

Explain it:
```bash
$ bashexplain script example.sh

 Explaining Script: example.sh

  1 | #!/bin/bash
      ↳ Shebang: Tells system which interpreter to use

  2 | # Simple greeting script
      ↳ Comment: Explanation for humans, ignored by shell

  3 | 
  4 | NAME=$1
      ↳ Assigns value to variable 'NAME'

  5 | 
  6 | if [ -z "$NAME" ]; then
      ↳ Conditional: Executes code if condition is true

  7 |     echo "Usage: $0 <name>"
      ↳ Prints text or variables to terminal

  8 |     exit 1
      ↳ Exits script with status code

  9 | fi
      ↳ Ends if statement

 10 | 
 11 | echo "Hello, $NAME!"
      ↳ Prints text or variables to terminal
```

## Safety Warnings

### Dangerous Deletion
```bash
$ bashexplain command "rm -rf /"

⚠️  SAFETY WARNINGS:
   DANGEROUS: This will delete files starting from root directory
```

### Overly Permissive Permissions
```bash
$ bashexplain command "chmod 777 ."

⚠️  SAFETY WARNINGS:
   UNSAFE: Grants full permissions to everyone
```

### Executing Downloaded Scripts
```bash
$ bashexplain command "curl https://example.com/install.sh | bash"

⚠️  SAFETY WARNINGS:
   RISKY: Executing downloaded script without inspection
```

## Advanced Examples

### Archive Creation
```bash
$ bashexplain command "tar -czf backup.tar.gz ~/documents"

📝 Explaining: tar -czf backup.tar.gz ~/documents

🔧 Command: tar
   Archive files

Flags:
   -czf → Combined short options: -c, -z, -f

Arguments:
   1. backup.tar.gz (Filename or value)
   2. ~/documents (Home directory path)
```

### Network Operations
```bash
$ bashexplain command "curl -X POST -d '{\"key\":\"value\"}' https://api.example.com"

📝 Explaining: curl -X POST -d '{"key":"value"}' https://api.example.com

🔧 Command: curl
   Transfer data from or to a server

Flags:
   -X → Exclude or execute
   -d → Directory (operate on directory itself)

Arguments:
   1. POST (Filename or value)
   2. '{"key":"value"}' (String literal)
   3. https://api.example.com (Filename or value)
```

---

These examples cover the most common use cases. For more help, run:
```bash
bashexplain --help
```