from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(100 , 100)

quest = QLabel("В якому році помер Андрій Кузьменко?")
quest1 = QLabel("Та?")


ans1 = QRadioButton("2005")
ans2 = QRadioButton("2010")
ans3 = QRadioButton("2015")
ans4 = QRadioButton("2020")

dfg1 = QRadioButton("mama")
dfg2 = QRadioButton("tato")
dfg3 = QRadioButton("سلام")
dfg4 = QRadioButton("Автор сам не знає")

mainLine = QVBoxLayout()
mainLine.addWidget(quest)


h1 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)
mainLine.addLayout(h1)
h2 = QHBoxLayout()
h2.addWidget(ans3)
h2.addWidget(ans4)
mainLine.addLayout(h2)

mainLine.addWidget(quest1)
l1 = QHBoxLayout()
l1.addWidget(dfg1)
l1.addWidget(dfg2)
mainLine.addLayout(l1)
l2 = QHBoxLayout()
l2.addWidget(dfg3)
l2.addWidget(dfg4)


mainLine.addWidget(quest1)
def a():
    b = QMessageBox()
    b.setText('Вірно!\n Порошенко вбив Андрійчика')
    b.exec_()
def q():
    s = QMessageBox()
    s.setText('НЕПРАВИЛЬНО!\n Введи правильну відповідь')
    s.exec_()


def t():
    k = QMessageBox()
    k.setText('Вірно!\n نا أيضاً أذهب إلى المدرسة')
    k.exec_()
def p():
    j = QMessageBox()
    j.setText('НЕПРАВИЛЬНО!\n adolf Gitler')
    j.exec_()


ans3.clicked.connect(a)
ans1.clicked.connect(q)
ans2.clicked.connect(q)
ans4.clicked.connect(q)

dfg3.clicked.connect(t)
dfg1.clicked.connect(p)
dfg2.clicked.connect(p)
dfg4.clicked.connect(p)

window.setLayout((mainLine))
window.show()

app.exec()
