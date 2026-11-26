#!/usr/bin/env python3
"""Funniest sign on a haunted server room door.

Writes one line to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""
import os

ENTRY = "IF THE SERVERS WHISPER YOUR NAME, LOG A TICKET. DO NOT ANSWER."
# Chosen sign: reads like a real posted notice, sysadmin-3am target,
# fresh haunting (servers whispering your name) + IT collision (log a ticket).


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 chars"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
