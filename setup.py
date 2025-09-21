#!/usr/bin/env python3

"""
Setup and installation script for CrewAI AgentOps Integration
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a shell command with error handling"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_dependencies():
    """Install required Python dependencies"""
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    return run_command(f"{sys.executable} -m pip install -r requirements.txt", 
                      "Installing Python dependencies")

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        try:
            env_file.write_text(env_example.read_text())
            print("✅ Created .env file from template")
            print("📝 Please edit .env file and add your API keys:")
            print("   - AGENTOPS_API_KEY")
            print("   - OPENAI_API_KEY")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    elif env_file.exists():
        print("✅ .env file already exists")
        return True
    else:
        print("⚠️  .env.example not found, please create .env manually")
        return False

def verify_installation():
    """Verify that all components are installed correctly"""
    try:
        import crewai
        import agentops
        print("✅ CrewAI and AgentOps imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import verification failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up CrewAI AgentOps Integration")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Create environment file
    create_env_file()
    
    # Verify installation
    if not verify_installation():
        return False
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your API keys")
    print("2. Get AgentOps API key from https://www.agentops.ai/")
    print("3. Add OpenAI API key for LLM functionality")
    print("4. Run: python main.py")
    print("\n🛡️ Your Cyber Defense Shield is ready to deploy!")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)