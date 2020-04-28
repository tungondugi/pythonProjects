"""Written by Nognut"""

"""This piece of code will move the files into their respective Directories."""
#importing the required modules
import os
import shutil

"""Path of the main directory"""
path_name = 'E:\Downloads'

"""changing directory to the specified path name"""
os.chdir(path_name)
"""list of all the file formats"""
document_file_extension=['.pdf','.docx','.txt','.pptx','.csv','.ppt']
image_extension = ['.jpg', '.png', '.svg', '.jpeg', '.gif', '.jfif']
zip_extension = ['.zip', '.rar']
video_extension = ['.mp4', '.avi', '.webm', '.m4v', '.flv']

"""Listing all the contents of the specified path name"""
dir_list = os.listdir(path_name)
for dirs in dir_list:
    """Ignoring the directories"""
    if os.path.isdir(dirs):
         pass#ignoring the directories.
    else:
        """contents of the specified directory excluding the directories"""

        #splitting the name and extension of the files using splitetext()
        file_name, f_format = os.path.splitext(dirs.strip())#tuple of file_name and file_format
        
        #checking for specified extensions
        if f_format in document_file_extension:
            #checking if the directory mentioned is present of not
            if os.path.isdir("PDF_FILES"):
                #if present then move the files to that directory
                shutil.move(dirs,"PDF_FILES")
            #if the directory if not present
            else:
                #create the directory
                os.mkdir("PDF_FILES")
                #and move the files to newly created directory
                shutil.move(dirs, "PDF_FILES")
        # """Rest of the code have same logic as above"""
        elif f_format in image_extension: 
            if os.path.isdir("Images"):
                shutil.move(dirs, "Images")
            else:
                os.mkdir("Images")
                shutil.move(dirs, "Images")
        elif f_format in zip_extension:    
            if os.path.isdir("ZIP_FILES"):
                shutil.move(dirs,'ZIP_FILES')
            else:
                os.mkdir("ZIP_FILES")
                shutil.move(dirs, "ZIP_FILES")

        elif f_format in video_extension:    
            if os.path.isdir("VIDEOS"):
                shutil.move(dirs, 'VIDEOS')
            else:
                os.mkdir("VIDEOS")
                shutil.move(dirs, "VIDEOS")
        #delete the remaining unwanted files.
        else:
            os.remove(dirs)