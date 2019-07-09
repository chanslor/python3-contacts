#!/usr/bin/python3
"""
This is a doc string
"""


def main():
    print("Contacts Manager")
    # Initialize friends list
    friends = []
    infile = open("contacts.txt", "r")
    line = infile.readline()
    while line:
        friends.append(line.rstrip("\n").split(","))
        line = infile.readline()
        infile.close()

        choice = 0
        while choice != 4:
            print("1) Add Friend")
            print("2) Lookup")
            print("3) Display all")
            print("4) Exit")
            choice = eval(input())

            if choice == 1:
                print("Adding to contacts")
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                friends.append([name, email, phone])

            elif choice == 2:
                print("Lookup a contact")
                keyword = input("Enter search term: ")
                for friend in friends:
                    if keyword in friend:
                        print(friend)

            elif choice == 3:
                print("Displaying all contacts:")
                for i in range(len(friends)):
                    print(friends[i])

            elif choice == 4:
                print("Quitting program")
            else:
                print("Invalid response.")

        outfile = open("contacts.txt", "w")
        for friend in friends:
            outfile.write(",".join(friend) + "\n")
        outfile.close()


main()
