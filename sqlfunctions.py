import mysql.connector  

# SQL FUNCTIONS FOR GODS

def connect_db():
    conn = mysql.connector.connect(

        host="127.0.0.1",     # or "localhost"
        port=3306,            # integer port
        user="root",
        password="",
        database="smite_stats"
    )
    return conn

def get_winrate(god_name):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) AS games, SUM(win) as wins
    FROM matches
    WHERE player_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    """

    cursor.execute(query,(god_name,))
    games, wins = cursor.fetchone()
    conn.close()

    winrate = (wins / games) * 100
    # return winrate
    print(god_name, "Winrate:", round(winrate, 2), "%")

print("Testing Get God winrate")
get_winrate("Bellona")
print("\n")


def get_enemy_winrate(god_name,enemy_god,role):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) AS games, SUM(win) as wins
    FROM matches
    WHERE player_god_id = (
        SELECT id FROM gods WHERE name = %s
  
    )
    AND enemy_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    AND match_role = %s
    """

    cursor.execute(query,(god_name,enemy_god,role))
    games, wins = cursor.fetchone()

    conn.close()
     

    if games == 0:
        return f"No games found for {god_name} vs {enemy_god} in {role}"

    winrate = (wins / games) * 100
    # return winrate
    print(god_name, "VS",enemy_god,"In",role,"\nWinrate:", round(winrate, 2), "%")

print("Testing Get enenmy winrate")
get_enemy_winrate("Bellona","Amaterasu","Solo")
print("\n")

def get_kda(god_name):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT AVG((kills + assists/2) / NULLIF(deaths,0))
    FROM matches
    WHERE player_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    """

    cursor.execute(query, (god_name,))
    result = cursor.fetchone()

    conn.close()

    kda = result[0]
    # return kda
    print(god_name,"KDA:",round(kda, 2) if kda else 0)
    

print("Testing KDA for God")
get_kda("Bellona")
print("\n")

def get_most_played_gods():
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT g.name, COUNT(*) AS games
    FROM matches m
    JOIN gods g ON m.player_god_id = g.id
    GROUP BY g.name
    ORDER BY games DESC
    """

    cursor.execute(query)
    results = cursor.fetchmany(5) 
    # IF YOU WANT ALL GODS CHANGE TO .fetchall

    conn.close()
    print("Most Played Gods:")
    for god, games in results:
        print(god, "-", games, "games")

print("Testing Get most played gods (top 5) ")
get_most_played_gods()
print("\n")

def get_avg_game_time(god_name, role=None):
    conn = connect_db()
    cursor = conn.cursor()

    if role:
        query = """
        SELECT AVG(TIME_TO_SEC(game_time))
        FROM matches
        WHERE player_god_id = (
            SELECT id FROM gods WHERE name = %s
        )
        AND match_role = %s
        """
        cursor.execute(query, (god_name, role))
    else:
        query = """
        SELECT AVG(TIME_TO_SEC(game_time))
        FROM matches
        WHERE player_god_id = (
            SELECT id FROM gods WHERE name = %s
        )
        """
        cursor.execute(query, (god_name,))

    result = cursor.fetchone()
    conn.close()

    seconds = result[0]

    if seconds:
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        print(god_name, "Average Game Time:", f"{minutes}:{seconds:02d}")
    else:
        print("No data found")

print("Testing Avg Game Time")
get_avg_game_time("Bellona")
print("Testing Average time in a specific role")
get_avg_game_time("Bellona", "Solo")
print("\n")



def get_best_matchups(god_name, min_games=2):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT g.name, COUNT(*) AS games,
           SUM(win)/COUNT(*) * 100 AS winrate
    FROM matches m
    JOIN gods g ON m.enemy_god_id = g.id
    WHERE m.player_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    GROUP BY g.name
    HAVING games >= %s
    ORDER BY winrate DESC
    LIMIT 5
    """

    cursor.execute(query, (god_name, min_games))
    results = cursor.fetchall()

    conn.close()

    print("Best Matchups for", god_name)
    for enemy, games, winrate in results:
        print(enemy, "-", games, "games -", round(winrate, 2), "%")
    
print("Testing best matchups")
get_best_matchups("Bellona")
print("\n")


def get_worst_matchups(god_name, min_games=2):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT g.name, COUNT(*) AS games,
           SUM(win)/COUNT(*) * 100 AS winrate
    FROM matches m
    JOIN gods g ON m.enemy_god_id = g.id
    WHERE m.player_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    GROUP BY g.name
    HAVING games >= %s
    ORDER BY winrate ASC
    LIMIT 5
    """

    cursor.execute(query, (god_name, min_games))
    results = cursor.fetchall()

    conn.close()

    print("Worst Matchups for", god_name)
    for enemy, games, winrate in results:
        print(enemy, "-", games, "games -", round(winrate, 2), "%")

print("Testing worst matchups")
get_worst_matchups("Bellona")
print("\n")


def get_matchup_kda(player_god, enemy_god):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT AVG((kills + assists/2) / NULLIF(deaths,0))
    FROM matches
    WHERE player_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    AND enemy_god_id = (
        SELECT id FROM gods WHERE name = %s
    )
    """

    cursor.execute(query, (player_god, enemy_god))
    result = cursor.fetchone()

    conn.close()

    kda = result[0]

    if kda:
        print(player_god, "vs", enemy_god, "KDA:", round(kda, 2))
    else:
        print("No data found")

print("KDA for one enemy God")
get_matchup_kda("Bellona","Amaterasu")