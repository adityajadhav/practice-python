firstName = 'Aditya'
lastName = 'Jadhav'

print('My name is %s %s' % (firstName, lastName))  # old format

print('My name is {} {}'.format(firstName, lastName))  # new format

print('My name is {n2} {n1}'.format(n1=firstName, n2=lastName))

print('{:d}'.format(31))

print('{:05.2f}'.format(3.141592653589793))

print('{:4d}'.format(42))  # padding

print('{:.6}'.format('AdityaJadhav'))  # truncating long string

person = {'first': 'Aditya', 'last': 'Jadhav!'}

print('{first} {last}'.format(**person))

print('{p[first]} {p[last]}'.format(p=person))
