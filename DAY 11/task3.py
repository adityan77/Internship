text="Hello Binary World"
t="\nWelcome To Python Programming" 
with open("Binary.bin","wb+") as writefile:
    writefile.write(text.encode())#Encoding The Text In The File
    writefile.write(t.encode())
    writefile.read()
with open("Binary.bin","rb+") as readfile:
    decodeFile=readfile.read()
    print(decodeFile.decode())#Decoding File Content
    