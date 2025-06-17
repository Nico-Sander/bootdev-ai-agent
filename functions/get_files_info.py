import os

def get_files_info(working_directory, directory=None):
    # print(f"\nget_files_info({working_directory}, {directory})")

    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)
    
    # print(f"Abs path of working directory: {abs_working_directory}")
    # print(f"Abs path of directory: {abs_directory}")

    combined_path = os.path.join(working_directory, directory)
    abs_combined_path = os.path.abspath(combined_path)
    # print(f"Abs path of combined path: {abs_combined_path}")


    if not abs_working_directory in abs_combined_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


    if not os.path.isdir(abs_combined_path):
        return f'Error: "{directory}" is not a directory'

    contents = os.listdir(abs_combined_path)
    # print(f"Found contents in '{abs_combined_path}': {contents}")

    output_string = ""

    for file in contents:
        # print(f"Analysing file: {file}")
        file_name = file
        abs_file_path = os.path.join(abs_combined_path, file)

        try:
            file_size = os.path.getsize(abs_file_path)
        except:
            return f"Error: file size could not be calculated for '{abs_file_path}'."


        try:
            is_dir = os.path.isdir(abs_file_path)
        except:
            return f"Error: an error occured when trying to determine if '{abs_file_path}' is a directory."

        output_string += f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n"

    return output_string

