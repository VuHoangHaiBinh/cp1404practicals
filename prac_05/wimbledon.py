"""
Wimbledon
Estimate: 5 minutes
Actual:   5 minutes
"""

FILENAME = "wimbledon.csv"

name_to_champion_count = dict()
champion_countries = set()

with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    # Remove the header first column
    lines = in_file.readlines()[1::]
    for line in lines:
        records = line.split(',')
        country = records[1]
        name = records[2]
        name_to_champion_count[name] = name_to_champion_count.get(name, 0) + 1
        champion_countries.add(country)

print("Wimbledon Champions:")
for name, champion_count in name_to_champion_count.items():
    print(name, champion_count)
print()
print(f"These {len(champion_countries)} have won Wimbledon:")
print(", ".join(sorted(champion_countries)))

