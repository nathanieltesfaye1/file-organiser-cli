import os
import shutil
from pathlib import Path
from file_mappings import FILE_EXTENSION_TO_FOLDER


def organise_files(target_directory, extension_map):

    try:
        #Step 0 - Validate input

        target_path = Path(target_directory)

        if not target_path.exists():
            raise FileNotFoundError(f"Target directory does not exist: {target_directory}")
        if not target_path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {target_directory}")
        

        # Step 1 = Scan files in target dir to determine which folders we'll need to create
        found_extensions = set()
        files_to_process = []

        for item in target_path.iterdir():
            try:
                if item.is_file():
                    extension = item.suffix.lower()
                    found_extensions.add(extension)
                    files_to_process.append(item)
            except PermissionError:
                print(f"Skipped {item.name} (permission denied)") # Handle exceptions due to unreadable files


        # Step 2 = Create the required folders
        required_folders = set()
        for extension in found_extensions:
            folder = extension_map.get(extension, "other")
            required_folders.add(folder)
        
        for folder in required_folders:
            try:
                (target_path / folder).mkdir(exist_ok = True)
            except PermissionError:
                raise PermissionError(f"Cannot create folder '{folder}' (permission denied)") # Again, we may not have appropriate permissions, but this time to create folder

        
        # Step 3 = Move files
        for file in files_to_process:
            try:
                extension = file.suffix.lower()
                destination_folder = extension_map.get(extension, "other") # Default = Other
                destination_path = target_path / destination_folder / file.name
                print(destination_path)

                # Handling duplication filenames
                counter = 1

                while destination_path.exists():
                    new_name = f"{file.stem}_{counter}{file.suffix}"
                    new_destination = target_path / destination_folder / new_name

                    if not new_destination.exists():
                        destination_path = new_destination
                        break
                    
                    counter += 1

                shutil.move(str(file), str(destination_path))
            
            except PermissionError:
                print(f"Skipped {file.name} (move permission denied)")

        return target_directory
    
    except Exception as e:
        print(f"Critical error: {str(e)}")
        raise # Re-raise the error for the caller to handle if they need/want






if __name__ == "__main__":
    while True:
        user_input = input("Enter the folder path to organise (or 'q' to quit): ").strip()

        if not user_input:
            print("Error: Please enter a valid path or 'q' to quit")
            continue
        if user_input.lower() == 'q':
            exit(0)

        target_directory = organise_files(user_input, FILE_EXTENSION_TO_FOLDER)
        print(f"File organisation is complete! Check your \"{user_input}\" folder.")

        break



# /Users/nathaniel/Job Prep/220525 Job Prep/file-organiser/samples