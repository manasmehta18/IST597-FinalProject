import os

# constable, lionel, lee, va, watts, boudin, cox

painter = 'cox'

path = "../annotations/sky/"

f = open(path + painter + ".json", "a")

f.write('{"annotations": [\n')


dir_list = os.listdir("../sky/" + painter)

for file in dir_list:
    f.write('{"image_id": ' + file.rsplit( ".", 1 )[ 0 ] +',"id": 1,"caption": ""},\n')

f.write(']}')

f.close()