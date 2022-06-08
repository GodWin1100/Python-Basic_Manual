print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nTRY AND EXCEPT\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# try and except is same as if and else the difference is that try will be executed if code is right and executable and if not except will be executed
print("\n")
try:
    if name > 3:
        print("Cheated python")
except:
    print("Something went wrong")
print("\n")

try:
    name = 2
    if name < 3:
        print("Correct code")
except:
    print("Something went wrong")
