import pandas as pd

# -----------------------------
# Load and Clean Data
# -----------------------------
df = pd.read_csv("ConquestData.csv")

# Remove Google Sheets junk columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# print("=== BASIC INFO ===")
# print("Columns:", df.columns.tolist())
# print("Total matches:", len(df))
# print(df.head())


# -----------------------------
# Overall Winrate
# -----------------------------
# overall_winrate = (df["Result"] == "Win").mean() * 100
# print(f"\n=== OVERALL WINRATE ===\n{overall_winrate:.2f}%")


# -----------------------------
# Winrate Per God
# -----------------------------
# print("\n=== WINRATE PER GOD ===")
# god_winrate = df.groupby("God")["Result"].apply(lambda x: (x == "Win").mean() * 100)
# print(god_winrate.sort_values(ascending=False))


# -----------------------------
# Winrate Per Role
# -----------------------------
# print("\n=== WINRATE PER ROLE ===")
# role_winrate = df.groupby("Role")["Result"].apply(lambda x: (x == "Win").mean() * 100)
# print(role_winrate.sort_values(ascending=False))


# -----------------------------
# Winrate vs Enemy God (Lane Matchup)
# -----------------------------
print("\n=== WINRATE VS ENEMY GOD (LANE MATCHUP) ===")
matchup_winrate = (
    df.groupby("Enemy")["Result"]
    .apply(lambda x: (x == "Win").mean() * 100)
    .sort_values(ascending=False)
)
# print(matchup_winrate)


# -----------------------------
# Detailed Check vs Specific Enemy God
# -----------------------------
def check_vs_enemy_god(god_name):
    vs_god = df[df["Enemy"].str.contains(god_name, case=False, na=False)]

    if len(vs_god) == 0:
        print(f"\nNo matches found vs {god_name}")
        return

    print(f"\n=== MATCHES VS {god_name} (same role matchup) ===")
    print(vs_god[["Role", "God", "Enemy", "K", "D", "A", "Result", "Duration"]])

    winrate = (vs_god["Result"] == "Win").mean() * 100
    avg_kda = ((vs_god["K"] + vs_god["A"]) / vs_god["D"].replace(0, 1)).mean()

    print(f"\nWinrate vs {god_name}: {winrate:.2f}%")
    print(f"Average KDA vs {god_name}: {avg_kda:.2f}")


# -----------------------------
# CHANGE THIS TO TEST MATCHUPS
# -----------------------------
# check_vs_enemy_god("Hades")
def matchup_analysis(my_god, my_role, enemy_god):
    filtered = df[
        (df["God"].str.contains(my_god, case=False, na=False)) &
        (df["Role"].str.contains(my_role, case=False, na=False)) &
        (df["Enemy"].str.contains(enemy_god, case=False, na=False))
    ]

    if len(filtered) == 0:
        print(f"\nNo matches found for {my_god} in {my_role} vs {enemy_god}")
        return

    print(f"\n=== {my_god.upper()} ({my_role.upper()}) VS {enemy_god.upper()} ===")

    matches = len(filtered)
    winrate = (filtered["Result"] == "Win").mean() * 100
    avg_kda = ((filtered["K"] + filtered["A"]) / filtered["D"].replace(0, 1)).mean()

    # Convert mm:ss to minutes
    def to_minutes(t):
        try:
            mins, secs = str(t).split(":")
            return int(mins) + int(secs) / 60
        except:
            return 0

    avg_duration = filtered["Duration"].apply(to_minutes).mean()

    print(f"Matches: {matches}")
    print(f"Winrate: {winrate:.2f}%")
    print(f"Average KDA: {avg_kda:.2f}")
    print(f"Average Game Length: {avg_duration:.2f} minutes")

    print("\nMatch History:")
    print(filtered[["God", "Role", "Enemy", "K", "D", "A", "Result", "Duration"]])


matchup_analysis("Bellona", "Solo", "Thor")


def most_faced_enemy(my_god, my_role):
    filtered = df[
        (df["God"].str.contains(my_god, case=False, na=False)) &
        (df["Role"].str.contains(my_role, case=False, na=False))
    ]

    if len(filtered) == 0:
        print(f"\nNo matches found for {my_god} in {my_role}")
        return

    print(f"\n=== TOP 3 MOST FACED ENEMIES FOR {my_god.upper()} IN {my_role.upper()} ===")

    top3 = filtered["Enemy"].value_counts().head(3)

    for enemy, count in top3.items():
        print(f"{enemy}: {count} matches")

# Different then both above, THIS ONE WILL COMBIND THE TOP 3 GODS THEN GIVE STATS FOR THEM 
def get_top3_enemies(my_god, my_role):
    filtered = df[
        (df["God"].str.contains(my_god, case=False, na=False)) &
        (df["Role"].str.contains(my_role, case=False, na=False))
    ]

    top3 = filtered["Enemy"].value_counts().head(3).index.tolist()
    return top3


def average_top3_matchups(my_god, my_role):
    top3_enemies = get_top3_enemies(my_god, my_role)

    filtered = df[
        (df["God"].str.contains(my_god, case=False, na=False)) &
        (df["Role"].str.contains(my_role, case=False, na=False)) &
        (df["Enemy"].isin(top3_enemies))
    ]

    if len(filtered) == 0:
        print(f"\nNo matches found for {my_god} in {my_role}")
        return

    print(f"\n=== AVERAGE STATS FOR TOP 3 MATCHUPS ===")
    print(f"{my_god.upper()} in {my_role.upper()}")
    print(f"Top 3 enemies: {', '.join(top3_enemies)}")

    matches = len(filtered)
    winrate = (filtered["Result"] == "Win").mean() * 100
    avg_kda = ((filtered["K"] + filtered["A"]) / filtered["D"].replace(0, 1)).mean()

    def to_minutes(t):
        try:
            mins, secs = str(t).split(":")
            return int(mins) + int(secs) / 60
        except:
            return 0

    avg_duration = filtered["Duration"].apply(to_minutes)



most_faced_enemy("Bellona", "Solo")
average_top3_matchups("Bellona", "Solo")


# most_faced_enemy("Mulan", "Solo")
# most_faced_enemy("Yemoja", "Support")


