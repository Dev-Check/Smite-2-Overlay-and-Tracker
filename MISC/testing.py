import csv
from datetime import datetime
import mysql.connector

conn = mysql.connector.connect(
        host="127.0.0.1",     # or "localhost"
        port=3306,            # integer port
        user="root",
        password="password",
        database="smite_stats",
        autocommit=False
    )
cur = conn.cursor()

# --- Path to your CSV ---
csv_path = r"C:/Users/dej72/Desktop/smitetracker/cleaned.csv"

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # --- Convert Date to MySQL format ---
        try:
            match_date = datetime.strptime(row['Date'], "%m/%d/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            print(f"Skipping row due to date error: {row['Date']}")
            continue
        
        # --- Convert Duration to HH:MM:SS ---
        try:
            parts = row['Duration'].split(":")
            while len(parts) < 3:
                parts.insert(0, "0")  # pad with 0 hours if missing
            h, m, s = parts
            game_time = f"{int(h):02}:{int(m):02}:{int(s):02}"
        except Exception as e:
            print(f"Skipping row due to duration error: {row['Duration']}")
            continue
        
        # --- Convert Win/Lose to 1/0 ---
        win = 1 if row['Result'].strip().lower() == "win" else 0
        
        # --- Insert into MySQL ---
        cur.execute("""
            INSERT INTO raw_matches
            (match_date, gamemode, match_role, god, enemy_god, kills, deaths, assists, game_time, win)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            match_date,
            row['Mode'].strip(),
            row['Role'].strip(),
            row['God'].strip(),
            row['Enemy'].strip(),
            int(row['K']),
            int(row['D']),
            int(row['A']),
            game_time,
            win
        ))

# --- Commit and close ---
conn.commit()
cur.close()
conn.close()

print("CSV successfully imported into raw_matches!")