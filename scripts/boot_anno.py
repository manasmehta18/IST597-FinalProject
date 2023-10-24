import os
import random

# constable, va, boudin, lee
# lionel, cox, watts

painter = 'va'

path = "../annotations/" + painter + "/"

for i in range(10):

    f = open(path + painter + "__" + str(i) + ".json", "a")

    boot_dir = []

    f.write('{"annotations": [\n')

    dir_list = os.listdir("../" + painter)

    print(len(dir_list))

    for _ in range(len(dir_list)):
        boot_dir.append(random.choice(dir_list))

    for file in boot_dir:
        f.write('{"image_id": ' + file.rsplit( ".", 1 )[ 0 ] +',"id": 1,"caption": ""},\n')

    f.write(']}')

    f.close()