import secrets
import string

stop=True
avChars=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation

while stop:
    length = input("Choose a length (default 20): ")
    # Checks length of input or uses default length
    if not length:
        length=20
    else:
        try:
            length = int(length)
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue
    
    if length <= 0:
        print("Invalid input. Please enter a positive integer.")
        continue
    
    password = ''.join([secrets.choice(avChars) for i in range(length)])

    print(password)
    if input("Save password to clipboard? (Press Enter to continue or 'Ctrl+C' to exit): ") != "":
        stop=False
