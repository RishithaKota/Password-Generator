import random
import string

character_set= string.ascii_letters + string.digits + string.punctuation
len= int(input("Enter the length of the password (should be positive): "))

password=''.join(random.choice(character_set) for _ in range(len))

print("The generated password is: ", password)