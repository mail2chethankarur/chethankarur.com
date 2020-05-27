from PIL import Image
from webptools import webplib as webp
import os, shutil



#input photos path (usually in website folder in documents - it can have subfolders)
input_base_path = '/Users/chethankarur/Documents/website/'
output_base_path = input_base_path+'webpoutput/'

folders_list = os.listdir(input_base_path)

# converts the photos to webp format
def converttowebp(input_file_path):
    output_file_path = input_file_path.replace("website/","website/webpoutput/").replace(".jpg",".webp")

    image = Image.open(input_file_path)
    width, height = image.size

    if (width<height):
        resize_wdth = 800
        resize_height = str(int((height*800)/width))
    else:
        resize_height = 1200
        resize_wdth = str(int((width*1200)/height))
    resize_command = "-resize {0} {1}".format(resize_wdth,resize_height)

    webp.cwebp(input_file_path,output_file_path,resize_command)
    print(input_file_path)
    print(output_file_path)
    print ("-----")

#deletes the old output folder of exists
if os.path.exists(output_base_path):
    shutil.rmtree(output_base_path)
os.mkdir(output_base_path)

#the main code
for i in folders_list:
    print (7*"#")
    print (i)
    print (7*"#")

    if (i=='webpoutput' or '.' in i):
        print ("Skipped "+str(i))
        continue
    else:
        os.mkdir(output_base_path+i)
        folder_path = input_base_path+i+"/"
        files_list = os.listdir(folder_path)
        for j in files_list:
            input_file_path = folder_path+j
            if ('.jpeg' in input_file_path):
                os.rename(input_file_path,input_file_path.replace('.jpeg','.jpg'))
                input_file_path = input_file_path.replace('.jpeg','.jpg')
            if ('.jpg' not in input_file_path):
                continue
            converttowebp(input_file_path)
