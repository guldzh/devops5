# A DevOps team needs to perform 
# a system update on 212 servers. However, 
# they can only update 8 servers per day due to 
# resource restrictions.
# They want to find out how many full 
# days it will take to complete the updates
# and if there will be servers left over on
# the end of final full day.

servers_to_update, servers_update_perday=212,8
days_of_update=servers_to_update//servers_update_perday
remeinder_servers=servers_to_update%servers_update_perday

print(days_of_update,remeinder_servers )
print(f"{days_of_update} days took to update servers and {remeinder_servers} servers left")
