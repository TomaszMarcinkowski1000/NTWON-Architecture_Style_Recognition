import glob, os

def rename(dir):
    counter = 0
    for pathAndFilename in os.listdir(dir):
        counter += 1
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(os.path.join(dir, pathAndFilename), os.path.join(dir, str(counter).zfill(4) + ext))

#rename('c:\\Users\\Tomasz Marcinkowski\\Downloads\\Extreme Picture Finder\\NTwON\\Russian Revival')
#rename('c:\\Users\\Tomasz Marcinkowski\\Downloads\\Extreme Picture Finder\\NTwON\\Postmodernism')
#rename('c:\\Users\\Tomasz Marcinkowski\\Documents\\MEGA\\Zbiory\\Zbior3_koledzy - kopia zapasowa\\Postmodernism')