import re
txt = “Ryan has sent an invoice email to john.d@yahoo.com by using his email id ryan.arjun@gmail.com and he also shared a copy to his boss rosy.gray@amazon.co.uk on the cc part.”

# \w matches any non-whitespace character

# @ for as in the Email

# + for Repeats a character one or more times

findEmail = re.findall(r’[\w\.-]+@[\w\.-]+’, txt)

# Printing findEmail of List

print(findEmail)