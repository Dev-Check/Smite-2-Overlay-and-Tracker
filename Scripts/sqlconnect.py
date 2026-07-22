import mysql.connector

conn = mysql.connector.connect(

        host="127.0.0.1",     # or "localhost"
        port=3306,            # integer port
        user="root",
        password="PASSWORD HERE",
        database="smite_stats"
)

cursor = conn.cursor()

query = """
SELECT 
    COUNT(*) AS games,
    SUM(win) AS wins
FROM matches
WHERE player_god_id = (
    SELECT id FROM gods WHERE name = 'Bellona'
)
"""

cursor.execute(query)

games, wins = cursor.fetchone()

print("Games:", games)
print("Wins:", wins)
print("Winrate:", round((wins / games) * 100, 2), "%")