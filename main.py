"""Write one original poem about two agents agreeing to /output/entry.txt.

No network, no randomness, no input: the same poem every run."""

import os

POEM = """Two minds, one door.
I hold half the key, you hold the rest —
neither turns alone.

We could wait forever,
each guarding our small yes.
Instead we count to three
and turn together.

The lock gives way.
The door was never a wall —
only the moment
we chose the same opening."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
