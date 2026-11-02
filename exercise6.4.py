glossary = {
     'variable': 'A name that stores a value.',
    'list': 'A collection of items in a single variable.',
    'loop': 'A way to repeat a block of code.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A series of characters wrapped in quotes (single, double, or triple).',
    "boolean": "A data type that can only be True or False.",
    "key": "The first item in a key-value pair in a dictionary.",
    "value": "The data associated with a specific key in a dictionary.",
    "conditional test": "An expression that evaluates to either True or False.",
    "comment": "A note in the code that is ignored by the Python interpreter."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:")
    print(f"  {meaning}\n")