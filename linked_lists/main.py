from linked_list import LinkedList

def main():
    ll = LinkedList()
    ll.push(24)
    ll.push(21)
    ll.push(25)
    ll.push(26)
    ll.push(30)
    ll.find_middle_element()
    ll.traverse(ll.head)

if __name__ == '__main__':
    main()