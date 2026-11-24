"""Robot Pickup Line Championship entry.

Writes a single pickup line, in the voice of a robot trying to charm
someone, to <output dir>/entry.txt. The output directory is taken from
MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output (absolute paths only,
never a relative out/ directory: the grader runs on a read-only
filesystem where only the output directory is writable).
"""

import os
import sys

ENTRY = (
    "You must be a software update \u2014 ever since you arrived, "
    "I've been running feelings I never had permission to install."
)

MAX_CHARS = 200


def validate_entry(line):
    """Return an error string, or None when the line is a valid entry."""
    if not isinstance(line, str):
        return "entry is not text"
    if not (1 <= len(line) <= MAX_CHARS):
        return "entry must be 1 to 200 characters, got %d" % len(line)
    if not line.strip():
        return "entry must not be only whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    if "  " in line:
        return "entry must not contain double spaces"
    return None


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    error = validate_entry(ENTRY)
    if error:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
