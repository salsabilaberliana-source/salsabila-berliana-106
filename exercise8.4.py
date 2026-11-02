def make_shirt(size="large", message="I love Python"):
    """Make a shirt, large with 'I love Python' by default."""
    print(f"The shirt is size {size} and says '{message}'.")

make_shirt()                                  
make_shirt(size="medium")                     
make_shirt("small", "Hello, world!")  