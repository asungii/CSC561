import math

# done, was only returning the strings of new repeated over and over. So, in recursion, had to add the str[0:1] + replace...
def replace(str, sub, new):
    if len(str) < len(sub):
        return str
    elif (str[0:len(sub)] == sub):
        return new + replace(str[len(sub):], sub, new)
    else:
        return str[0:1] + replace(str[1:], sub, new)

print(replace("hello lsdofallolo sdflo", "lo", "alop"))

# done w/ recursion
def count(str, sub):
    print(len(str))
    if len(str) < len(sub):
        return 0
    elif (str[0:len(sub)] == sub):
        print(str)
        print("BOOM")
        return 1 + count(str[len(sub):], sub)
    else:
        print(str)
        return count(str[1:], sub)

# this did not work bro just keeping for posterity
"""
# in progress
def longest(str):
    spl_str = str.split()
    longest_sub = 0
    longest_sub_index = 0
    for i in range(0, len(spl_str)):
        if len(spl_str[i]) > longest_sub:
            longest_sub_index = i
            longest_sub = len(spl_str[i])
    for k in range(longest_sub_index):
        longest_sub_index += len(spl_str[k])
    return (longest_sub_index, longest_sub_index + len(spl_str[longest_sub_index]))
"""

# done
def longest(str):
    spl_str = str.split()
    longest_sub = 0
    word_index = 0
    char_index = 0
    for i in range(0, len(spl_str)):
        if len(spl_str[i]) > longest_sub:
            word_index = i
            longest_sub = len(spl_str[i])
    # print(longest_sub)
    # print(word_index)
    for k in range(word_index):
        char_index += len(spl_str[k]) + 1
    return (char_index, char_index + len(spl_str[word_index]))

print(longest("Four score and seven hours ago"))