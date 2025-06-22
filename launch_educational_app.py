#!/usr/bin/env python3
"""
Launcher script for the Adventure Learning Educational App
Checks dependencies and launches the application with proper error handling
"""

import sys
import os
import subprocess
import importlib.util

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    required_modules = ['tkinter', 'PIL']
    missing_modules = []
    
    for module in required_modules:
        if module == 'PIL':
            # Check for Pillow specifically
            if importlib.util.find_spec('PIL') is None:
                missing_modules.append('Pillow')
        elif importlib.util.find_spec(module) is None:
            missing_modules.append(module)
    
    if missing_modules:
        print(f"❌ Missing dependencies: {', '.join(missing_modules)}")
        print("Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_educational.txt'])
            print("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies automatically.")
            print("Please run: pip install -r requirements_educational.txt")
            return False
    else:
        print("✅ All dependencies are installed!")
    
    return True

def check_files():
    """Check if required files exist"""
    required_files = ['educational_app.py', 'problem_data.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found!")
    return True

def launch_app():
    """Launch the educational app"""
    try:
        print("🚀 Launching Adventure Learning Educational App...")
        print("=" * 50)
        
        # Import and run the main app
        from educational_app import main
        main()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all files are in the same directory.")
        return False
    except Exception as e:
        print(f"❌ Error launching app: {e}")
        return False
    
    return True

def main():
    """Main launcher function"""
    print("🎓 Adventure Learning - Educational App Launcher")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        input("Press Enter to exit...")
        return
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    # Check files
    if not check_files():
        input("Press Enter to exit...")
        return
    
    print("\n🎯 Ready to launch!")
    print("The app will open in a new window.")
    print("=" * 50)
    
    # Launch the app
    if not launch_app():
        input("Press Enter to exit...")

if __name__ == "__main__":
    main() 
