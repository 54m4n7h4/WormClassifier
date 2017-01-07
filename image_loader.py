import glob
from image import create_image_from_file, Image
def load_files(directory):   
    w1files = []
    w2files = []
    files = []
    # go through all files, creating two lists for w1 and w2
    for file_name in glob.glob(str(directory) + '/*_w1_*'):
        w1files.append(file_name)
    for file_name in glob.glob(str(directory) + '/*_w2_*'):
        w2files.append(file_name)
    
    # now go through w1 files, finding the matching w2 file
    for w1file in w1files:
        file_split = w1file.split('_w1_')
        
        file_prefix = file_split[0]
        w2file = [f for f in w2files if f.startswith(file_prefix)]
        if(len(w2file) != 0):
            w2file = w2file[0]
            img = create_image_from_file(w1file,w2file,file_prefix)
            files.append(img)

    return files