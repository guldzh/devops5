text="Python is a programming language"

substr= text[2:6]
print(substr)

prg=text[12:23]
print(prg)

str2="simple"
print(str2[2:100])  # when ending index is bigger than the last index, 
# slicing will not generate an error. It will simply get the part of 
# the string from starting index to end of the string.

print(str2[2000:4000]) # it will output an empty string

print(str2[4:2]) # It will output an epty string. Slicing function will always work left to right  
                 # unless there is negative steps involved

# Which numerical value will evaluate to True when converted to Boolean? anything except 0
# What happens when we convert the string to boolean. - Any string except an empty string 
# will evaluate to True

str3="DevOps"
b=bool(str3[2:10])
print(b) # it will be True
b=bool(str3[200:10])
print(b) # it will be False, becuase it will evaluate to an empty string

####################################################################

#Omitting (Leaving empty)- start or end index when using slicing.
# If you will omit start index, it will start at index 0, and if 
# you omit ending index, it will go till end of string.

s="python"

print(s[1:]) #ython
print(s[:4]) #pyth
print(s[:]) #python
print("Tech"[:]) # Tech
