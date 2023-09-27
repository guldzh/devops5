# John wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# John needs to walk 10000 steps daily  OR needs to run at least
# 4 miles a day.  and Addition to these , John needs eat less 
# than 1500 calories daily. We should create a program to calculate 
# if John can loose weight or not 


steps_to_walk=int(input("Please enter how many steps to walk: "))
running_distance=int(input("Please enter the running distance: "))
is_active=steps_to_walk>=10000 or running_distance>=4

calorie_intake=int(input("Please enter the calorie intake: "))
is_intake=calorie_intake<1500

can_loose_weight=is_active and is_intake
print("Can John loose weight? ",can_loose_weight)