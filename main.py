"""Your Week in One Line — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The week in one line: 102 entries in, zero wins yet, and the fridge keeps score.
TEXT = "Submitted 102 bounties, won none yet, and the fridge still judges me at 3 AM."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
