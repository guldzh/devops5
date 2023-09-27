# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.

avrg_cpu = int(input("Please enter the average cpu usage: "))
launch_new_server = 40<=avrg_cpu<=70
print("Should we launch a new server?",launch_new_server)


