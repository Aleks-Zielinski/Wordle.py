import tkinter as tk
from tkinter import messagebox
from words import ANSWERS
import random

#   
#   Legacy wordle.py made with pure tkinter
#   won't change and comment anything there
#   Made to learn tkinter
#   

class Game():
    def __init__(self):
        self.answer = self.getanswer()
        self.letters = []
        self.round = 0
        self.win = False
        self.X = [11, 60, 66, 115, 121, 170, 176, 225, 231, 280]
        self.Y = [46, 95, 101, 150, 156, 205, 211, 260, 266, 315]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=327, width=292, bg=self.returnrgb(64, 64, 64))

    def init(self):
        self.root.geometry('292x327')
        self.root.resizable(False, False)
        self.root.title('Wördle')
        self.root.iconbitmap('C:\VSC\pyprojects\wordle\images\icon64.ico')      
        self.bind()
        self.gui()
        self.root.mainloop() 

    def bind(self):
        self.root.bind('q', lambda event: self.printkey('Q'))
        self.root.bind('w', lambda event: self.printkey('W'))
        self.root.bind('e', lambda event: self.printkey('E'))
        self.root.bind('r', lambda event: self.printkey('R'))
        self.root.bind('t', lambda event: self.printkey('T'))
        self.root.bind('y', lambda event: self.printkey('Y'))
        self.root.bind('u', lambda event: self.printkey('U'))
        self.root.bind('i', lambda event: self.printkey('I'))
        self.root.bind('o', lambda event: self.printkey('O'))
        self.root.bind('p', lambda event: self.printkey('P'))
        self.root.bind('a', lambda event: self.printkey('A'))
        self.root.bind('s', lambda event: self.printkey('S'))
        self.root.bind('d', lambda event: self.printkey('D'))
        self.root.bind('f', lambda event: self.printkey('F'))
        self.root.bind('g', lambda event: self.printkey('G'))
        self.root.bind('h', lambda event: self.printkey('H'))
        self.root.bind('j', lambda event: self.printkey('J'))
        self.root.bind('k', lambda event: self.printkey('K'))
        self.root.bind('l', lambda event: self.printkey('L'))
        self.root.bind('z', lambda event: self.printkey('Z'))
        self.root.bind('x', lambda event: self.printkey('X'))
        self.root.bind('c', lambda event: self.printkey('C'))
        self.root.bind('v', lambda event: self.printkey('V'))
        self.root.bind('b', lambda event: self.printkey('B'))
        self.root.bind('n', lambda event: self.printkey('N'))
        self.root.bind('m', lambda event: self.printkey('M'))
        self.root.bind('<BackSpace>', lambda event: self.printkey('Backspace'))
        self.root.bind('<Return>', lambda event: self.printkey('Enter'))

    def printkey(self, key):
        #print(self.answer)
        if self.win == True:return
        Len = len(self.letters)

        if key == 'Backspace':
            tk.Label(bg = self.returnrgb(64, 64, 64), fg='white', width=1, font=('Calibri', 24),  text = '').place(x = self.X[(Len - 1) * 2] + 13, y = self.Y[self.round * 2 + 1] - 47)
            #print(self.X[(Len-1)*2])
            if Len != 0:
                self.letters.pop()
                #print('t')
            return

        if key == 'Enter' and Len > 4:
            print(self.answer)
            print(self.letters)
            self.check()
            return    
        elif Len > 4 or key == 'Enter' or key == 'Backspace' or self.round == 5:
            return

        print(key)
        self.letters.append(key)
        tk.Label(bg = self.returnrgb(64, 64, 64), fg='white', width=1, font=('Calibri', 24),  text = self.letters[Len]).place(x = self.X[Len * 2] + 13, y = self.Y[self.round * 2 + 1] - 47)

    def check(self):
        list = [0, 0, 0, 0, 0]
        x = 0
        for i in range(len(self.letters)):
            if self.letters[i] == self.answer[i]:
                list[i] = 2
                continue
            elif self.letters[i] in self.answer:
                list[i] = 1
                continue

        j = 0
        for i in range(10):
            if i % 2 == 1:
                continue
            if i != 0:
                j += 1
            if list[j] == 0:
                self.canvas.create_rectangle(self.X[i], self.Y[self.round * 2], self.X[i + 1], self.Y[self.round * 2 + 1], fill=self.returnrgb(64, 64, 64))
                tk.Label(bg = self.returnrgb(64, 64, 64), fg='white', width=1, font=('Calibri', 24),  text = self.letters[j]).place(x = self.X[i] + 13, y = self.Y[self.round * 2 + 1] - 47)
            elif list[j] == 1:
                self.canvas.create_rectangle(self.X[i], self.Y[self.round * 2], self.X[i + 1], self.Y[self.round * 2 + 1], fill=self.returnrgb(211, 211, 50))
                tk.Label(bg = self.returnrgb(211, 211, 50), fg='white', width=1, font=('Calibri', 24), text = self.letters[j]).place(x = self.X[i] + 13, y = self.Y[self.round * 2 + 1] - 47)
            else:
                self.canvas.create_rectangle(self.X[i], self.Y[self.round * 2], self.X[i + 1], self.Y[self.round * 2 + 1], fill=self.returnrgb(9, 137, 50))
                tk.Label(bg = self.returnrgb(9, 137, 50), fg='white', width=1, font=('Calibri', 24), text = self.letters[j]).place(x = self.X[i] + 13, y = self.Y[self.round * 2 + 1] - 47)

        self.round += 1
        self.letters = []

        for i in list:
            x += i 
        if x == 10:
            self.win = True
            print('Win')
            return
        elif self.round == 5:
            print(f'Lose | {self.answer}')
            tk.messagebox.showinfo('Lose', 'You lose! The answer is ' + ''.join(self.answer))                            

    def returnrgb(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def gui(self):
        self.canvas.pack()
        RC = len(self.X)
        
        tk.Label(tk.Label(bg = self.returnrgb(64, 64, 64), font=('Arial', 18), text = 'Wördle').place(x = 102, y = 5))
        button = tk.Button(self.root, bg = self.returnrgb(64, 64, 64), borderwidth = 0, text = 'New game', command=lambda:self.reset())
        button.place(x = 218, y = 10)

        self.canvas.create_line(0, 38, 297, 38, width=1)

        for i in range(RC):
            if i % 2 == 1:
                continue
            for j in range(RC):
                if j % 2 == 1:
                    continue
                self.canvas.create_rectangle(self.X[i], self.Y[j], self.X[i + 1], self.Y[j + 1], fill=self.returnrgb(64, 64, 64))
                tk.Label(bg = self.returnrgb(64, 64, 64), fg='white', width=1, font=('Calibri', 24),  text = '').place(x = self.X[i] + 13, y = self.Y[j + 1] - 47)
                
    def reset(self):
        self.round = 0
        self.letters = []
        self.win = False
        self.answer = self.getanswer()
        self.gui()

    def getanswer(self):
        word = random.choice(ANSWERS)
        wordcut = list(word)
        print(wordcut)
        return wordcut                         

if __name__ == '__main__':
    g = Game()
    g.init()