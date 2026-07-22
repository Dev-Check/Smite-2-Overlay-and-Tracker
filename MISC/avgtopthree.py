import pandas as pd

# ---------- Load CSV ----------
df = pd.read_csv("ConquestData.csv")  # change path

# ---------- Helper: convert mm:ss to minutes ----------
def to_minutes(t):
    try:
        parts = str(t).split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2].split(".")[0])  # ignore milliseconds
        return hours * 60 + minutes + seconds / 60
    except:
        return 0



# ---------- Core Function ----------
def top3_enemy_matchup_stats(my_god, my_role):
    # Filter to ONLY your god + lane
    filtered = df[
        (df["God"].str.lower() == my_god.lower()) &
        (df["Role"].str.lower() == my_role.lower())
    ].copy()

    if filtered.empty:
        print(f"No matches for {my_god} in {my_role}")
        return

    # Find top 3 enemies you faced
    top3_enemies = filtered["Enemy"].value_counts().head(3).index.tolist()

    print(f"\n=== TOP 3 ENEMIES FACED AS {my_god.upper()} IN {my_role.upper()} ===\n")

    for enemy in top3_enemies:
        vs_enemy = filtered[filtered["Enemy"] == enemy].copy()

        matches = len(vs_enemy)
        winrate = (vs_enemy["Result"].str.lower() == "win").mean() * 100

        # KDA calculated like Smite
        kda_series = (vs_enemy["K"] + (vs_enemy["A"] / 2)) / vs_enemy["D"].replace(0, 1)
        avg_kda = kda_series.mean()

        # K/D/A averages
        avg_k = vs_enemy["K"].mean()
        avg_d = vs_enemy["D"].mean()
        avg_a = vs_enemy["A"].mean()

        # Match time
        avg_time = vs_enemy["Duration"].apply(to_minutes).mean()

        print(
            f"{enemy:<12} | "
            f"Matches: {matches:<3} | "
            f"Winrate: {winrate:.2f}% | "
            f"Avg KDA: {avg_kda:.2f} | "
            f"K/D/A: {avg_k:.2f}/{avg_d:.2f}/{avg_a:.2f} | "
            f"Avg Time: {avg_time:.2f} min"
        )


# ---------- Run ----------
top3_enemy_matchup_stats("Bellona", "Solo")
