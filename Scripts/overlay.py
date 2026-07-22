import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QFormLayout, QComboBox
)
from PyQt5.QtCore import Qt

from sqlfunctions import (
    get_enemy_winrate,
    get_matchup_kda,
    insert_match,
    get_all_gods,
    get_best_matchups,
    get_worst_matchups
)

# -------------------------
# BEST/WORST MATCHUPS WINDOW
# -------------------------
class MatchupsWindow(QWidget):
    def __init__(self, player, role):
        super().__init__()

        self.setWindowTitle("Matchups")
        self.setGeometry(700, 400, 300, 350)

        layout = QVBoxLayout()

        title = QLabel(f"{player} ({role}) Matchups")
        title.setStyleSheet("color: white; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        best_title = QLabel("Best Matchups")
        best_title.setStyleSheet("color: lightgreen; font-weight: bold;")
        best_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(best_title)

        best = get_best_matchups(player, role)

        if best:
            for enemy, games, winrate in best:
                label = QLabel(f"{enemy} - {winrate}% ({games})")
                label.setStyleSheet("color: white;")
                label.setAlignment(Qt.AlignCenter)
                layout.addWidget(label)
        else:
            layout.addWidget(QLabel("No data"))

        worst_title = QLabel("Worst Matchups")
        worst_title.setStyleSheet("color: red; font-weight: bold;")
        worst_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(worst_title)

        worst = get_worst_matchups(player, role)

        if worst:
            for enemy, games, winrate in worst:
                label = QLabel(f"{enemy} - {winrate}% ({games})")
                label.setStyleSheet("color: white;")
                label.setAlignment(Qt.AlignCenter)
                layout.addWidget(label)
        else:
            layout.addWidget(QLabel("No data"))

        self.setLayout(layout)
        self.setStyleSheet("background-color: rgb(18,22,40);")


# -------------------------
# ADD MATCH WINDOW
# -------------------------
class AddMatchWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

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

        layout.addRow("Date:", self.date)
        layout.addRow("Role:", self.role)
        layout.addRow("Player:", self.player)
        layout.addRow("Enemy:", self.enemy)
        layout.addRow("Kills:", self.kills)
        layout.addRow("Deaths:", self.deaths)
        layout.addRow("Assists:", self.assists)
        layout.addRow("Time:", self.time)
        layout.addRow("Win:", self.win)

        submit = QPushButton("Submit")
        submit.clicked.connect(self.submit_data)

        layout.addWidget(submit)
        self.setLayout(layout)

    def submit_data(self):
        success = insert_match(
            self.date.text(),
            "Conquest",
            self.role.currentText(),
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
            if self.parent:
                self.parent.update_stats()
            self.close()


# -------------------------
# MAIN OVERLAY
# -------------------------
class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        gods = get_all_gods()

        self.player_dropdown = QComboBox()
        self.enemy_dropdown = QComboBox()
        self.role_dropdown = QComboBox()

        self.player_dropdown.addItems(gods)
        self.enemy_dropdown.addItems(gods)
        self.role_dropdown.addItems(["Solo", "Jungle", "Mid", "ADC", "Support"])

        dropdown_style = """
            QComboBox {
                color: white;
                background-color: rgba(30, 30, 50, 200);
                border: 1px solid white;
                padding: 3px;
                border-radius: 4px;
            }

            QComboBox QAbstractItemView {
                color: white;
                background-color: rgb(30, 30, 50);
                selection-background-color: rgb(59, 130, 246);
                selection-color: white;
            }
        """

        self.player_dropdown.setStyleSheet(dropdown_style)
        self.enemy_dropdown.setStyleSheet(dropdown_style)
        self.role_dropdown.setStyleSheet(dropdown_style)

        self.setWindowTitle("Smite Overlay")

        # -------------------------
        # LEFT SIDE + WIDE + SHORT
        # -------------------------
        screen = QApplication.primaryScreen().geometry()

        width = 320   # balanced width
        height = 140  # short but usable

        x = 20
        y = screen.height() - height - 200

        self.setGeometry(x, y, width, height)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        main_layout = QVBoxLayout()
        content_layout = QHBoxLayout()

        # LEFT
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.player_dropdown)

        # CENTER
        center_layout = QVBoxLayout()

        self.matchup_label = QLabel("")
        self.role_label = QLabel("")
        self.winrate_label = QLabel("")
        self.kda_label = QLabel("")

        for w in [self.matchup_label, self.role_label, self.winrate_label, self.kda_label]:
            w.setStyleSheet("color: white;")
            w.setAlignment(Qt.AlignCenter)
            center_layout.addWidget(w)

        center_layout.insertWidget(0, self.role_dropdown)

        # RIGHT
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.enemy_dropdown)

        content_layout.addLayout(left_layout)
        content_layout.addLayout(center_layout)
        content_layout.addLayout(right_layout)

        # BUTTONS
        add_button = QPushButton("Add Match")
        add_button.clicked.connect(self.open_add_screen)

        matchups_button = QPushButton("View Matchups")
        matchups_button.clicked.connect(self.open_matchups_screen)

        for btn in [add_button, matchups_button]:
            btn.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: rgba(59, 130, 246, 150);
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: rgba(59, 130, 246, 200);
                }
            """)

        main_layout.addLayout(content_layout)
        main_layout.addWidget(add_button)
        main_layout.addWidget(matchups_button)

        self.setLayout(main_layout)

        self.setStyleSheet("""
            background-color: rgba(18, 22, 40, 200);
            border-radius: 8px;
        """)

        self.player_dropdown.currentIndexChanged.connect(self.update_stats)
        self.enemy_dropdown.currentIndexChanged.connect(self.update_stats)
        self.role_dropdown.currentIndexChanged.connect(self.update_stats)

        self.update_stats()

    def update_stats(self):
        player = self.player_dropdown.currentText()
        enemy = self.enemy_dropdown.currentText()
        role = self.role_dropdown.currentText()

        winrate = get_enemy_winrate(player, enemy, role)
        kda = get_matchup_kda(player, enemy)

        self.matchup_label.setText(f"{player} vs {enemy}")
        self.role_label.setText(f"Role: {role}")
        self.winrate_label.setText(f"Winrate: {winrate}%" if winrate else "Winrate: N/A")
        self.kda_label.setText(f"KDA: {kda}" if kda else "KDA: N/A")

    def open_add_screen(self):
        self.add_window = AddMatchWindow(self)
        self.add_window.show()

    def open_matchups_screen(self):
        player = self.player_dropdown.currentText()
        role = self.role_dropdown.currentText()

        self.matchups_window = MatchupsWindow(player, role)
        self.matchups_window.show()


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Overlay()
    window.show()
    sys.exit(app.exec_())