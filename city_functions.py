def city_country(city, country):
    return f"{city.title()}, {country.title()}"

def city_country(city, country, population=''):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"