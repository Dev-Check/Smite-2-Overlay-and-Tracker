import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

from sqlfunctions import get_enemy_winrate, get_matchup_kda


class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        
        #VALUES (CHANGE THESE)
        
        player_god = "Bellona"
        enemy_god = "Thor"
        role = "Solo"

        
        # GET DATA FROM DATABASE
        
        winrate_value = get_enemy_winrate(player_god, enemy_god, role)
        
        kda_value = get_matchup_kda(player_god, enemy_god)

        # DEBUG
        # print("DEBUG → Winrate:", winrate_value)
        # print("DEBUG → KDA:", kda_value)

        # WINDOW SETTINGS
        
        self.setWindowTitle("Smite Overlay")
        self.setGeometry(1500, 800, 420, 140)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(20)

        
        # LEFT (PLAYER GOD)
        
        left_layout = QVBoxLayout()

        left = QLabel(player_god)
        left.setStyleSheet("color: white; background: transparent; font-size: 14px; font-weight: bold;")
        left.setAlignment(Qt.AlignCenter)

        left_layout.addWidget(left)
        left_layout.setAlignment(Qt.AlignCenter)

        
        # CENTER (MATCHUP DATA)
        
        center_layout = QVBoxLayout()

        matchup = QLabel(f"{player_god} vs {enemy_god}")
        matchup.setStyleSheet("color: white; background: transparent; font-size: 14px; font-weight: bold;")

        role_label = QLabel(f"Role: {role}")
        role_label.setStyleSheet("color: rgba(255,255,255,0.6); background: transparent; font-size: 11px;")

        # Handle None values safely
        if winrate_value is not None:
            winrate = QLabel(f"Winrate: {winrate_value}%")
        else:
            winrate = QLabel("Winrate: N/A")

        if kda_value is not None:
            kda = QLabel(f"KDA: {kda_value}")
        else:
            kda = QLabel("KDA: N/A")

        for w in [matchup, role_label, winrate, kda]:
            w.setStyleSheet("color: white; background: transparent;")
            w.setAlignment(Qt.AlignCenter)
            center_layout.addWidget(w)

        center_layout.setAlignment(Qt.AlignCenter)

        
        # RIGHT (ENEMY GOD)
        
        right_layout = QVBoxLayout()

        right = QLabel(enemy_god)
        right.setStyleSheet("color: white; background: transparent; font-size: 14px; font-weight: bold;")
        right.setAlignment(Qt.AlignCenter)

        right_layout.addWidget(right)
        right_layout.setAlignment(Qt.AlignCenter)

        
        # ADD TO MAIN
        
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        
        # STYLE
        
        self.setStyleSheet("""
            background-color: rgba(18, 22, 40, 200);
            border-radius: 8px;
        """)



# RUN APP

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Overlay()
    window.show()
    sys.exit(app.exec_())