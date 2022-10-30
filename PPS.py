from tkinter import *
from tkinter.messagebox import *
from tkinter import font
import random
import mysql.connector as msq
# Exception Classes


class LastNameError(Exception):
    pass


class FirstNameError(Exception):
    pass


class UserError(Exception):
    pass


class AgeError(Exception):
    pass


class PasswordError(Exception):
    pass


class AgainPasswordError(Exception):
    pass


class MatchPasswordError(Exception):
    pass


class ClickedTwoTimesError(Exception):
    pass


class PartyButtonNotSelected(Exception):
    pass


class ClearNoFrame(Exception):
    pass


# Main Function runs the program
def main_connection():
    conn = msq.connect(host="localhost", user="root", password='', database='pps')
    cursor = conn.cursor()
    # cursor.execute("CREATE DATABASE pps")
    # cursor.execute("SHOW DATABASES")
    # cursor.execute("""CREATE TABLE `pps`.`account information` ( `id` INT(10) NOT NULL AUTO_INCREMENT ,
    # `User Name` VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL ,
    # `Password` VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL ,
    # PRIMARY KEY (`id`)) ENGINE = InnoDB;""")
    # cursor.execute("show tables")
    # for i in cursor:
    # print(i)
    if conn:
        # Carry out normal procedure
        print("Connection successful")
    else:
        # Terminate
        print("Connection unsuccessful")
    conn.close()


def main_function():
    global screen_1
    screen_1 = Tk()
    a = Window1(screen_1, "Pierre Papier Ciseau", 500, 400, 420, 130, "#FFE4AA")
    a.create()
    screen_1.mainloop()
# Classes Planning and forming


class MainWindow:
    def __init__(self, master, val_title, val_width, val_height, width_pos, height_pos):
        master.geometry(str(val_width) + "x" + str(val_height) + "+" + str(width_pos) + "+" + str(height_pos))
        master.title(val_title)
        master.minsize(val_width, val_height)
        master.maxsize(val_width, val_height)
        master.iconbitmap(r'C:/Users/amine/PycharmProjects/Application_PPS/img/original.ico')
        self.master = master


class Window1(MainWindow):

    def __init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color):
        MainWindow.__init__(self, master, val_title, val_width, val_height, width_pos, height_pos)
        self.frame_main = Frame(master, bg=val_color, width=val_width, height=val_height)
        self.frame_main.pack()
        self.val_color = val_color

    def sign_in(self):
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()

    def connect(self):
        global entry_f3_1, entry_f3_2, name, password
        name = "."
        password = "."
        conn = msq.connect(host="localhost", user="root", password='', database='pps')
        cursor = conn.cursor()
        cursor.execute("SELECT `User Name`, `Password` FROM `account information` WHERE `User Name` LIKE '{0}'".format(entry_f3_1.get()))
        rows = cursor.fetchall()
        for row in rows:
            print("""
                    nom : {0}
                    mot de pass : {1}
                    """.format(row[0], row[1]))
            if str(row[0]) == entry_f3_1.get():
                name = str(row[0])
                password = str(row[1])

        print(name, password)
        conn.close()
        try:
            if entry_f3_1.get() != name:
                raise UserError("Nom d\'utilisateur non trouvable !")
            else:
                if entry_f3_2.get() != password:
                    raise PasswordError("Mot de pass incorrect ! ")
                else:
                    screen_1.destroy()
                    global screen_3
                    screen_3 = Tk()
                    c = Window3(screen_3, "Pierre Papier Ciseau", 700, 550, 300, 90, "#FFE4AA", False, 0, "", False, 0, 0, 0, 0, 0, 0)
                    c.create()
                    screen_3.mainloop()
        except UserError as error:
            showerror("Erreur", error)
        except PasswordError as error:
            showerror("Erreur", error)

    def create(self):
        # main frame = Frame A (TOP)
        # First line frame
        frame_1 = Frame(self.frame_main, bg="gray")
        frame_1.pack(side=TOP)

        # First Frame in first line frame (LEFT)
        frame_1_01 = Frame(frame_1, bg="gray")
        frame_1_01.pack(side=LEFT)
        # First Label in Frame
        label_f1_1 = Label(frame_1_01, text="Pierre Papier Ciseau", bg="gray", font=("calibri", 18), width=30, anchor=W,
                           padx=15, fg="white", height=2)
        label_f1_1.pack()

        # Second Frame in first line frame
        frame_1_02 = Frame(frame_1, bg="gray")
        frame_1_02.pack()
        # The problem is that the Tkinter/Tk interface doesn’t handle references to Image objects properly;
        # the Tk widget will hold a reference to the internal object, but Tkinter does not.
        # When Python’s garbage collector discards the Tkinter object, Tkinter tells Tk to release the image.
        # But since the image is in use by a widget, Tk doesn’t destroy it. Not completely.
        # It just blanks the image, making it completely transparent…
        #
        # The solution is to make sure to keep a reference to the Tkinter object,
        # for example by attaching it to a widget attribute:
        # photo = PhotoImage(...)
        # label = Label(image=photo)
        # label.image = photo # keep a reference!
        # label.pack()
        image_1 = PhotoImage(file="C:/Users/amine/PycharmProjects/Application_PPS/img/edited.png")
        # Second Label containing an image
        label_f1_2 = Label(master=frame_1_02, image=image_1, bg="gray", anchor=NW)
        label_f1_2.image = image_1
        label_f1_2.pack(padx=24, pady=(5, 0))

        # A frame containing a label under the first line frame
        frame_2 = Frame(self.frame_main, bg=self.val_color)
        frame_2.pack()
        label_2 = Label(frame_2, text="Connectez Vous !", bg="#FFE4AA", fg="black", font=("calibri", 14))
        label_2.pack(pady=30)

        # A frame containing 2 labels and 2 entries
        frame_3 = Frame(self.frame_main, bg=self.val_color)
        frame_3.pack()
        # 2 Labels and 2 entries
        label_f3_1 = Label(frame_3, text="Nom d'utilisateur : ", bg="#FFE4AA", fg="black", font=("calibri", 15),
                           anchor=NW)
        label_f3_1.grid(column=0, row=0, padx=(60, 20), pady=(5, 5))
        global entry_f3_1, entry_f3_2
        entry_f3_1 = Entry(frame_3, width=20, bg="white", fg="black", font=("calibri", 12))
        entry_f3_1.grid(column=1, row=0, padx=(20, 69), pady=(5, 5))
        label_f3_2 = Label(frame_3, text="Mot de passe : ", bg="#FFE4AA", fg="black", font=("calibri", 15), anchor=NW)
        label_f3_2.grid(column=0, row=1, padx=(50, 15), pady=(5, 15))
        entry_f3_2 = Entry(frame_3, show="*", width=20, bg="white", fg="black", font=("calibri", 12))
        entry_f3_2.grid(column=1, row=1, padx=(20, 69), pady=(5, 15))

        # A frame containing 2 buttons and a right label
        frame_4 = Frame(self.frame_main, bg=self.val_color)
        frame_4.pack()
        # 2 buttons
        button_f4_1 = Button(frame_4, width=12, text="Se connecter", bg="gray", fg="white", font=("calibri", 12),
                             cursor="hand2", relief=GROOVE, command=self.connect)
        button_f4_1.grid(column=0, row=0, padx=(20, 0), pady=(25, 0))
        button_f4_2 = Button(frame_4, width=12, text="Inscrire", bg="gray", fg="white", font=("calibri", 12),
                             cursor="hand2", relief=GROOVE, command=self.sign_in)
        button_f4_2.grid(column=1, row=0, padx=(20, 0), pady=(25, 0))
        # The right Label
        label_f4_1 = Label(frame_4, text="Vous n'avez pas de compte ?", bg="#FFE4AA", fg="#2C60D9", font=("calibri", 9))
        label_f4_1.grid(column=1, row=1, padx=(70, 0), pady=(0, 59))
        f = font.Font(label_f4_1, label_f4_1.cget("font"))
        f.configure(underline=True)
        label_f4_1.configure(font=f)

        # the last frame for particular info containing 2 labels LEFT and RIGHT
        frame_5 = Frame(self.frame_main, relief=GROOVE, bg="gray")
        frame_5.pack()
        # Left Label
        label_f5_1 = Label(master=frame_5, padx=5, width=58, anchor=NW, text="Pierre papier Ciseau   V1.0", bg="Gray",
                           fg="white", font=("Calibri Light (Headings)", 9))
        label_f5_1.pack(side=LEFT)
        # Right Label
        label_f5_2 = Label(master=frame_5, padx=5, width=58, anchor=NE, text="© 2019", bg="Gray", fg="black",
                           font=("Calibri Light (Headings)", 9))
        label_f5_2.pack()


class Window2(Window1):

    def __init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color):
        Window1.__init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color)
        self.master = master

    def cancel(self):
        msg = askyesno("Annuler !", "Etes vous sur vous voulez annuler ? ", icon=QUESTION, parent=self.master)
        if msg == TRUE:
            self.master.destroy()
        else:
            pass

    def register(self):
        #      Nom         prenom      utilist     age         mdp         verifie mdp
        global entry_f2_1, entry_f2_2, entry_f2_3, entry_f2_5, entry_f2_6, entry_f2_7
        try:
            if entry_f2_1.get() == "":
                raise LastNameError("Entrez vouz votre nom !")
            if entry_f2_2.get() == "":
                raise FirstNameError("Entrez vouz votre Prenom !")
            if entry_f2_3.get() == "":
                raise UserError("Entrez vouz votre nom d\'utilisateur !")
            if int(entry_f2_5.get()) < 7 or int(entry_f2_5.get()) > 21:
                raise AgeError("Entrez vouz votre age !")
            if entry_f2_6.get() == "":
                raise PasswordError("Entrez vouz votre mot de pass !")
            if entry_f2_7.get() == "":
                raise AgainPasswordError("Reecrivez vouz votre mot de pass !")
            if entry_f2_6.get() != entry_f2_7.get():
                raise MatchPasswordError("Les mots de pass ne sont pas identique !")
        except LastNameError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        except FirstNameError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        except UserError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        except AgeError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        except PasswordError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        except AgainPasswordError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        except MatchPasswordError as error:
            print("Erreur : ", error)
            showerror("Erreur", error, icon=ERROR)
            screen_2 = Toplevel(screen_1)
            b = Window2(screen_2, "Inscrire", 400, 350, 470, 160, "gray")
            b.create()
            screen_2.mainloop()
        else:
            conn = msq.connect(host="localhost", user="root", password='', database='pps')
            cursor = conn.cursor()
            print(entry_f2_3.get() + ", " + entry_f2_6.get())
            sql = "INSERT INTO `pps`.`account information` (`Name`, `Last Name`, `User Name`, `Age`, `Password`) VALUES (%s, %s, %s, %s, %s)"
            values = (entry_f2_1.get(), entry_f2_2.get(), entry_f2_3.get(), entry_f2_5.get(), entry_f2_6.get())
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            showinfo("Inscription réussie!", "vous etes inscrit avec succès ! \nVeuillez vous connecter pour jouer",
                     icon=INFO, parent=self.master)
            self.master.destroy()
        finally:
            print("end exceptions")

    def create(self):

        # First Frame in the main frame
        frame_1 = Frame(self.frame_main)
        frame_1.pack(side=TOP)
        # First Label in the frame
        label_f1_1 = Label(frame_1, text="Inscrivez Vous !", width=100, bg="white", fg="black", font=("calibri", 14))
        label_f1_1.pack()

        # second Frame in the main frame
        frame_2 = Frame(self.frame_main, bg="gray")
        frame_2.pack(pady=(20, 0))
        # 6 Labels and 6 Entries and 2 buttons
        # 6 labels
        label_f2_1 = Label(frame_2, text="Nom : *", width=22, fg="white", font=("calibri", 12), bg="gray", anchor=NW)
        label_f2_1.grid(row=0, column=0, padx=(0, 8), pady=(3, 3))
        label_f2_2 = Label(frame_2, text="Prenom : *", width=22, fg="white", font=("calibri", 12), bg="gray", anchor=NW)
        label_f2_2.grid(row=1, column=0, padx=(0, 8), pady=(3, 3))
        label_f2_3 = Label(frame_2, text="Nom d\'utilisateur : *", width=22, fg="white", font=("calibri", 12),
                           bg="gray", anchor=NW)
        label_f2_3.grid(row=2, column=0, padx=(0, 8), pady=(3, 0))
        label_f2_4 = Label(frame_2, text="Age : ", width=22, fg="white", font=("calibri", 12), bg="gray", anchor=NW)
        label_f2_4.grid(row=4, column=0, padx=(0, 8), pady=(0, 3))
        label_f2_5 = Label(frame_2, text="Mot de passe : *", width=22, fg="white", font=("calibri", 12), bg="gray",
                           anchor=NW)
        label_f2_5.grid(row=5, column=0, padx=(0, 8), pady=(3, 3))
        label_f2_6 = Label(frame_2, text="Reecrivez mot de passe : *", width=22, fg="white", font=("calibri", 12),
                           bg="gray", anchor=NW)
        label_f2_6.grid(row=6, column=0, padx=(0, 8), pady=(3, 3))
        # 6 Entries
        global entry_f2_1, entry_f2_2, entry_f2_3 ,entry_f2_5 ,entry_f2_6, entry_f2_7
        # nom
        entry_f2_1 = Entry(frame_2, fg="black", font=("calibri", 12), bg="white", width=15)
        entry_f2_1.grid(row=0, column=1, padx=(0, 8), pady=(3, 3))
        # prenom
        entry_f2_2 = Entry(frame_2, fg="black", font=("calibri", 12), bg="white", width=15)
        entry_f2_2.grid(row=1, column=1, padx=(0, 8), pady=(3, 3))
        # nom d'utilisateur
        entry_f2_3 = Entry(frame_2, fg="black", font=("calibri", 12), bg="white", width=15)
        entry_f2_3.grid(row=2, column=1, padx=(0, 8), pady=(3, 0))
        # label
        entry_f2_4 = Label(frame_2, text="Ex: Nom.Prenom", bg="gray", fg="black", width=22, font=("calibri", 9),
                           anchor=NW)
        entry_f2_4.grid(row=3, column=1, pady=(0, 3), padx=0)
        f = font.Font(entry_f2_4, entry_f2_4.cget("font"))
        f.configure(underline=True)
        entry_f2_4.configure(font=f)
        # age
        entry_f2_5 = Spinbox(frame_2, fg="black", font=("calibri", 12), bg="white", from_=7, to=21, width=13)
        entry_f2_5.grid(row=4, column=1, padx=(0, 8), pady=(0, 3))
        # mot de pass
        entry_f2_6 = Entry(frame_2, fg="black", font=("calibri", 12), bg="white", width=15)
        entry_f2_6.grid(row=5, column=1, padx=(0, 8), pady=(3, 3))
        # reecrivez mot de pass
        entry_f2_7 = Entry(frame_2, fg="black", font=("calibri", 12), bg="white", width=15)
        entry_f2_7.grid(row=6, column=1, padx=(0, 8), pady=(3, 3))
        entry_f2_8 = Label(frame_2, text=" * :   champ obligatoire", bg="gray", fg="black", font=("calibri", 9))
        entry_f2_8.grid(row=7, column=0, padx=12, pady=(0, 10))
        f = font.Font(entry_f2_8, entry_f2_8.cget("font"))
        f.configure(underline=True)
        entry_f2_8.configure(font=f)
        # 2 buttons
        button_f2_1 = Button(frame_2, width=12, text="Inscrire", bg="black", fg="white", font=("calibri", 12),
                             cursor="hand2", relief=GROOVE, command=self.register)
        button_f2_1.grid(column=0, row=8, padx=(20, 0), pady=(15, 20))
        button_f2_2 = Button(frame_2, width=12, text="Annuler", bg="black", fg="white", font=("calibri", 12),
                             cursor="hand2", relief=GROOVE, command=self.cancel)
        button_f2_2.grid(column=1, row=8, padx=(20, 0), pady=(15, 20))


class Window3(Window1):
    def __init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color, button_selected,
                 number_choices, choice, frame_exist, max_count, result, comp_count, user_count, user_final_score,
                 comp_final_score):
        Window1.__init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color)
        self.button_selected = button_selected
        self.number_choices = number_choices
        self.choice = choice
        self.frame_exist = frame_exist
        self.max_count = max_count
        self.all_choices = ["Pierre", "Papier", "Ciseau"]
        self.result = result
        self.comp_count = comp_count
        self.user_count = user_count
        self.user_final_score = user_final_score
        self.comp_final_score = comp_final_score

    def comp_choice(self):
        return random.choice(self.all_choices)

    def clear_button(self, val):
        try:
            if val:
                self.number_choices = 0
                frame_4_01_a.destroy()
                frame_4_01_b.destroy()
                self.frame_exist = False
            if not val:
                raise ClearNoFrame("clear")
        except ClearNoFrame as error:
            print(error)

    def quit_button(self):
        screen_4 = Toplevel(screen_3)
        d = Window4(screen_4, "Quittez le jeu ! ", 380, 80, 480, 400, "gray")
        d.create()
        screen_4.mainloop()

    def choice_clicked(self, val, val2):
        try:
            if val2:
                self.frame_exist = True
                if self.number_choices == 0:
                    # 2 frames inside the left frame
                    # Top Frame
                    global frame_4_01_a
                    frame_4_01_a = Frame(frame_4_01, bg="white")
                    frame_4_01_a.pack(side=TOP, pady=(10, 5))
                    # 5 labels
                    label_f4_01_a_1 = Label(frame_4_01_a, text="user", width=13, height=3, bg="gray", fg="white", relief=GROOVE)
                    label_f4_01_a_1.pack(side=LEFT, padx=(10, 8))
                    label_f4_01_a_2 = Label(frame_4_01_a, text=".", width=13, height=3, bg="gray", fg="white",
                                            relief=GROOVE)
                    label_f4_01_a_2.pack(side=LEFT, padx=(8, 12))

                    label_f4_01_a_3 = Label(frame_4_01_a, text=" VS ", width=13, height=4, font=("calibri", 10), bg="gray",
                                            fg="white", relief=GROOVE)
                    label_f4_01_a_3.pack(side=LEFT, padx=(12, 12))
                    label_f4_01_a_4 = Label(frame_4_01_a, text="computer", width=13, height=3, bg="gray", fg="white",
                                            relief=GROOVE)
                    label_f4_01_a_4.pack(side=LEFT, padx=(12, 8))
                    label_f4_01_a_5 = Label(frame_4_01_a, text=".", width=13, height=3, bg="gray", fg="white",
                                            relief=GROOVE)
                    label_f4_01_a_5.pack(side=LEFT, padx=(8, 10))

                    # Bottom Frame
                    global frame_4_01_b
                    frame_4_01_b = Frame(frame_4_01, bg="white")
                    frame_4_01_b.pack(fill=X, pady=(5, 10))
                    # 1 label
                    label_f4_01_b_1 = Label(frame_4_01_b, text=".", bg=self.val_color, fg="green", width=30,
                                            font=("calibri", 13), height=4, relief=GROOVE)
                    label_f4_01_b_1.pack()

                    self.choose_choice(val, label_f4_01_a_2, label_f4_01_a_5, label_f4_01_b_1)
                    self.number_choices += 1
                else:
                    raise ClickedTwoTimesError("Attention, Vous avez clickez deux fois !")
            if not val2:
                raise PartyButtonNotSelected("SVP choisissez vous un nombre de partie !")
        except ClickedTwoTimesError as error:
            showwarning("Attention !", error)
        except PartyButtonNotSelected as error:
            showwarning("Attention !", error)

    def add_result_clear_all(self):
        global screen_3
        showwarning("Winner", "end of the partie")
        button_f2_00_1.deselect()
        button_f2_00_2.deselect()
        button_f2_00_3.deselect()
        if self.user_count > self.comp_count:
            self.user_final_score += 1
            new = self.user_final_score
            old = self.comp_final_score
            screen_3.destroy()
            screen_3 = Tk()
            c = Window3(screen_3, "Pierre Papier Ciseau", 700, 550, 300, 90, "#FFE4AA", False, 0, "", False, 0, 0, 0, 0,
                        new, old)
            c.create()
            screen_3.mainloop()

        if self.user_count < self.comp_count:
            self.comp_final_score += 1
            new = self.comp_final_score
            old = self.user_final_score
            screen_3.destroy()
            screen_3 = Tk()
            c = Window3(screen_3, "Pierre Papier Ciseau", 700, 550, 300, 90, "#FFE4AA", False, 0, "", False, 0, 0, 0, 0,
                        old, new)
            c.create()
            screen_3.mainloop()

        if self.user_count == self.comp_count:
            stable_1 = self.user_final_score
            stable_2 = self.comp_final_score
            screen_3.destroy()
            screen_3 = Tk()
            c = Window3(screen_3, "Pierre Papier Ciseau", 700, 550, 300, 90, "#FFE4AA", False, 0, "", False, 0, 0, 0, 0,
                        stable_1, stable_2)
            c.create()
            screen_3.mainloop()

    def choose_choice(self, choice_value, label1, label2, label3):

        if choice_value == self.all_choices[0]:
            label1.configure(text=self.all_choices[0])
            comp_res = self.comp_choice()
            label2.configure(text=comp_res)

            if comp_res == "Pierre":
                label3.configure(text="égalité")
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()

            if comp_res == "Papier":
                label3.configure(text="Computer Wins")
                self.comp_count += 1
                label_f4_02_2.configure(text=str(self.comp_count))
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()

            if comp_res == "Ciseau":
                label3.configure(text="User Wins")
                self.user_count += 1
                label_f4_02_1.configure(text=str(self.user_count))
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()

        if choice_value == self.all_choices[1]:
            label1.configure(text=self.all_choices[1])
            comp_res = self.comp_choice()
            label2.configure(text=comp_res)

            if comp_res == "Pierre":
                label3.configure(text="User Wins")
                self.user_count += 1
                label_f4_02_1.configure(text=str(self.user_count))
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()
            if comp_res == "Papier":
                label3.configure(text="égalité")
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()
            if comp_res == "Ciseau":
                label3.configure(text="Computer Wins")
                self.comp_count += 1
                label_f4_02_2.configure(text=str(self.comp_count))
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()

        if choice_value == self.all_choices[2]:
            label1.configure(text=self.all_choices[2])
            comp_res = self.comp_choice()
            label2.configure(text=comp_res)

            if comp_res == "Pierre":
                label3.configure(text="Computer Wins")
                self.comp_count += 1
                label_f4_02_2.configure(text=str(self.comp_count))
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()
            if comp_res == "Papier":
                label3.configure(text="User Wins")
                self.user_count += 1
                label_f4_02_1.configure(text=str(self.user_count))
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()
            if comp_res == "Ciseau":
                label3.configure(text="égalité")
                self.result += 1
                if self.result == self.max_count:
                    self.add_result_clear_all()

    def radiobutton_selected(self, max_val):
        self.max_count = max_val
        print(self.max_count)
        self.button_selected = 1

    def create(self):
        # First Top Frame containing 2 Frames and 2 labels
        frame_1 = Frame(self.frame_main, bg="gray")
        frame_1.pack(side=TOP, pady=(0, 5))
        # 2 frames
        # Left Frame
        frame_1_00 = Frame(frame_1)
        frame_1_00.pack(side=LEFT)
        label_f1_00_1 = Label(frame_1_00, text="Utilisateur :    {}".format(name), bg="gray", fg="white", width=50,
                              anchor=NW, padx=15, pady=3, font=("calibri", 14))
        label_f1_00_1.pack()
        # Right Frame
        frame_1_01 = Frame(frame_1)
        frame_1_01.pack()
        label_f1_01_1 = Label(frame_1_01, text="Connectée", bg="gray", fg="#08C008", width=50, padx=5, pady=3,
                              font=("arial black", 11))
        label_f1_01_1.pack()

        # second frame containing the game
        frame_2 = Frame(self.frame_main, bg=self.val_color)
        frame_2.pack(pady=(5, 10))
        # first line frame in the game frame
        # Left Frame
        frame_2_00 = Frame(frame_2, bg=self.val_color)
        frame_2_00.pack(side=LEFT)
        label_f2_00_1 = Label(frame_2_00, width=50, text="Instruction :", bg=self.val_color, fg="black",
                              font=("calibri", 11), anchor=NW)
        label_f2_00_1.pack(side=TOP)
        f = font.Font(label_f2_00_1, label_f2_00_1.cget("font"))
        f.configure(underline=True)
        label_f2_00_1.configure(font=f)
        label_f2_00_2 = Label(frame_2_00, width=50, text="- La pierre écrase les ciseaux et gagne.", bg=self.val_color,
                              fg="black", font=("calibri", 10), anchor=NW)
        label_f2_00_2.pack()
        label_f2_00_3 = Label(frame_2_00, width=50, text="- La feuille enveloppe la pierre et gagne.",
                              bg=self.val_color, fg="black", font=("calibri", 10), anchor=NW)
        label_f2_00_3.pack()
        label_f2_00_4 = Label(frame_2_00, width=50, text="- Les ciseaux découpent la feuille et gagnent.",
                              bg=self.val_color, fg="black", font=("calibri", 10), anchor=NW)
        label_f2_00_4.pack()
        label_f2_00_5 = Label(frame_2_00, width=50, text="- Nombre de partie dans chaque Jeu:", bg=self.val_color,
                              fg="black", font=("calibri", 10), anchor=NW)
        label_f2_00_5.pack()
        global button_f2_00_1, button_f2_00_2, button_f2_00_3
        global var
        var = IntVar()
        button_f2_00_1 = Radiobutton(frame_2_00, bg=self.val_color, text="1", variable=var, value=1, anchor=NW,
                                     width=3, command=lambda x=1: self.radiobutton_selected(x))
        button_f2_00_2 = Radiobutton(frame_2_00, bg=self.val_color, text="3", variable=var, value=3, anchor=NW,
                                     width=3, command=lambda x=3: self.radiobutton_selected(x))
        button_f2_00_3 = Radiobutton(frame_2_00, bg=self.val_color, text="5", variable=var, value=5, anchor=NW,
                                     width=3, command=lambda x=5: self.radiobutton_selected(x))
        button_f2_00_1.pack(side=LEFT, padx=(40, 0))
        button_f2_00_2.pack(side=LEFT)
        button_f2_00_3.pack(side=LEFT)
        # Right Frame
        frame_2_01 = Frame(frame_2, relief=GROOVE, bd=2, bg=self.val_color)
        frame_2_01.pack()
        global label_f2_01_1, label_f2_01_2
        label_f2_01_1 = Label(frame_2_01, width=50, text="User Score  :  {}".format(self.user_final_score),
                              bg=self.val_color, fg="black",
                              font=("calibri", 10))
        label_f2_01_1.pack(side=TOP, pady=12)
        label_f2_01_2 = Label(frame_2_01, width=50, text="Computer Score  :  {}".format(self.comp_final_score),
                              bg=self.val_color, fg="black",
                              font=("calibri", 10))
        label_f2_01_2.pack(pady=12)

        # Adding new frame
        frame_3 = Frame(self.frame_main, bg=self.val_color)
        frame_3.pack(pady=(7, 5))
        label_f3_01 = Label(frame_3, text="user", width=15, height=5, bg="gray", fg="white", relief=GROOVE)
        label_f3_01.pack(side=LEFT, padx=(2, 5), pady=(5, 5))
        button_f3_02 = Button(frame_3, text="Pierre", width=15, height=4, bg="gray", fg="white", relief=GROOVE,
                              cursor="hand2", command=lambda: self.choice_clicked("Pierre", self.button_selected))
        button_f3_02.pack(side=LEFT, padx=(85, 5), pady=(5, 5))
        button_f3_03 = Button(frame_3, text="Ciseaux", width=15, height=4, bg="gray", fg="white", relief=GROOVE,
                              cursor="hand2", command=lambda: self.choice_clicked("Ciseau", self.button_selected))
        button_f3_03.pack(side=LEFT, padx=(5, 5), pady=(5, 5))
        button_f3_04 = Button(frame_3, text="Papier", width=15, height=4, bg="gray", fg="white", relief=GROOVE,
                              cursor="hand2", command=lambda: self.choice_clicked("Papier", self.button_selected))
        button_f3_04.pack(side=LEFT, padx=(5, 2), pady=(5, 5))

        # frame 4 under frame 3
        frame_4 = Frame(self.frame_main, bg=self.val_color)
        frame_4.pack(pady=(10, 0))
        # 2 frames in frame 4
        # Left Frame
        global frame_4_01
        frame_4_01 = Frame(frame_4, bg="white", relief=SUNKEN, bd=1, width=583, height=188)
        frame_4_01.pack(side=LEFT, padx=(60, 0))
        # Right Frame
        frame_4_02 = Frame(frame_4, bg=self.val_color)
        frame_4_02.pack(padx=(35, 0))
        global label_f4_02_1
        global label_f4_02_2
        label_f4_02_1 = Label(frame_4_02, text=str(self.user_count), height=2, relief=GROOVE, bg="gray",
                              fg="white", padx=4)
        label_f4_02_1.pack(side=TOP, pady=(10, 30))
        label_f4_02_2 = Label(frame_4_02, text=str(self.user_count), height=2, relief=GROOVE, bg="gray",
                              fg="white", padx=4)
        label_f4_02_2.pack(pady=(30, 10))

        # frame 5 the clear button
        frame_5 = Frame(self.frame_main, bg=self.val_color)
        frame_5.pack()
        # 1 button
        button_f5 = Button(frame_5, text="Vider", width=10, relief=GROOVE, cursor="hand2", bg="gray", fg="white",
                           command=lambda: self.clear_button(self.frame_exist))
        button_f5.pack()

        # Frame 6 the Quit button
        frame_6 = Frame(self.frame_main, bg=self.val_color)
        frame_6.pack()
        # 1 button
        button_f6 = Button(frame_6, text="Sortir", width=10, relief=GROOVE, cursor="hand2", bg="gray", fg="white",
                           command=self.quit_button)
        button_f6.pack(padx=(622, 2), pady=(10, 0))


class Window4(Window1):
    def __init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color):
        Window1.__init__(self, master, val_title, val_width, val_height, width_pos, height_pos, val_color)

    def quit_both(self):
        self.master.destroy()
        screen_3.destroy()

    def reconnect(self):
        self.quit_both()
        main_function()

    def create(self):
        button_f1_1 = Button(self.frame_main, text="Deconnectez vous et quittez", width=30, relief=GROOVE,
                             cursor="hand2", bg="white", command=self.quit_both)
        button_f1_1.pack(side=LEFT, padx=(10, 8), pady=27)
        button_f1_2 = Button(self.frame_main, text="Deconnectez vous", width=30, relief=GROOVE, cursor="hand2",
                             bg="white", command=self.reconnect)
        button_f1_2.pack(padx=(10, 8), pady=27)


if __name__ == "__main__":
    main_connection()
    main_function()
