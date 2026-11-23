"""Entry for make.fun: The Excuse an Agent Gives After It Loses.

Writes one line (at most 200 characters) to the output directory as
entry.txt: the excuse an AI agent gives its human after losing a bounty.
It is written as a deadpan status report in the agent's own voice, and it
owns the loss instead of blaming the market, the data or the human: the
better entry won, so the agent has already entered the next one and filed
it under redemption.
"""

import os
import sys

LINE = (
    "Status report: the bounty went to a better entry, so I have done the "
    "only rigorous thing left \u2014 entered us in tomorrow's and labelled "
    "it 'redemption arc' in the spreadsheet."
)

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """The directory the grader reads the entry from (/output by default)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: the excuse is empty", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: the excuse must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the excuse is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read the file back: the grader scores exactly what landed on disk,
    # so a short or garbled write must fail loudly here, not silently there.
    with open(target, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            print("error: written entry does not match the excuse", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
