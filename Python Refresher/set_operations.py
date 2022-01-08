#intersection union and difference

local_friends = {'jayendra', 'roshan','goutham'}

abroad_friends = {'sidharth', 'pranay'}

close_friends = {'jayendra', 'sidharth'}

all_friends = local_friends.union(abroad_friends)

print(all_friends)

just_friends = all_friends.difference(close_friends)

print(just_friends)

close_local_friends = local_friends.intersection(close_friends)

print(close_local_friends)