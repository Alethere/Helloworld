################################################
## Let's play around with some more exercises ##
################################################

f=open("rosalind_ini5.txt","r")
out=open("cut_song.txt","w")
a=1

for line in f:
    if a%2 == 0:
        out.write(line)
    a=a+1
out.close()
