import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup, element
from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *
import time
import random
import re
from tkinter import messagebox

master = Tk()
window = Canvas(master, width=200, height=100)
master.title('Wikipedia quiz')

class titel_and_content:
    def __init__(self):
        self.linken = "https://en.wikipedia.org/wiki/Special:Random"
        self.linkhe = "https://he.wikipedia.org/wiki/%D7%9E%D7%99%D7%95%D7%97%D7%93:%D7%90%D7%A7%D7%A8%D7%90%D7%99"
        self.html = urllib.request.urlopen(self.linkhe)
        self.webfile = self.html.read().decode('utf-8')
        self.soup = BeautifulSoup(self.webfile , features="html.parser")
        self.soup.find_all("p")

    def titel(self):
        return (self.webfile[self.webfile.index('<title>') + 7: self.webfile.index('</title>')].replace(" – ויקיפדיה" , ""))

    def content(self):
        l = []
        for p in self.soup.find_all("p"):
            for a in p.contents:
                if isinstance(a , element.Tag):
                    a = a.next
                if isinstance(a , element.NavigableString):
                    l.append(str(a))
        return "".join(l)

def options():
    answers = [titel_and_content() for answer in range(0,4)]
    right_answer = random.choice(answers)
    titel_of_right_answer = right_answer.titel()
    content_of_right_answer = right_answer.content()
    return [[str(answer.titel()) for answer in answers], [titel_of_right_answer, content_of_right_answer]]

def press_play(textbutton, right_answer, button_pressd):
    global t0
    if button_pressd[0] == True:
        return
    t1 =time.time()
    delta = t1-t0
    button_pressd[0] = True
    if textbutton == right_answer:
        messagebox.showinfo("showinfo" , "True!\nscore:"+str(300-delta//0.1))
    else:
        messagebox.showinfo("showinfo" , "False!\nscore:0\nthe right answer:"+right_answer)

t0 = time.time()
button_pressd = [False]
def play(answers, right_answer, button_pressd):
    b = []
    for textbutton in answers:
        b.append(Button(window , text = str(textbutton) ,command = lambda textbutton=textbutton: press_play(textbutton, right_answer, button_pressd)))
        b[-1].grid(row = answers.index(textbutton)+1 , column = 1)
    label = Label(window , text="*", justify = RIGHT)
    label.grid(row=6, column=1)
    photo = PhotoImage(file=r"C:\Users\burstain\Documents\wikipedia_logo.png")
    image = Label(window , image=photo)
    image.image = photo
    t0 = time.time()
    image.grid(row=0, column=0)
    return label

def get_clues(content, right_answer, master, label):
    for word in right_answer.split(" "):
        content = content.replace(word, "---")
        content = content.replace("\n" , "")
        content = re.sub(r" ?\([^)]+\)" , "" , content)
        content = content.split()
        for num in range(len(content)//15):
            content[num*15] = content[num*15]+"\n"
        content = " ".join(content)
    stop = min(150, len(content))
    for num in range(stop):
        master.after(num*100 , boom , label, content[0:num])

def boom(label, clue):
    label['text'] = clue

def main(master):
    a = options()
    label = play(a[0] , a[1][0], button_pressd)
    get_clues(a[1][1] , a[1][0], master, label)

main(master)

window.pack()
mainloop()
