#!/usr/bin/env python
"""Setup VS Code for Flask Python Template"""
import os
import sys
import json
import subprocess
import platform

def create_venv_if_needed():
    """Create virtual environment if it doesn't exist"""
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        print("✓ Virtual environment created")
        
        # Install dependencies
        if platform.system() == 'Windows':
            pip_path = os.path.join('venv', 'Scripts', 'pip.exe')
        else:
            pip_path = os.path.join('venv', 'bin', 'pip')
        
        print("Installing dependencies...")
        subprocess.run([pip_path, 'install', '-r', 'requirements.txt'], check=True)
        print("✓ Dependencies installed")
    else:
        print("✓ Virtual environment already exists")

def setup_vscode():
    """Configure VS Code settings"""
    print("\nConfiguring VS Code...")
    
    # Ensure .vscode directory exists
    vscode_dir = '.vscode'
    os.makedirs(vscode_dir, exist_ok=True)
    
    # Don't set defaultInterpreterPath - let VS Code handle it
    print("✓ VS Code configuration updated")
    
    # Create a workspace recommendations file
    recommendations = {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "ms-python.debugpy"
        ]
    }
    
    with open(os.path.join(vscode_dir, 'extensions.json'), 'w') as f:
        json.dump(recommendations, f, indent=4)
    
    print("✓ VS Code extensions recommendations added")

def print_instructions():
    """Print setup instructions"""
    print("\n" + "="*60)
    print("Setup Complete!")
    print("="*60)
    print("\nIMPORTANT: Follow these steps in VS Code:")
    print("\n1. Open VS Code in this directory:")
    print("   code .")
    print("\n2. When VS Code opens, it will prompt to select a Python interpreter")
    print("   at the bottom-right corner of the window.")
    print("\n3. Click on it and select:")
    if platform.system() == 'Windows':
        print("   .\\venv\\Scripts\\python.exe")
    else:
        print("   ./venv/bin/python")
    print("\n4. If no prompt appears, manually select interpreter:")
    print("   - Press Ctrl+Shift+P (Cmd+Shift+P on Mac)")
    print("   - Type: Python: Select Interpreter")
    print("   - Choose the interpreter from the venv folder")
    print("\n5. Press F5 to run the application!")
    print("\nNOTE: You might need to reload VS Code after selecting the interpreter")
    print("(Ctrl+R or Cmd+R)")

def main():
    """Main setup function"""
    print("Flask Python Template - VS Code Setup")
    print("="*60)
    
    # Create virtual environment if needed
    create_venv_if_needed()
    
    # Setup VS Code
    setup_vscode()
    
    # Print instructions
    print_instructions()

if __name__ == "__main__":
    main()
