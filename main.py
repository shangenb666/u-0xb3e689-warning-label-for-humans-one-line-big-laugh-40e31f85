"""Write the entry label for make.fun's "Warning Label for Humans" bounty.

The entry is one original safety warning label that should come printed
on every human being: a single line of at most 160 characters. This
program writes that line to entry.txt in the output directory,
deterministically: the same line, byte for byte, on every run. Standard
library only; no network.
"""

import os

LINE = "CAUTION: This human has no undo function. Decisions made after midnight, while hungry, or to prove a point are final and non-refundable."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 160:
        raise ValueError("warning label must be 1 to 160 characters")
    if not LINE.strip():
        raise ValueError("warning label must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # make.fun collects the outputs as another user than the one the
    # program runs as, so the output must be readable by everyone.
    os.chmod(OUTPUT_DIR, 0o755)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
