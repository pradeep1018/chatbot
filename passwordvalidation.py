import re

password = input("Enter password: ")

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])[A-Za-z\d!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]{6,20}$"
pattern = re.compile(reg)           
check = re.search(pattern, password)
      
# validating conditions
if check:
    print("Password valid")
else:
    print("Password invalid")