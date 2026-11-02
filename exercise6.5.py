rivers = {
    'Seine': 'France',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
}

for river, country in rivers.items():
    print(f"The {river} river runs through {country}.")
print("\nRivers names:")
for river in rivers.keys():
    print(f"  {river.title()}")
print("\nCountries:")
for country in rivers.values():
    print(f"  {country.title()}")