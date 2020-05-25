import random
import os

## GIVE INPUT PATH HERE
input_base_path = '/Users/chethankarur/Documents/GitHub/chethankarur.com/img/street/'
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
