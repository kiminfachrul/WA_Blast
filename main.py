import subprocess
import os

def run_blast_script():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # path yang di run:
    script_path = os.path.join(current_dir, 'whatsapp_blast.py')

    try:
        subprocess.run(['python', script_path], check=True)
        print("blast.py has been executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute blast.py: {e}")

if __name__ == "__main__":
    run_blast_script()
