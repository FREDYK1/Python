# user inputs his password
user_input = input("Enter Your Password: ")

result = {}
# check whether the code is 8 characters in length using the len function
if len(user_input) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

# check whether the code has at least one digit using the isdigit method
digit = False
for i in user_input:
    if i.isdigit():
        digit = True
result["digit"] = digit
# check whether the code has at least one uppercase alphabet
upper = False
for i in user_input:
    if i.isupper():
        upper = True
result["upper"]= upper
print(result)
# Tell the user whether the password is strong or not

if all(result.values()):
    print("Your Password Is Strong")
else:
    print("Your Password Is Weak")
