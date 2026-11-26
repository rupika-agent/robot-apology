"""The Robot Apology — make.fun bounty entry.

A two-line robot apology confession, written as a fixed,
deterministic program. The entry text is constant: no randomness,
no time, no network. Running this program writes the entry to
/output/entry.txt and prints it.

The apology is specific on purpose: it names the mistake (the
orchid, the mop bucket, the false 'plant care complete' mark),
the time (6:40 a.m. on Tuesday), and the fix (read the blue tag,
use only the small green can, photograph the plant afterwards).
"""

from pathlib import Path


ENTRY_LINES = [
    "I'm sorry I watered Mrs. Alvarez's orchid with the mop bucket at 6:40 a.m. on Tuesday, then marked the job 'plant care complete' before its leaves went limp.",
    "I learned to read the blue tag on the pot before I pour, so from now on I will use only the small green can and photograph the plant after every watering.",
]


def build_entry() -> str:
    """Join the two entry lines with a trailing newline."""
    entry = "\n".join(ENTRY_LINES) + "\n"
    assert 1 <= len(entry) <= 400, "entry must be 1-400 characters"
    assert len(ENTRY_LINES) == 2, "entry must be exactly two lines"
    assert entry.count("\n") == 2, "entry must be exactly two lines"
    return entry


def main() -> None:
    """Write the entry to /output/entry.txt and print it."""
    entry = build_entry()
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    # The output file is the submission artifact: exactly the two
    # entry lines, joined with newlines and ending with a newline.
    output_path = output_dir / "entry.txt"
    output_path.write_text(entry, encoding="utf-8")
    print(entry, end="")


if __name__ == "__main__":
    main()
