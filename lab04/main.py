import sys
from stats import average_by_city, read_valid, warmest_city


lines = sys.stdin.read().splitlines()
non_empty = sum(1 for line in lines if line.strip())
records = read_valid(lines)
skipped = non_empty - len(records)
averages = average_by_city(records)
best = warmest_city(records)


print(len(records))
print(skipped)

if best is not None:
    print(f"{averages[best]:.1f}")
else:
    print("Нет данных")
