import os
import shutil
import random

def copy_random_files(source, target, percent):
    num_of_files = len([name for name in os.listdir(source)])
    num_to_copy = num_of_files * percent
    files = [file for file in os.listdir(source)]
    for x in range(int(num_to_copy)):
        if len(files) == 0:
            break
        else:
            file = random.choice(files)
            shutil.move(os.path.join(source, file), os.path.join(target, file))
            files.remove(file)

copy_random_files('c:\\Users\\Tomasz Marcinkowski\\Downloads\\Extreme Picture Finder\\NTwON\\Train\\Russian Revival', 'c:\\Users\\Tomasz Marcinkowski\\Downloads\\Extreme Picture Finder\\NTwON\\Test\\Russian Revival', 0.15)