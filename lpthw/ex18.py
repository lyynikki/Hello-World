def print_two(*lll):
    arg1,arg2 = lll
    print('arg1: %r,arg2:%r'%(arg1,arg2))

def print_two_again(lal,al):
    print('arg1:%r,arg2:%r'%(lal,al))

def print_one(aaa):
    print('arg1:%r'%aaa)

def print_none():
    print('I don\'t take argument')

print_two('this is a','this is b')
print_two_again('this is aaa','look at bbb')
print_one('only one')
print_none()
