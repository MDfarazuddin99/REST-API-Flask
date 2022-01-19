users = {"name":"faraz","accesslevel":"guest"}

def make_secure(func):
    def secure_function():
        if users["accesslevel"] == "admin":
            return func
        else:
            return f"You don't have acess to pwd"
    return secure_function

# get_pwd = make_secure(get_pwd)

@make_secure
def get_pwd():
    return "1234"

print(get_pwd())

a = "alakdj"
b = a
a+="avasv"
print(id(a),id(b))