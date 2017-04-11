print('I am 6\'2" tall')

"I \"understand\" this"

tabby_cat = "\tI'm tabbed in."
persian_Cat = "I'm split \non a a line"
backslash_cat = "I'm \\a \\ cat"

fat_cat = """
I'll do a list:
\t* cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_Cat)
print(backslash_cat)
print(fat_cat)

print('what if I \t\t\t tabbed here')

print('what is \b \'\\b\' represent \n and \r it is said'
      '  \'r\' is a return ')


while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i)