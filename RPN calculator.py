import tkinter as tk

class GUI:
    def __init__(self):
        inputs=["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "AC", "0", "ENTR", "/"]
        self.numberStack=[]
        self.answerStack=[]
        self.screen=[]
        self.fill=False
        self.root=tk.Tk()
        self.numberFrame=tk.Frame(self.root, bg="black")
        self.numberFrame.config(height=30, width=150)
        self.numberFrame.grid(row=0, column=0)

        self.keyPad=tk.Frame(self.root, bg="black")
        self.keyPad.grid(row=1, column=0)
        
        self.numberFrame.grid_propagate(False)
        self.stack=tk.Frame(self.root, bg="black")
        self.stack.config(pady=30, padx=5)
        self.stack.grid(row=1, column=4)
        self.stack2=tk.Frame(self.root, bg="black")
        self.stack2.config(pady=30, padx=5)
        self.stack2.grid(row=1, column=5)
        self.stackLabel=tk.Label(self.stack, bg="black", fg="white")
        self.stackLabel.grid(row=0, column=0)
        self.answerLabel=tk.Label(self.stack2, bg="black", fg="orange")
        self.answerLabel.grid(row=0, column=0)
        self.numberLabel=tk.Label(self.numberFrame)
        self.numberLabel.grid(row=0, column=0)
        myColumn=0
        myRow=0
        for i in inputs:
            if i =="AC":
                self.clearButton=tk.Button(self.keyPad, text=i, command=self.clear, bg="cyan", fg="black")
                self.clearButton.config(width=4, height=2)
                self.clearButton.grid(row=myRow, column=myColumn)
            else:
                self.inputButton=tk.Button(self.keyPad, text=i, bg="blue", fg="white")
                self.inputButton.config(width=4, height=2)
                self.inputButton.grid(row=myRow, column=myColumn)
                self.inputButton.bind("<Button-1>", self.buttonClicked)
            myColumn += 1
            if i == "+":
                myRow+=1
                myColumn=0
                self.inputButton.config(bg="cyan", fg="black")
            elif i=="-":
                myRow+=1
                myColumn=0
                self.inputButton.config(bg="cyan", fg="black")
            elif i=="*" or i=="/":
                myRow+=1
                myColumn=0
                self.inputButton.config(bg="cyan", fg="black")
            elif i=="ENTR":
                self.inputButton.config(bg="cyan", fg="black")
            else:
                pass
            

    def buttonClicked(self, event):
        self.clicked=event.widget.cget("text")
        
        if self.clicked=="-" or self.clicked=="+" or self.clicked=="/" or self.clicked=="*":
            place=len(self.numberStack)
            if place < 2:
                self.fill=True
                self.numberLabel.config(text="Error", fg="white", bg="black")
                self.clearButton.config(text="CLR")
                self.screen=[]
            else:
                number1=self.numberStack[place-1]
                number2=self.numberStack[place-2]
                self.numberStack.pop()
                self.numberStack.pop()
                value="({1}{2}{0})".format(number1, number2, self.clicked)
                self.numberStack.append(value)
                self.text=""""""
                value=len(self.numberStack)
                for i in self.numberStack:
                    value-=1
                    stackNumber=self.numberStack[value]
                    self.text += "\n{0}".format(stackNumber)
                self.stackLabel.config(text=self.text)

                number1=self.answerStack[place-1]
                number2=self.answerStack[place-2]
                self.answerStack.pop()
                self.answerStack.pop()
                if self.clicked=="+":
                    value=number2+number1
                elif self.clicked=="-":
                    value=number2-number1
                elif self.clicked=="/":
                    value=number2/number1
                else:
                    value=number2*number1
                self.answerStack.append(value)
                self.text=""""""
                value=len(self.answerStack)
                for i in self.answerStack:
                    value-=1
                    stackNumber=self.answerStack[value]
                    self.text += "\n{0}".format(stackNumber)
                self.answerLabel.config(text=self.text, fg="orange", bg="black")
                
        elif self.clicked=="ENTR":
            if self.fill==False:
                self.clearButton.config(text="AC")
                self.screen=[]
                self.number=""
                self.numberLabel.config(text=self.number, fg="white", bg="black")
            else:
                self.clearButton.config(text="AC")
                self.fill=False
                self.numberStack.append(self.number)
                self.text=""""""
                value=len(self.numberStack)
                for i in self.numberStack:
                    value-=1
                    stackNumber=self.numberStack[value]
                    self.text += "\n{0}".format(stackNumber)
                self.stackLabel.config(text=self.text)

                self.answerStack.append(self.number)
                self.text=""""""
                value=len(self.answerStack)
                for i in self.answerStack:
                    value-=1
                    stackNumber=self.answerStack[value]
                    self.text += "\n{0}".format(stackNumber)
                self.answerLabel.config(text=self.text, fg="orange", bg="black")
                self.screen=[]
                self.number=""
                self.numberLabel.config(text=self.number, fg="white", bg="black")
            
        else:
            self.fill=True
            self.clearButton.config(text="CLR")
            self.screen.append(self.clicked)
            string=""
            for i in self.screen:
                string+=str(i)
            self.number=int(string)
            self.numberLabel.config(text=self.number, fg="white", bg="black")

    def clear(self):
        if self.fill==True:
            self.clearButton.config(text="AC")
            self.fill=False
            self.screen=[]
            self.number=""
            self.numberLabel.config(text=self.number, fg="white", bg="black")
        else:
            self.clearButton.config(text="AC")
            self.answerStack=[]
            self.numberStack=[]
            self.text=""""""
            self.answerLabel.config(text=self.text, fg="orange", bg="black")
            self.stackLabel.config(text=self.text, fg="white", bg="black")

            

GUI()
