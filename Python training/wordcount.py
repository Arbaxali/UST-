def wordcount(strr):
    dicti ={}
    word = strr.split()

    for words in word:
        if words in dicti:
            dicti[words] += 1
        else:
            dicti[words] = 1

    return dicti

s = input("enter the string ")
print(wordcount(s))            