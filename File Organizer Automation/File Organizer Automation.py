import os
import shutil
from datetime import datetime

# Folder to organize
DIRECTORY_TO_ORGANIZE = r" Your Folder Path "

# Mapping of extensions to folder names
FILE_TYPE = {
    ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'): 'Images',
    ('.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.log', '.wpd'): 'Documents',
    ('.csv', '.xlsx', '.xls', '.json', '.xml', '.db'): 'Data_and_Sheets',
    ('.ppt', '.pptx'): 'Presentations',
    ('.zip', '.rar', '.7z', '.tar', '.gz'): 'Archives',
    ('.exe', '.msi', '.dmg', '.deb'): 'Applications',
    ('.py', '.js', '.html', '.css', '.md', '.java', '.c', '.cpp', '.sh'): 'Code_Scripts',
    ('.mp3', '.wav', '.flac', '.mp4', '.mov', '.avi', '.mkv'): 'Video_Audio_Media',
}


def get_destination_folder(filename):
    """Return the folder name based on file extension."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    for extensions, folder_name in FILE_TYPE.items():
        if ext in extensions:
            return folder_name

    return 'Other_Files'


def organize_files(target_dir):
    """Organize files in the given directory into categorized folders."""
    if not os.path.isdir(target_dir):
        print(f"error Target directory not found {target_dir}")
        return

    print(f"Starting file organization in: {target_dir}")
    file_count = 0

    for filename in os.listdir(target_dir):
        source_path = os.path.join(target_dir, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        destination_folder_name = get_destination_folder(filename)
        destination_folder_path = os.path.join(target_dir, destination_folder_name)

        try:
            os.makedirs(destination_folder_path, exist_ok=True)
        except OSError as system_error:
            print(f"error could not create folder {destination_folder_name}, {system_error}")
            continue

        final_file_name = filename
        final_destination_path = os.path.join(destination_folder_path, final_file_name)

        # Handle duplicate file names
        if os.path.exists(final_destination_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name, ext = os.path.splitext(filename)
            final_file_name = f"{name}_{timestamp}{ext}"
            final_destination_path = os.path.join(destination_folder_path, final_file_name)
            print(f"Duplicate file rename {filename} to {final_file_name}")

        try:
            shutil.move(source_path, final_destination_path)
            print(f"Move {filename} -> {destination_folder_name}")
            file_count += 1
        except OSError as system_error:
            print(f"Error Failed to move {filename} -> {system_error}")

    print(f"\n Organization complete. {file_count} files processed.")


if __name__ == "__main__":
    organize_files(DIRECTORY_TO_ORGANIZE)

