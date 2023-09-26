# Python Comparsion operators

### 1. Equal to **==**
- Checks if the value on the left is equal to valye on the right.

**Example**
```py
print (11=11)```

**Output:
### Note! Comparison operator always result in a boolean value.
- Zfor the code above simce 11 is the samee as 11 the output of the code will be "True"

### 2. Not equal to **!=**
- Checks if the left side is **not equal to** right side 
```py 
print(6!='6') # Since the text cannot be equal to numbers thisline will print True
print(6!=6) # Since this numbers are same this will print False
```

### 3. Greater sign **>**
- checks if teh ;eft side of equation is bigger than the right side
```py
print(5.0 > 5) #False
print(3  > 4)   # False
print(10 > 9)  # True
```

### 4. Less than sign **<**
- checks if teh left side of equation is smaller than the right side
```py
print(5.0 < 5) #False
print(3 < 4)  #True
print(10 < 9)  #False
```

### 5. Less than equal <= || Greater Equal sign >=
- checks if the left side of is smaller  OR equal <=
- checks if the left side of is bigger  OR equal >=

```py
print(5.0 <= 5) #True
print(5.0 >= 5) #True
print(3 <= 4)  #True
print(10 >= 9)  #True
```

## Note!
- **Type Matters**
- When comparing values type of the values also important:
For ex: `5 == "5"` is `False` becasue one is string and the other is a one type

- **We can chain the comparison operators in python**
```py
print(1<2<3)```
