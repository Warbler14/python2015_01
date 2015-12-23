str = 'Hello World!'
print str[0]
print str[1]
print str[2]
print str[-1]
print str[1:5]
print str[1:]
print str[:5]
print str[:]

str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print str1[::2]
print str1[::-1]


print 'Hello ' * 3
print 'a' + str1[1::1]
print '(' +  str1[0:len(str1)] + ')'

print 'M' in str1
print 'm' in str1

numbers = [1,2,3]
numbers.append(4)
print numbers
print numbers[0]
print numbers[0:len(numbers)]
print numbers[len(numbers)-1]
buffer = numbers[ len(numbers)/2 ]
del numbers[ len(numbers)/2 ]
print numbers
numbers.reverse()
print numbers
numbers.append(buffer)
numbers.sort()
print numbers