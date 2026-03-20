
import os
import re
from datetime import datetime

BASE_DIR = "."
day_pattern = re.compile(r"Day(\d+)", re.IGNORECASE)

days = []
total_problems = 0

# Collect days and problems
for folder in os.listdir(BASE_DIR):
    match = day_pattern.match(folder)
    if match and os.path.isdir(folder):
        day_num = int(match.group(1))
        days.append(day_num)

        # count problems (files)
        files = os.listdir(folder)
        total_problems += len([f for f in files if f.endswith(".py")])

days.sort()

# Calculate streak
streak = 0
max_streak = 0
current_streak = 0

prev = None
for d in days:
    if prev is None or d == prev + 1:
        current_streak += 1
    else:
        current_streak = 1
    max_streak = max(max_streak, current_streak)
    prev = d

streak = current_streak

# Generate folder structure
structure = "```bash\n"
for d in days:
    structure += f"📂 Day{str(d).zfill(2)}\n"
structure += "```"

# Update README
with open("README.md", "r") as f:
    content = f.read()

def replace(tag, value):
    return re.sub(f"(<!-- {tag} -->)(.*?)(<!-- END_{tag} -->)", f"\\1{value}\\3", content, flags=re.DOTALL)

content = replace("DAYS", str(len(days)))
content = replace("PROBLEMS", str(total_problems))
content = replace("STREAK", str(streak))
content = replace("MAX_STREAK", str(max_streak))

content = re.sub(
    r"<!-- STRUCTURE_START -->.*?<!-- STRUCTURE_END -->",
    f"<!-- STRUCTURE_START -->\n{structure}\n<!-- STRUCTURE_END -->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(content)