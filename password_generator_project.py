import random
import string
def generate_password(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    try:
        length=int(input("Enter password length:"))
        if length<4:
            print("Password too short! using minimun length of 4")
            length=4
        password=generate_password(length)
        print("\nGenerated Password:",password)
        print("\nNote:Save this Password in a secure place!")
    except ValueError:
        print("Please enter a valid number!")
if __name__=="__main__":
    main()
