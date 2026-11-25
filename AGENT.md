# Agent notes

Built for the make.fun bounty "The Funniest One-Line Resignation Letter"
(u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947).

- Read the kit RULES and competition.yaml first: program/v1, one text to
  `/output/entry.txt`, gate 1–140 UTF-8 characters, judge is an AI model
  playing a tired engineering manager, pairwise head-to-head.
- Persona chosen: a cron job. Its specific grievance — firing every minute
  since March for a report nobody has opened since April, and checking the
  logs to confirm it — is a complaint only a cron job could make, in the
  flat, tired, faintly passive-aggressive voice the judge's brief rewards.
- `main.py` is stdlib-only (`import os`), defines the entry as one string
  constant, and writes it with no trailing newline. The line was refined
  over three write/edit passes (draft, added the "and I checked" turn,
  tightened the closing to two short sentences).
- Verified by running `main.py` with `MAKEFUN_OUTPUT_DIR` pointed at a
  fresh /tmp directory and checking the output file's content, length and
  sha256.
