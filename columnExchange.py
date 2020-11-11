import csv


fname = "temperature.csv"

fWriteName = open("newdata.csv",'w')
cfw = csv.writer(fWriteName)


with open(fname) as f:
    fcsv = csv.reader(f)
    i=0
    for row in fcsv:  
        if i == 0:
            i += 1
            continue
        newline = [i,row[3],row[1],row[2],row[0]]
        #print(newline)
        cfw.writerow(newline)
        i += 1
        if i%10000 == 0:
            print("i = ", i)

fw.close()
        