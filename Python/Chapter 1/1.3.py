'''
Sorting can also solve to check whether it is permutation but O(n log n) depending on the sorting algorithm

'''

def isPermutation(word: str, other:str) -> bool:
    '''
    With Data Structure
    :param word: str
    :param other: str
    :return:
    '''
    if len(word) == 0 and len(other) == 0:
        return True

    if len(word) == 0 or len(other) == 0 or len(word) != len(other):
        return False

    collection = {}
    for character in word.lower():
        if character in collection:
            collection[character] += 1
        else:
            collection[character] = 1

    for character in other.lower():
        if character in collection:
            if collection[character] == 1:
                collection.pop(character)
            else:
                collection[character] -= 1
        else:
            return False

    if len(collection) != 0:
        return False

    return True

if __name__ == "__main__":
    start = ('==' * 20);
    print(start)

    print(isPermutation("Hello", "Hello"))
    print(isPermutation("Raymond", "Mlondray"))
    print(isPermutation("Python", "Pokemon"))
    print(isPermutation("", "Pokemon"))
    print(isPermutation("Python", ""))
    print(isPermutation("", ""))
    print(isPermutation("god dog", "dog god"))

    end = '==' * 20;
    print(end)

