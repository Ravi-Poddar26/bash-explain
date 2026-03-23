# Contributing to BashExplain

First off, thank you for considering contributing to BashExplain! It's people like you that make BashExplain a great learning tool for the Linux community.

## 🌟 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide the specific command or error message**
- **Explain the expected behavior**
- **Include your Python version and OS**

Example:
```
Title: "chmod explanation doesn't warn about 777 permissions"
Body: 
Steps to reproduce:
1. Run: bashexplain command "chmod 777 file.txt"
2. No warning appears

Expected: Should show safety warning about overly permissive permissions
Actual: No warning shown

Environment:
- Python 3.9.7
- Ubuntu 22.04
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar tools that have this feature**

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all classes and functions
- Keep functions focused and under 50 lines when possible
- Use type hints where appropriate

Example:
```python
def explain_command(self, command: str) -> str:
    """
    Explain a Bash command in detail
    
    Args:
        command: The bash command to explain
        
    Returns:
        A formatted string with the explanation
    """
    # Implementation
```

### Adding New Commands

To add a new command to the database:

1. Open `bash_explain.py`
2. Find the `COMMON_COMMANDS` dictionary in the `CommandExplainer` class
3. Add your command with a clear, concise description

```python
COMMON_COMMANDS = {
    # ... existing commands ...
    'newcmd': 'Brief description of what this command does',
}
```

**Guidelines for command descriptions:**
- Keep it under 10 words
- Focus on the main purpose
- Use simple, beginner-friendly language
- Avoid jargon when possible

### Adding New Error Patterns

To add a new error explanation:

1. Open `bash_explain.py`
2. Find the `ERROR_PATTERNS` dictionary in the `ErrorExplainer` class
3. Add your error pattern with regex and explanation

```python
ERROR_PATTERNS = {
    # ... existing patterns ...
    r'your-error-pattern': {
        'explanation': 'Clear explanation of what went wrong',
        'causes': [
            'First common cause',
            'Second common cause',
        ],
        'solutions': [
            'First solution to try',
            'Second solution to try',
        ]
    },
}
```

**Guidelines for error explanations:**
- Use regex patterns that match variations of the error
- Explain in plain language what the error means
- List causes from most to least common
- Provide actionable, safe solutions
- Avoid suggesting potentially dangerous fixes

### Adding New Flags

To add flag explanations:

1. Open `bash_explain.py`
2. Find the `COMMON_FLAGS` dictionary in the `CommandExplainer` class
3. Add your flag with explanation

```python
COMMON_FLAGS = {
    # ... existing flags ...
    '-X': 'Description of what this flag does',
}
```

**Guidelines for flag descriptions:**
- Keep it concise (under 8 words)
- Explain the effect, not just the name
- If a flag has different meanings for different commands, use the most common

### Testing

Before submitting a PR:

1. **Test your changes manually:**
```bash
python3 bash_explain.py command "your-test-command"
python3 bash_explain.py error "your-test-error"
```

2. **Run the test suite:**
```bash
python3 test_bashexplain.py
```

3. **Test edge cases:**
   - Empty input
   - Very long commands
   - Special characters
   - Multiple pipes and redirections

### Documentation

- Update README.md if you add new features
- Add examples for new functionality
- Update the roadmap if implementing planned features
- Keep the CHANGELOG.md updated

## 🎯 Good First Issues

Looking to get started? Check issues labeled `good-first-issue`:

- Adding common commands to the database
- Adding error patterns
- Improving existing explanations
- Adding examples to documentation
- Fixing typos

## 📋 Commit Messages

Write clear commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests

Examples:
```
Add explanation for rsync command

Fixes #123
```

```
Improve error handling for missing files

- Add try/catch for file operations
- Provide clearer error messages
- Update tests
```

## 🔍 Code Review Process

1. Maintainers will review your PR within a week
2. Feedback will be provided through PR comments
3. Make requested changes and push to your branch
4. Once approved, a maintainer will merge your PR

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all.

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy toward others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## 💬 Community

- **GitHub Discussions**: For questions and general discussion
- **GitHub Issues**: For bug reports and feature requests
- **Pull Requests**: For code contributions

## 🙏 Recognition

Contributors will be:
- Listed in the README.md
- Credited in release notes
- Added to CONTRIBUTORS.md

## 📚 Resources

- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
- [Regex Tutorial](https://www.regular-expressions.info/tutorial.html)

## ❓ Questions?

Feel free to:
- Open a discussion on GitHub
- Comment on existing issues
- Reach out to maintainers

Thank you for contributing to BashExplain! 🎉