from PIL import Image
from webptools import webplib as webp
import os

#input photos path (usually in website folder in documents - it can have subfolders)
input_base_path = '/Users/chethankarur/Documents/website/'
output_base_path = '/Users/chethankarur/Documents/website/webpoutput/'
os.mkdir(output_base_path)

folders_list = os.listdir(input_base_path)

def converttowebp(input_file_path):
    input_file_path = folder_path+j
    output_file_path = input_file_path.replace("website/","website/webpoutput/").replace(".jpg",".webp")

    image = Image.open(input_file_path)
    width, height = image.size
    #resize_command = "-resize 1200 800"
    if (width<height):
        resize_wdth = 800
        resize_height = str(int((height*800)/width))
    else:
        resize_height = 800
        resize_wdth = str(int((width*800)/height))
    resize_command = "-resize {0} {1}".format(resize_wdth,resize_height)

    webp.cwebp(input_file_path,output_file_path,resize_command)
    print(input_file_path)
    print(output_file_path)
    print ("-----")

for i in folders_list:
    print (7*"#")
    print (i)
    print (7*"#")
    os.mkdir(output_base_path+i)
    if (i=='webpoutput' or '.' in i):
        print ("Skipped webpoutput")
        continue
    else:
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
