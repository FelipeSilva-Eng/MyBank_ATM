import random
import string

cust_profile = open("cust_profile.txt", "a+")
# a+ -> abrir o arquivo e fazer append(escrever no final do arquivo)

cnt = 1
temp = ()
address = ()


def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return "".join(random.choice(chars) for x in range(size))


print("Hello! welcome to MyBank.")
print("This is Admin account.")

while True:

    print(
        """
        Hello! Welcome to MyBank.
        Enter [0] to proceed, [1] to finish.
        What would you like to do today?\n
        1. Create a customer profile
        2. View a customer transaction
        3. Search customer profile
    """
    )
    choice = int(input("Enter your choice: "))

    if choice == 1:
        firstname = input("Enter First Name: ")
        lastname = input("Enter last Name: ")
        address = input("Enter Address: ")
        username = lastname[0:2] + firstname
        username_integer = username + str(cnt)

        with open("cust_profile.txt", "r") as f:
            data = f.read()
            if username not in data:
                temp = username
                temp2 = randompassword()
                cust_profile.write(
                    "Username:"
                    + username
                    + "\t"
                    + "Password:"
                    + temp2
                    + "\t"
                    + "First Name:"
                    + firstname
                    + "\t"
                    + "Last Name:"
                    + lastname
                    + "\t"
                    + "Address:"
                    + address
                    + "\n"
                )
                print(
                    f"\nCreated username is: {temp} and password is: {temp2}\n"
                )

            else:
                cnt += 1
                temp = username_integer
                temp2 = randompassword()
                cust_profile.write(
                    "Username:"
                    + username
                    + "\t"
                    + "Password:"
                    + temp2
                    + "\t"
                    + "First Name:"
                    + firstname
                    + "\t"
                    + "Last Name:"
                    + lastname
                    + "\t"
                    + "Address:"
                    + address
                    + "\n"
                )
                print(
                    f"\nCreated username is: {temp} and password is: {temp2}\n"
                )

    elif choice == 2:
        username = input("Enter a username that you would like to view: ")
        transaction_filename = username + "_transactionhistory.txt"
        transaction_file = open(transaction_filename, "a")
        with open(transaction_filename, "r") as f:
            f.seek(0)
            if f.read(1):
                print(f.read())
                break
            else:
                print("There is no transaction history for this customer")
                break

    elif choice == 3:
        data = input("Please enter customer detail to search: ")
        file = open("cust_profile.txt")
        for line in file:
            line = line.rstrip()
            if data in line:
                print(line)
        break

cust_profile.close()
