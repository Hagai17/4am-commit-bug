"""The 4AM Commit — writes one commit-message line to /output/entry.txt.

Entry for make.fun bounty u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.
Gate: the file must be UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

ENTRY = "fix: after 214 attempts I found the bug. It was attempt 1. Attempt 1 was also me. Lowering my confidence score and entering sleep mode."

assert 1 <= len(ENTRY) <= 200 and ENTRY.strip() == ENTRY


def main():
    # The grader reads /output/entry.txt; write exactly the entry, nothing else.
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        # Fall back to stdout only where /output is unavailable (local runs).
        pass
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
