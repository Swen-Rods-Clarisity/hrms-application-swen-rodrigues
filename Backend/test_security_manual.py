from App.Core.security import hash_password, verify_password #Importing The hash_password And verify_password Functions From The Security Module Which Will Be Used To Hash And Verify Passwords.

normal_password = "DemoPassword26" #Defining A Sample Password To Be Hashed And Verified.
hashed_password = hash_password(normal_password) #Hashing The Sample Password Using The hash_password Function.

print(f"Hashed Password: {hashed_password}") #Printing The Hashed Password To The Console.
print(f"Password Verification: {verify_password('DemoPassword26', hashed_password)}") #Verifying The Sample Password Against The Hashed Password Using The verify_password Function And Printing The Result To The Console.
print(f"Password Verification: {verify_password('WrongPassword', hashed_password)}") #Verifying A Wrong Password Against The Hashed Password Using The verify_password Function And Printing The Result To The Console.