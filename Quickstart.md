# Quick Start Guide

Get up and running with BashExplain in 2 minutes!

## Installation

### Option 1: Quick Download (Recommended for trying it out)

```bash
# Download the script
curl -O https://raw.githubusercontent.com/singhashish12238-pixel/bash-explain/main/bash_explain.py

# Make it executable
chmod +x bash_explain.py

# Try it out!
./bash_explain.py command "ls -la"
```

### Option 2: Clone Repository (Recommended for contributors)

```bash
# Clone the repository
git clone https://github.com/singhashish12238-pixel/bash-explain.git
cd bash-explain

# Make it executable
chmod +x bash_explain.py

# Try it out!
./bash_explain.py command "ls -la"
```

### Option 3: Install System-Wide

```bash
# Clone the repository
git clone https://github.com/singhashish12238-pixel/bash-explain.git
cd bash-explain

# Option A: Install using pip
pip install -e .

# Option B: On Python 3.12+ (Debian/Ubuntu), use pipx to avoid
# "externally managed environment" errors — recommended for CLI tools
pipx install .

# Now you can use it from anywhere!
bashexplain command "ls -la"
```

## Basic Usage

### 1. Explain a Command

```bash
bashexplain command "grep -r 'TODO' ."
```

**What you'll see:**
- Command name and purpose
- Explanation of each flag
- What each argument means
- Safety warnings (if applicable)

### 2. Understand an Error

```bash
bashexplain error "Permission denied"
```

**What you'll see:**
- Plain language explanation
- Common causes
- Step-by-step solutions

### 3. Analyze a Script

```bash
bashexplain script myscript.sh
```

**What you'll see:**
- Line-by-line breakdown
- Explanation of variables
- Control flow explanation
- Command usage

## Common Commands to Try

```bash
# File operations
bashexplain command "cp -r source/ dest/"
bashexplain command "find . -name '*.log' -delete"

# Text processing
bashexplain command "cat file.txt | grep error | wc -l"

# Git operations
bashexplain command "git log --oneline --graph --all"

# System administration
bashexplain command "sudo systemctl restart nginx"

# Docker
bashexplain command "docker run -it --rm ubuntu bash"
```

## Common Errors to Try

```bash
bashexplain error "command not found"
bashexplain error "Permission denied"
bashexplain error "No such file or directory"
bashexplain error "syntax error near unexpected token"
```

## Tips

### 1. Use Quotes for Complex Commands

```bash
# Good
bashexplain command "ls -la | grep txt"

# Won't work as expected
bashexplain command ls -la | grep txt
```

### 2. Check Before You Execute

```bash
# Before running an unfamiliar command, understand it first
bashexplain command "rm -rf node_modules"
```

### 3. Learn from Errors

```bash
# When you get an error, understand it
bashexplain error "bash: ./script.sh: Permission denied"
```

### 4. Combine with Other Tools

```bash
# First understand, then execute
bashexplain command "tar -czf backup.tar.gz ~/documents"
tar -czf backup.tar.gz ~/documents
```

## Next Steps

1. **Read the full README** for detailed features
2. **Check EXAMPLES.md** for more use cases
3. **Star the repository** if you find it helpful
4. **Contribute** by adding commands, errors, or features
5. **Share** with others who are learning Linux

## Getting Help

- Run `bashexplain --help` for CLI help
- Check the [GitHub Issues](https://github.com/singhashish12238-pixel/bash-explain/issues)
- Read the [full documentation](README.md)

## What's Next?

Try explaining commands you use every day to deepen your understanding!

```bash
# Your daily git workflow
bashexplain command "git add ."
bashexplain command "git commit -m 'Update docs'"
bashexplain command "git push origin main"

# Your deployment commands
bashexplain command "ssh user@server"
bashexplain command "scp file.txt user@server:/path"

# Your development workflow
bashexplain command "npm install"
bashexplain command "pytest tests/"
```

Happy learning! 