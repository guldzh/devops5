# remove prefix method will take one string argument and it will remove argument 
# from the string if the string ends with argument

email="yct@techtorialacademy.com"
print(email.removeprefix("techtorial")) # it will print the sam estring sinc ethe string 
                                        # does not start with techtorial it wont remove anything
print(email.removeprefix("yct@t"))  # will output - echtorialacademy.com


# remove sufix method will take one string argument and it will remove argument 
# from the string if the string ends with argument

print(email.removesuffix("yc")) # it will print the sam estring since the string 
                                # does not end with 'yc' it wont remove anything 
print(email.removesuffix(".com")) 