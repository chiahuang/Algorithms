def isUnique(string: str) -> bool:
    '''
    Without Data Structure
    :param string:
    :return: bool
    '''
    if len(string) > 128:
        return False

    array = [False for _ in range(128)]
    for character in string:
        if array[ord(character)]:
            return False
        array[ord(character)] = True
    return True

def isUniqueW(string: str) -> bool:
    '''
    With Data Structure
    :param string:
    :return: bool
    '''
    return len(set(string)) == len(string)



if __name__ == "__main__":
    start = ('==' * 20) ; print(start)

    print(isUnique("Hello"))
    print(isUnique("Raymond"))
    print(isUnique("Python"))

    print('\n')

    print(isUniqueW("Hello"))
    print(isUniqueW("Raymond"))
    print(isUniqueW("Python"))

    end = '==' * 20 ; print(end)