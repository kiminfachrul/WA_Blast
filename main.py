import subprocess
import os

def run_blast_script():
    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the blast.py script
    script_path = os.path.join(current_dir, 'whatsapp_blast.py')

    try:
        # Run the blast.py script
        subprocess.run(['python', script_path], check=True)
        print("blast.py has been executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute blast.py: {e}")

if __name__ == "__main__":
    run_blast_script()