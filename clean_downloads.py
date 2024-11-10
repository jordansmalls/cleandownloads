import os
import shutil
from datetime import datetime

# Specify your downloads location if necessary.
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

# Define file type categories and their default directories.
# You can modify or add file extensions here to match your needs.
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".heic"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".js", ".py", ".sh", ".bat"],
    "Others": []  # This is a catch-all category for unidentified types.
}

# Specify custom locations for each file type category if desired.
CUSTOM_LOCATIONS = {
    # Example
    # "Images": "/path/to/images/directory"
}

# Path to the log file to record actions.
LOG_FILE = os.path.join(DOWNLOADS_DIR, "clean_downloads_log.txt")

def ensure_dir(directory):
    """Ensure a directory exists; create if it does not."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_target_folder(extension):
    """
    Return the target folder based on the file extension.
    Falls back to the 'Others' category if no match is found.
    """
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            # Use the custom location if specified, otherwise default to Downloads subfolder.
            return CUSTOM_LOCATIONS.get(category, os.path.join(DOWNLOADS_DIR, category))
    # Default to the 'Others' category if the extension is unrecognized.
    return CUSTOM_LOCATIONS.get("Others", os.path.join(DOWNLOADS_DIR, "Others"))

def move_file(file_path):
    """
    Move a file to the appropriate folder based on its extension,
    automatically handling duplicate files by renaming them.
    """
    file_name, extension = os.path.splitext(file_path)
    target_folder = get_target_folder(extension.lower())
    ensure_dir(target_folder)

    # Set the initial target path and prepare to handle duplicates.
    target_path = os.path.join(target_folder, os.path.basename(file_path))
    counter = 1

    # If the target file already exists, rename by appending a counter.
    while os.path.exists(target_path):
        base_name, ext = os.path.splitext(target_path)
        target_path = f"{base_name} ({counter}){ext}"
        counter += 1

    # Move the file and return the new path.
    shutil.move(file_path, target_path)
    return target_path

def log_action(action):
    """Write a log entry to the log file."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {action}\n")

def clean_downloads():
    """Main function to clean up the downloads folder."""
    for item in os.listdir(DOWNLOADS_DIR):
        item_path = os.path.join(DOWNLOADS_DIR, item)

        # Skip directories and hidden files.
        if os.path.isdir(item_path) or item.startswith("."):
            continue

        try:
            # Move the file and log the action.
            target_path = move_file(item_path)
            log_action(f"Moved: '{item}' to '{target_path}'")
        except Exception as e:
            # Log any errors encountered during the move process.
            log_action(f"Error moving '{item}': {e}")

    print(f"Cleaning complete. Log file at: {LOG_FILE}")

if __name__ == "__main__":
    # Run the script.
    clean_downloads()
