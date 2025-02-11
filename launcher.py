import os
import platform
import subprocess

def run_script():
    if platform.system() == "Windows":
        # Run Python script on Windows
        subprocess.run(["python", "MAIN.py"], check=True)
    elif platform.system() == "Linux":
        # Run Python script on Linux
        subprocess.run(["python3", "MAIN.py"], check=True)
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    run_script()
