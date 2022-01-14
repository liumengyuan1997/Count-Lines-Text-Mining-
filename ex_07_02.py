# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
t = 0
c = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        p = line.find("0")
        n = float(line[p:])
        t = t + n
        c = c + 1
print("Average spam confidence:", t/c)
