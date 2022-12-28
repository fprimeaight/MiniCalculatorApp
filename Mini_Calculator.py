import tkinter

class CalculatorApp:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("280x420")
        self.window.title("Calculator")
        self.window.resizable(0,0)
        
        self.expr_txt = ''
        self.expr_label = tkinter.StringVar()
        self.padding = 5

        # Initialise calculator buttons
        self.create_widgets()

    def click_button(self,char):
        self.expr_txt += str(char)
        self.expr_label.set(self.expr_txt)

    def solve(self):
        # Converts string into a suitable form first
        self.expr_txt = self.expr_txt.replace('%','/100')

        try:
            ans = str(round(eval(self.expr_txt),6))
            self.expr_label.set(ans)
            self.expr_txt = ''
        except:
            self.expr_txt = ''
            self.expr_label.set('Error')

    def backspace(self):
        self.expr_txt = self.expr_txt[:-1]
        self.expr_label.set(self.expr_txt)
    
    def clear(self):
        self.expr_txt = ''
        self.expr_label.set('')
    
    def create_widgets(self):
        label = tkinter.Label(master=self.window,
                            textvariable=self.expr_label,
                            font=('Calibri',24,'bold'),

                            borderwidth=10, 
                            relief="ridge",
                            width=13,
                            height=2)
        label.pack()

        frame = tkinter.Frame(master=self.window)
        frame.pack()

        button1 = tkinter.Button(master=frame,
                                text="1",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(1)).grid(row=1,column=0,padx=self.padding,pady=self.padding)

        button2 = tkinter.Button(master=frame,
                                text="2",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(2)).grid(row=1,column=1,padx=self.padding,pady=self.padding)

        button3 = tkinter.Button(master=frame,
                                text="3",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(3)).grid(row=1,column=2,padx=self.padding,pady=self.padding)

        button4 = tkinter.Button(master=frame,
                                text="4",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(4)).grid(row=2,column=0,padx=self.padding,pady=self.padding)
        
        button5 = tkinter.Button(master=frame,
                                text="5",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(5)).grid(row=2,column=1,padx=self.padding,pady=self.padding)

        button6 = tkinter.Button(master=frame,
                                text="6",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(6)).grid(row=2,column=2,padx=self.padding,pady=self.padding)
        
        button7 = tkinter.Button(master=frame,
                                text="7",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(7)).grid(row=3,column=0,padx=self.padding,pady=self.padding)
        
        button8 = tkinter.Button(master=frame,
                                text="8",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(8)).grid(row=3,column=1,padx=self.padding,pady=self.padding)

        button9 = tkinter.Button(master=frame,
                                text="9",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(9)).grid(row=3,column=2,padx=self.padding,pady=self.padding)

        button0 = tkinter.Button(master=frame,
                                text="0",
                                width=5,
                                height=2,
                                bg='white',
                                font=('Calibri',12,'bold'),
                                activebackground='white',
                                command=lambda:self.click_button(0)).grid(row=4,column=0,padx=self.padding,pady=self.padding)

        button_decimal = tkinter.Button(master=frame,
                                        text=".",
                                        width=5,
                                        height=2,
                                        bg='white',
                                        font=('Calibri',12,'bold'),
                                        activebackground='white',
                                        command=lambda:self.click_button('.')).grid(row=4,column=1,padx=self.padding,pady=self.padding)
        
        button_equal = tkinter.Button(master=frame,
                                    text="=",
                                    width=5,
                                    height=2,
                                    bg='#4285f4',
                                    fg='white',
                                    font=('Calibri',12,'bold'),
                                    activebackground='#4285f4',
                                    activeforeground='white',
                                    command=self.solve).grid(row=4,column=2,padx=self.padding,pady=self.padding)
        
        button_plus = tkinter.Button(master=frame,
                                    text="+",
                                    width=5,
                                    height=2,
                                    bg='white',
                                    font=('Calibri',12,'bold'),
                                    activebackground='white',
                                    command=lambda:self.click_button('+')).grid(row=1,column=3,padx=self.padding,pady=self.padding)

        button_minus = tkinter.Button(master=frame,
                                    text="-",
                                    width=5,
                                    height=2,
                                    bg='white',
                                    font=('Calibri',12,'bold'),
                                    activebackground='white',
                                    command=lambda:self.click_button('-')).grid(row=2,column=3,padx=self.padding,pady=self.padding)
        
        button_multiply = tkinter.Button(master=frame,
                                        text="*",
                                        width=5,
                                        height=2,
                                        bg='white',
                                        font=('Calibri',12,'bold'),
                                        activebackground='white',
                                        command=lambda:self.click_button('*')).grid(row=3,column=3,padx=self.padding,pady=self.padding)

        button_division = tkinter.Button(master=frame,
                                        text="/",
                                        width=5,
                                        height=2,
                                        bg='white',
                                        font=('Calibri',12,'bold'),
                                        activebackground='white',
                                        command=lambda:self.click_button('/')).grid(row=4,column=3,padx=self.padding,pady=self.padding)

        button_clear = tkinter.Button(master=frame,
                                    text="AC",
                                    width=5,
                                    height=2,
                                    bg='#ee5663',
                                    fg='white',
                                    font=('Calibri',12,'bold'),
                                    activebackground='#ee5663',
                                    activeforeground='white',
                                    command=self.clear).grid(row=0,column=0,padx=self.padding,pady=self.padding)

        button_backspace = tkinter.Button(master=frame,
                                        text="Del",
                                        width=5,
                                        height=2,
                                        bg='#ee5663',
                                        fg='white',
                                        font=('Calibri',12,'bold'),
                                        activebackground='#ee5663',
                                        activeforeground='white',
                                        command=self.backspace).grid(row=0,column=1,padx=self.padding,pady=self.padding)

        button_percentage = tkinter.Button(master=frame,
                                        text="%",
                                        width=5,
                                        height=2,
                                        bg='white',
                                        font=('Calibri',12,'bold'),
                                        activebackground='white',
                                        command=lambda:self.click_button('%')).grid(row=0,column=2,padx=self.padding,pady=self.padding)

        button_exponent = tkinter.Button(master=frame,
                                        text="aᵇ",
                                        width=5,
                                        height=2,
                                        bg='white',
                                        font=('Calibri',12,'bold'),
                                        activebackground='white',
                                        command=lambda:self.click_button('**')).grid(row=0,column=3,padx=self.padding,pady=self.padding)
    
def main():
    calc = CalculatorApp()
    calc.window.mainloop()

if __name__ == '__main__':
    main()