string1=input("Please enter String1 length more than 3: ")
string2=input("Please enter String2 length more than 3: ")

starts_with_last_three = string2.startswith(string1[-3:])

print(starts_with_last_three)
