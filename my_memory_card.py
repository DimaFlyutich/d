#Connecting libraries
from random import shuffle 
from PyQt5.Core import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QtBoxLayout, QRadioButton

def show_question():
    RadioGroupBox.show()
    ansGroup..hide()
    button.setText('Ответить')
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn1)
    RadioGroup.addButton(rbtn2)
    RadioGroup.addButton(rbtn3)
    RadioGroup.addButton(rbtn4)
    RadioGroup.set(Exclusive(False))
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
def show_result():
    RadioGroupBox.hide()
    ansGroup.show()
    button.setText('Next question')
def start_test():
    if butto.text()
        show_result()
    else:
        show_question()



class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3
question_list = []
question_list.append(Question('Как звали меня в 2015 году когда я был в детском саде'))

app = QApplication([])
main = QWidget







