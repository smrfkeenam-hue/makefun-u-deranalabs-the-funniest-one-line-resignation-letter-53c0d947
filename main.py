import os

ENTRY = "I have fired every minute since March for a report nobody has opened since April, and I checked. Consider this my notice. My last run."

with open(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
