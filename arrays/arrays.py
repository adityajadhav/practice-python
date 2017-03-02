def array_test():
    # Experiments using Python arrays

    array = [1, 2, 3, 4]
    print(array)

    array.append(5)
    print(array)

    item = array.pop()
    print(item)

    array.reverse()
    print(array)

    array.remove(4)  # remove item with given value
    print(array)

    array.sort()
    print("sorted in place: ", array)


def indexes_slices_test():
    a = ['a', 2, 4, 5, 'b', 2]
    print(a[0:len(a)])

    print(a[-2])

    print(a[2])

    print(a[0:])

    print(a[0:-1])

    print(a[1:-2])

    b = a[:]  # shallow copy of a

    a.pop()

    print(a)

    print(b)


def main():
    # array_test()
    indexes_slices_test()


if __name__ == '__main__':
    main()
