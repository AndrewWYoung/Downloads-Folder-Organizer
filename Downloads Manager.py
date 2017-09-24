import os
import shutil

# current_directory = os.getcwd() + "\\Test Files\\"
current_directory = os.getcwd() + "\\"
os.chdir(current_directory)

default_folders     = ["_old", "Documents", "Images", "Music", "Movies", "Miscellaneous"]
files               = os.listdir(current_directory)

image_extensions    = ['.png','.jpg','.gif','.bmp','.tiff']
document_extensions = ['.doc','.docx','.pdf','.rtf','.tex','.txt','.wpd','.xps','.svg','.jar','.html','.css','.css']
video_extensions    = ['.avi','.flv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.wmv']
music_extensions    = ['.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl']

def create_folder(folder_name):
    new_directory = current_directory + folder_name
    try:
        if not os.path.exists(new_directory):
            os.mkdir(folder_name)
            print(folder_name + " Created")
    except FileExistsError:
        print(folder_name + " is already created")
    print()

def create_default_folders():
    for folder in default_folders:
        create_folder(folder)

def move_safely_to(file, folder_name):
    destination = current_directory + folder_name
    # print(file + " : " + destination)
    if os.path.exists(destination):
        shutil.move(file, destination)

def is_document(document):
    file_name, file_extension = os.path.splitext(document)
    file_extension = file_extension.lower()
    if file_extension in document_extensions:
        return True
    else:
        return False
    
def is_image(image):
    file_name, file_extension = os.path.splitext(image)
    file_extension = file_extension.lower()
    if file_extension in image_extensions:
        return True
    else:
        return False

def is_video(video):
    file_name, file_extension = os.path.splitext(video)
    file_extension = file_extension.lower()
    if file_extension in video_extensions:
        return True
    else:
        return False

def is_music(music):
    file_name, file_extension = os.path.splitext(music)
    file_extension = file_extension.lower()
    if file_extension in music_extensions:
        return True
    else:
        return False

def move_files():
    document_count      = 0
    image_count         = 0
    music_count         = 0
    movie_count         = 0
    
    for _x_ in files:
        file_name, file_extension = os.path.splitext(_x_)
        if file_extension == ".py":
            continue
        elif is_document(_x_):
            file_path = current_directory + _x_
            move_safely_to(file_path, "Documents")
            document_count = document_count + 1
        elif is_image(_x_):
            file_path = current_directory + _x_
            move_safely_to(file_path, "Images")
            image_count = image_count + 1
        elif is_music(_x_):
            file_path = current_directory + _x_
            move_safely_to(file_path, "Music")
            music_count = music_count + 1
        elif is_video(_x_):
            file_path = current_directory + _x_
            move_safely_to(file_path, "Movies")
            movie_count = movie_count + 1

    print("Documents Moved: " + str(document_count))
    print("Images Moved: " + str(image_count))
    print("Music Files Moved: " + str(music_count))
    print("Movies Moved: " + str(movie_count))

            
def main():
    create_default_folders()
    move_files()

main()
