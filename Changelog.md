# Changelog

All notable changes to BashExplain will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-25

### Added
- Initial release of BashExplain
- Command explanation feature
  - Support for 50+ common commands (ls, cd, grep, git, docker, etc.)
  - Flag and argument parsing
  - Detection of pipes and redirections
  - Identification of file paths, variables, and patterns
- Error explanation feature
  - 10+ common error patterns with solutions
  - Plain language explanations
  - Multiple solutions for each error
  - Common causes analysis
- Script explanation feature
  - Line-by-line script analysis
  - Support for variables, conditionals, and loops
  - Function and control flow detection
  - Comment and shebang recognition
- Safety warnings system
  - Detection of dangerous commands (rm -rf /, chmod 777, etc.)
  - Warnings for executing untrusted scripts
  - Caution notices for sudo usage
- CLI interface with three modes: command, error, script
- Comprehensive documentation
  - README with installation and usage
  - Quick start guide
  - Examples document
  - Contributing guidelines
- Test suite for validation
- MIT License
- No external dependencies (pure Python)
- Offline-first operation

### Security
- No command execution - read-only analysis
- No root/sudo requirements
- No data collection or telemetry

## [Unreleased]

### Planned Features
- Interactive REPL mode
- Expanded command database (100+ commands)
- Advanced script parsing
  - Better handling of complex syntax
  - Function argument detection
  - Array and associative array support
- Support for other shells (zsh, fish)
- Plugin system for custom explanations
- Web interface
- IDE/editor integrations
  - VSCode extension
  - Vim plugin
  - Emacs mode
- Multilingual support
  - Spanish
  - French
  - German
  - Simplified Chinese
- Man page integration
- Colorized output with themes
- Export explanations to various formats (HTML, PDF, Markdown)
- History tracking of explained commands
- Learning path recommendations
- Quiz mode for testing knowledge
- Integration with package managers
  - pip install bashexplain
  - apt install bashexplain
  - homebrew formula

### Improvements Planned
- Better regex patterns for error detection
- More detailed flag explanations per command
- Context-aware suggestions
- Performance optimizations
- Enhanced safety warnings
- Better handling of command substitution
- Improved pipe chain visualization

---

## Version History Summary

- **1.0.0** (2026-03-25) - Initial Release
  - Core functionality: command, error, and script explanation
  - Safety warnings
  - 50+ commands, 10+ error patterns
  - Pure Python, no dependencies
  - Comprehensive documentation

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to BashExplain.

## Support

For bug reports and feature requests, please use [GitHub Issues](https://github.com/singhashish12238-pixel/bash-explain/issues).