import sys

spath = sys.argv[1]
psid = 0
file_object = open(spath, 'r') # Opens file for writing.Creates this file doesn't exist.
for line in file_object:
    if line.strip() == '':
        continue

    if line.find("mediaserver") > -1:
        line = ' '.join(line.split())
        lineTokens = line.split(' ')
        psid = int(lineTokens[1])
        print(lineTokens[1])
        break
file_object.close()
sys.exit(psid)
