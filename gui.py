import tkinter as tk            # Importing the tkinter library for GUI elements
from tkinter import messagebox  # Importing messagebox for displaying messages

from main import WebAutomation  # Importing the WebAutomation class from main.py

class App:
    def __init__(self, root):
        self.root = root  # Storing the main window object
        self.root.title("WEB AUTOMATION GUI!")  # Setting the title of the window

        # --- Login Frame ---
        self.login_frame = tk.Frame(self.root)  # Creating a frame for login widgets
        self.login_frame.pack(padx=10, pady=10)  # Placing the login frame in the window

        tk.Label(self.login_frame, text="USERNAME: ").grid(row=0, column=0, sticky="w")  # Label for username
        self.entry_username = tk.Entry(self.login_frame)  # Entry widget for username
        self.entry_username.grid(row=0, column=1, sticky="ew")  # Placing the username entry

        tk.Label(self.login_frame, text="PASSWORD: ").grid(row=1, column=0, sticky="w")  # Label for password
        self.entry_password = tk.Entry(self.login_frame, show='*')  # Entry widget for password (hidden)
        self.entry_password.grid(row=1, column=1, sticky="ew")  # Placing the password entry

        # --- Form Frame ---
        self.form_frame = tk.Frame(self.root)  # Creating a frame for form widgets
        self.form_frame.pack(padx=10, pady=10)  # Placing the form frame in the window

        tk.Label(self.form_frame, text="Full Name: ").grid(row=0, column=0, sticky="w")  # Label for full name
        self.entry_fullname = tk.Entry(self.form_frame)  # Entry widget for full name
        self.entry_fullname.grid(row=0, column=1, sticky="ew")  # Placing the full name entry

        tk.Label(self.form_frame, text="Email: ").grid(row=1, column=0, sticky="w")  # Label for email
        self.entry_email = tk.Entry(self.form_frame)  # Entry widget for email
        self.entry_email.grid(row=1, column=1, sticky="ew")  # Placing the email entry

        tk.Label(self.form_frame, text="Current Address: ").grid(row=2, column=0, sticky="w")  # Label for current address
        self.entry_current_address = tk.Entry(self.form_frame)  # Entry widget for current address
        self.entry_current_address.grid(row=2, column=1, sticky="ew")  # Placing the current address entry

        tk.Label(self.form_frame, text="Permanent Address: ").grid(row=3, column=0, sticky="w")  # Label for permanent address
        self.entry_permanent_address = tk.Entry(self.form_frame)  # Entry widget for permanent address
        self.entry_permanent_address.grid(row=3, column=1, sticky="ew")  # Placing the permanent address entry

        # --- Button Frame ---
        self.buttom_frame = tk.Frame(self.root)  # Creating a frame for buttons
        self.buttom_frame.pack(padx=10, pady=10)  # Placing the button frame in the window

        tk.Button(self.buttom_frame, text="SUBMIT!", command=self.submit_data).grid(row=0, column=0, padx=5)  # Submit button
        tk.Button(self.buttom_frame, text="CLOSE BROWSER!", command=self.close_browser).grid(row=0, column=1, padx=5)  # Close 'browser' button


    def submit_data(self):
        username = self.entry_username.get()  # Retrieving username from the entry
        password = self.entry_password.get()  # Retrieving password from the entry
        full_name = self.entry_fullname.get()  # Retrieving full name from the entry
        email = self.entry_email.get()  # Retrieving email from the entry
        current_address = self.entry_current_address.get()  # Retrieving current address from the entry
        permanent_address = self.entry_permanent_address.get()  # Retrieving permanent address from the entry

        self.web_automation = WebAutomation()  # Creating an instance of WebAutomation
        self.web_automation.login(username, password)  # Calling the login method
        self.web_automation.fill_form(full_name, email, current_address, permanent_address)  # Calling the fill_form method

    def close_browser(self):
        self.web_automation.close()  # Closing the browser
        messagebox.showinfo('Browser closed.', 'SUBMITTED SUCCESFULLY!!!!!!')  # Displaying a success message

root = tk.Tk()  # Creating the main window
app = App(root)  # Creating an instance of the App class
root.mainloop()  # Starting the Tkinter event loop