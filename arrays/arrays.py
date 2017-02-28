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


def main():
    array_test();


if __name__ == '__main__':
    main()
