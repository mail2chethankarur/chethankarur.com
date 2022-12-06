from PIL import Image
# from webptools import webplib as webp
import os, shutil, random

#input photos path (usually in website folder in documents - it can have subfolders)
input_base_path = '/Users/chethankarur/Pictures/chethankarur.com/img/homepage portfolio/untitled_folder2/'
output_base_path = input_base_path+'webpoutput/'
website_img_path = '/Users/chethankarur/Pictures/chethankarur.com/img/homepage portfolio/untitled_folder2/'

folders_list = os.listdir(input_base_path)

# converts the photos to webp format
def converttowebp(input_file_path):
    output_file_path = input_file_path.replace("/untitled_folder2/","/qw/")
    print("!!!!",input_file_path)

    image = Image.open(input_file_path)
    width, height = image.size

    if (width<height):
        resize_wdth = 700
        resize_height = str(int((height*resize_wdth)/width))
        image.thumbnail(size=((resize_wdth, resize_height)))
    else:
        resize_height = 800
        resize_wdth = str(int((width*resize_height)/height))
        image.thumbnail(size=((resize_wdth, resize_height)))

    resize_command = "-resize {0} {1}".format(resize_wdth,resize_height)

    #webp.cwebp(input_file_path,output_file_path,resize_command)
    image.save(output_file_path,'webp')
    print(input_file_path)
    print(output_file_path)
    return(output_file_path)

dict_legth = {}

for i in folders_list:
    if ('.' not in i):
        l=[]
        num_cal_path = website_img_path+i.lower()
        len_folder = len(os.listdir(num_cal_path))
        l.append(len_folder-1)
        dict_legth[i.lower()]=l

print(dict_legth)

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
            if ('.webp' not in input_file_path or 'q_t' in input_file_path):
                continue
            op_path = converttowebp(input_file_path)
            target_path_postfix = op_path.split('/')[-2:][0].lower()+'/'+op_path.split('/')[-2:][1]
            target_file_path = website_img_path+target_path_postfix
            shutil.copy(op_path, target_file_path)
            print(target_file_path)
            print ("-----")
    print (7*"#")

    if ('.' not in i):
        l = dict_legth[i]
        num_cal_path = website_img_path+i.lower()
        len_folder = len(os.listdir(num_cal_path))
        l.append(len_folder)
        dict_legth[i.lower()]=l

        ## GIVE INPUT PATH HERE
        input_base_path = num_cal_path+'/'
        photos_list = os.listdir(input_base_path)

        random_intset = random.sample(range(10000), len(photos_list))

        for i in range(0,len(photos_list)):
            file_actual_path = input_base_path+photos_list[i]
            file_randomrename_path = input_base_path+'rand{0}.webp'.format(random_intset[i])
            os.rename(file_actual_path, file_randomrename_path)

        print("Shuffling Done")
        photos_list = os.listdir(input_base_path)
        photos_list.sort()
        print (len(photos_list))

        for i in range(0, len(photos_list)):
            file_actual_path = input_base_path+photos_list[i]
            t = i+1
            file_actual_renamed_path = file_actual_path.replace(photos_list[i],str(t)+'.webp')
            os.rename(file_actual_path, file_actual_renamed_path)

print(dict_legth)
mainstring = ''

# for i in dict_legth:
#     folder_name = i
#     start_num = dict_legth[i][0]
#     end_num = dict_legth[i][1]
#     outputpath = '/Users/chethankarur/Pictures/addon.txt'
    
#     count  =1
#     for i in range(start_num,end_num+1):
#         iterstring = """<div class="mbr-gallery-item mbr-gallery-item__mobirise3 mbr-gallery-item--p0" data-tags="Animated" data-video-url="false">
#         <div href="#lb-gallery1-6" data-slide-to="{0}"data-toggle="modal">
#             <img alt="" src="img/{1}/{2}.webp">
#             <span class="icon-focus"></span>
#         </div>
#     </div> \n""".format(i,folder_name,i+1)

#         iterstring2 = """<div class="carousel-item">
#     <img alt="" src="img/{0}/{1}.webp">
#     </div>""".format(folder_name,i)
        
#         if (count==1):
#             i1 = iterstring
#             i2 = iterstring2
#             count+=1
#         else:
#             i1 += iterstring
#             i2 += iterstring2

#     mainstring += i1+"\n"+"\n"+i2+"\n"+"\n"

# text_file = open(outputpath, "w")
# n = text_file.write(mainstring)
# text_file.close()






