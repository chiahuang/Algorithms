def isUniqueW(string: str) -> bool:
    '''
    With Data Structure
    :param string:
    :return: bool
    '''
    if string is None:
        return False
    if len(string) > 128 or string == "":
        return False

    array = [False for _ in range(128)]
    for character in string:
        if array[ord(character)]:
            return False
        array[ord(character)] = True
    return True


def isUnique(string: str) -> bool:
    '''
    Without Data Structure
    :param string:
    :return: bool
    '''
    if string == "" or string is None: return False
    return len(set(string)) == len(string)


if __name__ == "__main__":
    start = ('==' * 20);
    print(start)

    print(isUniqueW("Hello"))
    print(isUniqueW("Raymond"))
    print(isUniqueW("Python"))
    print(isUniqueW(None))

    print('\n')

    print(isUnique("Hello"))
    print(isUnique("Raymond"))
    print(isUnique("Python"))
    print(isUnique(None))

    end = '==' * 20;
    print(end)
