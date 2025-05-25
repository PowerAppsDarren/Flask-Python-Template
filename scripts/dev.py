#!/usr/bin/env python
"""Development helper script"""
import os
import sys
import subprocess
import platform

def check_venv():
    """Check if running in virtual environment"""
    if not hasattr(sys, 'prefix'):
        return False
    return sys.prefix != sys.base_prefix

def get_venv_python():
    """Get the path to the Python executable in the virtual environment"""
    if platform.system() == "Windows":
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python")

def run_flask():
    """Run Flask development server"""
    if not check_venv() and os.path.exists("venv"):
        print("⚠ Using virtual environment Python")
        python = get_venv_python()
    else:
        python = sys.executable
    
    env = os.environ.copy()
    env.update({
        'FLASK_APP': 'run.py',
        'FLASK_ENV': 'development',
        'FLASK_DEBUG': '1'
    })
    subprocess.run([python, 'run.py'], env=env)

def run_docker():
    """Run with Docker Compose"""
    subprocess.run(['docker', 'compose', 'up', '--build'])

def run_tests():
    """Run tests with pytest"""
    if not check_venv() and os.path.exists("venv"):
        python = get_venv_python()
    else:
        python = sys.executable
    
    subprocess.run([python, '-m', 'pytest', '-v'])

def install_deps():
    """Install dependencies"""
    if not check_venv() and os.path.exists("venv"):
        python = get_venv_python()
    else:
        python = sys.executable
    
    subprocess.run([python, '-m', 'pip', 'install', '-r', 'requirements.txt'])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Development helper')
    parser.add_argument('command', choices=['flask', 'docker', 'test', 'install'],
                      help='Command to run')
    
    args = parser.parse_args()
    
    # Check for virtual environment
    if args.command != 'docker' and not check_venv() and not os.path.exists("venv"):
        print("⚠ No virtual environment found!")
        print("Run 'python scripts/setup.py' first to set up the project")
        sys.exit(1)
    
    commands = {
        'flask': run_flask,
        'docker': run_docker,
        'test': run_tests,
        'install': install_deps
    }
    
    commands[args.command]()
