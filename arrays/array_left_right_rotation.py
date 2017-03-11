def right_rotations(array, n, r):
    output_array = [None] * n
    for i in range(len(array)):
        index = i + r
        if index < n:
            output_array[index] = array[i]
        elif index >= n:
            output_array[index - n] = array[i]
    return output_array


def left_rotations(array, n, r):
    output_array = [None] * n
    for i in range(len(array)):
        index = i - r
        if index >= 0:
            output_array[index] = array[i]
        elif index < 0:
            output_array[index + n] = array[i]
    return output_array


def left(array, n, r):
    for i in range(r):
        tmp = array[0]
        for i in range(len(array) - 1):
            array[i] = array[i + 1]
        array[n - 1] = tmp
    return array


def right(array, n, r):
    for i in range(r):
        tmp = array[n - 1]
        for i in range(len(array) - 1, 0, -1):
            array[i] = array[i - 1]
        array[0] = tmp
    return array


def main():
    array = [1, 2, 3, 4, 5]
    shifts = 2

    print("Before", array)
    print("After Right Rotations", right_rotations(array, len(array), shifts))
    print("After Left Rotations", left_rotations(array, len(array), shifts))


if __name__ == '__main__':
    main()
