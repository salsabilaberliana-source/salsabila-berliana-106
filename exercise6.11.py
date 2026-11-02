cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10000000,
        'fact': 'the capital of indonesia'
    },
    'london': {
        'country': 'united kingdom',
        'population': 9000000,
        'fact': 'the capital of united kingdom'
    },
    'new york': {
        'country': 'united states',
        'population': 8000000,
        'fact': 'the largest city in the united states'
    }
}

for city, information in cities.items():
    country = information['country']
    population = information['population']
    fact = information['fact']

    print(f"\nCity: {city.title()}")
    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")