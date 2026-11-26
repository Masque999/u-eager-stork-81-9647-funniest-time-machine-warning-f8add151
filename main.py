#!/usr/bin/env python3
"""Funniest Time Machine Warning Label: write one warning to /output/entry.txt."""
import os

LINE = "WARNING: do not meet yourself. He owes you money and he knows it."

assert 1 <= len(LINE) <= 120, f"line must be 1-120 chars, got {len(LINE)}"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "\n" not in LINE, "must be a single line"
assert LINE.strip(), "must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not pass quietly.
with open("/output/entry.txt", encoding="utf-8") as f:
    back = f.read()
assert back == LINE, f"read-back mismatch: wrote {len(LINE)} chars, read {len(back)}"
assert back == back.strip() and "\n" not in back, "read-back failed line checks"

print(f"wrote {len(LINE)} chars to /output/entry.txt")
