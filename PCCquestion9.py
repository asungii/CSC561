import sys

for i in range(1, len(sys.argv)):
    file = open(sys.argv[i],"r+")

    print(file.name + ": DUPLICATED WORDS")

    lines = file.readlines()
    line_number = 0
    for line in lines:
        line_number += 1
        # words is a list of words
        words = line.split()
        for i in range(len(words) - 1):
            if words[i] == words[i+1]:
                index = 0
                for j in range(i+1):
                    index += len(words[j]) + 1
                print(str(line_number) + " " + words[i] + " " + str(index))

# first attempt: this code works, but it does not print the proper indices because i didn't account for spaces

"""
line_number = 0
for line in lines:
    line_number += 1
    # words is a list of words
    words = line.split()
    for i in range(len(words) - 1):
        if words[i] == words[i+1]:
            index = 0
            for j in range(i+1):
                index += len(words[j]) + 1
            print(str(line_number) + " " + words[i] + " " + str(index))
"""