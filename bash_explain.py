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