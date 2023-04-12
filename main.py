# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

file_exists = False
connection_failed = True
finished = True
print(id(file_exists))
print(id(connection_failed))
print(id(finished))

print (file_exists==connection_failed)
print (connection_failed==finished)

print (file_exists is connection_failed)
print (connection_failed is finished)

connection_failed = not connection_failed
print (connection_failed is finished)