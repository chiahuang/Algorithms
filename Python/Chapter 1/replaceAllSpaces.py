def replaceAllSpaces(word:str) -> str:
    '''

    :param word: str
    :return: str
    '''
    if word is None:
        return ""
    if word == "":
        return word
    return '%20'.join(word.split(' '))

def replaceAllSpacesW(word: str) -> str:
    '''

    :param word:
    :return: str
    '''
    collection = []
    for character in word:
        if character == " ":
            collection.append("%20")
        else:
            collection.append(character)
    return "".join(collection)



if __name__ == "__main__":
    start = ('==' * 20);
    print(start)

    print(replaceAllSpaces(None))
    print(replaceAllSpaces(""))
    print(replaceAllSpaces("Hello, World"))
    print(replaceAllSpaces("Welcome to coding interview questions"))
    print(replaceAllSpaces("Python is god"))
    print(replaceAllSpaces("Python is an animal"))
    print(replaceAllSpaces("god dog"))

    print("\n")

    print(replaceAllSpacesW("Hi, I came from the Netherland."))

    end = '==' * 20;
    print(end)