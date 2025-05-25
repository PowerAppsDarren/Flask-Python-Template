#!/usr/bin/env python
"""Development helper script"""
import os
import sys
import subprocess

def run_flask():
    """Run Flask development server"""
    env = os.environ.copy()
    env.update({
        'FLASK_APP': 'run.py',
        'FLASK_ENV': 'development',
        'FLASK_DEBUG': '1'
    })
    subprocess.run([sys.executable, 'run.py'], env=env)

def run_docker():
    """Run with Docker Compose"""
    subprocess.run(['docker', 'compose', 'up', '--build'])

def run_tests():
    """Run tests with pytest"""
    subprocess.run([sys.executable, '-m', 'pytest', '-v'])

def install_deps():
    """Install dependencies"""
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Development helper')
    parser.add_argument('command', choices=['flask', 'docker', 'test', 'install'],
                      help='Command to run')
    
    args = parser.parse_args()
    
    commands = {
        'flask': run_flask,
        'docker': run_docker,
        'test': run_tests,
        'install': install_deps
    }
    
    commands[args.command]()
