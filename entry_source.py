"""Entry builder for The Comment Above the Code (make.fun).

Judge brief from RULES.txt (quoted):
- One line, at most 200 characters, written as a comment a developer
  might leave above fragile production code, funny and painfully honest.
- Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters,
  not only white space. Entry filename: entry.txt
- Judge weighs, most important first:
  1. Funny comment about fragile legacy code, real developer afraid to touch it.
  2. Honesty stings: names a real, recognisable failure in code/process.
  3. Economical: every word earns its place, punchline on the last few words.
  4. Fresh angle: not off-by-one, who-wrote-this, or no-comments cliche.
  5. Reads like a comment actually left in a codebase, working dev voice.
"""
import os

# Each candidate: (text, on_subject, sting, economy, fresh, authentic) 0-10
CANDIDATES = [
    ("// Do not touch this. It works, nobody knows why, and the last person who tried is now in a different career.",
     9, 7, 7, 5, 9),
    ("// This function is held together by fear, prayer, and one customer who still uses Internet Explorer.",
     8, 7, 8, 6, 8),
    ("// Warning: removing this line breaks production. Adding it back also breaks production, just slower.",
     9, 8, 8, 7, 8),
    ("// I know this looks wrong. It is. But the bug depends on it, and so does payroll.",
     9, 8, 7, 6, 9),
    ("// Temporary workaround from 2019. It now has users, a fan club, and tenure.",
     8, 8, 9, 7, 8),
    ("// If you understand this code, please explain it to me before you change it.",
     7, 6, 8, 4, 9),
    ("// Nobody owns this module anymore. It owns us, and it knows it.",
     8, 7, 9, 6, 8),
    ("// This code is wrong, slow, and undocumented, but it has survived five rewrites, so legally it is now the specification.",
     9, 9, 7, 9, 9),
    ("// Touch this on a Friday and you will meet everyone who depends on its bug, starting with Finance, at 3 a.m.",
     9, 8, 8, 8, 9),
    ("// Do not fix the bug below: Sales sold it, Support documented it, and Finance now charges extra for it.",
     10, 10, 10, 10, 9),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate):
    return sum(w * s for w, s in zip(WEIGHTS, candidate[1:]))


def main():
    winner = max(CANDIDATES, key=score)[0]
    assert 1 <= len(winner) <= 200, f"char count {len(winner)} outside 1-200 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(winner)


if __name__ == "__main__":
    main()
