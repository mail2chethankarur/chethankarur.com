from PIL import Image
# from webptools import webplib as webp
import os, shutil



#input photos path (usually in website folder in documents - it can have subfolders)
input_base_path = '/Users/chethankarur/Pictures/chethankarur.com/img/homepage portfolio/'
output_base_path = input_base_path+'webpoutput/'

folders_list = os.listdir(input_base_path)

# converts the photos to webp format
def converttowebp(input_file_path):
    output_file_path = input_file_path.replace(".jpg",".webp")

    image = Image.open(input_file_path)
    width, height = image.size

    if (width<height):
        resize_wdth = 1200
        resize_height = str(int((height*resize_wdth)/width))
        image.thumbnail(size=((resize_wdth, resize_height)))
    else:
        resize_height = 1500
        resize_wdth = str(int((width*resize_height)/height))
        image.thumbnail(size=((resize_wdth, resize_height)))

    resize_command = "-resize {0} {1}".format(resize_wdth,resize_height)

    #webp.cwebp(input_file_path,output_file_path,resize_command)
    image.save(output_file_path,'webp')
    print(input_file_path)
    print(output_file_path)
    print ("-----")

#the main code
for i in folders_list:
    print (7*"#")
    print (i)


    if ('.' in i):
        print ("Skipped "+str(i))
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
    print (7*"#")


#The below code is to copy the webp files from the above folder
#and place it in their corresponding folder

for i in folders_list:
    print(i)



