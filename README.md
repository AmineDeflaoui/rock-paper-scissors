# rock-paper-scissors
rock paper scissors Game using Python &amp; Tkinter

## Introduction :
The application in general is a game that a single person can play against the computer, the user has the option of choosing from three choices and the computer too, but randomly the program will have the ability to determine who is the winner (user, computer).
In detail, the program will first contain a login interface, where the user can create an account and save their information to log in.
Once the homepage log is displayed, we will discuss the homepage details later in the report.
In general, the main language used is Python version 3, and worked especially with classes, inheritance and exceptions.
Next, we used the Python GUI (Graphical User Interface) combined with the script to create a graphical appearance for the code.
And finally, we also used the databases to save the information and get it when logging into the game.

## Analyse the Script: 
### Python Syntaxe:
#### Classes:
Before digging into the classes used in the script, we first used in our program two functions: (main function, main connection), the main connection function, we will discuss this later, and the main function is a function which we call 'if __name__=__main__' which contains the first object initialized with the first class and a function inside that class, and before we created the first variable containing the function 'Tk()' which initializes the graphics system.
In general, the main function is responsible for the execution of the whole program.
The first class used and created is ‘MainWindow’ only contains an initializer with 6 parameters, the first is the master that controls the graphics window (this class will be inherited later).
The second class is 'Window1' (This class will be inherited later) representing the first interface of the game (login) contains the initializer with 7 parameters, it also contains 3 functions, first 'sign_in', which activates when you click on the 'register' button, then the 'connect' function which is activated when you click on the 'Connect' button, finally the 'create' function which contains the composition of the page, the organization of labels and buttons, images...
The third class used and created is 'Window2' contains an initializer with 7 parameters of which the first is the master that controls the graphics window, this class representing the second interface of the game (register) contains 3 functions, first cancellation, which activates when the 'Cancel' button is clicked, then the registration function which is activated when the 'Register' button is clicked, finally the creation function which contains the composition of the page, the organization of the 'Label ' and buttons, images...
The fourth class used and created is 'Window3' (contains the main functions of the game) contains an initializer with 17 parameters the first is the master that controls the graphics window, this class represents the third (the main) interface of the game contains 8 functions , the first 'comp_choice', which returns the results of the random choice that the computer will make, next to the 'clear_button' function which is activated when the 'Clear button' is clicked, next to the 'quit_button' which activates when the 'exit' button is clicked, next to the 'choice_clicked' function which activates when the user selects a choice, then the 'add_result_clear_all' function which activates when the program determines the winner and the loser and modifies the final results, then the 'choose_choice' function which activates when the user selects his option and the computer also and the function will determine the winner and the looser or the equalizer, beside the a function 'radiobutton_selected' which is activated when the radio button is clicked, finally the function 'create' which contains the composition of the page, the organization of labels and buttons, images ...
The fifth and last class is 'Window4' which contains an initializer with 7 parameters and 3 functions, the first function 'quit_both' is launched when the user chooses to logout and quit the game, the next function is to reconnect , will be activated when the user wants to reconnect with the same account or use another account.

#### Inheritance:
Inheritance is used twice in our program, the first when we created the main window which contains the configuration of the window: the title, the width, the height, the position of the width, the position of the height.
The second class will be inherited from the main window to create the first game image (login), the new class will inherit the old settings and add a new color.
The other classes remain, will also inherit all parameters from Window1 and add new ones like the 'Window3' class which needs 17 parameters combined between old and new.
In this program, we have not inherited any function in another class, because functions will only work in those classes, there is no need to call a function in another class.

#### Exceptions:
We have certainly used the exceptions in the application, in many cases like the first window where the user enters their username and password if the information entered does not match the information saved an error will occur .
In the second window, registration window, we find many exceptions where the user must enter their first name last name username password, repeat the password, and in each case we have an exception for some familiar errors (blank first name, blank last name, blank username, age above 21 or below 7, blank password, blank repeat password, and password does not match)
In the main game, we have an exception if the user selects no button (1,3,5) number of games, an error will appear informing the user to first choose an option to continue.
The last exception is if the user has clicked twice on a single choice an error appears to inform that the user has already selected a button (a choice), and that he has performed another illegal action.

### GUI(Tkinter) Syntax:
In the program, we used a python module specific to graphical interfaces (GUI), the 'window' gadgets correspond to classes of objects whose attributes and methods will have to be studied.
In the "Mainwindow" class, we used the following gadgets to configure the window:
- “geometry ()”: to determine the width and height and position of the window.
- "Title ()”: to give a title to the window.
- “minsize ()”: to control the minimum size that the window can take.
- “maxsize ()”: to control the maximum size that the window can take.
- “iconbitmap ()”: to give the window an image (icon) in the upper left corner.
In the following classes, we used some gadgets as follows:
frames,
button,
Label,
entry,
Spinbox,
Radio button…
We imported 'tkinter. Messagebox' to use 'showerror', 'showinfo', 'askyesno', 'showwarning' gadgets.
We also imported the font from 'tkinter' to style characters such as underline...

### DataBase (SQL) syntax:
To save information and get them to log into the game, we've included Database to handle this.
First we connect to the database (database already created, table already created)
To save information in the database, we use “cursor. Execute(“INSERT…”)”.
To get the information to check in the connection, we use “cursor. Execute("SELECT....")".

## Conclusion:
The program in general works well Without any bugs, there is no problem connecting to the database or receiving information, the script is a bit long (700 Line) it needs to be optimized to reduce the amount of line used in the code use a class or a function that combines several functions doing almost the same thing, and there are many possibilities to develop the game, add new features, improve the current game and its features.
