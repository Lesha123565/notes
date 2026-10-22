from PyQt6.QtWidgets import QMainWindow,QFrame , QScrollArea, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton
from PyQt6.QtCore import Qt
from modules.app import app 


main_window = QMainWindow()

WIDTH_WINDOW = 800
HEIGHT_WINDOW  = 600

# получаем обьект экрана
primary_screen = app.primaryScreen()
# получаем размеры экрана
screen_size = primary_screen.size()
# получаем ширину экрана
width_screen = screen_size.width()
# получаем высоту экрана
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)




main_frame = QFrame(parent = main_window)
main_frame.setStyleSheet("background-color: #1f242e")
main_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)

main_layout = QHBoxLayout()
main_frame.setLayout(main_layout)


frame_1 = QFrame(parent = main_frame)
frame_1.setStyleSheet("background-color: #313d4f; border-radius: 15px")
frame_1.setFixedSize(280, 550)
layout_1 = QHBoxLayout()
frame_1.setLayout(layout_1)



frame_2 = QFrame(parent = main_frame)
frame_2.setStyleSheet("background-color: #313d4f; border-radius: 15px")
frame_2.setFixedSize(460, 550)
layout_2 = QHBoxLayout()
frame_2.setLayout(layout_2)


notes_name = QLineEdit(parent= frame_1)
notes_name.setStyleSheet("background-color: white; border-radius: 15px; color: black")
notes_name.setFixedSize(160, 30)
notes_name.setPlaceholderText("Назва нотатки")





notes_list = QComboBox(parent = frame_1)
notes_list.setStyleSheet("background-color: white; border-radius: 15px; color: black")
notes_list.setFixedSize(70, 30)
notes_list.addItems(["Робота","Особисте", "Ідеї", "Навчання"])



def select_note(text):
    print(f"обрана категорія:{text}")
    

notes_list.currentTextChanged.connect(select_note)




note_text = QTextEdit(parent= frame_2)
note_text.setStyleSheet("background-color: white; border-radius: 15px; color: black")
note_text.setFixedSize(220, 510)
note_text.setPlaceholderText("Опис нотатки")
# note = []

# def print_notes():
#     print(notes.toPlainText())
# notes.textChanged.connect(print_notes)


    

add_note = QPushButton(parent = frame_2, text = "Створити нотатку")
add_note.setStyleSheet("background-color: green; border-radius: 10px")
add_note.setFixedSize(120, 30)


def adding_note():
    print("  Нова нотатка створена!")
    print(f"Назва: {notes_name.text()}")
    print(f"Категорія: {notes_list.currentText()}")
    print(f"Текст: {note_text.toPlainText()}")
    #notes_name.text()
    # notes_list.addItem(name)
    
    
    
    
add_note.clicked.connect(adding_note)


clear_button = QPushButton(parent = frame_2, text = "очистити")
clear_button.setStyleSheet("background-color: red; border-radius: 10px")
clear_button.setFixedSize(90, 30)

def clear():
    notes_name.clear()
    note_text.clear()


clear_button.clicked.connect(clear)




main_layout.addWidget(frame_1)
main_layout.addWidget(frame_2)
layout_1.addWidget(notes_name)
layout_1.addWidget(notes_list)
layout_2.addWidget(note_text)
layout_2.addWidget(add_note)
layout_2.addWidget(clear_button)




