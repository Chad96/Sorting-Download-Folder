Explanation

Watchdog Library: This library is used to monitor the file system for changes. When a new file is created in the Downloads folder, the on_created method is called.

File Handling: The script checks the file extension of the new file and moves it to the appropriate folder (Videos, Pictures, MP3s).

Directory Setup: Ensures that the target directories (Videos, Pictures, MP3s) exist. If not, it creates them.

Extension Sets: The sets VIDEO_EXTENSIONS, PICTURE_EXTENSIONS, and MP3_EXTENSIONS contain the file extensions that the script will sort.

This script should effectively keep your Downloads folder organized by moving new files to their respective subfolders based on their type.
