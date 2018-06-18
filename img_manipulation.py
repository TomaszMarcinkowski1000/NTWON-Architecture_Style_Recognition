import os
import glob
import numpy as np
import cv2
import dataset

def resizeAndPad(img, size, padColor=0):

    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    # aspect ratio of image
    aspect = w/h  # if on Python 2, you might need to cast as a float: float(w)/h

    # compute scaling and pad sizing
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
        pad_vert = (sh-new_h)/2
        pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
        pad_left, pad_right = 0, 0
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
        pad_horz = (sw-new_w)/2
        pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
        pad_top, pad_bot = 0, 0
    else: # square image
        new_h, new_w = sh, sw
        pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

    # set pad color
    if len(img.shape) is 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
        padColor = [padColor]*3

    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)

    return scaled_img


def resizeAndEnlarge(img, size):
    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw:  # shrinking image
        interp = cv2.INTER_AREA
    else:  # stretching image
        interp = cv2.INTER_CUBIC

    if h > w :
        new_w = sw
        new_h = np.round(h*(new_w/w)).astype(int)
    else:
        new_h = sh
        new_w = np.round(w*(new_h/h)).astype(int)

    image = cv2.resize(img, (new_w, new_h), interpolation=interp)
    width = new_w
    height = new_h

    aspect = width / float(height)

    ideal_width = sw
    ideal_height = sh

    ideal_aspect = ideal_width / float(ideal_height)

    if aspect > ideal_aspect:
        # Then crop the left and right edges:
        new_width = int(ideal_aspect * height)
        offset = np.round((width - new_width) / 2).astype(int)
        resize = (offset, 0, width - offset, height)
    else:
        # ... crop the top and bottom:
        new_height = int(width / ideal_aspect)
        offset = np.round((height - new_height) / 2).astype(int)
        resize = (0, offset, width, height - offset)

    scaled_img = image[resize[0]:resize[2], resize[1]:resize[3]]
    scaled_img = cv2.resize(scaled_img, (ideal_width, ideal_height), interpolation=interp)
    return scaled_img


def resize_and_pad_folder(source_folder, destination_folder, size, padColor=0, method = 1):
    classes = dataset.get_classes(source_folder)

    print('Reading images')
    for fld in classes:
        print ('Processing {folder}'.format(folder = fld))

        path = os.path.join(source_folder, fld, '*g')
        files = glob.glob(path)

        destination_path = os.path.join(destination_folder, fld)
        os.makedirs(destination_path)
        for fl in files:
            try:
                image = cv2.imread(fl)
                if method == 1:
                    resized_img = resizeAndPad(image,size,padColor)
                else :
                    resized_img = resizeAndEnlarge(image, size)
                file_to_save = os.path.join(destination_path, os.path.basename(fl))
                cv2.imwrite(file_to_save, resized_img)
            except Exception as e:
                print("Exception for file:{file_name}".format(file_name = fl))
                continue


orginal_folder_test = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final/Test"
orginal_folder_train = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final/Train"

processed_folder_test1 = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final_tr3/Test"
processed_folder_train1 = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final_tr3/Train"

# processed_folder_test1 = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final_tr1/Test"
#processed_folder_train1 = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final_tr1/Train"

#processed_folder_test2 = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final_tr2/Test"
#processed_folder_train2 = "c:/Users/Tomasz Marcinkowski/Documents/MEGA/Zbiory/Zbior4_final_tr2/Train"

resize_and_pad_folder(orginal_folder_test, processed_folder_test1, (224,224), 127, method=2)
resize_and_pad_folder(orginal_folder_train, processed_folder_train1, (224,224), 127, method=2)

#resize_and_pad_folder(orginal_folder_test, processed_folder_test2, (224,224), 127, method=2)
#resize_and_pad_folder(orginal_folder_train, processed_folder_train2, (224,224), 127, method=2)