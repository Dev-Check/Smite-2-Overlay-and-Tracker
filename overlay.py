import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QFormLayout, QComboBox
)
from PyQt5.QtCore import Qt

from sqlfunctions import get_enemy_winrate, get_matchup_kda, insert_match, get_all_gods


# -------------------------
# ADD MATCH WINDOW
# -------------------------
class AddMatchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Match")
        self.setGeometry(600, 400, 300, 400)

        layout = QFormLayout()

        self.date = QLineEdit()
        self.role = QComboBox()
        self.role.addItems(["Solo", "Jungle", "Mid", "ADC", "Support"])
        self.player = QComboBox()
        self.enemy = QComboBox()
        gods = get_all_gods()
        self.player.addItems(gods)
        self.enemy.addItems(gods)
        self.kills = QLineEdit()
        self.deaths = QLineEdit()
        self.assists = QLineEdit()
        self.time = QLineEdit()
        self.win = QLineEdit()

        layout.addRow("Date (YYYY-MM-DD):", self.date)
        layout.addRow("Role:", self.role)
        layout.addRow("Player God:", self.player)
        layout.addRow("Enemy God:", self.enemy)
        layout.addRow("Kills:", self.kills)
        layout.addRow("Deaths:", self.deaths)
        layout.addRow("Assists:", self.assists)
        layout.addRow("Game Time (HH:MM:SS):", self.time)
        layout.addRow("Win (1 or 0):", self.win)

        submit = QPushButton("Submit")
        submit.clicked.connect(self.submit_data)

        layout.addWidget(submit)
        self.setLayout(layout)

    def submit_data(self):
        

        success = insert_match(
            self.date.text(),
            "Conquest",
            self.role.text(),
            self.player.currentText(),
            self.enemy.currentText(),
            int(self.kills.text()),
            int(self.deaths.text()),
            int(self.assists.text()),
            self.time.text(),
            int(self.win.text())
        )

        if success:
            print("Match Added!")
            self.close()
        else:
            print("Insert Failed")

# -------------------------
# MAIN OVERLAY
# -------------------------
class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        # LOAD GODS
        gods = get_all_gods()

        # DROPDOWNS
        self.player_dropdown = QComboBox()
        self.enemy_dropdown = QComboBox()
        self.role_dropdown = QComboBox()

        self.player_dropdown.addItems(gods)
        self.enemy_dropdown.addItems(gods)
        self.role_dropdown.addItems(["Solo", "Jungle", "Mid", "ADC", "Support"])

        # WINDOW
        self.setWindowTitle("Smite Overlay")
        self.setGeometry(1500, 800, 420, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        main_layout = QVBoxLayout()
        content_layout = QHBoxLayout()

        # LEFT (PLAYER DROPDOWN)
        left_layout = QVBoxLayout()
        self.player_dropdown.setStyleSheet("color: white; background: transparent;")
        left_layout.addWidget(self.player_dropdown)
        left_layout.setAlignment(Qt.AlignCenter)

        # RIGHT (ENEMY DROPDOWN)
        right_layout = QVBoxLayout()
        self.enemy_dropdown.setStyleSheet("color: white; background: transparent;")
        right_layout.addWidget(self.enemy_dropdown)
        right_layout.setAlignment(Qt.AlignCenter)

        # CENTER
        center_layout = QVBoxLayout()

        self.matchup_label = QLabel("")
        self.role_label = QLabel("")
        self.winrate_label = QLabel("")
        self.kda_label = QLabel("")

        for w in [self.matchup_label, self.role_label, self.winrate_label, self.kda_label]:
            w.setStyleSheet("color: white; background: transparent;")
            w.setAlignment(Qt.AlignCenter)
            center_layout.addWidget(w)

        # ADD ROLE DROPDOWN AT TOP
        center_layout.insertWidget(0, self.role_dropdown)

        # ADD CONTENT
        content_layout.addLayout(left_layout)
        content_layout.addLayout(center_layout)
        content_layout.addLayout(right_layout)

        # BUTTON
        add_button = QPushButton("Add Match")
        add_button.clicked.connect(self.open_add_screen)
        add_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: rgba(59, 130, 246, 150);
                border: none;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgba(59, 130, 246, 200);
            }
        """)

        # FINAL LAYOUT
        main_layout.addLayout(content_layout)
        main_layout.addWidget(add_button)

        self.setLayout(main_layout)

        # STYLE
        self.setStyleSheet("""
            background-color: rgba(18, 22, 40, 200);
            border-radius: 8px;
        """)

        # CONNECT EVENTS
        self.player_dropdown.currentIndexChanged.connect(self.update_stats)
        self.enemy_dropdown.currentIndexChanged.connect(self.update_stats)
        self.role_dropdown.currentIndexChanged.connect(self.update_stats)

        # INITIAL LOAD
        self.update_stats()

    def update_stats(self):
        player = self.player_dropdown.currentText()
        enemy = self.enemy_dropdown.currentText()
        role = self.role_dropdown.currentText()

        winrate = get_enemy_winrate(player, enemy, role)
        kda = get_matchup_kda(player, enemy)

        self.matchup_label.setText(f"{player} vs {enemy}")
        self.role_label.setText(f"Role: {role}")

        if winrate is not None:
            self.winrate_label.setText(f"Winrate: {winrate}%")
        else:
            self.winrate_label.setText("Winrate: N/A")

        if kda is not None:
            self.kda_label.setText(f"KDA: {kda}")
        else:
            self.kda_label.setText("KDA: N/A")

    def open_add_screen(self):
        self.add_window = AddMatchWindow()
        self.add_window.show()


# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Overlay()
    window.show()
    sys.exit(app.exec_())