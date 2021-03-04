# Author: Pacifique & Serge
# Library Management System

from os import write
from book import Book
from audiobook import Audiobook
from film import Film

""" This How our main program looks like with the different methods
"""

items_all = {'book': {}, 'audiobook': {}, 'film': {}}
""" In this part we are trying to open file using the open file method
"""
f = open('user_actions.txt', 'w')
""" User input , we ask the user name
"""
name = input('What is your name? \n')
""" Using the write function we have the User name
"""
f.write(name)

print("""Welcome
This program enables you to:
add an item(audiobook, book or film) to the system
sell an item
lend an item
Check all available items""")

print()
while True:
    try:
        choose_type_add = int(input("""
    Choose item to add:
    1. book
    2. audiobook
    3. film \n"""))    # added int() - convert input to integer
    except ValueError:  # changed error to ValueError - expected error
        print("oops invalid input!. Please Enter an integer")
        continue   # use continue to start over the loop, ask for the input again
        
    if choose_type_add == 1:
        log = 'Choose to add book'
        f.write(log + '\n')

        title = input('Enter book title: ').lower()
        log = 'Entered book title' + title
        f.write(log + '\n')

        genre = input('Enter the genre of the book: ')
        log = 'Entered genre ' + genre
        f.write(log + '\n')

        try:
            price = int(input('Enter the selling price: '))
            log = 'Entered price ' + str(price)
            f.write(log + '\n')
        except ValueError:
            print('Sorry, enter an integer')

        author = input('Enter the author name: ')
        log = 'Entered author ' + author
        f.write(log + '\n')

        year = input('Enter the year published: ')
        log = 'Entered author ' + year
        f.write(log + '\n')

        try:
            no_item = int(input('Enter the number of copies of the book: '))
            log = 'Entered no of items ' + str(no_item)
            f.write(log + '\n')
        except ValueError:
            print('Sorry, enter an integer')

        items_all['book'][title] = Book(title, genre, price, author, year, no_item)
        log = 'Added a book '
        f.write(log + '\n')

        print('Book added!')
        print()

    elif choose_type_add == 2:
        log = 'Choose to add audiobook'
        f.write(log + '\n')

        title = input('Enter audiobook title: ').lower()
        log = 'Entered audiobook title ' + title
        f.write(log + '\n')

        genre = input('Enter the genre of the audiobook: ')
        log = 'Entered genre ' + genre
        f.write(log + '\n')

        try:
            price = int(input('Enter the selling price: '))
            log = 'Entered price ' + str(price)
            f.write(log + '\n')
        except ValueError:
            print('Sorry, enter an integer')

        author = input('Enter the author name: ')
        log = 'Entered author ' + author
        f.write(log + '\n')

        year = input('Enter the year published: ')
        log = 'Entered year ' + year
        f.write(log + '\n')

        format_f = input('Enter the format of the audiobook: ')
        log = 'Entered format ' + format_f
        f.write(log + '\n')

        try:
            no_item = int(input('Enter the number of copies of the book: '))
            log = 'Entered no of items ' + str(no_item)
            f.write(log + '\n')
        except ValueError:
            print('Sorry, enter an integer')

        items_all['audiobook'][title] = Audiobook(title, genre, price, author, year, format_f, no_item)
        log = 'Added an audiobook ' + str(choose_type_add)
        f.write(log + '\n')

        print('Audiobook added!')
        print()

    elif choose_type_add == 3:
        log = 'Choose to add film'
        f.write(log + '\n')

        title = input('Enter film title: ').lower()
        log = 'Entered a film title ' + title
        f.write(log + '\n')

        genre = input('Enter the genre of the film: ')
        log = 'Entered the genre ' + genre
        f.write(log + '\n')

        try:
            price = int(input('Enter the selling price: '))
            log = 'Entered the price ' + str(price)
            f.write(log + '\n')
        except ValueError:
            print('Sorry, enter an integer')

        year = input('Enter the year published: ')
        log = 'Entered year ' + year
        f.write(log + '\n')

        type = input('Enter the type of film: ')
        log = 'Entered type ' + type
        f.write(log + '\n')

        studios = input('Enter the studios name: ')
        log = 'Entered the studios ' + studios
        f.write(log + '\n')

        try:
            no_item = int(input('Enter the number of copies of the book: '))
            log = 'Entered the no if items' + str(no_item)
            f.write(log + '\n')
        except ValueError:
            print('Sorry, enter an integer')

        items_all['film'][title] = Film(title, genre, price, year, type, studios, no_item)
        log = 'Added a film' + str(choose_type_add)
        f.write(log + '\n')

        print('Film added!')
        print()

    else:
        print('Invalid Input! Please try again!!! ')
        print(" Always! You must enter valid integer between 1, 2 and 3")
        print()
       
    try:
        other_add = int(input("""add another item?
    1. yes
    2. no\n"""))
    except ValueError:
        print('Sorry, enter an integer')
        continue

    if other_add == 1:
        continue
    elif other_add == 2:
        break
    else:
        print('Invalid input. Pleasetry again!')
        continue
    


while True:
    try:
        user_action = int(input("""
    Choose action below:
    1. sell
    2. lend
    3. view all items\n"""))
    except ValueError:
        print('Sorry, enter an integer')
        continue

    if user_action == 1:
        log = 'Choose to sell'
        f.write(log + '\n')

        title_sell = input('Enter the title of item to sell: ').lower()
        log = 'provided title to sell ' + title_sell
        f.write(log + '\n')
        
        for typ, all in items_all.items():
            for t, item in all.items():
                if title_sell == t:
                    print('Item selected: ' + typ + ' : ' + t)
                    item.sell()
                    log = 'Sold Item ' + t
                    f.write(log + '\n')
                    print()
        

    elif user_action == 2:
        log = 'Choose to lend'
        f.write(log + '\n')
        title_lend = input('Enter the title of item to sell: ').lower()
        log = 'Choose to add ' + title_lend
        f.write(log + '\n')

        for typ, all in items_all.items():
            for t, item in all.items():
                if title_lend == t:
                    print('Item selected: ' + typ + ' : ' + t)
                    item.lend()
                    log = 'Lend an item ' + t
                    f.write(log + '\n')
                    print()

    elif user_action == 3:
        log = 'Choose to view'
        f.write(log + '\n')
        print('The collection is:')
        
        for typ, all in items_all.items():
            for t, item in all.items():
                print(typ + ' : ' + t)


    else:
        print('Invalid Input, Please Try again!')

        
    try:
        other_act = int(input("""Perform another action?
    1. Yes
    2. No\n"""))
    except ValueError:
        print('Sorry, enter an integer')
        continue

    if other_act == 1:
        continue
    elif other_act == 2:
        break
    else:
        print('Invalid input, make sure you always enter valid input between 1 and 2')
        continue
""" After running the Whole program and creating the new file we need to close the file using the close file function
"""
f.close()


