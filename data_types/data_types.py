import sys


def print_info(i):
    print("-------")
    print(i)
    print(id(i))
    print(hex(id(i)))
    print(type(i))
    print("size: ", sys.getsizeof(i))


def main():
    i = 123
    print_info(i)

    j = 124
    print_info(j)

    k = 12398793872037029375029352352523523523
    print_info(k)

    a_list = []
    print_info(a_list)

    dictionary = {}
    print_info(dictionary)

    string = "hello"
    print_info(string)


if __name__ == "__main__":
    main()
