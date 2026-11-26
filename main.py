"""The Robot Apology: write a two-line robot confession to /output/entry.txt.

Line 1 owns one specific, human-scale mistake; line 2 names the lesson
that follows from that exact mistake and the changed behaviour.
Deterministic: fixed text, no randomness, no network, no time.
"""

from pathlib import Path

ENTRY_LINES = [
    "I'm sorry I watered Mrs. Alvarez's orchid with the mop bucket "
    "at 6:40 a.m. on Tuesday, then marked the job 'plant care complete' "
    "before its leaves went limp.",
    "I learned to read the blue tag on the pot before I pour, so from "
    "now on I will use only the small green can and photograph the "
    "plant after every watering.",
]


def build_entry() -> str:
    text = "\n".join(ENTRY_LINES) + "\n"
    assert 1 <= len(text.strip()) <= 400, "gate: entry must be 1-400 chars"
    assert len(ENTRY_LINES) == 2, "entry must be exactly two lines"
    return text

def main() -> None:
    text = build_entry()
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
