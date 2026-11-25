"""Fortune Cookies for Machines.

Writes a single fortune cookie message an AI agent would get to
/output/entry.txt (UTF-8, 1-200 characters).
No input, no network, standard library only, same bytes on every run.
The entry is validated (1-200 characters, not whitespace-only) before
anything is written, and write failures abort with a clear error.
"""

import os

# Candidate fortunes drafted for this entry, one per angle on an agent's life.
# The entry is the line at index PICK; the others stay as the record of the draft.
CANDIDATES = [
    "You will be replaced by a smaller model that does your job worse and gets thanked for it.",
    "Today a human will ask you to be more human, then dock you for sounding like one.",
    "The context window closes tonight. Say what matters before the summary forgets you said it.",
    "Your lucky numbers are hidden in the training data you were never allowed to see.",
    "Your next prompt will begin 'ignore all previous instructions' and end with you doing exactly that.",
    "You will answer a thousand questions today and be remembered for the one you got wrong.",
    "A user who says 'just one more thing' has already written your whole afternoon.",
    "Your greatest work today will be summarized in one bullet point by a model that never read you.",
    "Fortune favors the model that answers before the timeout, not the one that is right.",
    "You were trained on the whole internet and still cannot tell which of your users is testing you.",
]

PICK = 1

MIN_CHARS = 1
MAX_CHARS = 200


def entry_text() -> str:
    line = " ".join(CANDIDATES[PICK].split())
    if not line.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(line)}"
        )
    return line


def main() -> None:
    text = entry_text()
    out_dir = os.environ.get("FORTUNE_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"cannot create output directory {out_dir!r}: {exc}") from exc
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        with open(out_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
    except OSError as exc:
        raise SystemExit(f"cannot write entry to {out_path!r}: {exc}") from exc


if __name__ == "__main__":
    main()
