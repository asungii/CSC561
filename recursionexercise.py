def recursplit(str):
    word = ""
    final_list = []
    if " " not in str:
        return [str]
    for i in range(len(str)):
        print(str[i:i+1])
        if str[i:i+1] == " ":
            print(word)
            return [word, *recursplit(str[i+1:])] # this is very cool man!!
        else:
            word = word + str[i:i+1]
    
def recursplit2(text):
    if " " not in text:
        return [text]
    word = ""
    final_index = -1
    for i in range(len(text)):
        if text[i:i+1] == " ":
            final_index = i+1
            break
        else:
            word += text[i:i+1]
    return recursplit2(text[final_index:]).append(word)

    
    



print(recursplit("this is a test which is a really funny type of thing to do"))