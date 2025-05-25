#!/usr/bin/env python
"""Setup script for Flask Python Template"""
import os
import sys
import subprocess
import platform
import shutil

def run_command(command, shell=False):
    """Run a command and return success status"""
    try:
        subprocess.run(command, check=True, shell=shell)
        return True
    except subprocess.CalledProcessError:
        return False

def create_virtualenv():
    """Create virtual environment"""
    print("Creating virtual environment...")
    if run_command([sys.executable, "-m", "venv", "venv"]):
        print("✓ Virtual environment created")
        return True
    else:
        print("✗ Failed to create virtual environment")
        return False

def get_venv_python():
    """Get the path to the Python executable in the virtual environment"""
    if platform.system() == "Windows":
        return os.path.join("venv", "Scripts", "python.exe")
    else:
        return os.path.join("venv", "bin", "python")

def install_dependencies():
    """Install Python dependencies"""
    print("\nInstalling dependencies...")
    venv_python = get_venv_python()
    if run_command([venv_python, "-m", "pip", "install", "--upgrade", "pip"]):
        print("✓ Pip upgraded")
    
    if run_command([venv_python, "-m", "pip", "install", "-r", "requirements.txt"]):
        print("✓ Dependencies installed")
        return True
    else:
        print("✗ Failed to install dependencies")
        return False

def setup_environment():
    """Set up environment file"""
    print("\nSetting up environment...")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy(".env.example", ".env")
            print("✓ Environment file created from .env.example")
            print("  Please edit .env to set your configuration")
        else:
            print("⚠ No .env.example found, creating basic .env")
            with open(".env", "w") as f:
                f.write("FLASK_APP=run.py\n")
                f.write("FLASK_ENV=development\n")
                f.write("SECRET_KEY=dev-secret-key-change-in-production\n")
    else:
        print("✓ Environment file already exists")

def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "="*50)
    print("Setup completed successfully!")
    print("="*50)
    print("\nNext steps:")
    
    if platform.system() == "Windows":
        print("1. Activate virtual environment: venv\\Scripts\\activate")
    else:
        print("1. Activate virtual environment: source venv/bin/activate")
    
    print("2. Run the application: python run.py")
    print("3. Open http://localhost:5000 in your browser")
    print("\nFor VS Code users:")
    print("- Press F5 to start debugging")
    print("- Press Ctrl+Shift+B to see build tasks")

def main():
    """Main setup function"""
    print("Flask Python Template Setup")
    print("="*50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        print(f"  Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✓ Python {sys.version.split()[0]} detected")
    
    # Create virtual environment
    if not create_virtualenv():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup environment
    setup_environment()
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main()
