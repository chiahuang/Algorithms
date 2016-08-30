def compression(word: str) -> str:
    '''
    Without Data Structure
    :param word: str
    :return: str
    '''
    size = len(word) - 1
    index = 1
    count = 1
    result = ""
    while(index <= size):
        if index == size:
            count +=1
            result += ''.join(word[index - 1] + str(count))

        if word[index - 1] == word[index]:
            count += 1
        else:
            result += ''.join(word[index-1] + str(count))
            count = 1

        index += 1
    return result

def compressionW(word: str) -> str:
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

    print(compression("aabcccccaaa"))
    print(compressionW("aabcccccaaa"))




    print('==' * 20)