user_str=input("Please provide a string with 'x': ")

first_l=user_str[0]
last_l=user_str[-1]
mid_str=user_str[1:-1].replace("x","")

new_version=first_l+mid_str+last_l
print(new_version)
    