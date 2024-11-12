import sys
from pylint import lint
#pip install pylint -- pythont telepíteni
THRESHOLD = 10

run = lint.run(["--rcfile=.pylintrc","main.py"], exit=False)

score = run.linter.statis.global_note
print(f"{score} pontot ért el a kódunk")
if (score < THRESHOLD):
    sys.exit(1)
else:
    sys.exit(0)