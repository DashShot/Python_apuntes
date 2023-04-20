# Texto
error_message = "NameError: name 'a' is not defined."
start = 11
stop = 15

print(error_message[start:stop]) # portion from index 11 to 15
print(error_message[start:]) # portion from 11 till last element
print(error_message[:stop]) # portion from index 0 to 15
print(error_message[:]) # all items

step=2
print(error_message[start:stop:step]) # portion from 11 till 15 with increment of 2