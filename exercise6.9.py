favorite_places = {
    'nayya': ['Bali', 'Lombok', 'Raja Ampat'],
    'vela': ['Yogyakarta', 'Bandung', 'Jakarta'],
    'salsa': ['Surabaya', 'Medan', 'Semarang']
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")