with open("adi.jpg","rb") as file:
    readData=file.read()
with open("image.jpg","wb") as file:
    file.write(readData)#copying The Data Of Image File Into Another Image File
