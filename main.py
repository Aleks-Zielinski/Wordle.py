import tkinter
import tkinter.messagebox
import customtkinter # python install customtkinter
from words import ANSWERS
import random
import os
from PIL import Image, ImageTk

PATH = os.path.dirname(os.path.realpath(__file__))

#
#   Wordle.py main file
#   custom tkinter gui: https://github.com/TomSchimansky/CustomTkinter
#   Made to learn GUI with Python
#   Copied Class App from CTK example and modified it
#   Python 3.10.7
#

# set standard themes
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    # perfect match 
    WIDTH = 444
    HEIGHT = 582

    def __init__(self):
        super().__init__()

        ##############
        # config gui #
        ##############

        self.title("Wördle")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.resizable(False, False) # to keep prefect working size
        self.iconbitmap(f'{PATH}/images/icon64w.ico') 

        self.grid_columnconfigure(0, weight=10)
        self.grid_rowconfigure(0, weight=10)

        self.frame_main = customtkinter.CTkFrame(master=self)
        self.frame_main.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        # config grid layout (5x7)
        self.frame_main.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
        self.frame_main.columnconfigure((0, 1, 2, 3, 4), weight=0)
        
        self.label_1st = customtkinter.CTkLabel(master=self.frame_main,
                                              text='Wördle',
                                              width=70,
                                              text_font=("Roboto Medium", 30))  # font name and size in px
        self.label_1st.grid(row=0, column=1, columnspan=3, pady=5, padx=5)

        self.button_1 = customtkinter.CTkButton(master=self.frame_main,
                                                image=self.load_image('/images/resetw.png'),
                                                text = '',
                                                width= 64,
                                                hover_color=None,
                                                fg_color=None,
                                                command=self.reset)
        self.button_1.grid(row=0, column=4, pady=0, padx=0, sticky="we")

        self.labels = []
        for i in range(5): # for loop to spawn squares
            for j in range(6):
                self.label_bg = customtkinter.CTkLabel(master=self.frame_main,
                                              text='',
                                              text_font=("Roboto Medium", -16),
                                              width=70,
                                              height=70,
                                              bg_color='black')
                self.label_bg.grid(row=j+1, column=i, pady=5, padx=5)
                self.label = customtkinter.CTkLabel(master=self.frame_main,
                                              text='',
                                              text_font=("Roboto Medium", -24),
                                              width=64,
                                              height=64)
                self.labels.append(self.label)
                self.labels[j+6*i].grid(row=j+1, column=i, pady=5, padx=5) 

        ###############
        # config game #
        ###############

        self.letters = []
        self.answers = ANSWERS # doesn't have to be but is more complex, self.answers > ANSWERS
        self.answer = self.getanswer()
        self.round = 0
        self.win = False
        
        if True: # to wrap in in vsc
            self.bind('q', lambda event: self.printkey('Q'))
            self.bind('w', lambda event: self.printkey('W'))
            self.bind('e', lambda event: self.printkey('E'))
            self.bind('r', lambda event: self.printkey('R'))
            self.bind('t', lambda event: self.printkey('T'))
            self.bind('y', lambda event: self.printkey('Y'))
            self.bind('u', lambda event: self.printkey('U'))
            self.bind('i', lambda event: self.printkey('I'))
            self.bind('o', lambda event: self.printkey('O'))
            self.bind('p', lambda event: self.printkey('P'))
            self.bind('a', lambda event: self.printkey('A'))
            self.bind('s', lambda event: self.printkey('S'))
            self.bind('d', lambda event: self.printkey('D'))
            self.bind('f', lambda event: self.printkey('F'))
            self.bind('g', lambda event: self.printkey('G'))
            self.bind('h', lambda event: self.printkey('H'))
            self.bind('j', lambda event: self.printkey('J'))
            self.bind('k', lambda event: self.printkey('K'))
            self.bind('l', lambda event: self.printkey('L'))
            self.bind('z', lambda event: self.printkey('Z'))
            self.bind('x', lambda event: self.printkey('X'))
            self.bind('c', lambda event: self.printkey('C'))
            self.bind('v', lambda event: self.printkey('V'))
            self.bind('b', lambda event: self.printkey('B'))
            self.bind('n', lambda event: self.printkey('N'))
            self.bind('m', lambda event: self.printkey('M'))
            self.bind('<BackSpace>', lambda event: self.printkey('Backspace'))
            self.bind('<Return>', lambda event: self.printkey('Enter'))  

    # get answer from list
    def getanswer(self):
        word = random.choice(self.answers) # can be ANSWERS or self.answers
        wordcut = list(word)
        print(wordcut)
        return wordcut                                              

    # print letters on gui
    def printkey(self, key):
        if self.win == True:return
        answer = ''.join(self.letters)
        Len = len(self.letters)

        if key == 'Backspace':
            self.labels[self.round + 6 * (Len - 1)].configure(text = '')
            if Len != 0:
                self.letters.pop()
            return
        print(answer)
        if key == 'Enter' and Len > 4 and answer in self.answers:
            print(self.answer)
            print(self.letters)
            self.check()
            return    
        elif Len > 4 or key == 'Enter' or key == 'Backspace' or self.round == 6:
            return

        print(key)
        self.letters.append(key)
        self.labels[self.round + 6 * Len].configure(text = key)

    # check if answer given is an answer
    def check(self):
        list = [0, 0, 0, 0, 0]
        for i in range(len(self.letters)):
            if self.letters[i] == self.answer[i]:
                list[i] = 2
                continue
            elif self.letters[i] in self.answer:
                list[i] = 1
                continue

        for i in range(5):
            if list[i] == 0:
                self.labels[self.round + 6 * i].configure(bg_color= 'black')
            elif list[i] == 1:
                self.labels[self.round + 6 * i].configure(bg_color= 'chocolate')
            else:
                self.labels[self.round + 6 * i].configure(bg_color= 'green')

        self.round += 1
        self.letters = []

        x = 0
        for i in list:
            x += i 
        if x == 10:
            self.win = True
            print('Win')
            self.label_1st.configure(text = ''.join(self.answer))
            return
        elif self.round == 6:
            print(f'Lose | {self.answer}')
            self.label_1st.configure(text = ''.join(self.answer))

    # reset game on click
    def reset(self):
        for i in range(len(self.labels)):
            self.labels[i].configure(text = '', bg_color = None)
        self.round = 0
        self.letters = []
        self.win = False
        self.label_1st.configure(text = 'Wördle')
        self.answer = self.getanswer()

    # load images
    def load_image(self, path):
        return ImageTk.PhotoImage(Image.open(PATH + path))                    

    # big red button
    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()