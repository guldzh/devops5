# TASK-1
# Using count() method find the count of total words in the given string. 
# Get the given string by asking the user

# user_str=input("Please provide some string: ")
# cut_spaces_str=user_str.strip()
# word_count=cut_spaces_str.count(" ")+1
# print(word_count)


# TASK-2
# Given a string, if the first or last chars are 'z', 
# print the string without those 'z' chars, and
#  otherwise print the string unchanged.

# "zHiz" → "Hi"
# "zHi" → "Hi"
# "Hziz" → "Hzi"
# "zzHizz" → zHiz

# str=input("Please provide some strings: ")
# if str[0] =="z" or str[-1]=="z":
#     print(str.removeprefix("z").removesuffix("z")) 
# else:
#     print(str)

# TASK-3
#Create a simple python program to print if a given string 
# ends with another given string. 
#For that ask this two strings to user.

user_str1=input("Please provide String-1: ")
user_str2=input("Please provide String-2: ")
# string1 - academy.lower
# strinf2 - techtorialacademy.lower
# if str2.count(str1)>=1 and str2.endswith(str1)

if user_str2.lower().endswith(user_str1.lower()):
    print("Second string ends with first string!")
else:
    print("It doesnt end with another string!")
