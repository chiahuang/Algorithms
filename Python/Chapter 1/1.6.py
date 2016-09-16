def matrix(column: int, row: int) -> list:
    '''
    Given an image represented by an NxN matrix, where each pixel in the image is
    4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
    place?
    :param column: int
    :param row: int
    :return: list
    '''
    image = [[row * c + r + 1 for r in range(row)] for c in range(column)]

    





    return image


if __name__ == "__main__":
    print('==' * 20)

    print(matrix(5, 5))

    print('==' * 20)
