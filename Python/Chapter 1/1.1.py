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
    Without Data Structure ??? set is a data-structure...
    :param string:
    :return: bool
    '''
    if string == "" or string is None: return False
    return len(set(string)) == len(string)


if __name__ == "__main__":
    start = ('==' * 20);
    print(start)

    list_of_strings = ["Hello", "Raymond", "Python", None]

    for string in list_of_strings:
        print("Result of (isUniqueW) & (isUnique): ", isUniqueW(string), isUnique(string))


    end = '==' * 20;
    print(end)
