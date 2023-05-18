import os
import shutil
from_dir = "D:/python/Organizer"
to_dir = "D:/python/Organizer"
list = os.listdir(from_dir)
for file in list:
    name,ext = os.path.splitext(file)
    if ext in [".gif" , ".png" ,".jpeg" ,".jpg" ,".jfif"]:
        if os.path.exists(to_dir + "/" + "images"):
            print("moving....")
            shutil.move(from_dir + "/" + file,to_dir + "/" + "images" + "/" + file)
        else:
            os.mkdir(to_dir + "/" + "images")
            print("moving....")
            shutil.move(from_dir + "/" + file,to_dir + "/" + "images" + "/" + file)
            print("Done !")
            
