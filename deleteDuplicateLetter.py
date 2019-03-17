## whaaaaaat => what

def deleteDuplicateLetter(word):
    if not word:
        return word
    lastElem = word[0]
    count =1 
    res = ''
    for ch in word[1:]:
        if lastElem == ch:
            count += 1 
        else:
            res = res + lastElem
            lastElem = ch 

    res = res + lastElem
    return res 

def main():
    nw = deleteDuplicateLetter("whaaaaaat")
    print(nw)

main()




