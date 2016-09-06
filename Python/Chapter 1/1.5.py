def compress(word: str) -> str:
    '''
    for loop
    :param word:
    :return:
    '''
    if word == "" or word is None:
        return ""

    count = 0
    currChar = ""
    result = ""
    for character in word:
        if currChar == "":
            currChar = character
            count += 1

        elif character != currChar:
            result += ''.join(currChar + str(count))
            currChar = character
            count = 1
        else:
            count +=1
    result += ''.join(currChar + str(count))

    return result



def compression(word: str) -> str:
    '''
    Without Data Structure - While loop
    :param word: str
    :return: str
    '''
    if word == "" or word is None:
        return ""
    size = len(word)
    index = 1
    count = 1
    result = ""

    while(index < size):
        if word[index - 1] == word[index]:
            count += 1
        else:
            result += ''.join(word[index-1] + str(count))
            count = 1

        index += 1

    result += ''.join(word[index - 1] + str(count))
    return result

def compressionW(word: str) -> str:
    if word == "" or word is None:
        return ""
    curchar = word[0]
    count = 0
    result = []
    for character in word:

        if curchar == character:
            count += 1
        else:
            result.append((curchar, count))
            curchar = character
            count = 1

    result.append((curchar, count))

    temp = ''
    for key, value in result:
        temp += ''.join(key + str(value))
    return temp



if __name__ == "__main__":
    print('==' * 20)

    print(compress("aabcccccaaa"))
    print(compress("aabbcchhddkks"))
    print(compress(""))
    print(compress(None))
    print(compression("aabcccccaaa"))
    print(compression("aabbcchhddkks"))
    print(compression(""))
    print(compression(None))
    print(compressionW("aabcccccaaa"))
    print(compressionW("aabbcchhddkks"))
    print(compressionW(""))
    print(compressionW(None))




    print('==' * 20)