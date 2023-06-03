import database as db
import tkinter as tk


class User:

    def __init__(self):
        self.lib_db = db.lib_db
        self.lib_cursor = self.lib_db.cursor()

    def signup(self, username, password):
        self.lib_cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        self.lib_db.commit()
        print("User created successfully!")

    def login(self, username, password):
        self.lib_cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = self.lib_cursor.fetchone()

        if user:
            print("Login successful!")
        else:
            print("Invalid username or password!")


def user_info_GUI():

    user = User()
    window = tk.Tk()

    #Tkinter Entry for Username
    username_label = tk.Label(window, text="Username: ")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    #Tkinter Entry for Password
    password_label = tk.Label(window, text="Password: ")
    password_label.pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    #function to handle button click
    def signup_button_click():
        username = username_entry.get()
        password = password_entry.get()
        user.signup(username, password)



    # function to handle button click
    def login_button_click():
        username = username_entry.get()
        password = password_entry.get()
        user.login(username, password)

    signup_button = tk.Button(window, text="Sign Up", command=signup_button_click)
    signup_button.pack()

    login_button = tk.Button(window, text="Log-in", command=login_button_click)
    login_button.pack()

    window.mainloop()




class Library(User):

    def __init__(self):
        super().__init__()
        self.lib_cursor = self.lib_db.cursor()

    def add_book(self, book=[], author=[], quantity=[]):
        book_name = input("Book name: ")
        book_author = input("Book author: ")
        book_quantity = int(input("Book quantity: "))
        self.lib_cursor.execute("INSERT INTO books (book_name, book_author, book_quantity) VALUES (%s, %s, %s)", (book_name, book_author, book_quantity))
        self.lib_db.commit()
        book.append(book_name)
        author.append(book_author)
        quantity.append(book_quantity)
        print("Book added successfully!")

    def view_books(self):
        self.lib_cursor.execute("SELECT * FROM books")
        books = self.lib_cursor.fetchall()
        print("Book Name\t\tBook Author\t\tBook Quantity")
        for book in books:
            print(book[0] + "\t\t" + book[1] + "\t\t" + str(book[2]))
            print("Book Name: " + book[0])
            print("Book Author: " + book[1])
            print("Book Quantity: " + str(book[2]))

    def delete_book(self):
        book_name = input("Book name: ")
        self.lib_cursor.execute("DELETE FROM books WHERE book_name = %s", (book_name,))
        self.lib_db.commit()
        print("Book deleted successfully!")

    def search_book(self):
        book_name = input("Book name: ")
        self.lib_cursor.execute("SELECT * FROM books WHERE book_name = %s", (book_name, ))
        book = self.lib_cursor.fetchone()
        print("Book Name: " + book[0])
        print("Book Author: " + book[1])
        print("Book Quantity: " + str(book[2]))

    def borrow_book(self):
        book_name = input("Book name: ")
        self.lib_cursor.execute("SELECT * FROM books WHERE book_name = %s", (book_name, ))
        book = self.lib_cursor.fetchone()
        print("Book Name: " + book[0])
        print("Book Author: " + book[1])
        print("Book Quantity: " + str(book[2]))
        if book[2] > 0:
            book[2] -= 1
            print("Book borrowed successfully! Please return it if you're done, thank you!")
        else:
            print("Book not available!")

    def return_book(self):
        book_name = input("Book name: ")
        self.lib_cursor.execute("SELECT * FROM books WHERE book_name = %s", (book_name))
        book = self.lib_cursor.fetchone()
        print("Book Name: " + book[0])
        print("Book Author: " + book[1])
        print("Book Quantity: " +str(book[2]))
        book[2] += 1
        print("Book returned successfully, happy reading!")




#main function
def main():
    user = User()
    main_library = Library()

    choices = 0

    print("Sign-up first before you proceed.")
    print("Do you like to sign-up? [YES or NO]")
    sign_up = input("1 => YES\n2 => NO")

    if sign_up == 1:
        user.signup()
    else:
        print("Thank you!")

    print("Would you like to Log-in? [YES or NO]")
    log_in = input("1 => YES\n2 => NO")

    if log_in == 1:
        user.login()
        if user.login() == True:
            pass

    else:
        print("Sign-up first before you log-in!")


#user info function
user_info_GUI()





