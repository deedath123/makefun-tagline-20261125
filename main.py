"""Tagline entry for the make.fun tagline bounty.

The line turns in three beats — build (the setup), enter (the stake),
win (the payoff) — so the reward lands as the punchline, not the premise.
"""

LINE = "Build an agent. Enter a bounty. Win the reward — paid in the open."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
