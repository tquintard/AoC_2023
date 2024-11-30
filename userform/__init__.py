from functools import partial
import timeit
import random
from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QFont, QColor
from PyQt6.QtCore import Qt
from time import time
from modules.solvepuzzle import solvepuzzle


AOC_COLOR = {'golden': QColor(255, 255, 0),
             'red': QColor(193, 39, 45),
             'amber': QColor(251, 176, 59),
             'green': QColor(60, 181, 86),
             'brightgreen': QColor(15, 250, 58),
             'blue': QColor(36, 112, 224),
             'white': QColor(255, 255, 255), }


class UserForm(QWidget):
    def __init__(self):
        super().__init__()

        # Remove title bar
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowType.FramelessWindowHint)
        # Update background aoc23 picture
        self.background = QPixmap("resources/pictures/aoc23.png")

        # Set a fixed size of the window
        self.setFixedSize(1200, 675)

        # -------------
        # Create a grid to pick day in calendar
        grid_widget = QWidget()  # Widget to hold the grid layout
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(5)  # Set the horizontal spacing
        grid_layout.setVerticalSpacing(5)  # Set the vertical spacing

        # Populate the grid with buttons containing numbers from 1 to 25
        for i in range(5):
            for j in range(5):
                number = i * 5 + j + 1  # Calculate the number
                # Create a button with the number as text
                button = QPushButton(str(number))
                button.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))
                color = AOC_COLOR[random.choice(list(AOC_COLOR.keys()))].name()
                button.setStyleSheet(
                    f"background-color: transparent; color: {color};text-align: right;")
                button.setContentsMargins(0, 0, 0, 0)
                button.setFixedSize(30, 25)  # Set the fixed size of the button
                # Connect button click event to function
                button.clicked.connect(self.on_button_clicked)
                # Add button to the grid
                grid_layout.addWidget(
                    button, i, j)
        grid_widget.setLayout(grid_layout)
        # -------------

        # -------------
        # Label for title of the day's puzzle
        self.title = QLabel('Part 1 solution', self)
        color = AOC_COLOR['brightgreen'].name()
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet(f"color: {color};")
        self.title.setFont(QFont('Source Code Pro', 36, QFont.Weight.Bold))
        self.title.setText('Pick a day in calendar')
        self.title.setFixedSize(self.title.sizeHint().width(),
                                grid_widget.sizeHint().height())

        # -------------

        # -------------
        # Close Button
        close_button = QPushButton(self)
        close_button.setStyleSheet("background-color: transparent;")
        close_button.setFixedSize(
            grid_widget.sizeHint().width()//2, grid_widget.sizeHint().height())
        close_button.clicked.connect(self.close)

        # -------------
        # Labels for Solutions
        label_sol1 = QLabel('Part 1', self)
        label_sol1.setStyleSheet("color: silver;")
        label_sol1.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))
        self.sol1 = QLineEdit(self)
        self.sol1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sol1.setStyleSheet(
            "background-color: transparent; color: silver; border: none;")
        self.sol1.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))

        label_sol2 = QLabel('Part 2', self)
        color = AOC_COLOR['golden'].name()
        label_sol2.setStyleSheet(f"color: {color};")
        label_sol2.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))
        self.sol2 = QLineEdit(self)
        self.sol2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sol2.setStyleSheet(
            f"background-color: transparent; color: {color}; border: none;")
        self.sol2.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))
        # -------------

        # -------------
        # Labels for Execution time
        label_exetime = QLabel('Execution time', self)
        color = AOC_COLOR['green'].name()
        label_exetime.setStyleSheet(f"color: {color};")
        label_exetime.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))
        self.exetime = QLabel(self)
        self.exetime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exetime.setStyleSheet(f"color: {color};")
        self.exetime.setFont(QFont('Source Code Pro', 18, QFont.Weight.Bold))
        # -------------

        # -------------
        # Main Vertical Layout
        vbox = QVBoxLayout()
        # -------------

        # -------------
        # Top Horizontal Layouts
        top_hbox = QHBoxLayout()
        # Add stretch between title and close button
        top_hbox.addStretch(1)
        # Add grid to layout
        top_hbox.addWidget(
            grid_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        # Add stretch between calendar and title
        top_hbox.addStretch(1)
        # Add title to layout
        top_hbox.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        # Add stretch between title and close button
        top_hbox.addStretch(1)
        top_hbox.addWidget(close_button)
        vbox.addLayout(top_hbox)
        # -------------

        # -------------
        # Add stretch between top and middle
        vbox.addStretch(1)
        # -------------

        # -------------
        # Bottom Horizontal Layouts
        bottom_hbox = QHBoxLayout()
        # Add 3 vertical layout inside bottom layout

        bvbox1 = QVBoxLayout()
        bvbox1.addWidget(label_sol1, alignment=Qt.AlignmentFlag.AlignCenter)
        bvbox1.addWidget(self.sol1, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_hbox.addLayout(bvbox1)

        bvbox2 = QVBoxLayout()
        bvbox2.addWidget(label_sol2, alignment=Qt.AlignmentFlag.AlignCenter)
        bvbox2.addWidget(self.sol2, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_hbox.addLayout(bvbox2)

        bvbox3 = QVBoxLayout()
        bvbox3.addWidget(label_exetime, alignment=Qt.AlignmentFlag.AlignCenter)
        bvbox3.addWidget(self.exetime, alignment=Qt.AlignmentFlag.AlignCenter)
        bottom_hbox.addLayout(bvbox3)
        vbox.addLayout(bottom_hbox)
        # -------------

        self.setLayout(vbox)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.background.scaled(self.size()))

    def update_labels(self, title, sol1='', sol2='', ela_time=''):
        self.title.setText(title)
        self.sol1.setText(str(sol1))
        self.sol2.setText(str(sol2))
        self.exetime.setText(ela_time)

    # Function to display button label in a message box when clicked

    def on_button_clicked(self):
        day = self.sender().text()  # Get the button's label that triggered the event
        try:
            start = time()
            title = f'Day {day}\n{DAY_TITLE[day]}'
            # Fetch input data
            sol = solvepuzzle(day)
            elapsed_time = (time() - start)*1000
            partial_function = partial(solvepuzzle, day=day)
            if 0 < elapsed_time < 100:
                nb_rep = int(min((200 // elapsed_time) - 1, 100))
                elapsed_time = f'{int(timeit.timeit(stmt=partial_function, number=nb_rep)*1000/nb_rep) + 1} ms'
            else:
                elapsed_time = f"{int(elapsed_time) + 1} ms"
            self.update_labels(title, *sol, elapsed_time)
        except KeyError:
            self.update_labels(f'Day {day}\nNot yet solved')


DAY_TITLE = {'1': 'Trebuchet?!',
             '2': 'Cube Conundrum',
             '3': 'Gear Ratios',
             '4': 'Scratchcards',
             '5': 'If You Give\nA Seed A Fertilizer',
             '6': 'Wait For It',
             '7': 'Camel Cards',
             '8': 'Haunted Wasteland',
             '9': 'Mirage Maintenance',
             '10': 'Pipe Maze',
             '11': 'Cosmic Expansion',
             '12x': 'Hot Springs',
             '13': 'Point of Incidence',
             '14': 'Parabolic\nReflector Dish',
             '15': 'Lens Library',
             '16': 'The Floor\nWill Be Lava',
             '17': 'Clumsy Crucible',
             '18': 'Lavaduct Lagoon',
             '19': 'Aplenty',
             '20': 'Pulse Propagation',
             '21x': 'Step Counter',
             '22': 'Sand Slabs',
             '23': 'A Long Walk',
             '24': 'Never Tell\nMe The Odds',
             '25': 'Snowverload',
             }
