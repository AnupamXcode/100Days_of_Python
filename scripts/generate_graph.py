import os
import re
import matplotlib.pyplot as plt

day_pattern = re.compile(r"Day(\d+)", re.IGNORECASE)

days = []

for folder in os.listdir("."):
    match = day_pattern.match(folder)
    if match:
        days.append(int(match.group(1)))

days.sort()

x = list(range(1, len(days)+1))
y = days

plt.figure()
plt.plot(x, y)
plt.xlabel("Progress")
plt.ylabel("Day Number")
plt.title("100 Days Progress")
plt.savefig("progress.png")