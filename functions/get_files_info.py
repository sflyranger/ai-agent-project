import os

def get_files_info(working_directory, directory="."):

    full_path = os.path.join(working_directory, directory)
    if not os.path.exists(full_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    else:
        final_string = []
        for f in os.listdir(full_path):
            file_path = os.path.join(full_path, f)
            dir_status = os.path.isdir(file_path)
            size = os.path.getsize(file_path)
            out_string = f"- {f}: file_size={size}"

        


    
    

wd = "./ai-agent-project"
directory = "calculator"

print(get_files_info(wd, directory))




