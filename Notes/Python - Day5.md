# Logical operator in Python:
## and Operator
- this operator check if all conditipns are true. For ex:
```py
#Lest write a program to see if the person can drive. In order to drive the person has to be 16 years old and they must have a valid license
age=15
has_license=True
can drive =has_license and age>15
```

## or Operator
- this operator checks if at least one condition is True.
```py
#A worker can get the rest if it is weekend or when it is holiday
is_holiday=True
is_weekend=False
can_rest=is_holiday or is_weekend
```

## not operator
- Reverses the result of the boolean variable. For ex:
```py
b1=True
b2=not b1
```

print(True and not False) #True
print(not True and True) #False
print(True and True and True and False) #False
print(True or False) #True
print(not False or False) #True
print(False or False) #False
print(False and False) #False

# Using both `and` and `or` operator at the same time.
# In python `and` operator will be executed before the or operator. 
print( False or True and False) #  False
#Note: not operator will be executed before the `and` and `or` operators.

# Immutablity
- All numerical data types in python are immutable which means their value will not be modified in any case other than reassignment.

# escape Characters in String
- If you wnat to add unallowed chaarachters to the string (text) ypu can use backlash \ to insert those unallowed chanarchters.
# in python we cant use " if the text is defined in "" (double quotes)

print("\"") #prints " only
print('\'') #prints ' only
print('"')#prints " only
print("'")#prints ' only

# Note!
- Any boolean variable 


