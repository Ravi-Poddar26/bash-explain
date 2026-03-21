#!/usr/bin/env python3
"""
Test suite for BashExplain
Demonstrates functionality with various examples
"""

import subprocess
import sys

# ANSI color codes for better output
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def run_test(description, command):
    """Run a single test case"""
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{GREEN}TEST: {description}{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")

def main():
    print(f"{YELLOW}")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║           BashExplain - Comprehensive Test Suite              ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    
    # Test 1: Simple command
    run_test(
        "Simple ls command",
        "python3 bash_explain.py command 'ls -la'"
    )
    
    # Test 2: Complex command with pipes
    run_test(
        "Command with pipes and grep",
        "python3 bash_explain.py command 'cat file.txt | grep error | wc -l'"
    )
    
    # Test 3: Dangerous command
    run_test(
        "Dangerous command warning",
        "python3 bash_explain.py command 'chmod 777 myfile'"
    )
    
    # Test 4: Command with redirection
    run_test(
        "Command with output redirection",
        "python3 bash_explain.py command 'echo hello > output.txt'"
    )
    
    # Test 5: Git command
    run_test(
        "Git command with flags",
        "python3 bash_explain.py command 'git log --oneline --graph --all'"
    )
    
    # Test 6: Find command
    run_test(
        "Find command with complex options",
        "python3 bash_explain.py command 'find /home -name *.txt -type f'"
    )
    
    # Test 7: Error - command not found
    run_test(
        "Error: command not found",
        "python3 bash_explain.py error 'bash: foobar: command not found'"
    )
    
    # Test 8: Error - permission denied
    run_test(
        "Error: Permission denied",
        "python3 bash_explain.py error 'Permission denied'"
    )
    
    # Test 9: Error - no such file
    run_test(
        "Error: No such file or directory",
        "python3 bash_explain.py error 'No such file or directory: config.txt'"
    )
    
    # Test 10: Script explanation
    run_test(
        "Script explanation",
        "python3 bash_explain.py script sample_backup.sh"
    )
    
    # Test 11: Docker command
    run_test(
        "Docker command",
        "python3 bash_explain.py command 'docker run -it --rm -v /data:/data ubuntu bash'"
    )
    
    # Test 12: Tar command
    run_test(
        "Tar archive command",
        "python3 bash_explain.py command 'tar -czf backup.tar.gz /home/user'"
    )
    
    print(f"\n{YELLOW}{'='*70}{RESET}")
    print(f"{GREEN}All tests completed!{RESET}")
    print(f"{YELLOW}{'='*70}{RESET}\n")

if __name__ == '__main__':
    main()