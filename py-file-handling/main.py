name = input("Input your name:")
f = open("altcode.py", "w")
intext = "print('" + name + "')"
f.write(intext)
f.close()