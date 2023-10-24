import os

# constable, lionel, lee, va, watts, boudin, cox

painter = "cox"


for i, filename in enumerate(os.listdir("../sky/" + painter)):
    print(filename)
    if filename[-5:] == ".jpeg" or filename[-5:] == ".tiff" or filename[-5:] == ".JPEG":
        os.rename("../sky/" + painter + "/" + filename, "../sky/" + painter + "/" + str(i + 1) + filename[-5:])
    else:
        os.rename("../sky/" + painter + "/" + filename, "../sky/" + painter + "/" + str(i + 1) + filename[-4:])