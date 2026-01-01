import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# STEP 1: Read the CSV file
# --------------------------------------------------
df = pd.read_csv("wellness_data_300_rows (1).csv")

# --------------------------------------------------
# STEP 2: Define wellness score calculation
# --------------------------------------------------
def calculate_wellness_score(row):
    sleep_score = min(max((row["sleep_hours"] / 8) * 100, 0), 100)
    steps_score = min(max((row["steps"] / 10000) * 100, 0), 100)
    mood_score = (row["mood"] / 5) * 100

    wellness_score = (
        0.40 * sleep_score +
        0.35 * steps_score +
        0.25 * mood_score
    )
    return round(wellness_score, 2)

# --------------------------------------------------
# STEP 3: Apply function
# --------------------------------------------------
df["wellness_score"] = df.apply(calculate_wellness_score, axis=1)

# --------------------------------------------------
# STEP 4: Save output
# --------------------------------------------------
df.to_csv("wellness_output.csv", index=False)

# --------------------------------------------------
# STEP 5: GRAPH 1 - Wellness Score Over Time
# --------------------------------------------------
fig, ax = plt.subplots()

ax.plot(df["wellness_score"])
ax.set_title("Wellness Score Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Wellness Score")

# 🔹 Remove x-axis tick labels (no overlap)
ax.set_xticks([])

# 🔹 Custom coordinate display (bottom-right)
def format_coord(x, y):
    index = int(round(x))
    if 0 <= index < len(df):
        date = df.iloc[index]["date"]
        return f"({date}, {y:.2f})"
    return ""

ax.format_coord = format_coord

plt.tight_layout()
plt.show()

# --------------------------------------------------
# STEP 6: GRAPH 2 - Sleep Hours vs Wellness Score (Line)
# --------------------------------------------------
sleep_sorted = df.sort_values("sleep_hours")

plt.figure()
plt.plot(sleep_sorted["sleep_hours"], sleep_sorted["wellness_score"])
plt.title("Sleep Hours vs Wellness Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Wellness Score")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# STEP 7: GRAPH 3 - Steps vs Wellness Score (Line)
# --------------------------------------------------
steps_sorted = df.sort_values("steps")

plt.figure()
plt.plot(steps_sorted["steps"], steps_sorted["wellness_score"])
plt.title("Steps vs Wellness Score")
plt.xlabel("Steps Walked")
plt.ylabel("Wellness Score")
plt.tight_layout()
plt.show()

print("Wellness score calculation successfully!")
