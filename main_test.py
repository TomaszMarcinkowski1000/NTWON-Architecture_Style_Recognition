import img_manipulation

orginal_folder = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior3_koledzy/"
processed_folder = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior3_koledzy_transformed/"
img_manipulation.resize_and_pad_folder(orginal_folder, processed_folder, (200,200), 127)