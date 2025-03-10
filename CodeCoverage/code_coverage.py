import coverage
import os
cov = coverage.Coverage()
cov.load()

with open(os.devnull, "w") as f:
    total = cov.report(file=f)

print("{0:.0f}%".format(total))