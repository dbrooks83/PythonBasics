#Write a program that prompts for a file name, then opens that file 
#and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each 
#of the lines and compute the average of those values and produce 
#an output as shown below.
#Desired output:
#Average spam confidence: 0.750718518519

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        zeropos = line.find("0")
        num = line[zeropos:]
        number = float(num)
        count = count+1
        total=total+(number)
        average=total/count
print "Average spam confidence:", average 
