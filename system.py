
import re




    


if __name__== "__main__":

    def validate_input(prompt, regex):
        while True:
            value = input(prompt)
            if re.match(regex, value):
                return value
            print("Invalid input. Please try again.")
    lis = dict()
    while True:
        print("Welcome to the system, these are the options: \n 1. Create an user: \n 2. Delete an user:  \n 3. List all users: \n 4. Sort users by name, mail, phone and fodselsnr: \n 5. Stop the program:  ")
        user_input = input("Choose option by entering the corresponding number: ")
        if user_input == "1":
            n = input("How many users do you want to enter?: ")
            lis = {}
            for i in range(int(n)):
                name = validate_input("What is your name?: ", r"^[A-Za-z\s]+$")
                mail = validate_input("What is your mail?: ", r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
                phone = validate_input("What is your phone number?: ", r"^[0-9]{8}$")
                fodselsnr = validate_input("What is your fodselsnr?: ", r"^\d{11}$")
                lis[name] = [mail, phone, fodselsnr]
                """ print(lis) """ # for å sjekke at listen med navn blir printet ut.
        elif user_input == "2":
            name = input("name of the user?: ")
            lis.pop(name)
            print(list)
        elif user_input == "3":
            print("Printing all users: ")
            print(lis)
        elif user_input == "4":
            print("Sort by 1. name, 2. mail, 3. phone or 4. fodselsnr: ")
            sec_input = input("Choose the options by entering the corresponding number: ")
            if sec_input == "1":
                mykeys = list(lis.keys())
                mykeys.sort()
                sortedDict = {i:lis[i] for i in mykeys}
                print(sortedDict)
            elif sec_input == "2":
                sortedDict = {k: v for k, v in sorted(lis.items(), key=lambda item: item[1][0])}
                print(sortedDict)
                print()
            elif sec_input == "3":
                sortedDict = {k: v for k, v in sorted(lis.items(), key=lambda item: item[1][1])}
                print(sortedDict)
                print()
            elif sec_input == "4":
                sortedDict = {k: v for k, v in sorted(lis.items(), key=lambda item: item[1][2])}
                print(sortedDict)
                print()
            else:
                print("The number you selected is not an option! ")
        elif user_input == "5":
            print("Thank you for using the application! ")
            break
            
        else: 
            print("The number you selected is not an option! ")
            





