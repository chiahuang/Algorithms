def reverseString(word: str, recursion: bool = False) -> str:
    '''

    :param word: str
    :param recursion: bool
    :return:
    '''
    if recursion:
        if word == "":
            return ""
        else:
            return word[-1] + reverseString(word[:-1], recursion)
    else:
        return word[::-1]



if __name__ == "__main__":
    start = ('==' * 20);
    print(start)

    print(reverseString("Hello", True))
    print(reverseString("Raymond", True))
    print(reverseString("Python", True))

    print('\n')

    print(reverseString("Hello"))
    print(reverseString("Raymond"))
    print(reverseString("Python"))

    end = '==' * 20;
    print(end)