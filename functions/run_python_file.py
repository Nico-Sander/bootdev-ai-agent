import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)    
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Error handling
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'    

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python", target_file]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,    # capture stdout and stderr
            text=True,              # output as text instead ob binary
            timeout=30,             # limit the process to 30 seconds
            cwd=abs_working_dir,    # limit the scope of the process to the working directory
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"


    
