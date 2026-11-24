"""Two Lines to Your Past Self.

Writes a two-line warning to /output/entry.txt: line one warns the past
self about one specific moment, line two says why that moment mattered
and what changed because of it. Deterministic: same bytes every run.
"""

import os

ENTRY = (
    "Don't walk out of the kitchen at 11:47 p.m. on your last night in the flat "
    "\u2014 sit back down and tell your father you were wrong about the money.\n"
    "He waits eleven years to hear it, and by the time you say it, "
    "he can no longer answer.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
