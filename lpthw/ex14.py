from sys import argv

script, user_name = argv

prompt = '>'

print('Hi, %s, I am the %s script' %(user_name, script))
print('i\'d like to ask you a few questions')

print('do you like me %s' %user_name)
likes = input(prompt)

print('where do you live %s ?' % user_name)
lives = input(prompt)

print('what kind of computer do you have?')
computer = input(prompt)

print('''
alright, so you said %r about liking me.
You live in %r. And you have a %r computer.
''' %(likes,lives,computer))