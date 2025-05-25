#!/usr/bin/env python
"""First run setup for VS Code users"""
import os
import sys
import json
import subprocess
import platform

def setup_vscode_python_path():
    """Configure VS Code to use the correct Python interpreter"""
    vscode_dir = os.path.join(os.getcwd(), '.vscode')
    settings_file = os.path.join(vscode_dir, 'settings.json')
    
    # Determine the correct Python path based on OS
    if platform.system() == 'Windows':
        python_path = os.path.join('venv', 'Scripts', 'python.exe')
    else:
        python_path = os.path.join('venv', 'bin', 'python')
    
    # Read existing settings if they exist
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            settings = json.load(f)
    else:
        settings = {}
    
    # Update the interpreter path
    settings['python.defaultInterpreterPath'] = python_path
    
    # Write back the settings
    os.makedirs(vscode_dir, exist_ok=True)
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=4)
    
    print(f"✓ VS Code configured to use: {python_path}")

def main():
    """Run the complete first-time setup"""
    print("Flask Python Template - First Run Setup")
    print("=" * 50)
    
    # Run the main setup
    setup_script = os.path.join('scripts', 'setup.py')
    if os.path.exists(setup_script):
        subprocess.run([sys.executable, setup_script])
    
    # Configure VS Code
    print("\nConfiguring VS Code...")
    setup_vscode_python_path()
    
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("\nNOTE: In VS Code, you may need to:")
    print("1. Reload the window (Ctrl+R or Cmd+R)")
    print("2. Select the Python interpreter:")
    print("   - Press Ctrl+Shift+P (Cmd+Shift+P on Mac)")
    print("   - Type 'Python: Select Interpreter'")
    print("   - Choose the interpreter from ./venv/")
    print("\nThen press F5 to run the application!")

if __name__ == "__main__":
    main()
