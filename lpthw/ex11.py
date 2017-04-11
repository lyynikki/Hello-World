print('how old are you'),

age = input()

print('how tall are you'),

height = input()

print('how much do you weigh'),
weight = input()

print('so, you are %r years old,\n %r tall and %r heavy'
      %(age,height,weight))

a = input().strip().split(' ')

list = [int(i) for i in input().strip().split(' ')]