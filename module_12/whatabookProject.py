# Keril Ivanchuk
# 02/16/2023

from operator import truediv
import mysql.connector
from mysql.connector import errorcode
# imports

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
# MySQL user login

db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("USE whatabook;")

# Connection stuff, and selection of whatabook database

def view_books (title):
    cursor.execute ("SELECT * FROM books")
    bookslist = cursor.fetchall()
    print ("\n  -- {} --".format(title))
    for books in bookslist:
        print ("  Book ID: {}\n  Book Name: {}\n  Details: {}\n  Author: {}\n".format( 
            books[0], books[1], books[2], books[3]))

# view_books function via user input menu

def view_stores (title):
    cursor.execute ("SELECT * FROM whatabook")
    locations = cursor.fetchall()
    print ("\n  -- {} --".format(title))
    for whatabook in locations:
        print ("  Store ID: {}\n  Locale: {}\n".format(
            whatabook[0], whatabook[1]))

# view_stores function via user input menu

def view_account (title):
    print ("Please provide your User_ID Type: ") # Prompt for user_id from user
    user_id_input = input() # Actual input command to pull user_id
    cursor.execute ("SELECT * FROM user WHERE user_id = %s", (user_id_input,)) # SQL command for pulling user information from database
    users = cursor.fetchall()
    print ("\n  -- {} --".format(title))
    for user in users:
        print ("  User ID: {}\n  First Name: {}\n  Last Name: {}\n".format( # Print command to show the selected users information
            user[0], user[1], user[2]))
    answer=True
    while answer:
        print ("\n WISHLIST MENU \n 1. View Wishlist \n 2. Add a book? \n 3. Remove a book? \n 4. Main Menu \n") # Printed WISHLIST MENU
        user_input = input("What would you like to do? Type: ") # Prompting the user for next steps via WISHLIST MENU
        if user_input=="1":
            print ("\n Viewing wishlist! \n") 
            cursor.execute ("SELECT * FROM wishlist WHERE user_id = %s", (user_id_input,)) # Pulling user input to confirm their ID for the following prompts
            user_wishlist = cursor.fetchall()
            print ("\n  -- {} --".format(title))
            for wishlist in user_wishlist:
                print ("  Wishlist ID: {}\n  User ID: {}\n  Book ID: {}\n".format( # SQL command for viewing the wishlist
                    wishlist[0], wishlist[1], wishlist[2]))
        elif user_input=="2":
            print ("\n Adding a book! \n")
            view_books("Here are all the book options")
            user_book_pick = input("What book ID do you want to add? Type: ") # Getting the users input for book selection
            cursor.execute ("INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)", (user_id_input, user_book_pick,)) # SQL command that will be adding the book to the database
            db.commit()
            print ("Book Successfully removed! \n") # Success print after adding a book to your wishlist
        elif user_input=="4":
            print ("\n Going to main menu! \n") # Prompt for going to the MAIN MENU
            user_input = None
            return
        elif user_input=="3":
            print ("\n Removing a book! \n") 
            print ("\n Viewing wishlist! \n")  
            cursor.execute ("SELECT * FROM wishlist WHERE user_id = %s", (user_id_input,)) # SQL command that will pull wishlist information to later print
            user_wishlist = cursor.fetchall()
            print ("\n  -- Your Wishlist --")
            for wishlist in user_wishlist:
                print ("  Wishlist ID: {}\n  User ID: {}\n  Book ID: {}\n".format( # Showing the wishlist again
                    wishlist[0], wishlist[1], wishlist[2]))
            user_remove_pick = input("What book ID do you want to remove? Type: ") # Input for book removal choice
            cursor.execute ("DELETE FROM wishlist WHERE user_id = %s AND book_id = %s", (user_id_input, user_remove_pick,)) # SQL command for removing the book
            db.commit()
            print ("Book Successfully removed! \n") # Success print after removing a book from your wishlist

        else:
            print ("\n Not a valid option, please try again! \n") # Error print for wrong selections

# view_stores function via user input menu

answer=True
while answer:
    print ("\n MAIN MENU \n 1. View Books \n 2. View Store Locations \n 3. My Account \n 4. Exit/Quit \n") # MAIN MENU print 
    user_input = input("What would you like to do? Type: ") # MAIN MENU selection input command, used to traverse the options on MAIN MENU
    if user_input=="1":
      print ("\n Viewing all books! \n") 
      view_books(title="All Books") # Calling view_books function
    elif user_input=="2":
      print ("\n Viewing store locations! \n")
      view_stores(title="All Stores") # Calling view_stores function
    elif user_input=="3":
      view_account(title="Your Account") # Calling view_account function
    elif user_input=="4": 
      print ("\n Goodbye! \n") 
      user_input = None
      exit () # Exiting via users '4' selection
    else:
      print ("\n Not a valid option, please try again! \n") # Error print for wrong selections
