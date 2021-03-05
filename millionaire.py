from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pickle
import os

master = Tk()
master.title("MILLIONAIRE")
master.geometry("550x550")
master.resizable(False, False)
accounts = dict()
question = dict()
scores = dict()
entered_account = str()
count_sym = count_num = 0
selection = IntVar()

if os.path.exists("database.txt") and os.stat("database.txt").st_size != 0:
    file = open("database.txt", "rb")
    accounts = pickle.load(file)
    file.close()

if os.path.exists("questions.txt") and os.stat("questions.txt").st_size != 0:
    file = open("questions.txt", "rb")
    question = pickle.load(file)
    file.close()

if os.path.exists("scores.txt") and os.stat("scores.txt").st_size != 0:
    file = open("scores.txt", "rb")
    scores = pickle.load(file)
    file.close()

design = ImageTk.PhotoImage(Image.open("img/mill.png"))
background_image = Label(master, image=design)
background_image.place(relheight=1, relwidth=1)

first_frame = Frame(master, bg="#F8EDB8")
first_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

image1 = PhotoImage(file=r"C:\Users\User\PycharmProjects\python123\img\login-button-png-18030 (1).gif")
sign_in_image = image1.subsample(3, 3)

sign_in_button = Button(master, image=sign_in_image, compound=LEFT, borderwidth=0, command=lambda: login(),
                        bg="#F8EDB8")
sign_in_button.place(relx=0.32, rely=0.38, relwidth=0.35, relheight=0.13)

image2 = PhotoImage(file=r"C:\Users\User\PycharmProjects\python123\img\register-button-png-18477.gif")
sign_up_image = image2.subsample(3, 3)

sign_up_button = Button(master, image=sign_up_image, compound=LEFT, borderwidth=0, command=lambda: register(),
                        bg="#F8EDB8")
sign_up_button.place(relx=0.32, rely=0.55, relwidth=0.35, relheight=0.13)

logo = PhotoImage(file=r"C:\Users\User\PycharmProjects\python123\img\second.png")
game_image = logo.subsample(11, 11)


def register():
    register_frame = Frame(master, bg="#1BB818")
    register_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    register_form = Label(register_frame, text="REGISTRATION FORM", bg="#1BB818", font="Merriweather 15")
    register_form.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.1)

    username_label = Label(register_frame, text="Enter username:", bg="#1BB818", font="Merriweather 12")
    username_label.place(relx=0, rely=0.2, relwidth=0.3, relheight=0.1)

    username_entry1 = Entry(register_frame, bd=5)
    username_entry1.place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.1)

    password_label = Label(register_frame, text="Enter password:", bg="#1BB818", font="Merriweather 12")
    password_label.place(relx=0, rely=0.4, relwidth=0.3, relheight=0.1)

    password_entry = Entry(register_frame, bd=5, show="*")
    password_entry.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.1)

    password_label_again = Label(register_frame, text="Confirm password:", bg="#1BB818", font="Merriweather 12")
    password_label_again.place(relx=0, rely=0.6, relwidth=0.3, relheight=0.1)

    password_entry_again = Entry(register_frame, bd=5, show="*")
    password_entry_again.place(relx=0.3, rely=0.6, relwidth=0.5, relheight=0.1)

    back_to_login_btn = Button(register_frame, text="Back to login", bg="#EDBF0C", fg="black",
                               command=lambda: back_to_login())
    back_to_login_btn.place(relx=0.05, rely=0.1, relwidth=0.3)

    def back_to_login():
        login()

    def saved():
        global count_sym, count_num
        check_password = str(password_entry.get())
        for item in check_password:
            if item.isnumeric():
                count_num += 1
            if not item.isalnum() and not item.isspace():
                count_sym += 1
        if username_entry1.get() == "" or password_entry.get() == "" or password_entry_again.get() == "":
            messagebox.showwarning("Try again", "All fields are required, please enter your information correctly")
        elif username_entry1.get() in accounts.keys():
            messagebox.showerror("Try again", "This username already exists, please enter another one")
        elif count_num < 1 or count_sym < 1:
            messagebox.showerror("Try again", "Passwords must be consisted of at least one number and one symbol")
        elif len(username_entry1.get()) < 6:
            messagebox.showerror("Try again", "You have to enter at least 6 characters to \"Username\" field")
        elif password_entry.get() != password_entry_again.get():
            messagebox.showerror("Try again", "Passwords do not match")
        elif len(password_entry.get()) < 8 or len(password_entry_again.get()) < 8:
            messagebox.showerror("Try again", "You have to enter at least 8 characters to \"Password\" field")
        else:
            accounts[username_entry1.get()] = password_entry.get()
            loaded_file = open("database.txt", "wb")
            pickle.dump(accounts, loaded_file)

            login()

    sign_up = Button(register_frame, text="Sign up", bg="#EDBF0C", fg="black", command=saved)
    sign_up.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.1)


def login():
    login_frame = Frame(master, bg="#1BB818")
    login_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    greeting_label = Label(login_frame, text="LOGIN FORM", bg="#1BB818", font="Merriweather 15")
    greeting_label.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.1)

    username_label = Label(login_frame, text="Username:", bg="#1BB818", font="Merriweather 12")
    username_label.place(relx=0, rely=0.2, relwidth=0.3, relheight=0.1)

    username_entry = Entry(login_frame, bd=5)
    username_entry.place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.1)

    password_label = Label(login_frame, text="Password:", bg="#1BB818", font="Merriweather 12")
    password_label.place(relx=0, rely=0.4, relwidth=0.3, relheight=0.1)

    password_entry = Entry(login_frame, bd=5, show="*")
    password_entry.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.1)

    check = Checkbutton(login_frame, text="Show password", bg="#1BB818", variable=selection, onvalue=1, offvalue=0,
                        command=lambda: show_password())
    check.place(relx=0.4, rely=0.5, relwidth=0.3, relheight=0.1)

    def show_password():
        if selection.get() == 1:
            password_entry["show"] = ""
        else:
            password_entry["show"] = "*"

    def call_database():
        global entered_account
        if username_entry.get() == "" or password_entry.get() == "":
            messagebox.showwarning("Try again", "All fields are required, please enter your information correctly")
        elif username_entry.get() in accounts.keys() and password_entry.get() == accounts.get(username_entry.get()):
            messagebox.showinfo("Welcome", f"Nice to see you {username_entry.get()}")
            entered_account = username_entry.get()
            main_menu()
        else:
            messagebox.showerror("Try again", "Enter your account details correctly")

    sign_in = Button(login_frame, text="Sign IN", bg="#EDBF0C", fg="black",
                     command=lambda: [call_database()])
    sign_in.place(relx=0.3, rely=0.6, relwidth=0.5, relheight=0.1)

    return username_entry.get()


def main_menu():
    menu_frame = Frame(master, bg="#000030")
    menu_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

    logo_of_game = Label(menu_frame, image=game_image, bg="#000030")
    logo_of_game.place(relx=0.22, rely=0.05, relwidth=0.57, relheight=0.45)

    play_game = Button(menu_frame, text="PlAY GAME", bg="#1B3269", fg="white", command=lambda: start())
    play_game.place(relx=0.32, rely=0.53, relwidth=0.37, relheight=0.08)

    score_table = Button(menu_frame, text="High scores", bg="#1B3269", fg="white", command=lambda: scores())
    score_table.place(relx=0.32, rely=0.68, relwidth=0.37, relheight=0.08)

    exit_game = Button(menu_frame, text="EXIT", bg="#1B3269", fg="white", command=lambda: close_game())
    exit_game.place(relx=0.32, rely=0.83, relwidth=0.37, relheight=0.08)

    def start():
        game_frame = Frame(master, bg="#104889")
        game_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

        name_of_game = Label(game_frame, text="GOOD LUCK", font="Merriweather 15", bg="#1B3269", fg="white")
        name_of_game.place(relx=0.35, rely=0.05)

        bank = Label(game_frame, text="Your bank($$$)", bg="#1B3269", fg="white")
        bank.place(relx=0.16, rely=0.2)

        user_bank = Label(game_frame, text="0", font="Merriweather 13", bg="#1B3269", fg="white")
        user_bank.place(relx=0.1, rely=0.31, relwidth=0.3, relheight=0.09)

        question_value = Label(game_frame, text="Value of question($$$)", bg="#1B3269", fg="white")
        question_value.place(relx=0.63, rely=0.2)

        show_question_value = Label(game_frame, text="100", font="Merriweather 13", bg="#1B3269", fg="white")
        show_question_value.place(relx=0.60, rely=0.31, relwidth=0.3, relheight=0.09)

        main_question = Label(game_frame, bg="#1B3269", fg="white")
        main_question.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.08)

        btn1 = Button(game_frame, command=lambda: win(btn1), bg="#1B3269", fg="white")
        btn1.place(relx=0.08, rely=0.6, relwidth=0.28, relheight=0.08)

        btn2 = Button(game_frame, command=lambda: win(btn2), bg="#1B3269", fg="white")
        btn2.place(relx=0.6, rely=0.6, relwidth=0.31, relheight=0.08)

        btn3 = Button(game_frame, command=lambda: win(btn3), bg="#1B3269", fg="white")
        btn3.place(relx=0.08, rely=0.8, relwidth=0.28, relheight=0.08)

        btn4 = Button(game_frame, command=lambda: win(btn4), bg="#1B3269", fg="white")
        btn4.place(relx=0.6, rely=0.8, relwidth=0.31, relheight=0.08)

        list_of_questions = open("questions.txt", "wb")
        pickle.dump(question, list_of_questions)

        def win(btn):
            global entered_account
            global scores
            if question[main_question["text"]] == btn["text"]:
                pass
            else:
                end_of_game = Frame(master, bg="#A01801")
                end_of_game.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

                you_lost = Label(end_of_game, text="YOU LOST", font="bold")
                you_lost.place(relx=0.25, rely=0.04, relwidth=0.5)

                your_money = Label(end_of_game, text="Amount of money", font="arial 15")
                your_money.place(relx=0.2, rely=0.3, relwidth=0.57, relheight=0.1)

                money_label = Label(end_of_game, text=user_bank["text"], font="arial 15")
                money_label.place(relx=0.2, rely=0.42, relwidth=0.57, relheight=0.1)

                try_again = Button(end_of_game, text="TRY AGAIN", command=lambda: try_again())
                try_again.place(relx=0.29, rely=0.6, relwidth=0.4, relheight=0.1)

                exit_button = Button(end_of_game, text="EXIT", command=lambda: exit_win())
                exit_button.place(relx=0.29, rely=0.75, relwidth=0.4, relheight=0.1)

                scores[entered_account] = money_label["text"]
                loaded_file2 = open("scores.txt", "wb")
                pickle.dump(scores, loaded_file2)

                def exit_win():
                    response = messagebox.askyesno("EXIT", "Are you sure?")
                    if response:
                        exit()

                def try_again():
                    main_menu()

        main_question["text"] = "What sort of animal is Walt Disney's Dumbo?"
        btn1["text"] = "Deer"
        btn2["text"] = "Rabbit"
        btn3["text"] = "Donkey"
        btn4["text"] = "Elephant"
        btn4["command"] = lambda: [win(btn4), question2()]

        def question2():
            main_question["text"] = "What was the name of the Spanish waiter in the TV sitcom \"Fawlty Towers\"?"
            btn1["text"] = "Pedro"
            btn2["text"] = "Alfonso"
            btn3["text"] = "Manuel"
            btn4["text"] = "Javier"
            btn3["command"] = lambda: [win(btn3), question3()]
            user_bank["text"] = "100"
            show_question_value["text"] = "300"

        def question3():
            main_question["text"] = "Which battles took place between the Royal Houses of York and Lancaster?"
            btn1["text"] = "War of the Roses"
            btn2["text"] = "Hundred Years War"
            btn3["text"] = "Thirty Years War"
            btn4["text"] = "English Civil War"
            btn1["command"] = lambda: [win(btn1), question4()]
            user_bank["text"] = "400"
            show_question_value["text"] = "500"

        def question4():
            main_question["text"] = "Which former Beatle narrated the TV adventures of Thomas the Tank Engine?"
            btn1["text"] = "John Lennon"
            btn2["text"] = "Ringo Starr"
            btn3["text"] = "Paul McCartney"
            btn4["text"] = "George Harrison"
            btn2["command"] = lambda: [win(btn2), question5()]
            user_bank["text"] = "900"
            show_question_value["text"] = "1000"

        def question5():
            main_question["text"] = "Queen Anne was the daughter of which English Monarch?"
            btn1["text"] = "Henry VIII"
            btn2["text"] = "Victoria"
            btn3["text"] = "William I"
            btn4["text"] = "James II"
            btn4["command"] = lambda: [win(btn4), question6()]
            user_bank["text"] = "1900"
            show_question_value["text"] = "4000"

        def question6():
            main_question["text"] = "Who composed \"Rhapsody in Blue\"?"
            btn1["text"] = "Irving Berlin"
            btn2["text"] = "George Gershwin"
            btn3["text"] = "Aaron Copland"
            btn4["text"] = "Cole Porter"
            btn2["command"] = lambda: [win(btn2), question7()]
            user_bank["text"] = "5900"
            show_question_value["text"] = "16000"

        def question7():
            main_question["text"] = "What is the Celsius equivalent of 77 degrees Fahrenheit?"
            btn1["text"] = "25"
            btn2["text"] = "15"
            btn3["text"] = "20"
            btn4["text"] = "30"
            btn1["command"] = lambda: [win(btn1), question8()]
            user_bank["text"] = "21900"
            show_question_value["text"] = "32000"

        def question8():
            main_question["text"] = "Suffolk Punch and Hackney are types of what?"
            btn1["text"] = "Carriage"
            btn2["text"] = "Horse"
            btn3["text"] = "Cocktail"
            btn4["text"] = "Wrestling style"
            btn2["command"] = lambda: [win(btn2), question9()]
            user_bank["text"] = "53900"
            show_question_value["text"] = "64000"

        def question9():
            main_question["text"] = "Which Shakespeare play features the line Neither a borrower, nor a lender be?"
            btn1["text"] = "Hamlet"
            btn2["text"] = "Othello"
            btn3["text"] = "The Merchant of Venice"
            btn4["text"] = "Macbeth"
            btn1["command"] = lambda: [win(btn1), question10()]
            user_bank["text"] = "117900"
            show_question_value["text"] = "125000"

        def question10():
            main_question["text"] = "Which is the largest city in the USA's largest state?"
            btn1["text"] = "Dallas"
            btn2["text"] = "Los Angeles"
            btn3["text"] = "New York"
            btn4["text"] = "Anchorage"
            btn4["command"] = lambda: [win(btn4), question11()]
            user_bank["text"] = "242900"
            show_question_value["text"] = "250000"

        def question11():
            main_question["text"] = "The word \"aristocracy\" literally means power in the hands of whom?"
            btn1["text"] = "The few"
            btn2["text"] = "The best"
            btn3["text"] = "The barons"
            btn4["text"] = "The rich"
            btn2["command"] = lambda: [win(btn2), question12()]
            user_bank["text"] = "492900"
            show_question_value["text"] = "500000"

        def question12():
            main_question["text"] = "Where would a \"peruke\" be worn?"
            btn1["text"] = "On the head"
            btn2["text"] = "Around the neck"
            btn3["text"] = "Around the waist"
            btn4["text"] = "On the wrist"
            btn1["command"] = lambda: [win(btn1), winner()]
            user_bank["text"] = "992900"
            show_question_value["text"] = "1000000"
            user_bank["text"] = "1992900"

        def winner():
            global scores
            winner_frame = Frame(game_frame, bg="#11D657")
            winner_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

            you_won = Label(winner_frame, text="YOU WON", font="bold")
            you_won.place(relx=0.25, rely=0.04, relwidth=0.5)

            your_money = Label(winner_frame, text="Amount of money", font="arial 15")
            your_money.place(relx=0.2, rely=0.3, relwidth=0.57, relheight=0.1)

            money_label = Label(winner_frame, text=user_bank["text"], font="arial 15")
            money_label.place(relx=0.2, rely=0.42, relwidth=0.57, relheight=0.1)

            main_menu_btn = Button(winner_frame, text="MAIN MENU", command=lambda: main_menu_func())
            main_menu_btn.place(relx=0.29, rely=0.6, relwidth=0.4, relheight=0.1)

            exit_button = Button(winner_frame, text="EXIT", command=lambda: quit_game())
            exit_button.place(relx=0.29, rely=0.75, relwidth=0.4, relheight=0.1)

            scores[entered_account] = money_label["text"]
            loaded_file3 = open("scores.txt", "wb")
            pickle.dump(scores, loaded_file3)

            def quit_game():
                response = messagebox.askyesno("EXIT", "Are you sure?")
                if response:
                    exit()

            def main_menu_func():
                main_menu()

    def scores():
        global scores
        score_frame = Frame(master, bg="#104889")
        score_frame.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

        header_label = Label(score_frame, text="Score table", font="Merriweather 15", bg="#1B3269", fg="white")
        header_label.place(relx=0.25, rely=0.02, relwidth=0.5, relheight=0.1)

        score_label = Label(score_frame, font="Merriweather 15", bg="#1B3269", fg="white")
        score_label.place(relx=0.3, rely=0.2, relwidth=0.25)

        show_score = Button(score_frame, text="Show score", bg="#1B3269", fg="white", command=lambda: show_scores())
        show_score.place(relx=0.02, rely=0.2, relwidth=0.25)

        scrollbar = Scrollbar(score_frame)
        scrollbar.place(rely=0.29, relx=0.9, relheight=0.6)

        usernames_list = Listbox(score_frame, font="Merriweather 12")
        usernames_list.place(relx=0.1, rely=0.29, relwidth=0.8, relheight=0.6)
        usernames_list.config(yscrollcommand=scrollbar)
        scrollbar.config(command=usernames_list.yview)

        back_to_login_btn = Button(score_frame, text="Back", bg="#1B3269", fg="white",
                                   command=lambda: back_to_menu())
        back_to_login_btn.place(relx=0.05, rely=0.03, relwidth=0.12)

        def back_to_menu():
            main_menu()

        def show_accounts():
            for element in accounts:
                usernames_list.insert(END, element)
            return usernames_list

        show_accounts()

        def show_scores():
            global accounts
            selected = usernames_list.curselection()
            index_of_item = selected[0]
            loaded_scores = open("scores.txt", "rb")
            scores_dict = dict(pickle.load(loaded_scores))
            lst = list(scores_dict)
            key = lst[index_of_item]
            score_label["text"] = scores_dict[key]

    def close_game():
        response = messagebox.askyesno("Warning", "Are you sure?")
        if response:
            exit()


master.mainloop()
