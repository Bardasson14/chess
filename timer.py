import tkinter as tk
import datetime

class Countdown(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.createWidgets()
        self.showWidgets()
        self.secondsLeft = 600
        self.timerOn = False

    def showWidgets(self):

        self.label.pack()
        #self.entry.pack()
        self.start.pack()

    def createWidgets(self):

        self.label = tk.Label(self, text="00:10:00")
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()
        self.start = tk.Button(self, text="Start",
                               command=self.startButton)

    def countdown(self):
        '''Atualuza o label conforme o tempo restante.'''
        self.label['text'] = self.convertSecondsLeftToTime()

        if self.secondsLeft:
            self.secondsLeft -= 1
            self.timerOn = self.after(1000, self.countdown)
        else:
            self.timerOn = False

    def startButton(self):
        '''começa a contagem'''
        
        self.stopTimer()
        self.countdown()                            

    def stopTimer(self):
        '''Para ele após o tempo estipulado.'''
        if self.timerOn:
            self.afterCancel(self.timerOn)
            self.timerOn = False

    def convertSecondsLeftToTime(self):
        return datetime.timedelta(seconds=self.secondsLeft)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)

    countdown = Countdown(root)
    countdown.pack()

    root.mainloop()

