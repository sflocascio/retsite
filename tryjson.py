# import json
# with open("1.txt", "rb") as fin:
#     content = json.load(fin)
# with open("stringJson.txt", "wb") as fout:
#     json.dump(content, fout, indent=1)


import csv
import itertools
import json

cntr = 5

with open('2.txt', 'r') as in_file:
    #lines = (line.split(":") for line in in_file)
    for x in in_file.read().split("\n"):
        with open('newfile.txt', 'w') as newfile:
            newfile.write( '\n' + x + '\n' )
        print(x)


# with open("stringJson.txt", "wb") as fout:
#     json.dump(lines, fout, indent=1)


