import os

# Replace 'your_folder_path' with the path to your folder
folder_path = r"C:\Users\mark.rainey\eigen_emoji\emoji\training"

# Iterate through each file in the folder
for i, filename in enumerate(os.listdir(folder_path)):
    # Construct the full file path
    old_file = os.path.join(folder_path, filename)

    # Skip directories, only rename files
    if os.path.isfile(old_file):
        # Define the new filename
        # Add a file extension if you need, e.g., '.txt'
        new_filename = f"{i}"

        # Construct the full new file path
        new_file = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file, new_file)

print("Files have been renamed successfully.")
