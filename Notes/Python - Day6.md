# Python is a case sensitive language 
# true and True is not same  .....
#
# How spaces effect the python code? 
a =                   5 
print(  a   )

#1. spaces in the same line( not in the beginning)
#2. spaces that takes code to the next line (this will effect the output of thecode)
#3. spaces that is in the beginning of the line(indents)
# indentations are expected when a code belongs to certain group of 
# implementations.

# Python relies on indentation, defined by the whitespace at
# the beginning of a line, to establish the scope of code blocks.

# If statement in Python 
- Purpuse of If statement is executing scertain parts of the code depending on the given boolean condiations. 
- When a boolen `condition` is True for the if statement the **next** block of the code will be execcuted

### How do we know where next block of code starts and ends?
- In python same block of codes has same indentation. So that by looking at the indentatiosn we couuld understand beggining and the end of the block codes.
***Note*** a block of code refers to the lines of codes that belongs to same implementations. This implementations could be `if statemnt`, methods, class etc.

### How if statemn works?
```py
if boolean conditions:
    # code belwongs to if
    # code belwongs to if
#code that is not effected by if statemnet, this line will always be executed  regradless of the if statemnt's condition. 

```
***Note** As seen on the above only if boolean condition is Ture if block will be executed

