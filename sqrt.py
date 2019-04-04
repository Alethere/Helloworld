##f=open("D:/Escritorio/camarosa_probes_100.txt","r")
##
##for line in f.readlines():
##    print(line.split(","))
##        
##f.close()

f=open("output.txt","w")

inscription=["We are made of gold",245,
             "karats of pure gold. What is the same,\n",4500,"mg of Au."]
inscription=" ".join(map(str,inscription))
f.write(inscription)

f.close()

