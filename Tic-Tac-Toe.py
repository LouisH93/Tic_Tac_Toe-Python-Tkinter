'''A simple tic-tac-toe game built using tkinter'''
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox as messagebox
from tkinter import ttk, PhotoImage


class GameRoot(tk.Tk):
    '''Root widget, inherits from Tk class'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Pass positional and keyword args straight to the Tk class to avoid any possible errors
        self.title('Tic-Tac-Toe')
        self.geometry('435x450')
        self.resizable(0, 0) # Not resizable
        self.iconbitmap('Tic-Tac-Toe-assets/icon.ico') # Root icon

        self.clickX = True # Ensures X goes first, re-initialised to True for each new game
        self.count = 0 # Count == 3 when either X or O wins, 9 for a draw. Will be re_initialised to 0 for each new game

        # Textvariables, will be used to determine where to insert the photo images
        self.btn1 = tk.StringVar()
        self.btn2 = tk.StringVar()
        self.btn3 = tk.StringVar()
        self.btn4 = tk.StringVar()
        self.btn5 = tk.StringVar()
        self.btn6 = tk.StringVar()
        self.btn7 = tk.StringVar()
        self.btn8 = tk.StringVar()
        self.btn9 = tk.StringVar()

        # X and O images
        self.x_photo = PhotoImage(file='Tic-Tac-Toe-assets/cross.png')
        self.o_photo = PhotoImage(file='Tic-Tac-Toe-assets/cool.png')


    def play(self):
        '''Method for configuring buttons and placing them in the root's grid system'''
        button1 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn1, bg='#ccffcc', command=lambda: self.press(1, 0, 0))
        button2 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn2, bg='#ccffcc', command=lambda: self.press(2, 0, 1))
        button3 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn3, bg='#ccffcc', command=lambda: self.press(3, 0, 2))
        button4 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn4, bg='#99ff99', command=lambda: self.press(4, 1, 0))
        button5 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn5, bg='#99ff99', command=lambda: self.press(5, 1, 1))
        button6 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn6, bg='#99ff99', command=lambda: self.press(6, 1, 2))
        button7 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn7, bg='#66ff66', command=lambda: self.press(7, 2, 0))
        button8 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn8, bg='#66ff66', command=lambda: self.press(8, 2, 1))
        button9 = tk.Button(self, width=19, height=9, relief='ridge', textvariable=self.btn9, bg='#66ff66', command=lambda: self.press(9, 2, 2))

        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)
        button4.grid(row=1, column=0)
        button5.grid(row=1, column=1)
        button6.grid(row=1, column=2)
        button7.grid(row=2, column=0)
        button8.grid(row=2, column=1)
        button9.grid(row=2, column=2)

        # All button padx and pady configurations  
        for child in self.winfo_children():
            child.grid_configure(padx=1, pady=1)
            

    def press(self, button_num, row_num, column_num):
        '''Method for setting each textvariable with either an 'X' or an 'O'. X moves first, so they're configured first. Label widget is
        used to insert the photo images'''
        if self.clickX:
            
            photo_label = tk.Label(self, image=self.x_photo)
            photo_label.grid(row=row_num, column=column_num)
            
            if button_num == 1:
                self.btn1.set('X')
            elif button_num == 2:
                self.btn2.set('X')
            elif button_num == 3:
                self.btn3.set('X')
            elif button_num == 4:
                self.btn4.set('X')
            elif button_num == 5:
                self.btn5.set('X')
            elif button_num == 6:
                self.btn6.set('X')
            elif button_num == 7:
                self.btn7.set('X')
            elif button_num == 8:
                self.btn8.set('X')
            else: 
                self.btn9.set('X')
                    
            self.clickX = False 
            self.count += 1
            self.check_win()
            
        else:
            
            photo_label = tk.Label(self, image=self.o_photo)
            photo_label.grid(row=row_num, column=column_num)

            if button_num == 1:
                self.btn1.set('O')
            elif button_num == 2:
                self.btn2.set('O')
            elif button_num == 3:
                self.btn3.set('O')
            elif button_num == 4:
                self.btn4.set('O')
            elif button_num == 5:
                self.btn5.set('O')
            elif button_num == 6:
                self.btn6.set('O')
            elif button_num == 7:
                self.btn7.set('O')
            elif button_num == 8:
                self.btn8.set('O')
            else: 
                self.btn9.set('O')
            
            self.clickX = True
            self.count += 1
            self.check_win()
            

    def check_win(self):
        '''Method for checking all possible means of victory for both X and O. Also checks whether a draw occured. A messagebox is outputted
        accordingly'''

        # X wins
        if (self.btn1.get() == 'X' and self.btn2.get() == 'X' and self.btn3.get() == 'X' or
            self.btn4.get() == 'X' and self.btn5.get() == 'X' and self.btn6.get() == 'X' or
            self.btn7.get() == 'X' and self.btn8.get() == 'X' and self.btn9.get() == 'X' or
            self.btn1.get() == 'X' and self.btn4.get() == 'X' and self.btn7.get() == 'X' or
            self.btn2.get() == 'X' and self.btn5.get() == 'X' and self.btn8.get() == 'X' or
            self.btn3.get() == 'X' and self.btn6.get() == 'X' and self.btn9.get() == 'X' or
            self.btn1.get() == 'X' and self.btn5.get() == 'X' and self.btn9.get() == 'X' or
            self.btn3.get() == 'X' and self.btn5.get() == 'X' and self.btn7.get() == 'X'):
            messagebox.showinfo('That\'s Game!', 'X Wins..')
            self.clickX = True 
            self.count = 0 
            self.clear() 
            self.play()  

        # O wins
        '''If O was clicked last, self.clickX is initialised to True in the press() method so no need to re-set that property if O wins
        the game'''
        elif (self.btn1.get() == 'O' and self.btn2.get() == 'O' and self.btn3.get() == 'O' or
              self.btn4.get() == 'O' and self.btn5.get() == 'O' and self.btn6.get() == 'O' or
            self.btn7.get() == 'O' and self.btn8.get() == 'O' and self.btn9.get() == 'O' or
              self.btn1.get() == 'O' and self.btn4.get() == 'O' and self.btn7.get() == 'O' or
            self.btn2.get() == 'O' and self.btn5.get() == 'O' and self.btn8.get() == 'O' or
              self.btn3.get() == 'O' and self.btn6.get() == 'O' and self.btn9.get() == 'O' or
            self.btn1.get() == 'O' and self.btn5.get() == 'O' and self.btn9.get() == 'O' or
              self.btn3.get() == 'O' and self.btn5.get() == 'O' and self.btn7.get() == 'O'):
            messagebox.showinfo('That\'s Game!', 'O Wins..')
            self.count = 0
            self.clear()
            self.play()

        # Draw
        elif self.count == 9:
            messagebox.showinfo('That\'s Game!', ':/ Draw..')
            self.clickX = True
            self.count = 0
            self.clear()
            self.play()
            

    def clear(self):
        '''Simple method for clearing the textvariables'''
        self.btn1.set('')
        self.btn2.set('')
        self.btn3.set('')
        self.btn4.set('')
        self.btn5.set('')
        self.btn6.set('')
        self.btn7.set('')
        self.btn8.set('')
        self.btn9.set('')

        
i = GameRoot()
i.play()
i.mainloop()
