#---------OPTION ONE--------
#1st Round
a = "True"
b = "True"

print(not a or b)
#2nd round
b = not b

print(not a or b)
#3rd round
a = b
b = not b

print(not a or b)
#4th round
b = not b

print(not a or b)
print("\n")


#---------SECOND OPTION----------
#1st Round
a = "True"
b = "True"

print((a or b) and not (a and b))
#2nd round
b = not b

print((a or b) and not (a and b))
#3rd round
a = b
b = not b

print((a or b) and not (a and b))
#4th round
b = not b

print((a or b) and not (a and b))
print("\n")


#---------THIRD OPTION---------
#1st Round
a = "True"
b = "True"

print((a and b) or not (a or b))
#2nd round
b = not b

print((a and b) or not (a or b))
#3rd round
a = b
b = not b

print((a and b) or not (a or b))
#4th round
b = not b

print((a and b) or not (a or b))
print("\n")


#---------FOURTH OPTION-----------
#1st Round
a = "True"
b = "True"

print((a and not b) or (not a and b))
#2nd round
b = not b

print((a and not b) or (not a and b))
#3rd round
a = b
b = not b

print((a and not b) or (not a and b))
#4th round
b = not b

print((a and not b) or (not a and b))
print("\n")


#--------FIFTH OPTION-------
#1st Round
a = "True"
b = "True"

print(a and not b)
#2nd round
b = not b

print(a and not b)
#3rd round
a = b
b = not b

print(a and not b)
#4th round
b = not b

print(a and not b)
print("\n")