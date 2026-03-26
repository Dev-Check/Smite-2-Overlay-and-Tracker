import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smite Overlay")
        self.setGeometry(1500, 800, 400, 140)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(20)

        # --- LEFT (Player God) ---
        left_layout = QVBoxLayout()
        left = QLabel("Bellona")
        left.setStyleSheet("color: white; font-size: 14px; font-weight: bold;")
        left.setAlignment(Qt.AlignCenter)

        left_layout.addWidget(left)
        left_layout.setAlignment(Qt.AlignCenter)

        # --- CENTER (Matchup Info) ---
        center_layout = QVBoxLayout()

        matchup = QLabel("Bellona vs Thor")
        matchup.setStyleSheet("color: white; font-size: 14px; font-weight: bold;")

        role = QLabel("Role: Solo")
        role.setStyleSheet("color: rgba(255,255,255,0.6); font-size: 11px;")

        winrate = QLabel("Winrate: 75%")
        winrate.setStyleSheet("color: white;")

        kda = QLabel("KDA: 2.83")
        kda.setStyleSheet("color: white;")

        for w in [matchup, role, winrate, kda]:
            w.setAlignment(Qt.AlignCenter)
            center_layout.addWidget(w)

        center_layout.setAlignment(Qt.AlignCenter)

        # --- RIGHT (Enemy God) ---
        right_layout = QVBoxLayout()
        right = QLabel("Thor")
        right.setStyleSheet("color: white; font-size: 14px; font-weight: bold;")
        right.setAlignment(Qt.AlignCenter)

        right_layout.addWidget(right)
        right_layout.setAlignment(Qt.AlignCenter)

        # --- ADD TO MAIN ---
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        # Background styling
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 200);
            border-radius: 8px;
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Overlay()
    window.show()
    sys.exit(app.exec_())