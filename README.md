# Clean Downloads

A Python script that organizes your downloads folder by moving files into specified or predefined folders based on file type. The script works on macOS, Windows, and Linux.

## Features

- **Customizable Folder Locations**: Specify custom folder names and locations for different file types.
- **Automatic File Organization**: Moves files into predefined categories (Images, Documents, Audio, etc.).
- **Duplicate Handling**: Automatically renames duplicate files by appending numbers (e.g., `file (1).pdf`).
- **Logging**: Generates a single log file summarizing actions and errors to avoid clutter.

## Requirements

- Python 3.6 or higher

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jordansmalls/cleandownloads.git
   cd cleandownloads
   ```

2. **Edit the script**: Open `clean_downloads.py` in your editor and update the `CUSTOM_LOCATIONS` dictionary to specify custom folders if desired. By default, files are moved into folders within the downloads directory.

## Usage

1. **Run the script manually**:
   ```bash
   python clean_downloads.py
   ```
   > **Note**: If `python` does not work on your system, try using `python3` instead.

   This will organize files in your downloads folder and print the location of the log file in the console.

2. **Log File**: After running, a single log file named `clean_downloads_log.txt` is generated in the downloads directory. This file records all moved files and any errors encountered.

   > **Note**: To keep your downloads folder clutter-free, the script overwrites this log file each time it runs, ensuring that only the latest activity is logged.

## File Categories

The script categorizes files into these default folders:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.heic`, etc.
- **Documents**: `.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx`, etc.
- **Videos**: `.mp4`, `.mov`, `.avi`, etc.
- **Audio**: `.mp3`, `.wav`, `.aac`, etc.
- **Archives**: `.zip`, `.rar`, `.tar`, etc.
- **Scripts**: `.js`, `.py`, `.sh`, `.bat`, etc.
- **Others**: Any other files that don’t match the predefined categories.

You can edit the `FILE_CATEGORIES` dictionary in `clean_downloads.py` to add or change categories and extensions.

## Future Optimizations

Consider implementing the following enhancements for a more robust experience:

1. **Real-Time Monitoring**: Use a file watcher to automatically organize new files as they’re downloaded. This can be done with libraries like `watchdog` in Python, enabling the script to clean the downloads folder continuously without requiring manual execution.

2. **Improve Log File Format**: Currently, the script generates a simple log file, but this could be enhanced for better readability and usability. Consider the following improvements:

    - **Timestamps**: Include timestamps for each log entry to track when files were processed.

    - **Log Levels**: Implement different log levels such as `INFO`, `ERROR`, and `WARNING` to differentiate between regular actions and potential issues.
    - **File Path Details**: Log the source and destination paths for each moved file, helping users verify where files are being relocated.
    - **Success/Failure Status**: Add status indicators to each action (e.g., "Moved", "Renamed", "Failed").

3. **Expand Functionality of Script**: Allow users to specify what folders they want to clean, not just their Downloads directory.

Example:

```
[INFO] 2024-11-10 10:00:00 - Moved file 'example.pdf' from /Downloads to /Documents
[ERROR] 2024-11-10 10:02:30 - Failed to move file 'duplicate.mp3' due to permission issues
```

This will guide users toward refining the log file format for a better user experience.

3. **Config File for User Preferences**: Implement a configuration file (e.g., `config.yaml` or `config.json`) that allows users to define custom folder mappings, categories, and logging options in a more accessible way. This would make it easier for users to manage settings without modifying the main script directly.

4. **Automated Scheduling**: Set up a scheduled task to run this script periodically, keeping your downloads folder organized automatically:
   - **macOS/Linux**: Use `cron` jobs
   - **Windows**: Use Task Scheduler
   
   These scheduled setups will eliminate the need to run the script manually, allowing for hands-free cleaning. Instructions for setting up scheduled tasks will be added in future releases.

## Contributing

I welcome contributions to improve and optimize the script. Whether you're fixing bugs, adding new features, or optimizing existing ones, your input is valuable.

### How to Contribute

1. **Fork the repository**: Create a copy to work on by forking the repository to your GitHub account.

2. **Clone your fork**: 
   ```bash
   git clone https://github.com/your-username/cleandownloads.git
   cd cleandownloads
   ```
3. **Create a new branch**: Use a clear and descriptive branch name for your feature or fix.
   ```bash
   git checkout -b feature-or-bug-description
   ```
4. **Commit your changes**: Make sure to add meaningful commit messages explaining your work.
5. **Push to GitHub**: Push your branch to GitHub.
6. **Submit a pull request**: Open a pull request to merge your changes into the main repository.

Feel free to explore the code, suggest new features, and contribute fixes or optimizations. All feedback and contributions are appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 

If you have any questions, suggestions, or feedback, feel free to reach out.

- **Twitter**: [@jsmallsdev](https://www.twitter.com/jsmallsdev)
- **Instagram**: [@jsmallsdev](https://www.instagram.com/jsmallsdev)

I would love to hear from you. Let me know if you have ideas for new features, run into any issues, or want to discuss potential improvements.

## Be sure to leave a ⭐ on [Clean Downloads](https://github.com/jordansmalls/cleandownloads) if you found it useful!
