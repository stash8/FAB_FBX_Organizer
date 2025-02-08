import os
import shutil
import tkinter as tk
from tkinter import simpledialog, messagebox

def extract_fbx_files(source_dir, destination_dir):
    """
    Extracts all .fbx files from subfolders within a source directory and copies them
    to a specified destination directory.

    Args:
        source_dir: The root directory to search for .fbx files in.
        destination_dir: The directory to copy the found .fbx files to.  Will be created if it doesn't exist.
    """

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)  # Create the directory
        except OSError as e:
            messagebox.showerror("Error", f"Could not create destination directory: {e}")
            return

    for root, _, files in os.walk(source_dir):  # walk through all subdirectories

        for file in files:  # iterate files in the current directory (root)
            if file.endswith(".fbx"):  # Check file extension

                source_path = os.path.join(root, file) # create full path to original file
                destination_path = os.path.join(destination_dir, file) # create full path to destination

                try:
                    shutil.copy2(source_path, destination_path)  # Copy file, preserving metadata (timestamps, etc.)
                    print(f"Copied '{file}' from '{root}' to '{destination_dir}'")
                except Exception as e:
                    print(f"Error copying '{file}' from '{root}' to '{destination_dir}': {e}")
                    messagebox.showerror("Error", f"Error copying '{file}': {e}")


def get_directory_from_user(prompt):
    """Gets a directory path from the user via a popup dialog."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = simpledialog.askstring("Input", prompt)
    root.destroy() # Destroy Tk instance when done
    return directory

if __name__ == "__main__":
    source_directory = get_directory_from_user("Enter the source directory:")
    if not source_directory:
        messagebox.showinfo("Info", "No source directory provided. Exiting.")
        exit()

    destination_directory = get_directory_from_user("Enter the destination directory:")
    if not destination_directory:
        messagebox.showinfo("Info", "No destination directory provided. Exiting.")
        exit()

    if not os.path.isdir(source_directory):
        messagebox.showerror("Error", "Invalid source directory.")
        exit()

    extract_fbx_files(source_directory, destination_directory)
    messagebox.showinfo("Info", "Finished processing.")
    print("Finished processing.")