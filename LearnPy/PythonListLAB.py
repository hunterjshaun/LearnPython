# create an empty user list
users = []
# add users kevin, bob, and alice
users.append('kevin')
users.append('bob')
users.append('alice')
print(users)

#remove bob form the users list
del users[1]
print(users)

# reverse the users list and assign the result to 'rev_users'

rev_users = list(reversed(users))
print(rev_users)

# add the user 'melody' to users where 'bob' used to be.
users.insert(1,'melody')
print(users)

# add users 'and, 'wanda, and 'jim' to the users list using a single command
users += ['andy','wanda','jim']
print(users)

# slice the users lists to return the 3rd and 4th items and assign the reult to 'center_users'
center_users = users[2:4]
print(center_users)
