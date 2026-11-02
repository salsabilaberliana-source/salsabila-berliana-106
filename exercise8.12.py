def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("turkey")
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("chicken", "tomato", "mayo", "pickles", "onion")