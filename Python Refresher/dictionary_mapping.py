user_db = [
    (0,'faraz','FEVCADC2432'),
    (1,'jake','StrongCop123'),
    (2,'Amy','4mes|$4Ewesome'),
]

user_mapping = {user[1]: user for user in user_db}

print(user_mapping)