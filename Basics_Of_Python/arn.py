arn ="arn:aws:iam::123456789012:user/johndoe"

# split the text
getUsername= arn.split("/") [1]
print(getUsername)

# Convert the text to uppercase
Uppercase=getUsername.upper()
print(Uppercase)

# Find the length of the text
length=len(Uppercase)
print(length)

# Replace a text
replaceName= arn.replace("johndoe", "sri")
print(replaceName)

# Find Substring
substring= "123456789012"
if substring in arn:
    print(substring, "is found in arn")

# concatenate
newName=replaceName.split("/") [1]
concatenate= newName + " " + getUsername
print(concatenate)
