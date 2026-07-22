import mysql.connector  

# SQL FUNCTIONS


def connect_db():
    conn = mysql.connector.connect(

        host="127.0.0.1",     # or "localhost"
        port=3306,            # integer port
        user="root",
        password="PASSWORD HERE",
        database="smite_stats"
    )
    return conn

def get_all_gods():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT name FROM gods ORDER BY name"
    cursor.execute(query)

    results = cursor.fetchall()
    conn.close()

    # Convert [('Bellona',), ('Thor',)] → ['Bellona', 'Thor']
    return [row[0] for row in results]

def insert_match(match_date, gamemode, role, player_god, enemy_god,
                 kills, deaths, assists, game_time, win):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO matches (
        match_date,
        gamemode,
        match_role,
        player_god_id,
        enemy_god_id,
        kills,
        deaths,
        assists,
        game_time,
        win
    )
    VALUES (
        %s,
        %s,
        %s,
        (SELECT id FROM gods WHERE name = %s),
        (SELECT id FROM gods WHERE name = %s),
        %s,
        %s,
        %s,
        %s,
        %s
    )
    """

    try:
        cursor.execute(query, (
            match_date,
            gamemode,
            role,
            player_god,
            enemy_god,
            kills,
            deaths,
            assists,
            game_time,
            win
        ))

        conn.commit()
        return True  # success

    except Exception as e:
        print("ERROR inserting match:", e)
        return False

    finally:
        conn.close()

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

    cursor.execute(query, (god_name,))
    games, wins = cursor.fetchone()

    conn.close()

    if games == 0:
        return None

    wins = wins or 0
    winrate = (wins / games) * 100
    return round(winrate, 2)


def get_enemy_winrate(god_name, enemy_god, role):
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

    cursor.execute(query, (god_name, enemy_god, role))
    games, wins = cursor.fetchone()

    conn.close()

    if games == 0:
        return None

    wins = wins or 0
    winrate = (wins / games) * 100
    return round(winrate, 2)

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
    return round(kda, 2) if kda else None

def get_most_played_gods(limit=5):
    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT g.name, COUNT(*) AS games
    FROM matches m
    JOIN gods g ON m.player_god_id = g.id
    GROUP BY g.name
    ORDER BY games DESC
    LIMIT %s
    """

    cursor.execute(query, (limit,))
    results = cursor.fetchall()

    conn.close()

    return results  # list of tuples

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

    if not seconds:
        return None

    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02d}"


def get_best_matchups(god_name, role=None, min_games=3):
    conn = connect_db()
    cursor = conn.cursor()

    if role:
        query = """
        SELECT g.name,
               COUNT(*) AS games,
               (SUM(win) * 100.0 / COUNT(*)) AS winrate
        FROM matches m
        JOIN gods g ON m.enemy_god_id = g.id
        WHERE m.player_god_id = (
            SELECT id FROM gods WHERE name = %s
        )
        AND m.match_role = %s
        GROUP BY g.name
        HAVING games >= %s
        ORDER BY winrate DESC
        LIMIT 5
        """
        cursor.execute(query, (god_name, role, min_games))
    else:
        query = """
        SELECT g.name,
               COUNT(*) AS games,
               (SUM(win) * 100.0 / COUNT(*)) AS winrate
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

    if not results:
        return None

    # 🔥 Round winrate before returning
    cleaned = [(enemy, games, round(winrate, 2)) for enemy, games, winrate in results]

    return cleaned

# print("Testing best matchups")
# get_best_matchups("Bellona")
# print("\n")

def get_worst_matchups(god_name, role=None, min_games=2):
    conn = connect_db()
    cursor = conn.cursor()

    if role:
        query = """
        SELECT g.name,
               COUNT(*) AS games,
               (SUM(win) * 100.0 / COUNT(*)) AS winrate
        FROM matches m
        JOIN gods g ON m.enemy_god_id = g.id
        WHERE m.player_god_id = (
            SELECT id FROM gods WHERE name = %s
        )
        AND m.match_role = %s
        GROUP BY g.name
        HAVING games >= %s
        ORDER BY winrate ASC
        LIMIT 5
        """
        cursor.execute(query, (god_name, role, min_games))
    else:
        query = """
        SELECT g.name,
               COUNT(*) AS games,
               (SUM(win) * 100.0 / COUNT(*)) AS winrate
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

    if not results:
        return None

    return [(enemy, games, round(winrate, 2)) for enemy, games, winrate in results]


# print("Testing worst matchups")
# get_worst_matchups("Bellona")
# print("\n")


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
    return round(kda, 2) if kda else None

# print("KDA for one enemy God")
# get_matchup_kda("Bellona","Amaterasu")