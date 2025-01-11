from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from chinese_checkers_board import ChineseCheckersBoard

class GameWindow(QWidget):
    def __init__(self, lobby_name, switch_to_lobbies):
        super().__init__()
        self.lobby_name = lobby_name
        self.switch_to_lobbies = switch_to_lobbies
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        header = QHBoxLayout()
        lbl_lobby = QLabel(f"Lobby: {self.lobby_name}")
        lbl_lobby.setStyleSheet("font-size: 18px;")
        header.addWidget(lbl_lobby)

        header.addStretch()

        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.switch_to_lobbies)
        header.addWidget(btn_exit)

        layout.addLayout(header)

        self.board = ChineseCheckersBoard()
        layout.addWidget(self.board)

        self.setLayout(layout)
