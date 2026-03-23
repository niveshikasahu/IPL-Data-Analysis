# ============================================================
#   IPL DATA ANALYSIS PROJECT
#   Tools: Python, Pandas, Matplotlib, Seaborn
#   Author: Your Name
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Style ────────────────────────────────────────────────────
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# ============================================================
# STEP 1 — LOAD DATA
# ============================================================
# Download datasets from:
# https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020
# Place both CSV files in the same folder as this script.

matches  = pd.read_csv("matches.csv")
delivery = pd.read_csv("deliveries.csv")

print("✅ Data Loaded Successfully!")
print(f"   Matches  : {matches.shape[0]} rows, {matches.shape[1]} columns")
print(f"   Deliveries: {delivery.shape[0]} rows, {delivery.shape[1]} columns")
print()

# ============================================================
# STEP 2 — BASIC INFO
# ============================================================
print("── Seasons covered ──")
print(sorted(matches['season'].unique()))
print()
print("── Teams ──")
print(matches['team1'].unique())
print()

# ============================================================
# STEP 3 — MOST SUCCESSFUL TEAMS (by wins)
# ============================================================
team_wins = matches['winner'].value_counts().head(10)

plt.figure()
ax = team_wins.plot(kind='bar', color=sns.color_palette("Set2", len(team_wins)))
plt.title("🏆 Top 10 Teams by Total IPL Wins", fontsize=15, fontweight='bold')
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45, ha='right')
for i, v in enumerate(team_wins):
    ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("01_team_wins.png", dpi=150)
plt.show()
print("✅ Chart saved: 01_team_wins.png")

# ============================================================
# STEP 4 — TOSS IMPACT: Does winning toss = winning match?
# ============================================================
matches['toss_match_win'] = matches['toss_winner'] == matches['winner']
toss_impact = matches['toss_match_win'].value_counts()

labels = ['Won Toss & Match', 'Won Toss, Lost Match']
colors = ['#2ecc71', '#e74c3c']
plt.figure()
plt.pie(toss_impact, labels=labels, autopct='%1.1f%%', colors=colors,
        startangle=140, textprops={'fontsize': 13})
plt.title("🎯 Toss Impact on Match Result", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig("02_toss_impact.png", dpi=150)
plt.show()
print("✅ Chart saved: 02_toss_impact.png")

# ============================================================
# STEP 5 — TOP RUN SCORERS
# ============================================================
top_batsmen = (
    delivery.groupby('batsman')['batsman_runs']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
ax = top_batsmen.plot(kind='barh', color=sns.color_palette("mako", len(top_batsmen)))
plt.title("🏏 Top 10 Run Scorers in IPL History", fontsize=15, fontweight='bold')
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
for i, v in enumerate(top_batsmen):
    ax.text(v + 50, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig("03_top_batsmen.png", dpi=150)
plt.show()
print("✅ Chart saved: 03_top_batsmen.png")

# ============================================================
# STEP 6 — TOP WICKET TAKERS
# ============================================================
dismissals = delivery[delivery['dismissal_kind'].notna()]
top_bowlers = (
    dismissals.groupby('bowler')['dismissal_kind']
    .count()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
ax = top_bowlers.plot(kind='barh', color=sns.color_palette("flare", len(top_bowlers)))
plt.title("🎳 Top 10 Wicket Takers in IPL History", fontsize=15, fontweight='bold')
plt.xlabel("Total Wickets")
plt.ylabel("Bowler")
for i, v in enumerate(top_bowlers):
    ax.text(v + 0.5, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig("04_top_bowlers.png", dpi=150)
plt.show()
print("✅ Chart saved: 04_top_bowlers.png")

# ============================================================
# STEP 7 — SEASON-WISE TOTAL RUNS (trend over years)
# ============================================================
season_runs = delivery.merge(
    matches[['id', 'season']], left_on='match_id', right_on='id'
)
season_total = season_runs.groupby('season')['total_runs'].sum()

plt.figure()
plt.plot(season_total.index, season_total.values,
         marker='o', linewidth=2.5, color='#3498db', markersize=8)
plt.fill_between(season_total.index, season_total.values, alpha=0.15, color='#3498db')
plt.title("📈 Total Runs Scored Per Season", fontsize=15, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("05_season_runs.png", dpi=150)
plt.show()
print("✅ Chart saved: 05_season_runs.png")

# ============================================================
# STEP 8 — PLAYER OF THE MATCH AWARDS
# ============================================================
top_pom = matches['player_of_match'].value_counts().head(10)

plt.figure()
ax = top_pom.plot(kind='bar', color=sns.color_palette("coolwarm", len(top_pom)))
plt.title("🌟 Most Player of the Match Awards", fontsize=15, fontweight='bold')
plt.xlabel("Player")
plt.ylabel("Awards")
plt.xticks(rotation=45, ha='right')
for i, v in enumerate(top_pom):
    ax.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("06_player_of_match.png", dpi=150)
plt.show()
print("✅ Chart saved: 06_player_of_match.png")

# ============================================================
# DONE
# ============================================================
print()
print("🎉 All 6 charts generated and saved!")
print("📁 Upload your charts + this script to GitHub")
print("📢 Share your findings on LinkedIn!")
