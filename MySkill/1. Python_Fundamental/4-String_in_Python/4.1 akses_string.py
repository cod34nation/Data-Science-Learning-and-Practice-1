print("myskill providing course"[9])
print("aditya pramana putra"[-10])

# Creating a String
# with single Quotes
string1 = 'Welcome to My Skill'
print("String with the use of single Quotes:")
print(string1)

# Creating a String
# with double Quotes
string1 = "I'm jon"
print("\nString with the use of Double Quotes : ")
print(string1)

# Creating a String
# with triple Quotes
string1 = '''I'am My Skill Student and I Develop "Skill"'''
print("\nString with the use of Triple Quotes :")
print(string1)


# Creating String with triple
# Quotes allows multiple lines
string1 = '''
        My Skill
        for
        Life
'''
print("\nCreating a multiline String :")
print(string1)


#Program to reverse a string

msk = "My Skill"
print(msk[::-1])

# Reverse the string using reversed and join function

msk = "afrizal setyo"
msk = "-".join(reversed(msk))
print(msk)

balik_nama = "Afrizal"
balik_nama = "".join(reversed(balik_nama))
print(balik_nama)
print(balik_nama[::1])

#STRING SLICING : 
#Creating a String
String = "AFRIZAL SETYO WIBISONO"
print ("Initial String :")
print(String)

#printing 3rd to 12 th character
print ("\nSlicing characters from 3-12:")
print(String[3:8])


#Printing characters between
#3rd and 2nd last character
print ("\nSlicing characters between "+"3rd and 2nd last character:")
print (String[3:-1])
print(String[-1])
print(String[:])

# Python Program to Update
# character of a String

String1 = "AFRIZAL SETYO WIBISONO"
print("Initial String : ")
print(String1)


# Updating a character of the string
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1

list1 = list(String1)
list1[4] = 'Y'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index : ")
print(String2)

#2 
String3 = String1[0:4] + 'Y' + String1[5:]
print(String3)
print(String3[2:3])

#Update Entire String

String4 = "Hello, I'm AFRIZAL"
print ("Initial String :")
print (String4)
# Updating a String

String4 = "Hello, I'm OCTAVIA"
print("\nUpdated String : ")
print(String4)




#Delete Chacacter
String1 = "AFRIZAL SETYO WIBISONO"
print("Initial String : ")
print(String1)

#Deleting a character 
#of the String
String2 = String1[5:0] + String1[6:]
print("\nDeleting character at 2nd Index: ")
print(String2)

String1 = "Weclome to My Skill"
print("initial String")
print(String1)


# del String1
# print("\nDeleting entire String:")
# print(String1)


#Escape Sequence in Python

#initial String
String2 = '''I 'm "Smart"'''
print("initial string with of triple quotes :")
print(String2)


# Escaping Single Quote
String2 = 'I\'m very "tired" with you'
print("\nEscaping Single Quote: ")
print(String2)

#Escaping Double Quotes
String2 = "I'm very \" Tired\" with you "
print("\nEscaping Double Qoutes : ")
print(String2)

# Printing Paths with the
# use of tab
String2 = "Note: \t Jika ada sesuatu..."
print("n\Tab: ")
print(String2)


#Printing paths with the
#use of new line
String2 = "Nama\nNIM"
print("\nNew Line: ")
print(String2)

#Formating in String

# Default Order
String4 = "{} {} {}".format('My Skill', 'for','Learning')
print("Print String in default order :")
print(String4)

#Positional Formating
String4 = "{1} {0} {2}".format('MySkill','for','Learning')
print(String4)

# Keyword Formatiing
String4 = "{l} {f} {g}".format(g='My Skill',f='For', l='Learning')
print("\nPrint String in order of keywords: ")
print(String4)


#Formating of Integers
String1 = "{0:b}".format(16)
print("\Binary representation of 16 is ")
print(String1)

#formating of floats 
String1 = "{0:e}".format(150.20)
print("\nExponent representation of 150.20 is ")
print(String1)

String1 = "{0: .2f}".format(23/400)
print("\none-sixth is : ")
print(String1)


# String alignment
String1 = "|{:<1}|{:^1}|{:>1}|".format('MySkill','for','Learning')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("MySkillForLearning",
													2021)
print(String1)

Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %1.1fd' % Integer1)

print('The value of Integer1 is %3.3f' % Integer1)















