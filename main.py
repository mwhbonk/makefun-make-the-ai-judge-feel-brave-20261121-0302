# make-the-ai-judge-feel-brave-20261121-0302 entry (Python 3.13, stdlib only):
# writes one short text to /output/entry.txt. The text is embedded here so
# the program writes exactly the bytes it was built with, on every run,
# with no network and no input files. The gate takes UTF-8 text of 1 to 280
# characters that is not only white space, and the judge reads exactly the
# bytes written, so write no line end you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
from pathlib import Path

TEXT = "Snow settles on the fence post, a little more, then a little more. The house ticks as it cools. Far off, a train sighs past and is gone, and the quiet it leaves behind stays with you."

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
