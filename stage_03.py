with open("artifact.txt",'r') as f:
    txt=f.read()

with open("artifact.txt",'w') as f:
    text=f.write(txt+'this the end of the stage03')
print(text)