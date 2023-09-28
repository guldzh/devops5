#Create two string variables bigger than the length 3.
#If the second string starts with the first string’s 
#last three characters, print true. If not, print false.

string1=input("Please enter String1 length more than 3: ")
string2=input("Please enter String2 length more than 3: ")

if string2.startswith(string1[-3:]):
    print(True)
else:
    print(False)




