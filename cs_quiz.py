# =============================================================================
# Imports
# =============================================================================

import customtkinter  # Import the "customtkinter" module, which is based on the library "tkinter", which provides new and modern features
import tkinter  # Import the "tkinter" module, which provides the basic tools for creating graphical user interfaces
from tkinter import (
    messagebox,
)  # Import the "messagebox" submodule from "tkinter", which allows displaying various types of message boxes to the user
import os  # Import the "os" module to access operating system-related functions
from PIL import (
    Image,
)  # Import the "Image" class from the "PIL" (Python Imaging Library) module, used for working with images
import pygame  # Imports the "Pygame" module, which is used for creating games
import sqlite3  # Import the "sqlite3" module, which provides a way to interact with SQLite databases using SQL queries
import re  # Import the "re" module, which provides support for regular expressions (pattern matching and manipulation)
import random  # Import the "random" module for random number generation

# =============================================================================
# File paths
# =============================================================================

# Get's the current directory of the Quiz application and store's it in "current_directory"
current_directory = os.path.dirname(os.path.abspath(__file__))

# Defining the names of directories for assets and sound effects
assets_directory = "assets"
sound_effects_directory = "sound_effects"

# The paths for icon and logo files within the "assets" directory
icon_path = os.path.join(current_directory, assets_directory, "icon.ico")
logo_path = os.path.join(current_directory, assets_directory, "logo.png")

# The paths for correct and incorrect sound effect files
correct_sound_path = os.path.join(
    current_directory,
    assets_directory,
    sound_effects_directory,
    "correct_answer_sound.wav",
)
incorrect_sound_path = os.path.join(
    current_directory,
    assets_directory,
    sound_effects_directory,
    "incorrect_answer_sound.wav",
)

# The path for the SQLite database file
database_path = os.path.join(current_directory, "cs_quiz.db")

# =============================================================================
# Sound effects
# =============================================================================

# Initialises the Pygame library
pygame.init()
correct_answer_sound = pygame.mixer.Sound(correct_sound_path)
incorrect_answer_sound = pygame.mixer.Sound(incorrect_sound_path)

# =============================================================================
# Database System
# =============================================================================

# Connect to or create a SQLite database file named "cs_quiz.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# =============================================================================
# Set the Main Menu GUI
# =============================================================================

# Set appearance mode to "system" and default colour theme to "dark-blue" using the customtkinter library
customtkinter.set_appearance_mode(
    "dark"
)  # Appearance Themes: system, light, dark (default)
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Colour Themes: dark-blue (default), blue, green

# Create the main tkinter window
root = customtkinter.CTk()
root.title("Computer Science Quiz")

# Create and pack the quiz title label
title_label = customtkinter.CTkLabel(
    master=root,
    text="Computer Science Quiz",
    font=("Poppins", 26, "bold"),
    text_color="#0047AB",
)
title_label.pack(pady=10)

# Define the width and height of the GUI window
menu_width = 900
menu_height = 550
# Calculate the x-coordinate for centering the window
x_coordinate = (root.winfo_screenwidth() // 2) - (menu_width // 2)
y_coordinate = (root.winfo_screenheight() // 3) - (menu_height // 3)
# Set the size and position of the GUI window using the calculated values
root.geometry("{}x{}+{}+{}".format(menu_width, menu_height, x_coordinate, y_coordinate))

# Disable resizing of the GUI window in both horizontal and vertical directions
root.resizable(False, False)
# Set the icon for the GUI window to "icon.ico"
root.iconbitmap(icon_path)

# =============================================================================
# Switching menus
# =============================================================================

# These functions are responsible for switching between different menus
# Each function hides the elements of the current menu and then shows the specified menu


def main_menu_to_register_menu():
    main_menu_frame.pack_forget()
    main_menu_label.pack_forget()
    main_menu_subheading_label.pack_forget()
    register_menu()


def main_menu_to_login_menu():
    main_menu_frame.pack_forget()
    main_menu_label.pack_forget()
    main_menu_subheading_label.pack_forget()
    login_menu()


def register_menu_to_main_menu():
    register_menu_frame.pack_forget()
    register_menu_label.pack_forget()
    register_menu_subheading_label.pack_forget()
    main_menu()


def login_menu_to_main_menu():
    login_menu_frame.pack_forget()
    login_menu_label.pack_forget()
    login_menu_subheading_label.pack_forget()
    main_menu()


def login_menu_to_forgot_password_menu():
    login_menu_frame.pack_forget()
    login_menu_label.pack_forget()
    login_menu_subheading_label.pack_forget()
    forgot_password_menu()


def forgot_password_menu_to_login_menu():
    forgot_password_menu_frame.pack_forget()
    forgot_password_menu_label.pack_forget()
    forgot_password_menu_subheading_label.pack_forget()
    login_menu()


def login_menu_to_user_menu():
    login_menu_frame.pack_forget()
    login_menu_label.pack_forget()
    login_menu_subheading_label.pack_forget()
    user_menu()


def user_menu_to_main_menu():
    user_menu_frame.pack_forget()
    user_menu_label.pack_forget()
    user_menu_subheading_label.pack_forget()

    # Reset's the quiz's appearance and colour theme back to default settings
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")
    main_menu()


def user_menu_to_quiz_settings_menu():
    if signed_in_role == "Student":
        user_menu_frame.pack_forget()
        user_menu_label.pack_forget()
        user_menu_subheading_label.pack_forget()
        quiz_settings_menu()
    else:
        messagebox.showerror(
            title="Error", message="Must be a student to play the quiz."
        )


def quiz_settings_menu_to_quiz_game_menu():
    quiz_settings_menu_frame.pack_forget()
    quiz_settings_menu_label.pack_forget()
    quiz_settings_menu_subheading_label.pack_forget()
    quiz_settings_topics_frame.pack_forget()
    quiz_settings_topics_label.pack_forget()
    quiz_settings_topics_subheading_label.pack_forget()
    quiz_game_menu()


def quiz_settings_menu_to_user_menu():
    quiz_settings_menu_frame.pack_forget()
    quiz_settings_menu_label.pack_forget()
    quiz_settings_menu_subheading_label.pack_forget()
    quiz_settings_topics_frame.pack_forget()
    quiz_settings_topics_label.pack_forget()
    quiz_settings_topics_subheading_label.pack_forget()
    user_menu()


def quiz_game_menu_to_user_menu():
    quit_quiz_game_result = messagebox.askyesno(
        title="Confirm", message="Do you want to quit the current quiz?"
    )
    if quit_quiz_game_result is True:
        quiz_game_menu_frame.pack_forget()
        quiz_game_question_frame.pack_forget()
        user_menu()


def quiz_game_menu_to_quiz_end_menu():
    quiz_game_menu_frame.pack_forget()
    quiz_game_question_frame.pack_forget()
    quiz_game_end_menu()


def quiz_game_end_menu_to_view_progress_menu():
    quiz_game_end_menu_frame.pack_forget()
    quiz_game_end_menu_label.pack_forget()
    quiz_game_end_menu_subheading_label.pack_forget()
    view_progress_menu()


def quiz_game_end_menu_to_quiz_settings_menu():
    quiz_game_end_menu_frame.pack_forget()
    quiz_game_end_menu_label.pack_forget()
    quiz_game_end_menu_subheading_label.pack_forget()
    quiz_settings_menu()


def quiz_game_end_menu_to_user_menu():
    quiz_game_end_menu_frame.pack_forget()
    quiz_game_end_menu_label.pack_forget()
    quiz_game_end_menu_subheading_label.pack_forget()
    user_menu()


def user_menu_to_leaderboard_menu():
    user_menu_frame.pack_forget()
    user_menu_label.pack_forget()
    user_menu_subheading_label.pack_forget()
    leaderboard_menu()


def leaderboard_menu_to_user_menu():
    leaderboard_menu_frame.pack_forget()
    leaderboard_menu_label.pack_forget()
    leaderboard_menu_subheading_label.pack_forget()
    user_menu()


def user_menu_to_view_progress_menu():
    user_menu_frame.pack_forget()
    user_menu_label.pack_forget()
    user_menu_subheading_label.pack_forget()
    view_progress_menu()


def view_progress_menu_to_user_menu():
    view_progress_menu_frame.pack_forget()
    view_progress_menu_label.pack_forget()
    view_progress_menu_subheading_label.pack_forget()
    user_menu()


def user_menu_to_settings_menu():
    user_menu_frame.pack_forget()
    user_menu_label.pack_forget()
    user_menu_subheading_label.pack_forget()
    settings_menu()


def settings_menu_to_user_menu():
    settings_menu_frame.pack_forget()
    settings_menu_label.pack_forget()
    settings_menu_subheading_label.pack_forget()
    user_menu()


# =============================================================================
# Registration and Login system
# =============================================================================


# Function to manage the registration system
def register():
    # Retrieve input values and clean them up
    first_name = first_name_entry.get().replace(" ", "").lower().capitalize()
    last_name = last_name_entry.get().replace(" ", "").lower().capitalize()
    username = username_entry.get().replace(" ", "")
    password = password_entry.get()
    email = email_entry.get().replace(" ", "").lower()
    role = role_entry_choice.get()

    # Define patterns for input validation
    first_name_validation = r"^[A-Za-z]+$"
    last_name_validation = r"^[A-Za-z]+$"
    username_validation = r"^\S{3,}$"
    password_validation = r"^\S{8,}$"
    email_validation = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if all input values are non-empty and meet validation criteria
    if (
        first_name != ""
        and last_name != ""
        and username != ""
        and password != ""
        and email != ""
        and role != ""
        and role != "Role"
        and re.match(first_name_validation, first_name)
        and re.match(last_name_validation, last_name)
        and re.match(username_validation, username)
        and re.match(password_validation, password)
        and re.match(email_validation, email)
    ):
        # Check if the username and email already exist in the database
        cursor.execute(
            "SELECT username, email FROM Users WHERE username = ? AND email = ?",
            [username, email],
        )
        try:
            cursor.execute(
                "INSERT INTO Users (first_name, last_name, username, password, email, role) VALUES (?, ?, ?, ?, ?, ?)",
                [first_name, last_name, username, password, email, role],
            )
            # Commit the changes to the database
            connection.commit()
            messagebox.showinfo(title="Success", message="Account has been created.")
        except sqlite3.IntegrityError:
            # Rollback changes due to failed insertion
            connection.rollback()
            messagebox.showerror(
                title="Error", message="Username or email already exists."
            )
    else:
        # Show an error message if any input is missing or invalid
        messagebox.showerror(title="Error", message="Enter all data or valid data.")


# Function to manage the login system
def login():
    # Get the entered username and password from the input fields
    username = username_entry.get()
    password = password_entry.get()
    # Check if both username and password fields are non-empty
    if username != "" and password != "":
        # Execute an SQL query to check if the provided username and password match in the database
        cursor.execute(
            "SELECT * FROM Users WHERE username = ? AND password = ?",
            [username, password],
        )
        # Fetch the first result from the executed query
        if cursor.fetchone():
            # If a matching record is found, show a success message and proceed to the user menu
            messagebox.showinfo(title="Success", message="Logged in successfully.")

            cursor.execute("SELECT role FROM Users WHERE username=?", [username])
            result = cursor.fetchone()

            global signed_in_username
            signed_in_username = username

            global signed_in_role
            signed_in_role = result[0]

            login_menu_to_user_menu()
        else:
            # If no matching record is found, show an error message for incorrect credentials
            messagebox.showerror(
                title="Error", message="Incorrect username or password."
            )
    else:
        # If either the username or password field is empty, show an error message
        messagebox.showerror(title="Error", message="Enter all data.")


# Function to manage the forgot password system
def forgot_password():
    # Get the email and new password input from the entry widgets and preprocess them
    email = email_entry.get().lower()
    new_password = new_password_entry.get().replace(" ", "")

    # Define patterns for input validation
    email_validation = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    new_password_validation = r"^\S{8,}$"

    # Check if both email and new password are provided and meet validation criteria
    if (
        email != ""
        and new_password != ""
        and re.match(new_password_validation, new_password)
        and re.match(email_validation, email)
    ):
        # Check if the email exists in the database
        if cursor.execute("SELECT * FROM Users WHERE email = ?", [email]):
            if cursor.fetchone():
                # Update the password for the provided email and commit the changes
                cursor.execute(
                    "UPDATE Users SET password = ? WHERE email = ?",
                    [new_password, email],
                )
                connection.commit()
                messagebox.showinfo(
                    title="Success", message="Password has been changed."
                )
            else:
                # Display an error message if the email is not associated with any account
                messagebox.showerror(
                    title="Error", message="Email is not associated with any account."
                )
    else:
        messagebox.showerror(title="Error", message="Enter all data or valid data.")


# =============================================================================
# Quiz System
# =============================================================================


# Function to manage the quiz settings system
def quiz_settings():
    # Dictionary mapping topic identifiers to the corresponding variables
    quiz_topics = {
        "1.1": choose_quiz_topic_choice_1_1,
        "1.3": choose_quiz_topic_choice_1_3,
        "1.4": choose_quiz_topic_choice_1_4,
        "2.1": choose_quiz_topic_choice_2_1,
        "2.2": choose_quiz_topic_choice_2_2,
        "2.5": choose_quiz_topic_choice_2_5,
    }

    global quiz_chosen_topics
    quiz_chosen_topics = []

    global difficulty_level_chosen
    difficulty_level_chosen = difficulty_level_choice.get()

    # Iterate through topics and add selected ones to the quiz_chosen_topics list
    for topic_choice, topic_number in quiz_topics.items():
        if quiz_topics[topic_choice].get() == "on":
            quiz_chosen_topics.append(topic_choice)

    # Check if both difficulty level and topics are selected to ensure difficulty and topics are selected
    if (
        difficulty_level_choice.get() != "Difficulty Level"
        and len(quiz_chosen_topics) != 0
    ):
        # Execute SQL query to fetch questions based on difficulty and selected topics
        cursor.execute(
            """
        SELECT question, answer, option1, option2, option3, option4
        FROM Questions
        WHERE difficulty = ? AND topic in ({})
        ORDER BY RANDOM() 
    """.format(
                ",".join(["?"] * len(quiz_chosen_topics)),
            ),
            [difficulty_level_chosen] + quiz_chosen_topics,
        )

        global questions
        questions = cursor.fetchall()

        quiz_settings_menu_to_quiz_game_menu()
    else:
        messagebox.showerror(
            title="Error", message="Select a difficulty level or quiz topic."
        )


# Function to manage the colour associated with the selected difficulty level
def difficulty_level_choice_colour():
    if difficulty_level_choice.get() == "Easy":
        return "GREEN"
    elif difficulty_level_choice.get() == "Medium":
        return "ORANGE"
    elif difficulty_level_choice.get() == "Hard":
        return "RED"


# Function to load the first question
def load_first_question():
    global count
    global current_score
    global questions_correct_count
    global questions_incorrect_count

    global answer
    global question
    global option_1
    global option_2
    global option_3
    global option_4

    global check

    # Reset or initialise the variables to their default values
    count = 0
    current_score = 0
    questions_correct_count = 0
    questions_incorrect_count = 0

    question = None
    answer = None
    option_1 = None
    option_2 = None
    option_3 = None
    option_4 = None

    check = None

    # Load details of the first question from the questions list
    item = questions[count]
    question = item[0]
    answer = item[1]
    option_1 = item[2]
    option_2 = item[3]
    option_3 = item[4]
    option_4 = item[5]


# Function to load to the next question
def next_question():
    global count
    global current_score
    global questions_correct_count
    global questions_incorrect_count

    global question
    global answer
    global option_1
    global option_2
    global option_3
    global option_4

    global check

    # Check if the user has already checked the answer of the current question
    if check is True:
        # Move to the next question
        count = count + 1

        # Reset UI elements for the next question
        response_label.configure(text="")
        option_checkbox_1.configure(state="normal")
        option_checkbox_2.configure(state="normal")
        option_checkbox_3.configure(state="normal")
        option_checkbox_4.configure(state="normal")
        check_answer_button.configure(state="normal")

        option_checkbox_1.deselect()
        option_checkbox_2.deselect()
        option_checkbox_3.deselect()
        option_checkbox_4.deselect()

        # Check if there are more questions in the quiz
        if count < len(questions):
            # Load details of the next question
            item = questions[count]

            question = item[0]
            answer = item[1]
            option_1 = item[2]
            option_2 = item[3]
            option_3 = item[4]
            option_4 = item[5]

            # Update UI with the next question details
            question_label.configure(text=question)
            option_checkbox_1.configure(text=option_1)
            option_checkbox_2.configure(text=option_2)
            option_checkbox_3.configure(text=option_3)
            option_checkbox_4.configure(text=option_4)

            # Reset the check variable for the next question
            check = False
        else:
            # Update the user's score in the database and switch to the quiz end menu
            cursor.execute(
                "UPDATE Users SET Score = Score + ? WHERE username = ?",
                [current_score, signed_in_username],
            )
            connection.commit()
            quiz_game_menu_to_quiz_end_menu()
    else:
        messagebox.showerror(title="Error", message="Check your answer.")


# Function to check the answer of the current question
def check_answer():
    global current_score
    global questions_correct_count
    global questions_incorrect_count
    global check

    try:
        # Determine the selected choice based on the checkbox states and ensure multiple checkboxes aren't selected
        if (
            option_checkbox_1.get() == "on"
            and option_checkbox_2.get() == "off"
            and option_checkbox_3.get() == "off"
            and option_checkbox_4.get() == "off"
        ):
            selected_choice = option_1
        elif (
            option_checkbox_2.get() == "on"
            and option_checkbox_1.get() == "off"
            and option_checkbox_3.get() == "off"
            and option_checkbox_4.get() == "off"
        ):
            selected_choice = option_2
        elif (
            option_checkbox_3.get() == "on"
            and option_checkbox_1.get() == "off"
            and option_checkbox_2.get() == "off"
            and option_checkbox_4.get() == "off"
        ):
            selected_choice = option_3
        elif (
            option_checkbox_4.get() == "on"
            and option_checkbox_1.get() == "off"
            and option_checkbox_2.get() == "off"
            and option_checkbox_3.get() == "off"
        ):
            selected_choice = option_4

        # Check if the selected choice is correct
        if selected_choice == answer:
            # Changes the check variable to show that the question has been checked
            check = True

            correct_answer_sound.play()

            # Update score based on difficulty level
            if difficulty_level_chosen == "Easy":
                current_score = current_score + random.randint(1, 25)
            elif difficulty_level_chosen == "Medium":
                current_score = current_score + random.randint(25, 55)
            elif difficulty_level_chosen == "Hard":
                current_score = current_score + random.randint(55, 100)

            # Update UI with the current score and correct response
            current_score_number_label.configure(text=current_score)
            questions_correct_count = questions_correct_count + 1

            response_label.configure(text="Correct!")
            option_checkbox_1.configure(state="disabled")
            option_checkbox_2.configure(state="disabled")
            option_checkbox_3.configure(state="disabled")
            option_checkbox_4.configure(state="disabled")
            check_answer_button.configure(state="disabled")
        else:
            # Changes the check variable to show that the question has been checked
            check = True

            incorrect_answer_sound.play()

            # Update UI with the correct response
            questions_incorrect_count = questions_incorrect_count + 1

            response_label.configure(text=answer)
            option_checkbox_1.configure(state="disabled")
            option_checkbox_2.configure(state="disabled")
            option_checkbox_3.configure(state="disabled")
            option_checkbox_4.configure(state="disabled")
            check_answer_button.configure(state="disabled")

    except UnboundLocalError:
        messagebox.showerror(title="Error", message="Select an option or one option.")


# =============================================================================
# Leaderboard System
# =============================================================================


# Function to manage the leaderboard system
def leaderboard():
    # Execute the SQL query to retrieve the top 10 scores and usernames from the database
    cursor.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
    result = cursor.fetchall()

    global username_1
    global score_1

    global username_2
    global score_2

    global username_3
    global score_3

    global username_4
    global score_4

    global username_5
    global score_5

    global username_6
    global score_6

    global username_7
    global score_7

    global username_8
    global score_8

    global username_9
    global score_9

    global username_10
    global score_10

    # Initialise the variables with empty strings
    username_1, score_1 = "", ""
    username_2, score_2 = "", ""
    username_3, score_3 = "", ""
    username_4, score_4 = "", ""
    username_5, score_5 = "", ""
    username_6, score_6 = "", ""
    username_7, score_7 = "", ""
    username_8, score_8 = "", ""
    username_9, score_9 = "", ""
    username_10, score_10 = "", ""

    # Iterate through the query result and store usernames and scores in the global variables
    for i in range(0, len(result)):
        row = result[i]

        if i == 0:
            username_1 = row[0]
            score_1 = row[1]
        elif i == 1:
            username_2 = row[0]
            score_2 = row[1]
        elif i == 2:
            username_3 = row[0]
            score_3 = row[1]
        elif i == 3:
            username_4 = row[0]
            score_4 = row[1]
        elif i == 4:
            username_5 = row[0]
            score_5 = row[1]
        elif i == 5:
            username_6 = row[0]
            score_6 = row[1]
        elif i == 6:
            username_7 = row[0]
            score_7 = row[1]
        elif i == 7:
            username_8 = row[0]
            score_8 = row[1]
        elif i == 8:
            username_9 = row[0]
            score_9 = row[1]
        elif i == 9:
            username_10 = row[0]
            score_10 = row[1]


# =============================================================================
# View Progress System
# =============================================================================


# Function to manage the view progress system
def view_progress():
    pass


# =============================================================================
# Settings System
# =============================================================================


# Function to manage the appearance theme
def change_appearance_theme(choice):
    if choice == "Dark Mode (Default)":
        customtkinter.set_appearance_mode("dark")
    elif choice == "System Mode":
        customtkinter.set_appearance_mode("system")
    elif choice == "Light Mode":
        customtkinter.set_appearance_mode("light")


# Function to manage the colour theme
def change_colour_theme(choice):
    if choice == "Dark Blue (Default)":
        customtkinter.set_default_color_theme("dark-blue")
    elif choice == "Blue":
        customtkinter.set_default_color_theme("blue")
    elif choice == "Green":
        customtkinter.set_default_color_theme("green")


# Function to manage the sound system
def toggle_sound():
    if toggle_sound_choice.get() == "off":
        pass
    elif toggle_sound_choice.get() == "on":
        pass


# =============================================================================
# Menu Screens
# =============================================================================


# Function to display the Main Menu
def main_menu():
    # Create and pack the Main Menu frame
    global main_menu_frame
    main_menu_frame = customtkinter.CTkFrame(master=root)
    main_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=main_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Main Menu label
    global main_menu_label
    main_menu_label = customtkinter.CTkLabel(
        master=main_menu_frame, text="Main Menu", font=("Poppins", 20, "bold")
    )
    main_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global main_menu_subheading_label
    main_menu_subheading_label = customtkinter.CTkLabel(
        master=main_menu_frame,
        text="Make an account or login!",
        font=("Poppins", 17, "underline"),
    )
    main_menu_subheading_label.pack(padx=10, pady=12)

    # Register button
    register_button = customtkinter.CTkButton(
        master=main_menu_frame,
        text="Register",
        command=main_menu_to_register_menu,
        font=("Poppins", 15),
    )
    register_button.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    # Login button
    login_button = customtkinter.CTkButton(
        master=main_menu_frame,
        text="Login",
        command=main_menu_to_login_menu,
        font=("Poppins", 15),
    )
    login_button.place(relx=0.5, y=220, anchor=customtkinter.CENTER)


# Function to display the Register Menu
def register_menu():
    # Create and pack the Register Menu frame
    global register_menu_frame
    register_menu_frame = customtkinter.CTkFrame(master=root)
    register_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=register_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Display requirements information in a textbox
    requirements_textbox = customtkinter.CTkTextbox(
        master=register_menu_frame,
        font=("Poppins", 13),
        width=200,
        height=108,
        wrap="word",
    )
    requirements_textbox.insert(
        "0.0",
        "Username's must be 3 characters long\nPassword must have 8 characters minimum",
    )
    requirements_textbox.configure(state="disabled")
    requirements_textbox.place(x=560, y=20)

    # Register Menu label
    global register_menu_label
    register_menu_label = customtkinter.CTkLabel(
        master=register_menu_frame, text="Register Menu", font=("Poppins", 20, "bold")
    )
    register_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global register_menu_subheading_label
    register_menu_subheading_label = customtkinter.CTkLabel(
        master=register_menu_frame,
        text="Register Account",
        font=("Poppins", 17, "underline"),
    )
    register_menu_subheading_label.pack(padx=10, pady=12)

    # Entry fields for user details
    global first_name_entry
    first_name_entry = customtkinter.CTkEntry(
        master=register_menu_frame, placeholder_text="First Name", font=("Poppins", 15)
    )
    first_name_entry.place(x=240, y=120)

    global last_name_entry
    last_name_entry = customtkinter.CTkEntry(
        master=register_menu_frame, placeholder_text="Last Name", font=("Poppins", 15)
    )
    last_name_entry.place(x=400, y=120)

    global username_entry
    username_entry = customtkinter.CTkEntry(
        master=register_menu_frame, placeholder_text="Username", font=("Poppins", 15)
    )
    username_entry.place(x=240, y=160)

    global password_entry
    password_entry = customtkinter.CTkEntry(
        master=register_menu_frame, placeholder_text="Password", font=("Poppins", 15)
    )
    password_entry.place(x=400, y=160)

    global email_entry
    email_entry = customtkinter.CTkEntry(
        master=register_menu_frame,
        placeholder_text="Email",
        font=("Poppins", 15),
        width=300,
    )
    email_entry.place(relx=0.5, y=220, anchor=customtkinter.CENTER)

    # Dropdown menu for selecting the role
    global role_entry_choice
    role_entry_choice = customtkinter.StringVar(value="Role")
    role_entry = customtkinter.CTkOptionMenu(
        master=register_menu_frame,
        values=["Student", "Teacher", "Parent"],
        variable=role_entry_choice,
        font=("Poppins", 15),
    )
    role_entry.place(relx=0.5, y=260, anchor=customtkinter.CENTER)

    # Register button
    register_account_button = customtkinter.CTkButton(
        master=register_menu_frame,
        text="Register",
        command=register,
        font=("Poppins", 15),
    )
    register_account_button.place(relx=0.5, y=300, anchor=customtkinter.CENTER)

    # Back to main menu button
    back_to_main_menu_button = customtkinter.CTkButton(
        master=register_menu_frame,
        text="Back to Main Menu",
        command=register_menu_to_main_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_main_menu_button.place(relx=0.5, y=340, anchor=customtkinter.CENTER)


# Function to display the Login Menu
def login_menu():
    # Create and pack the login Menu frame
    global login_menu_frame
    login_menu_frame = customtkinter.CTkFrame(master=root)
    login_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=login_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Login Menu label
    global login_menu_label
    login_menu_label = customtkinter.CTkLabel(
        master=login_menu_frame, text="Login Menu", font=("Poppins", 20, "bold")
    )
    login_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global login_menu_subheading_label
    login_menu_subheading_label = customtkinter.CTkLabel(
        master=login_menu_frame,
        text="Log into an Account",
        font=("Poppins", 17, "underline"),
    )
    login_menu_subheading_label.pack(padx=10, pady=12)

    # Entry fields for username and password
    global username_entry
    username_entry = customtkinter.CTkEntry(
        master=login_menu_frame, placeholder_text="Username", font=("Poppins", 15)
    )
    username_entry.place(relx=0.5, y=140, anchor=customtkinter.CENTER)

    global password_entry
    password_entry = customtkinter.CTkEntry(
        master=login_menu_frame,
        placeholder_text="Password",
        font=("Poppins", 15),
        show="*",
    )
    password_entry.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    # Button to handle forgot password functionality
    forgot_password_button = customtkinter.CTkButton(
        master=login_menu_frame,
        text="Forgot Password?",
        command=login_menu_to_forgot_password_menu,
        font=("Poppins", 15, "underline"),
        fg_color="transparent",
        hover=customtkinter.DISABLED,
    )
    forgot_password_button.place(relx=0.5, y=220, anchor=customtkinter.CENTER)

    # Button to initiate the login process
    login_in_to_account_button = customtkinter.CTkButton(
        master=login_menu_frame, text="Login", command=login, font=("Poppins", 15)
    )
    login_in_to_account_button.place(relx=0.5, y=260, anchor=customtkinter.CENTER)

    # Button to go back to the Main Menu
    back_to_main_menu_button = customtkinter.CTkButton(
        master=login_menu_frame,
        text="Back to Main Menu",
        command=login_menu_to_main_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_main_menu_button.place(relx=0.5, y=300, anchor=customtkinter.CENTER)


# Function to display the Forgot Password Menu
def forgot_password_menu():
    # Create and pack the Forgot Password Menu frame
    global forgot_password_menu_frame
    forgot_password_menu_frame = customtkinter.CTkFrame(master=root)
    forgot_password_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=forgot_password_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Forgot Password Menu label
    global forgot_password_menu_label
    forgot_password_menu_label = customtkinter.CTkLabel(
        master=forgot_password_menu_frame,
        text="Forgot Password Menu",
        font=("Poppins", 20, "bold"),
    )
    forgot_password_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global forgot_password_menu_subheading_label
    forgot_password_menu_subheading_label = customtkinter.CTkLabel(
        master=forgot_password_menu_frame,
        text="Change Your Password",
        font=("Poppins", 17, "underline"),
    )
    forgot_password_menu_subheading_label.pack(padx=10, pady=12)

    # Entry fields for email and new password
    global email_entry
    email_entry = customtkinter.CTkEntry(
        master=forgot_password_menu_frame,
        placeholder_text="Account Email",
        font=("Poppins", 15),
        width=230,
    )
    email_entry.place(relx=0.5, y=140, anchor=customtkinter.CENTER)

    # Button to initiate the password change process
    global new_password_entry
    new_password_entry = customtkinter.CTkEntry(
        master=forgot_password_menu_frame,
        placeholder_text="New Password",
        font=("Poppins", 15),
    )
    new_password_entry.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    # Button to go back to the login menu
    change_password_button = customtkinter.CTkButton(
        master=forgot_password_menu_frame,
        text="Change Password",
        command=forgot_password,
        font=("Poppins", 15),
    )
    change_password_button.place(relx=0.5, y=220, anchor=customtkinter.CENTER)

    back_to_login_menu_button = customtkinter.CTkButton(
        master=forgot_password_menu_frame,
        text="Back to Login Menu",
        command=forgot_password_menu_to_login_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_login_menu_button.place(relx=0.5, y=260, anchor=customtkinter.CENTER)


# Function to display the User Menu
def user_menu():
    # Create and pack the User Menu frame
    global user_menu_frame
    user_menu_frame = customtkinter.CTkFrame(master=root)
    user_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=user_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # User Menu label
    global user_menu_label
    user_menu_label = customtkinter.CTkLabel(
        master=user_menu_frame, text="User Menu", font=("Poppins", 20, "bold")
    )
    user_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global user_menu_subheading_label
    user_menu_subheading_label = customtkinter.CTkLabel(
        master=user_menu_frame,
        text="Explore Your Options",
        font=("Poppins", 17, "underline"),
    )
    user_menu_subheading_label.pack(padx=10, pady=12)

    # Button to play the Quiz Settings Menu
    play_button = customtkinter.CTkButton(
        master=user_menu_frame,
        text="Play",
        command=user_menu_to_quiz_settings_menu,
        font=("Poppins", 15),
    )
    play_button.place(relx=0.5, y=140, anchor=customtkinter.CENTER)

    # Button to go to the Leaderboard Menu
    leaderboard_button = customtkinter.CTkButton(
        master=user_menu_frame,
        text="Leaderboard",
        command=user_menu_to_leaderboard_menu,
        font=("Poppins", 15),
    )
    leaderboard_button.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    # Button to go to the View Progress Menu
    view_progress_button = customtkinter.CTkButton(
        master=user_menu_frame,
        text="View Progress",
        command=user_menu_to_view_progress_menu,
        font=("Poppins", 15),
    )
    view_progress_button.place(relx=0.5, y=220, anchor=customtkinter.CENTER)

    # Button to go to the Settings Menu
    settings_button = customtkinter.CTkButton(
        master=user_menu_frame,
        text="Settings",
        command=user_menu_to_settings_menu,
        font=("Poppins", 15),
    )
    settings_button.place(relx=0.5, y=260, anchor=customtkinter.CENTER)

    # Button to Log out
    log_out_button = customtkinter.CTkButton(
        master=user_menu_frame,
        text="Log Out",
        command=user_menu_to_main_menu,
        font=("Poppins", 15, "bold"),
        text_color="RED",
    )
    log_out_button.place(relx=0.5, y=300, anchor=customtkinter.CENTER)


# Function to display the Quiz Settings Menu
def quiz_settings_menu():
    # Create and pack the Quiz Settings Menu frame
    global quiz_settings_menu_frame
    quiz_settings_menu_frame = customtkinter.CTkFrame(master=root)
    quiz_settings_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Create and pack the Quiz Settings Topics Frame
    global quiz_settings_topics_frame
    quiz_settings_topics_frame = customtkinter.CTkFrame(
        master=quiz_settings_menu_frame, width=260, height=190
    )
    quiz_settings_topics_frame.place(relx=0.5, y=235, anchor=customtkinter.CENTER)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=quiz_settings_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Quiz Settings Menu label
    global quiz_settings_menu_label
    quiz_settings_menu_label = customtkinter.CTkLabel(
        master=quiz_settings_menu_frame,
        text="Quiz Settings Menu",
        font=("Poppins", 20, "bold"),
    )
    quiz_settings_menu_label.pack(padx=10, pady=12)

    # Subheadings label
    global quiz_settings_menu_subheading_label
    quiz_settings_menu_subheading_label = customtkinter.CTkLabel(
        master=quiz_settings_menu_frame,
        text="Change Your Quiz Settings",
        font=("Poppins", 17, "underline"),
    )
    quiz_settings_menu_subheading_label.pack(padx=10, pady=12)

    # Topics label
    global quiz_settings_topics_label
    quiz_settings_topics_label = customtkinter.CTkLabel(
        master=quiz_settings_topics_frame,
        text="Topics",
        font=("Poppins", 15, "underline"),
    )
    quiz_settings_topics_label.place(relx=0.5, y=15, anchor=customtkinter.CENTER)

    # Topics subheading label
    global quiz_settings_topics_subheading_label
    quiz_settings_topics_subheading_label = customtkinter.CTkLabel(
        master=quiz_settings_topics_frame,
        text="Paper 1",
        font=("Poppins", 15, "underline"),
    )
    quiz_settings_topics_subheading_label.place(x=20, y=25)

    quiz_settings_topics_subheading_label = customtkinter.CTkLabel(
        master=quiz_settings_topics_frame,
        text="Paper 2",
        font=("Poppins", 15, "underline"),
    )
    quiz_settings_topics_subheading_label.place(x=185, y=25)

    # Create a difficulty level option menu
    global difficulty_level_choice
    difficulty_level_choice = customtkinter.StringVar(value="Difficulty Level")
    difficulty_level_option_menu = customtkinter.CTkOptionMenu(
        master=quiz_settings_menu_frame,
        values=["Easy", "Medium", "Hard"],
        variable=difficulty_level_choice,
        font=("Poppins", 15),
    )
    difficulty_level_option_menu.place(relx=0.5, y=120, anchor=customtkinter.CENTER)

    # Create topic check boxes
    global choose_quiz_topic_choice_1_1
    choose_quiz_topic_choice_1_1 = customtkinter.StringVar(value="off")

    topic_checkbox_1_1 = customtkinter.CTkCheckBox(
        master=quiz_settings_topics_frame,
        text="1.1",
        variable=choose_quiz_topic_choice_1_1,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 15),
    )
    topic_checkbox_1_1.place(x=20, y=65)

    global choose_quiz_topic_choice_1_3
    choose_quiz_topic_choice_1_3 = customtkinter.StringVar(value="off")

    topic_checkbox_1_3 = customtkinter.CTkCheckBox(
        master=quiz_settings_topics_frame,
        text="1.3",
        variable=choose_quiz_topic_choice_1_3,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 15),
    )
    topic_checkbox_1_3.place(x=20, y=105)

    global choose_quiz_topic_choice_1_4
    choose_quiz_topic_choice_1_4 = customtkinter.StringVar(value="off")

    topic_checkbox_1_4 = customtkinter.CTkCheckBox(
        master=quiz_settings_topics_frame,
        text="1.4",
        variable=choose_quiz_topic_choice_1_4,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 15),
    )
    topic_checkbox_1_4.place(x=20, y=145)

    global choose_quiz_topic_choice_2_1
    choose_quiz_topic_choice_2_1 = customtkinter.StringVar(value="off")

    topic_checkbox_2_1 = customtkinter.CTkCheckBox(
        master=quiz_settings_topics_frame,
        text="2.1",
        variable=choose_quiz_topic_choice_2_1,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 15),
    )
    topic_checkbox_2_1.place(x=185, y=65)

    global choose_quiz_topic_choice_2_2
    choose_quiz_topic_choice_2_2 = customtkinter.StringVar(value="off")

    topic_checkbox_2_2 = customtkinter.CTkCheckBox(
        master=quiz_settings_topics_frame,
        text="2.2",
        variable=choose_quiz_topic_choice_2_2,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 15),
    )
    topic_checkbox_2_2.place(x=185, y=105)

    global choose_quiz_topic_choice_2_5
    choose_quiz_topic_choice_2_5 = customtkinter.StringVar(value="off")

    topic_checkbox_2_5 = customtkinter.CTkCheckBox(
        master=quiz_settings_topics_frame,
        text="2.5",
        variable=choose_quiz_topic_choice_2_5,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 15),
    )
    topic_checkbox_2_5.place(x=185, y=145)

    # Button to start the Quiz
    start_quiz_button = customtkinter.CTkButton(
        master=quiz_settings_menu_frame,
        text="Start Quiz",
        command=quiz_settings,
        font=("Poppins", 15),
    )
    start_quiz_button.place(relx=0.5, y=360, anchor=customtkinter.CENTER)

    # Button to go back to the User Menu
    back_to_user_menu_button = customtkinter.CTkButton(
        master=quiz_settings_menu_frame,
        text="Back to User Menu",
        command=quiz_settings_menu_to_user_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_user_menu_button.place(relx=0.5, y=400, anchor=customtkinter.CENTER)


# Function to display the Quiz Game Menu
def quiz_game_menu():
    # Calls the function to load the first question on the menu
    load_first_question()

    # Create and pack the Quiz Game Menu frame
    global quiz_game_menu_frame
    quiz_game_menu_frame = customtkinter.CTkFrame(master=root)
    quiz_game_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Create and pack the Quiz Game Question Menu frame
    global quiz_game_question_frame
    quiz_game_question_frame = customtkinter.CTkFrame(
        master=quiz_game_menu_frame, width=475, height=280
    )
    quiz_game_question_frame.place(relx=0.5, y=150, anchor=customtkinter.CENTER)

    # Displays the quiz question
    global question_label
    question_label = customtkinter.CTkLabel(
        master=quiz_game_question_frame,
        text=question,
        font=("Poppins", 15, "underline"),
    )
    question_label.place(relx=0.5, y=30, anchor=customtkinter.CENTER)

    # Display option choices checkboxes
    global option_chosen_1
    option_chosen_1 = customtkinter.StringVar(value="off")

    global option_checkbox_1
    option_checkbox_1 = customtkinter.CTkCheckBox(
        master=quiz_game_question_frame,
        text=option_1,
        variable=option_chosen_1,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 13),
        checkbox_width=20,
        checkbox_height=20,
    )
    option_checkbox_1.place(x=35, y=60)

    global option_chosen_2
    option_chosen_2 = customtkinter.StringVar(value="off")

    global option_checkbox_2
    option_checkbox_2 = customtkinter.CTkCheckBox(
        master=quiz_game_question_frame,
        text=option_2,
        variable=option_chosen_2,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 13),
        checkbox_width=20,
        checkbox_height=20,
    )
    option_checkbox_2.place(x=35, y=100)

    global option_chosen_3
    option_chosen_3 = customtkinter.StringVar(value="off")

    global option_checkbox_3
    option_checkbox_3 = customtkinter.CTkCheckBox(
        master=quiz_game_question_frame,
        text=option_3,
        variable=option_chosen_3,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 13),
        checkbox_width=20,
        checkbox_height=20,
    )
    option_checkbox_3.place(x=35, y=140)

    global option_chosen_4
    option_chosen_4 = customtkinter.StringVar(value="off")

    global option_checkbox_4
    option_checkbox_4 = customtkinter.CTkCheckBox(
        master=quiz_game_question_frame,
        text=option_4,
        variable=option_chosen_4,
        onvalue="on",
        offvalue="off",
        font=("Poppins", 13),
        checkbox_width=20,
        checkbox_height=20,
    )
    option_checkbox_4.place(x=35, y=180)

    # Display if the answer is correct, if not display the correct answer
    global response_label
    response_label = customtkinter.CTkLabel(
        master=quiz_game_question_frame,
        text="",
        font=("Poppins", 15),
        text_color="GREEN",
        fg_color="transparent",
    )
    response_label.place(relx=0.5, y=250, anchor=customtkinter.CENTER)

    # Button to go to the next question
    next_question_button = customtkinter.CTkButton(
        master=quiz_game_menu_frame,
        text="Next Question",
        command=next_question,
        font=("Poppins", 15),
    )
    next_question_button.place(x=190, y=335)

    # Button to go to check the answer
    global check_answer_button
    check_answer_button = customtkinter.CTkButton(
        master=quiz_game_menu_frame,
        text="Check Answer",
        command=check_answer,
        font=("Poppins", 15),
    )
    check_answer_button.place(x=450, y=335)

    # Display the difficulty chosen
    difficulty_level_word = difficulty_level_choice.get()
    difficulty_level_word_colour = difficulty_level_choice_colour()

    global difficulty_label
    difficulty_label = customtkinter.CTkLabel(
        master=quiz_game_menu_frame, text="Difficulty:", font=("Poppins", 15)
    )
    difficulty_label.place(x=10, y=20)

    global difficulty_level_choice_label
    difficulty_level_choice_label = customtkinter.CTkLabel(
        master=quiz_game_menu_frame,
        text=difficulty_level_word,
        font=("Poppins", 15),
        text_color=difficulty_level_word_colour,
    )
    difficulty_level_choice_label.place(x=85, y=20)

    # Display the score
    global current_score_label
    current_score_label = customtkinter.CTkLabel(
        master=quiz_game_menu_frame, text="Score:", font=("Poppins", 15)
    )
    current_score_label.place(x=10, y=40)

    global current_score_number_label
    current_score_number_label = customtkinter.CTkLabel(
        master=quiz_game_menu_frame, text=current_score, font=("Poppins", 15)
    )
    current_score_number_label.place(x=60, y=40)

    quit_quiz_button = customtkinter.CTkButton(
        master=quiz_game_menu_frame,
        text="Quit Quiz",
        command=quiz_game_menu_to_user_menu,
        font=("Poppins", 15, "bold"),
        text_color="RED",
    )
    quit_quiz_button.place(x=630, y=380)


# Function to display the Quiz Game End Menu
def quiz_game_end_menu():
    # Create and pack the Quiz Game End Menu frame
    global quiz_game_end_menu_frame
    quiz_game_end_menu_frame = customtkinter.CTkFrame(master=root)
    quiz_game_end_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Quiz Game End Menu label
    global quiz_game_end_menu_label
    quiz_game_end_menu_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame,
        text="Quiz End Menu",
        font=("Poppins", 20, "bold"),
    )
    quiz_game_end_menu_label.pack(padx=10, pady=12)

    # Subheadings label
    global quiz_game_end_menu_subheading_label
    quiz_game_end_menu_subheading_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame,
        text="Quiz Summary",
        font=("Poppins", 17, "underline"),
    )
    quiz_game_end_menu_subheading_label.pack(padx=10, pady=12)

    # Total Questions label
    global total_questions_label
    total_questions_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame, text="Total Questions:", font=("Poppins", 15)
    )
    total_questions_label.place(relx=0.5, y=140, anchor=customtkinter.CENTER)

    total_questions_number = len(questions)

    # Total Questions Number label
    global total_questions_number_label
    total_questions_number_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame,
        text=total_questions_number,
        font=("Poppins", 15),
    )
    total_questions_number_label.place(x=460, y=140, anchor=customtkinter.CENTER)

    # Questions correct label
    global questions_correct_label
    questions_correct_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame, text="Questions Correct:", font=("Poppins", 15)
    )
    questions_correct_label.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    # Questions correct number label
    global questions_correct_number_label
    questions_correct_number_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame,
        text=questions_correct_count,
        font=("Poppins", 15),
    )
    questions_correct_number_label.place(x=470, y=180, anchor=customtkinter.CENTER)

    # Questions incorrect label
    global questions_incorrect_label
    questions_incorrect_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame,
        text="Questions Incorrect:",
        font=("Poppins", 15),
    )
    questions_incorrect_label.place(relx=0.5, y=220, anchor=customtkinter.CENTER)

    # Questions incorrect number label
    global questions_incorrect_number_label
    questions_incorrect_number_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame,
        text=questions_incorrect_count,
        font=("Poppins", 15),
    )
    questions_incorrect_number_label.place(x=475, y=220, anchor=customtkinter.CENTER)

    # Total score label
    global total_score_label
    total_score_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame, text="Total Score:", font=("Poppins", 15)
    )
    total_score_label.place(relx=0.5, y=260, anchor=customtkinter.CENTER)

    # Total score number label
    global total_score_number_label
    total_score_number_label = customtkinter.CTkLabel(
        master=quiz_game_end_menu_frame, text=current_score, font=("Poppins", 15)
    )
    total_score_number_label.place(x=450, y=260, anchor=customtkinter.CENTER)

    # Button to view progress
    view_progress_button = customtkinter.CTkButton(
        master=quiz_game_end_menu_frame,
        text="View Progress",
        command=quiz_game_end_menu_to_view_progress_menu,
        font=("Poppins", 15),
    )
    view_progress_button.place(relx=0.5, y=320, anchor=customtkinter.CENTER)

    # Button to play the Quiz again
    play_again_button = customtkinter.CTkButton(
        master=quiz_game_end_menu_frame,
        text="Play Again",
        command=quiz_game_end_menu_to_quiz_settings_menu,
        font=("Poppins", 15),
    )
    play_again_button.place(relx=0.5, y=360, anchor=customtkinter.CENTER)

    # Button to go back to the User Menu
    back_to_user_menu_button = customtkinter.CTkButton(
        master=quiz_game_end_menu_frame,
        text="Back to User Menu",
        command=quiz_game_end_menu_to_user_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_user_menu_button.place(relx=0.5, y=400, anchor=customtkinter.CENTER)


# Function to display the Leaderboard Menu
def leaderboard_menu():
    # Calls the function to get the usernames and scores to display on the Leaderboard Menu
    leaderboard()

    # Create and pack the leaderboard menu frame
    global leaderboard_menu_frame
    leaderboard_menu_frame = customtkinter.CTkFrame(master=root)
    leaderboard_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Create a textbox to display the leaderboard information
    leaderboard_textbox = customtkinter.CTkTextbox(
        master=leaderboard_menu_frame,
        font=("Poppins", 13),
        width=250,
        height=265,
        wrap="word",
    )

    # Insert leaderboard information into the textbox
    leaderboard_textbox.insert("0.0", "Username - Score\n")
    leaderboard_textbox.insert("2.0", f"1. {username_1} - {score_1}\n")
    leaderboard_textbox.insert("3.0", f"2. {username_2} - {score_2}\n")
    leaderboard_textbox.insert("4.0", f"3. {username_3} - {score_3}\n")
    leaderboard_textbox.insert("5.0", f"4. {username_4} - {score_4}\n")
    leaderboard_textbox.insert("6.0", f"5. {username_5} - {score_5}\n")
    leaderboard_textbox.insert("7.0", f"6. {username_6} - {score_6}\n")
    leaderboard_textbox.insert("8.0", f"7. {username_7} - {score_7}\n")
    leaderboard_textbox.insert("9.0", f"8. {username_8} - {score_8}\n")
    leaderboard_textbox.insert("10.0", f"9. {username_9} - {score_9}\n")
    leaderboard_textbox.insert("11.0", f"10. {username_10} - {score_10}\n")

    # Disable the textbox to make it read-only
    leaderboard_textbox.configure(state="disabled")
    leaderboard_textbox.place(relx=0.5, y=240, anchor=customtkinter.CENTER)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=leaderboard_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Leaderboard Menu label
    global leaderboard_menu_label
    leaderboard_menu_label = customtkinter.CTkLabel(
        master=leaderboard_menu_frame,
        text="Leaderboard Menu",
        font=("Poppins", 20, "bold"),
    )
    leaderboard_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global leaderboard_menu_subheading_label
    leaderboard_menu_subheading_label = customtkinter.CTkLabel(
        master=leaderboard_menu_frame,
        text="See Your Competition",
        font=("Poppins", 17, "underline"),
    )
    leaderboard_menu_subheading_label.pack(padx=10, pady=12)

    # Button to go back to the User Menu
    back_to_user_menu_button = customtkinter.CTkButton(
        master=leaderboard_menu_frame,
        text="Back to User Menu",
        command=leaderboard_menu_to_user_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_user_menu_button.place(relx=0.5, y=400, anchor=customtkinter.CENTER)


# Function to display the View Progress Data Menu
def view_progress_data_and_menu():
    view_progress_data_window = tkinter.Toplevel(root)
    view_progress_data_window.title("View Progress")
    # Define the width and height of the GUI window
    window_width = 500
    window_height = 430
    # Calculate the x-coordinate and y-coordinate for centering the window
    x_coordinate = (view_progress_data_window.winfo_screenwidth() - window_width) // 2
    y_coordinate = (view_progress_data_window.winfo_screenheight() - window_height) // 2
    # Set the size and position of the GUI window using the calculated values
    view_progress_data_window.geometry(
        "{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate)
    )

    # Disable resizing of the GUI window in both horizontal and vertical directions
    view_progress_data_window.resizable(False, False)
    view_progress_data_window.configure(bg="#292929")
    # Set the icon for the GUI window to "icon.ico"
    view_progress_data_window.iconbitmap(icon_path)

    # Create a container frame within the window
    container = tkinter.Frame(view_progress_data_window, bg="#292929")
    container.pack(expand=True)
    container.place(relx=0.5, rely=0.5, anchor="center")


# Function to display the View Progress Menu
def view_progress_menu():
    global view_progress_menu_frame
    view_progress_menu_frame = customtkinter.CTkFrame(master=root)
    view_progress_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=view_progress_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    global view_progress_menu_label
    view_progress_menu_label = customtkinter.CTkLabel(
        master=view_progress_menu_frame,
        text="View Progress Menu",
        font=("Poppins", 20, "bold"),
    )
    view_progress_menu_label.pack(padx=10, pady=12)

    global view_progress_menu_subheading_label
    view_progress_menu_subheading_label = customtkinter.CTkLabel(
        master=view_progress_menu_frame,
        text="Explore Your Performance",
        font=("Poppins", 17, "underline"),
    )
    view_progress_menu_subheading_label.pack(padx=10, pady=12)

    global enter_username_entry
    enter_username_entry = customtkinter.CTkEntry(
        master=view_progress_menu_frame,
        placeholder_text="Enter a Username",
        font=("Poppins", 15),
        width=200,
    )
    enter_username_entry.place(relx=0.5, y=140, anchor=customtkinter.CENTER)

    search_username_button = customtkinter.CTkButton(
        master=view_progress_menu_frame,
        text="Search Username",
        command=view_progress_data_and_menu,
        font=("Poppins", 15),
    )
    search_username_button.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    back_to_user_menu_button = customtkinter.CTkButton(
        master=view_progress_menu_frame,
        text="Back to User Menu",
        command=view_progress_menu_to_user_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_user_menu_button.place(relx=0.5, y=220, anchor=customtkinter.CENTER)


# Function to display the Settings Menu
def settings_menu():
    # Create and pack the Settings Menu frame
    global settings_menu_frame
    settings_menu_frame = customtkinter.CTkFrame(master=root)
    settings_menu_frame.pack(padx=60, pady=30, fill="both", expand=True)

    # Load and display the logo image
    logo_image = customtkinter.CTkImage(
        light_image=Image.open(logo_path),
        dark_image=Image.open(logo_path),
        size=(150, 150),
    )
    logo_image_label = customtkinter.CTkLabel(
        master=settings_menu_frame, image=logo_image, text=""
    )
    logo_image_label.place(x=25, y=20)

    # Settings Menu label
    global settings_menu_label
    settings_menu_label = customtkinter.CTkLabel(
        master=settings_menu_frame, text="Settings Menu", font=("Poppins", 20, "bold")
    )
    settings_menu_label.pack(padx=10, pady=12)

    # Subheading label
    global settings_menu_subheading_label
    settings_menu_subheading_label = customtkinter.CTkLabel(
        master=settings_menu_frame,
        text="Change your settings",
        font=("Poppins", 17, "underline"),
    )
    settings_menu_subheading_label.pack(padx=10, pady=12)

    # Button to change the Quiz Appearance Theme
    appearance_themes_choice = customtkinter.StringVar(value="Themes")
    appearance_themes_option_menu = customtkinter.CTkOptionMenu(
        master=settings_menu_frame,
        values=["System Mode", "Dark Mode (Default)", "Light Mode"],
        command=change_appearance_theme,
        variable=appearance_themes_choice,
        font=("Poppins", 15),
    )
    appearance_themes_option_menu.place(relx=0.5, y=140, anchor=customtkinter.CENTER)

    # Button to change the Colour Appearance Theme
    colour_themes_choice = customtkinter.StringVar(value="Colour")
    colour_themes_option_menu = customtkinter.CTkOptionMenu(
        master=settings_menu_frame,
        values=["Dark Blue (Default)", "Blue", "Green"],
        command=change_colour_theme,
        variable=colour_themes_choice,
        font=("Poppins", 15),
    )
    colour_themes_option_menu.place(relx=0.5, y=180, anchor=customtkinter.CENTER)

    # Switch to toggle sound on or off
    global toggle_sound_choice
    toggle_sound_choice = customtkinter.StringVar(value="on")
    toggle_sound_switch = customtkinter.CTkSwitch(
        master=settings_menu_frame,
        text="Sound",
        command=toggle_sound,
        variable=toggle_sound_choice,
        font=("Poppins", 15),
        onvalue="on",
        offvalue="off",
    )
    toggle_sound_switch.place(relx=0.5, y=220, anchor=customtkinter.CENTER)

    # Button to go back to the User Menu
    back_to_user_menu_button = customtkinter.CTkButton(
        master=settings_menu_frame,
        text="Back to User Menu",
        command=settings_menu_to_user_menu,
        font=("Poppins", 15, "bold"),
    )
    back_to_user_menu_button.place(relx=0.5, y=260, anchor=customtkinter.CENTER)


# =============================================================================
# Starts the quiz
# =============================================================================

# Call the main menu function to start the GUI
main_menu()
# Start the tkinter event loop
root.mainloop()
