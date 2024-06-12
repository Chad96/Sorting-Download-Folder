import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the folder to be monitored and the target folders
DOWNLOAD_FOLDER = os.path.expanduser('~/Downloads')
VIDEO_FOLDER = os.path.join(DOWNLOAD_FOLDER, 'Videos')
PICTURE_FOLDER = os.path.join(DOWNLOAD_FOLDER, 'Pictures')
MP3_FOLDER = os.path.join(DOWNLOAD_FOLDER, 'MP3s')

# Ensure target folders exist
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(PICTURE_FOLDER, exist_ok=True)
os.makedirs(MP3_FOLDER, exist_ok=True)

# File extensions to be sorted
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.flv', '.avi', '.mov'}
PICTURE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
MP3_EXTENSIONS = {'.mp3'}

class DownloadFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.move_file(event.src_path)

    def move_file(self, src_path):
        file_extension = os.path.splitext(src_path)[1].lower()

        if file_extension in VIDEO_EXTENSIONS:
            target_folder = VIDEO_FOLDER
        elif file_extension in PICTURE_EXTENSIONS:
            target_folder = PICTURE_FOLDER
        elif file_extension in MP3_EXTENSIONS:
            target_folder = MP3_FOLDER
        else:
            return  # Ignore files that don't match the specified extensions

        try:
            shutil.move(src_path, target_folder)
            print(f"Moved {src_path} to {target_folder}")
        except Exception as e:
            print(f"Failed to move {src_path}: {e}")

if __name__ == "__main__":
    event_handler = DownloadFolderHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOAD_FOLDER, recursive=False)
    observer.start()

    print(f"Monitoring {DOWNLOAD_FOLDER} for new files...")

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

