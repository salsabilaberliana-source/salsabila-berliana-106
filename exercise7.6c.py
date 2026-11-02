prompt = "\nEnter a pizza topping."
prompt += "\nEnter 'quit' to stop: "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    
    print(f"I'll add {topping} to your pizza.")