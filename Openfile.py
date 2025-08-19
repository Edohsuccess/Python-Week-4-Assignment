file = open("./WEEK4/Kingsuccess_Contacts.pdf", "w")
# file.write("Kingsuccess1, Kingsuccess2, Kingsuccess3\n")


# Appending content to a file
#file = open("./WEEK4/Kingsuccess_Contacts.pdf", "a")
#file.write("Ooh my Sweet Wive, I love you so much")


# Reading content from a file

file = open("./WEEK4/Kingsuccess_Contacts.pdf", "r")
content = file.readline()
print(content)

# Reading content from a file

file = open("./WEEK4/Kingsuccess_Contacts.pdf", "r")
content = file.readline()
print(content)
file = open("./WEEK4/Kingsuccess_Contacts.pdf", "r")
content = file.readline()
print(content)

#Error Handling
try:
    file = open("Kingsuccess_Contacts.pdf", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")



# file = open("Kingsuccess_Contacts.pdf", "r")
# content = file.read()
# print(content)