s ="programming"

print(s[2:10:2]) ##ormi
print(s[2:10:3]) ##oai
print(s[1:10:3]) ##rrm

# Negative Steps
# Slicing function will always works
# left to right Unless there is negative steps involved

print(s[1:10:-3]) # it works right to left

print(s[7:0:-3]) # mrr

t="techtorial"
print(t[::1]) # techtorial
print(t[::2]) # tctra
print(t[::-1]) # will return the reversed version of the string.

# Negative indexes in python
pl="python"
print(pl[-1:-3]) # empty string, this is not the step, this is an index.
print(pl[-1:]) #n 
print(pl[:-3]) #n 


