#count total number of "is","up" and "to"
def ISTOUPCOUNT():
    count=0
    f=open("writer.txt","r")
    line=f.read()
    word=line.split()
    for i in word:
        if i=="is" or i=="to" or i=="up":
        count+=1
    print(count)
    f.close()
ISTOUPCOUNT()