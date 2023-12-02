import sys
import book_dao

menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

search_menu_options = {
    # To be added
}
def search_all_books():
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print("The following are the ISBNs and titles of all books.")
    for item in results:
        print(item['ISBN'], item['title'])
    print("The end of books.")


def search_by_title(Title):
    results = list(book_dao.findByTitle(Title))
    # Display results
    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print("*" * 60)
            print(" " * 60)
            print(f"ISBN: {item['ISBN']}")
            print(f"Title: {item['title']}")
            print(f"published_by: {item['published_by']}")
            print(f"Price: {item['price']}")
            print(f"Year: {item['year']}")
            print("*" * 60)
            print(" " * 60)
    else:
        print("The title you wanted does not exist in our database.")
    print("The end.")


def search_by_ISBN(ISBN_num):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = list(book_dao.findByISBN(ISBN_num))

    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print("*" * 60)
            print(" " * 60)
            print(f"ISBN: {item['ISBN']}")
            print(f"Title: {item['title']}")
            print(f"published_by: {item['published_by']}")
            print(f"Price: {item['price']}")
            print(f"Year: {item['year']}")
            print("*" * 60)
            print(" " * 60)
    else:
        print("The ISBN you wanted does not exist in our database.")
    print("The end.")


def search_by_Publisher(Publisher_name):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = list(book_dao.findByPublisher(Publisher_name))

    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print("*" * 60)
            print(" " * 60)
            print(f"ISBN: {item['ISBN']}")
            print(f"Title: {item['title']}")
            print(f"published_by: {item['published_by']}")
            print(f"Price: {item['price']}")
            print(f"Year: {item['year']}")
            print("*" * 60)
            print(" " * 60)
    else:
        print("The publisher you wanted does not exist in our database.")
    print("The end.")




def search_by_PriceRange(Min, Max):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = list(book_dao.PriceRanger(Min, Max))

    if len(results) != 0:
        print("We found the following matching titles for you.")
        for item in results:
            print("*" * 60)
            print(" " * 60)
            print(f"ISBN: {item['ISBN']}")
            print(f"Title: {item['title']}")
            print(f"published_by: {item['published_by']}")
            print(f"Price: {item['price']}")
            print(f"Year: {item['year']}")
            print("*" * 60)
            print(" " * 60)
    else:
        print("The price range you searched does not exist in our database.")
    print("The end.")


def search_by_Year(year):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = list(book_dao.findByYear(year))

    if len(results) != 0:
        print("We found the following matching year for you.")
        for item in results:
            print("*" * 60)
            print(" " * 60)
            print(f"ISBN: {item['ISBN']}")
            print(f"Title: {item['title']}")
            print(f"published_by: {item['published_by']}")
            print(f"Price: {item['price']}")
            print(f"Year: {item['year']}")
            print("*" * 60)
            print(" " * 60)
    else:
        print(" There is no book published in this year")
    print("The end.")


def search_by_Title_Publisher(title, publisher_name):
    # Use a data access object (DAO) to
    # abstract the retrieval of data from
    # a data resource such as a database.
    results = list(book_dao.findByTitleAndPublisher(title, publisher_name))

    if len(results) != 0:
        print("We found the following matching year for you.")
        for item in results:
            print("*" * 60)
            print(" " * 60)
            print(f"ISBN: {item['ISBN']}")
            print(f"Title: {item['title']}")
            print(f"published_by: {item['published_by']}")
            print(f"Price: {item['price']}")
            print(f"Year: {item['year']}")
            print("*" * 60)
            print(" " * 60)
    else:
        print(" There is no book the publisher and title")
    print("The end.")

# search_by_PriceRange(Min, Max)



def print_menu():
    print()
    print("Please make a selection")
    for key in menu_options.keys():
        print(str(key)+'.', menu_options[key], end="  ")
    print()
    print("The end of top-level options")
    print()


def option1():  
    # Displaying information for adding a publisher
    print()
    print("-----Add Publisher-----")
    print("Type Null for no entry")

    # Taking user input for name
    name = input("Enter Name: ")
    
    if not book_dao.Publisher_chercker(name):

    # Initializing phone variable and ensuring it is a valid 10-digit integer
        phone = " "
        while phone == " ":
            phone = input("Enter phone Number: ")
            if len(phone) != 10:
                phone = ""
                return print("Error: Phone number length must be 10!")
            try:
                int(phone)
            except ValueError:
                phone = ""
                return print("Error: Phone number must consist of integers!")

        # Initializing city variable and ensuring it is not longer than 20 characters
        city = " "
        while city == " ":
            city = input("Enter city: ")
            if len(city) > 20:
                city = ""
                print("Error: City name too long (max 20 characters)!")

        # Calling the addPublisher function with the provided information
        result = book_dao.addPublisher(city, name, phone)

        # Displaying the result of the operation
        print(result)
        
    else: print("pusher already exists")
    
  
  
  
  
  
  
  
  
  
  
  

def option2():

    # Displaying information for adding a book
    print()
    print("-------Add Book-------")
    print("Type NULL for no entry.")

    # Taking user input for ISBN number and ensuring it is a valid 10-digit integer
    ISBN_num = ""
    while ISBN_num == "":
        ISBN_num = input("Enter ISBN Number: ")
        if len(ISBN_num) != 10:
            ISBN_num = ""
            print("Error: ISBN number length must be 10!")
        try:
            int(ISBN_num)
        except ValueError:
            ISBN_num = ""
            print("Error: ISBN number must consist of integers!")
    if not book_dao.ISBN_checker(ISBN_num):
        # Taking user input for book title and ensuring it is not longer than 50 characters
        title = ""
        while title == "":
            title = input("Enter title: ")
            if len(title) > 50:
                title = ""
                print("Error: title name too long (max 50 characters)!")

        # Taking user input for the year and ensuring it is a valid 4-digit integer
        year = ""
        while year == "":
            year = input("Enter year: ")
            if len(year) != 4:
                year = ""
                print("Error: year is invalid")
            try:
                int(year)
            except ValueError:
                year = ""
                print("Error: year must consist of integers!")

        # Taking user input for the publisher and ensuring it is not longer than 25 characters
        published_by = ""
        while published_by == "":
            published_by = input("Enter published_by: ")
            if len(published_by) > 25:
                published_by = ""
                print("Error: published_by name is too long")

        # Taking user input for the previous edition and ensuring it is not longer than 25 characters
        previous_edition = ""
        while previous_edition == "":
            previous_edition = input("Enter ISBN previous_edition: ")
            if len(previous_edition) > 25:
                previous_edition = ""
                print("Error: previous_edition name is too long")

        # Taking user input for the price and ensuring it is a valid float
        price = ""
        while price == "":
            price = input("Enter price: ")
            try:
                float(price)
            except ValueError:
                price = ""
                print("Error: price must consist of integers!")

        # Calling the addBook function with the provided information
        result = book_dao.addBook(ISBN_num, title, year,
                                  published_by, previous_edition, price)

    else:
        print("The book already exits ")
        # Displaying the result of the operation











def option3():
    # Displaying information for editing a book
    print()
    print("-------Edit Book-------")
    print("Type NULL for no entry.")

    # Dictionary to store updated information
    updated = {}

    # Taking user input for the ISBN number and ensuring it is a valid 10-digit integer
    ISBN_num = ""
    while ISBN_num == "":
        ISBN_num = input("Enter ISBN Number of the book you want to Edit: ")
        if len(ISBN_num) != 10:
            ISBN_num = ""
            print("Error: ISBN number length must be 10!")
        try:
            int(ISBN_num)
        except ValueError:
            ISBN_num = ""
            print("Error: ISBN number must consist of integers!")

    # Checking if the ISBN exists in the database
    if book_dao.ISBN_checker(ISBN_num):
        # Asking the user if they want to edit each field
        title = ""
        if input("Do you want to change the title? y or n: ") == 'y':
            while title == "":
                title = input("Enter title: ")
                if len(title) > 50:
                    title = ""
                    print("Error: title name too long (max 50 characters)!")
                updated['title'] = title

        year = ""
        if input("Do you want to change the year? y or n: ") == 'y':
            while year == "":
                year = input("Enter year: ")
                if len(year) != 4:
                    year = ""
                    print("Error: year is invalid")
                try:
                    int(year)
                    updated['year'] = year
                except ValueError:
                    year = ""
                    print("Error: year must consist of integers!")

        published_by = ""
        if input("Do you want to change the published_by? y or n: ") == 'y':
            while published_by == "":
                published_by = input("Enter published_by: ")
                if len(published_by) > 25:
                    published_by = ""
                    print("Error: published_by name is too long")
                updated['published_by'] = published_by

        previous_edition = ""
        if input("Do you want to change the previous_edition? y or n: ") == 'y':
            while previous_edition == "":
                previous_edition = input("Enter previous_edition: ")
                if len(previous_edition) > 25:
                    previous_edition = ""
                    print("Error: previous_edition name is too long")
                updated['previous_edition'] = previous_edition

        price = ""
        if input("Do you want to change the price? y or n: ") == 'y':
            while price == "":
                price = input("Enter price: ")
                try:
                    float(price)
                    updated['price'] = price
                except ValueError:
                    price = ""
                    print("Error: price must consist of integers!")

        # Checking if any fields were edited
        if len(updated) == 0:
            print("You have not edited any field!")
        else:
            # Calling the editBook function with the provided information
            result = book_dao.editBook(ISBN_num, updated)
            print("Editing successful")
    else:
        print("ISBN you entered does not EXIST!")
    return


def option4():
    # Displaying information for deleting a book
    print()
    print("-----Delete a Book")
    print("Type ISBN of the book you want to delete")

    # Taking user input for the ISBN number and ensuring it is a valid 10-digit integer
    ISBN_num = ""
    while ISBN_num == "":
        ISBN_num = input("Enter ISBN Number: ")
        if len(ISBN_num) != 10:
            ISBN_num = ""
            print("Error: You must enter 10 digits")
        try:
            int(ISBN_num)
        except ValueError:
            ISBN_num = ""
            print("Error: ISBN number must consist of only integers!")
    # Calling the deleteBook function with the provided ISBN number
    result = book_dao.deleteBook(ISBN_num)
    if result:
        print(result)
    else:
        print(f"The book with {ISBN_num} doesn't exist in the database")

    # Displaying the result of the operation


# The system shall allow the user to search for books based on various criteria.
def option5():
    # Displaying information for searching books
    print()
    print("----- Search Book ----------")
    print()
    print("""
    Type A to search ALL BOOK
    Type B to search by TITLE
    Type C to search by ISBN
    Type D to search by PUBLISHER
    Type E to search by PRICE RANGE
    Type F to search by YEAR
    Type G to search by TITLE AND PUBLISHER""")

    # Taking user input for the choice of search criteria
    choice = input("Type your choice LETTER: ")

    # Performing the search based on the user's choice
    if choice == "A":
        # Calling the function to search for all books
        search_all_books()
    elif choice == "B":
        # Taking user input for the title and calling the function to search by title
        Title = input("Type a valid Title of a book: ")
        search_by_title(Title)

    elif choice == "C":
        # Taking user input for the ISBN and calling the function to search by ISBN
        ISBN_num = input("Type a valid ISBN: ")
        search_by_ISBN(ISBN_num)

    elif choice == "D":
        # Taking user input for the publisher name and calling the function to search by publisher
        Publisher_name = input("Type the name of the publisher: ")
        search_by_Publisher(Publisher_name)

    elif choice == "E":
        # Taking user input for the price range and calling the function to search by price range
        Min = input("Type Min price: ")
        Min = float(Min)
        Max = input("Type Max price: ")
        Max = float(Max)
        search_by_PriceRange(Min, Max)

    elif choice == "F":
        # Taking user input for the year and calling the function to search by year
        year = input("Type the year: ")
        year = int(year)
        search_by_Year(year)

    elif choice == "G":
        # Taking user input for title and publisher and calling the function to search by title and publisher
        print("Choose by Title and Publisher: ")
        title = input("Type Title name: ")
        publisher_name = input("Type publisher name: ")
        search_by_Title_Publisher(title, publisher_name)

    else:
        # Handling invalid input
        print("Please type a valid Letter")


if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thanks your for using our database services! Bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')