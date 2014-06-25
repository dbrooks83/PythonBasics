#Write a program to read through the mbox-short.txt and figure out 
#who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those 
#lines as the person who sent the mail. The program creates a Python 
#dictionary that maps the sender's mail address to a count of the number
#of times they appear in the file. After the dictionary is produced, 
#the program reads through the dictionary using a maximum loop to find 
#the most prolific committer.

fname = raw_input("Enter file:")
fh = open(fname)
counts = dict()
wordlist=list()


for line in fh:
    if not line.startswith('From: '): continue
    if line.startswith('From: '):
        words = line.split()
        wordlist.append(words[1])
for word in wordlist:
    counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount