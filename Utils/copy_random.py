import os
import shutil
import random

def copy_random_files(source_main, target_main, percent):
    for source in os.listdir(source_main):
        num_of_files = len([name for name in os.listdir(os.path.join(source_main, source))])
        num_to_copy = num_of_files * percent
        files = [file for file in os.listdir(os.path.join(source_main, source))]
        for x in range(int(num_to_copy)):
            if len(files) == 0:
                break
            else:
                file = random.choice(files)
                if not os.path.exists(os.path.join(target_main, source)):
                    os.makedirs(os.path.join(target_main, source))
                shutil.move(os.path.join(source_main, source, file), os.path.join(target_main, source, file))
                files.remove(file)

copy_random_files('c:\\Users\\Tomasz Marcinkowski\\Documents\\MEGA\\Zbiory\\Zbior4_final_tr3\\Train\\', 'c:\\Users\\Tomasz Marcinkowski\\Documents\\MEGA\\Zbiory\\Zbior4_final_tr3\\Valid\\', 0.15)
#copy_random_files('c:\\Users\\Tomasz Marcinkowski\\Documents\\MEGA\\Zbiory\\Zbior4_final_tr2\\Train\\', 'c:\\Users\\Tomasz Marcinkowski\\Documents\\MEGA\\Zbiory\\Zbior4_final_tr2\\Valid\\', 0.15)