"""
BashExplain - A command-line tool to explain Bash commands, errors, and scripts
"""

import sys
import re
import argparse
from typing import Dict, List, Tuple, Optional


class CommandExplainer:
    """Explains individual Bash commands and their components"""
    
    COMMON_COMMANDS = {
        'ls': 'List directory contents',
        'cd': 'Change directory',
        'pwd': 'Print working directory',
        'mkdir': 'Make directory',
        'rmdir': 'Remove empty directory',
        'rm': 'Remove files or directories',
        'cp': 'Copy files or directories',
        'mv': 'Move or rename files',
        'cat': 'Concatenate and display file contents',
        'grep': 'Search for patterns in text',
        'find': 'Search for files in directory hierarchy',
        'chmod': 'Change file permissions',
        'chown': 'Change file owner and group',
        'sudo': 'Execute command as superuser',
        'apt': 'Package manager (Debian/Ubuntu)',
        'yum': 'Package manager (RedHat/CentOS)',
        'systemctl': 'Control systemd services',
        'ps': 'Report process status',
        'kill': 'Send signal to process',
        'top': 'Display running processes',
        'echo': 'Display text or variables',
        'export': 'Set environment variable',
        'source': 'Execute commands from file in current shell',
        'tar': 'Archive files',
        'gzip': 'Compress files',
        'gunzip': 'Decompress files',
        'wget': 'Download files from the web',
        'curl': 'Transfer data from or to a server',
        'ssh': 'Secure shell remote login',
        'scp': 'Secure copy files over SSH',
        'git': 'Version control system',
        'docker': 'Container platform',
        'pip': 'Python package installer',
        'npm': 'Node.js package manager',
        'touch': 'Create empty file or update timestamp',
        'head': 'Display first lines of file',
        'tail': 'Display last lines of file',
        'less': 'View file contents page by page',
        'more': 'View file contents page by page (simpler)',
        'diff': 'Compare files line by line',
        'sed': 'Stream editor for text transformation',
        'awk': 'Pattern scanning and text processing',
        'sort': 'Sort lines of text',
        'uniq': 'Remove duplicate lines',
        'wc': 'Word, line, and byte count',
        'man': 'Display manual pages',
        'which': 'Show full path of command',
        'whereis': 'Locate binary, source, and manual page',
        'alias': 'Create command shortcut',
        'history': 'Show command history',
        'df': 'Report file system disk space usage',
        'du': 'Estimate file space usage',
        'free': 'Display memory usage',
        'uname': 'Print system information',
        'hostname': 'Show or set system hostname',
        'ping': 'Test network connectivity',
        'netstat': 'Network statistics',
        'ifconfig': 'Configure network interface',
        'ip': 'Show/manipulate routing and network devices',
    }

    COMMON_FLAGS = {
        '-a': 'All (include hidden files)',
        '-l': 'Long format (detailed listing)',
        '-h': 'Human-readable (sizes in KB, MB, GB)',
        '-r': 'Recursive (include subdirectories)',
        '-f': 'Force (don\'t prompt for confirmation)',
        '-v': 'Verbose (show detailed output)',
        '-i': 'Interactive (prompt before action)',
        '-n': 'Numeric (use numbers instead of names)',
        '-p': 'Parent (create parent directories if needed)',
        '-R': 'Recursive (uppercase version)',
        '-d': 'Directory (operate on directory itself)',
        '-s': 'Silent or summarize',
        '-u': 'Update or user',
        '-g': 'Group',
        '-o': 'Output file',
        '-e': 'Expression or edit',
        '-w': 'Word match',
        '-c': 'Count',
        '-x': 'Exclude or execute',
        '-z': 'Compress',
        '-t': 'Time or timestamp',
        '-k': 'Kill or kilobytes',
        '-m': 'Modify or message',
        '-q': 'Quiet (suppress output)',
        '-y': 'Yes (assume yes to prompts)',
        '-b': 'Backup',
        '--help': 'Display help information',
        '--version': 'Display version information',
        '--force': 'Force operation (do not prompt for confirmation)',
        '--recursive': 'Operate recursively (same as -r)',
        '--no-preserve-root': 'Do not treat "/" as special for "rm -rf" (dangerous)',
        '--dry-run': 'Show what would be done without making changes',
        '--no-clobber': 'Do not overwrite existing files',
        '--verbose': 'Show detailed output (same as -v)',
        '--quiet': 'Suppress most output (same as -q)',
    }

    UNSAFE_PATTERNS = [
        (r'rm\s+-rf\s+/', 'DANGEROUS: This will delete files starting from root directory'),
        (r'rm\s+-rf\s+--no-preserve-root', 'EXTREMELY DANGEROUS: Overrides safety and can delete the entire filesystem'),
        (r'rm\s+-rf\s+\.', 'DANGEROUS: Deletes the current directory recursively'),
        (r'rm\s+-rf\s+\*', 'DANGEROUS: Deletes all files in the current directory'),
        (r'chmod\s+777', 'UNSAFE: Grants full permissions to everyone'),
        (r'curl\s+.*\|\s*bash', 'RISKY: Executing downloaded script without inspection'),
        (r'curl\s+-sSL\s+.*\|\s*sh', 'RISKY: Silent download-and-execute without inspection'),
        (r'wget\s+.*\|\s*sh', 'RISKY: Executing downloaded script without inspection'),
        (r'wget\s+-qO-.*\|\s*bash', 'RISKY: Silent download-and-execute without inspection'),
        (r'sudo\s+chmod', 'CAUTION: Changing permissions as superuser'),
        (r'sudo\s+rm', 'CAUTION: Deleting files as superuser'),
        (r':\(\)\{.*\};:', 'DANGEROUS: Fork bomb - will crash system'),
        (r'dd\s+if=.*of=/dev/(?:sd|nvme|mmcblk)\b', 'DANGEROUS: Writing raw data to a disk device'),
        (r'fdisk\s+/dev/(?:sd|nvme|mmcblk)', 'DANGEROUS: Partitioning can destroy existing data'),
        (r'mkfs\.?', 'DANGEROUS: Formatting disk - will erase all data'),
        (r'echo\s+.*>\s*/etc/passwd', 'DANGEROUS: Overwriting system password file'),
        (r'kill\s+-9\s+1\b', 'DANGEROUS: Killing init process may crash the system'),
        (r'iptables\s+-F', 'CAUTION: Flushing firewall rules may break connectivity'),
        (r'systemctl\s+stop\s+ssh', 'CAUTION: Stopping SSH may lock you out of remote servers'),
        (r'chown\s+-R\s+root:root\s+/', 'CAUTION: Recursively changing ownership of root can break permissions'),
        (r'>\s*/dev/(?:sd|nvme|mmcblk)', 'DANGEROUS: Redirecting output to a disk device can overwrite it'),
        (r'cat\s+/dev/zero\s*>\s*/dev/(?:sd|nvme|mmcblk)', 'DANGEROUS: Overwriting disk with zeros'),
        (r'nohup\s+.*&\s*$', 'CAUTION: Backgrounding processes without control may leave unmanaged jobs'),
    ]

def explain_command(self, command: str) -> str:
        """Explain a Bash command in detail"""
        command = command.strip()
        
        if not command:
            return "No command provided."
        
        output = []
        output.append(f" Explaining: {command}\n")
        
        # Check for unsafe patterns
        warnings = self._check_safety(command)
        if warnings:
            output.append("⚠️  SAFETY WARNINGS:")
            for warning in warnings:
                output.append(f"   {warning}")
            output.append("")
        
        # Parse the command
        parts = self._parse_command(command)
        
        # Explain main command
        if parts['command']:
            cmd_name = parts['command']
            cmd_desc = self.COMMON_COMMANDS.get(cmd_name, 'Custom command or script')
            output.append(f"🔧 Command: {cmd_name}")
            output.append(f"   {cmd_desc}\n")
        
        # Explain flags
        if parts['flags']:
            output.append("Flags:")
            for flag in parts['flags']:
                flag_desc = self.COMMON_FLAGS.get(flag, self._guess_flag_meaning(flag))
                output.append(f"   {flag} → {flag_desc}")
            output.append("")
        
        # Explain arguments
        if parts['arguments']:
            output.append("Arguments:")
            for i, arg in enumerate(parts['arguments'], 1):
                arg_type = self._identify_argument_type(arg)
                output.append(f"   {i}. {arg} ({arg_type})")
            output.append("")
        
        # Explain pipes
        if parts['pipes']:
            output.append("Pipes:")
            output.append("   Commands are chained - output of one becomes input of next")
            for i, pipe_cmd in enumerate(parts['pipes'], 1):
                output.append(f"   {i}. {pipe_cmd}")
            output.append("")
        
        # Explain redirections
        if parts['redirections']:
            output.append("Redirections:")
            for redir in parts['redirections']:
                output.append(f"   {redir['symbol']} {redir['target']} → {redir['description']}")
            output.append("")
        
        # Add educational note
        output.append("💡 Tip: Use 'man <command>' for detailed documentation")
        
        return "\n".join(output)
def _parse_command(self, command: str) -> Dict:
        """Parse command into components"""
        result = {
            'command': None,
            'flags': [],
            'arguments': [],
            'pipes': [],
            'redirections': []
        }
        
        # Check for pipes
        if '|' in command:
            pipe_parts = command.split('|')
            result['pipes'] = [p.strip() for p in pipe_parts]
            command = pipe_parts[0].strip()  # Process first part
        
        # Check for redirections
        redir_patterns = [
            (r'>>?\s*(\S+)', 'redirect output to file'),
            (r'2>>?\s*(\S+)', 'redirect errors to file'),
            (r'&>>?\s*(\S+)', 'redirect both output and errors to file'),
            (r'<\s*(\S+)', 'read input from file'),
        ]
        
        for pattern, desc in redir_patterns:
            matches = re.finditer(pattern, command)
            for match in matches:
                symbol = match.group(0).split()[0]
                target = match.group(1)
                result['redirections'].append({
                    'symbol': symbol,
                    'target': target,
                    'description': desc
                })
                command = command.replace(match.group(0), '')
        
        # Split into tokens
        tokens = command.split()
        
        if not tokens:
            return result
        
        # First token is usually the command
        result['command'] = tokens[0]
        
        # Process remaining tokens
        for token in tokens[1:]:
            if token.startswith('-'):
                result['flags'].append(token)
            else:
                result['arguments'].append(token)
        
        return result

    
def _check_safety(self, command: str) -> List[str]:
        """Check for unsafe command patterns"""
        warnings = []
        for pattern, warning in self.UNSAFE_PATTERNS:
            if re.search(pattern, command):
                warnings.append(warning)
        return warnings
    
def _guess_flag_meaning(self, flag: str) -> str:
        """Guess the meaning of an unknown flag"""
        if flag.startswith('--'):
            name = flag[2:].replace('-', ' ')
            return f"Long option: {name}"
        elif flag.startswith('-') and len(flag) > 2:
            return "Combined short options: " + ", ".join(f"-{c}" for c in flag[1:])
        return "Option (see 'man' for details)"

def _identify_argument_type(self, arg: str) -> str:
        """Identify what type of argument this is"""
        if arg.startswith('/'):
            return "Absolute path"
        elif arg.startswith('~'):
            return "Home directory path"
        elif arg.startswith('./') or arg.startswith('../'):
            return "Relative path"
        elif '/' in arg:
            return "Path"
        elif arg.startswith('$'):
            return "Variable"
        elif arg.startswith('"') or arg.startswith("'"):
            return "String literal"
        elif arg.isdigit():
            return "Number"
        elif '*' in arg or '?' in arg:
            return "Glob pattern"
        else:
            return "Filename or value"
        
class ErrorExplainer:
    """Explains common Bash and terminal errors"""
    
    ERROR_PATTERNS = {
        r'command not found': {
            'explanation': 'The shell cannot find the command you typed.',
            'causes': [
                'Typo in command name',
                'Command not installed on system',
                'Command not in PATH environment variable',
                'Missing ./ prefix for local script'
            ],
            'solutions': [
                'Check spelling of command',
                'Install the required package',
                'Use full path to command',
                'For local script, use: ./script.sh'
            ]
        },
        r'Permission denied': {
            'explanation': 'You don\'t have permission to perform this operation.',
            'causes': [
                'File is not executable',
                'Insufficient user permissions',
                'File/directory owned by another user',
                'SELinux or AppArmor restrictions'
            ],
            'solutions': [
                'Make file executable: chmod +x filename',
                'Use sudo if appropriate (be careful!)',
                'Check file ownership: ls -l filename',
                'Request access from system administrator'
            ]
        },
        r'No such file or directory': {
            'explanation': 'The file or directory you specified does not exist.',
            'causes': [
                'Typo in filename or path',
                'File was moved or deleted',
                'Wrong current directory',
                'Case sensitivity (Linux is case-sensitive)'
            ],
            'solutions': [
                'Check spelling and case',
                'Use ls to list available files',
                'Use pwd to verify current directory',
                'Use absolute path instead of relative'
            ]
        },
        r'syntax error': {
            'explanation': 'The shell found invalid syntax in your command or script.',
            'causes': [
                'Missing quotes or brackets',
                'Unclosed string or command substitution',
                'Invalid operator or special character',
                'Wrong syntax for control structure'
            ],
            'solutions': [
                'Check for matching quotes and brackets',
                'Review Bash syntax documentation',
                'Use shellcheck to validate scripts',
                'Break complex commands into simpler parts'
            ]
        },
        r'cannot remove.*Directory not empty': {
            'explanation': 'Cannot delete directory because it contains files.',
            'causes': [
                'Using rmdir on non-empty directory',
                'Directory contains hidden files'
            ],
            'solutions': [
                'Use rm -r to remove directory and contents',
                'Use rm -ri for interactive deletion (safer)',
                'Check for hidden files with ls -la'
            ]
        },
        r'Disk quota exceeded': {
            'explanation': 'You have exceeded your allocated disk space.',
            'causes': [
                'Too many files or large files',
                'Disk quota policy on system'
            ],
            'solutions': [
                'Delete unnecessary files',
                'Check disk usage: du -sh *',
                'Contact administrator for quota increase'
            ]
        },
        r'Text file busy': {
            'explanation': 'Cannot modify file because it is being executed.',
            'causes': [
                'Trying to edit or delete running script/binary',
                'File is currently in use by a process'
            ],
            'solutions': [
                'Stop the running process first',
                'Use ps aux | grep filename to find process',
                'Kill process with: kill <PID>'
            ]
        },
    }
def explain_error(self, error_message: str) -> str:
        """Explain a Bash error message"""
        output = []
        output.append(f" Error Message: {error_message}\n")
        
        # Find matching error pattern
        matched = False
        for pattern, info in self.ERROR_PATTERNS.items():
            if re.search(pattern, error_message, re.IGNORECASE):
                matched = True
                output.append(f" Explanation:")
                output.append(f"   {info['explanation']}\n")
                
                output.append("Common Causes:")
                for i, cause in enumerate(info['causes'], 1):
                    output.append(f"   {i}. {cause}")
                output.append("")
                
                output.append("Possible Solutions:")
                for i, solution in enumerate(info['solutions'], 1):
                    output.append(f"   {i}. {solution}")
                output.append("")
                
                break
        
        if not matched:
            output.append(" This error is not in our database yet.")
            output.append("   General troubleshooting steps:")
            output.append("   1. Read the full error message carefully")
            output.append("   2. Check your command syntax")
            output.append("   3. Verify file/directory names and paths")
            output.append("   4. Search online for the specific error")
            output.append("   5. Check relevant log files")
            output.append("")
        
        output.append("💡 Tip: Copy the exact error message when searching online")
        
        return "\n".join(output)