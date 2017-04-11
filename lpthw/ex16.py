from sys import argv

script, filename = argv

print('we are going to erase %r' %filename)
print('if you don\'t want that, hit CTRL-C (^C).')
print('if you do want that, hit return')

input('?')

print('opening the file ...')
target = open(filename,'w')

print('truncating the file. Goodbye!')
target.truncate()

print('Now I am going to ask you for three lines')

line1 = input('line1:')
line2 = input('line2:')
line3 = input('line3:')

print('I am going to write those in the file')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('and finally, we close it')
target.close()
