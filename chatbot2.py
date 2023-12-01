import re

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is: {result}"
    except Exception as e:
        return f"Error evaluating the expression: {str(e)}"

def get_sublocality_prices():
    sublocality_prices = {
        "gandhi nagar": 20296,
        "indira nagar": 16945,
        "kasturba nagar": 18500,
        "sastri nagar": 17108
    }
    return sublocality_prices

def calculate_average_price(sublocality_prices):
    total_price = sum(sublocality_prices.values())
    total_sublocalities = len(sublocality_prices)
    if total_sublocalities > 0:
        return total_price / total_sublocalities
    else:
        return 0

def chatbot(message):
    if message.lower() == "hi":
        return "Hi there! How can I assist you today?"
    elif "talk about" in message.lower():
        return "Adyar is a vibrant neighborhood in Chennai, India. It has a rich cultural heritage, educational institutions, and the beautiful Adyar River flowing through it. The Theosophical Society, located in Adyar, is known for promoting spiritual wisdom and universal brotherhood."
    elif "weather" in message.lower():
        return "Adyar is known for its pleasant weather, making it a comfortable place to live."
    elif "price" in message.lower():
        return "Adyar is among the poshest localities in Chennai. Therefore, property prices tend to be higher than in other neighborhoods."
    elif "restaurants" in message.lower():
        return "Adyar offers a diverse range of restaurants, catering to various tastes. You can find everything from local South Indian cuisine to international dishes."
    elif "schools" in message.lower():
        return "Adyar is home to several reputable educational institutions, making it a popular choice for families. Some well-known schools in the area include Adyar Primary School and Adyar High School."
    elif "parks" in message.lower():
        return "Adyar has several beautiful parks, providing a green and serene environment. The popular Adyar Eco Park is a must-visit for nature enthusiasts."
    elif "shopping" in message.lower():
        return "Adyar has a mix of traditional markets and modern shopping centers. You can explore places like Adyar Ananda Bhavan for traditional items and Adyar Depot for a more modern shopping experience."
    elif "fun facts" in message.lower():
        return "Here are some fun facts about Adyar:\n1. Adyar has South India's first cancer hospital.\n2. It is home to India's largest mural painting.\n3. Kalki's 'Ponniyin Selvan' was written here.\n4. Adyar is home to India's first drone police unit.\n5. It has India's first coffee-themed restaurant.\n6. Adyar boasts India's first walking corridor.\n7. It is home to India's second cancer hospital, among other notable achievements."
    elif "python" in message.lower():
        return "Python is a versatile programming language known for its simplicity and readability. It's widely used in web development, data science, artificial intelligence, and more. Is there anything specific you'd like to know about Python?"
    elif "bye" in message.lower():
        return "Goodbye! If you have more questions in the future, feel free to ask. Have a great day!"
    elif re.match(r"^[0-9+\-*/. ]+$", message):
        return evaluate_expression(message)
    elif "sublocalities" in message.lower():
        sublocality_prices = get_sublocality_prices()
        table = "Sublocality Prices as of 2022:\n"
        table += "{:<15} {:<10}\n".format("Sublocality", "Avg. Price (Rs)")
        for sublocality, price in sublocality_prices.items():
            table += "{:<15} {:<10}\n".format(sublocality.capitalize(), price)
        average_price = calculate_average_price(sublocality_prices)
        table += "\nOverall Average Price for Adyar: Rs {:.2f}".format(average_price)
        return table
    elif "educational institutes" in message.lower():
        return "Notable educational institutes in Adyar include:\n1. IIT Madras\n2. Anna University\n3. National Institute of Fashion Technology (NIFT)\n4. Central Leather Research Institute (CLRI)"
    else:
        return "I'm not sure how to respond to that. Is there anything else you'd like to talk about?"

# Interactive conversation loop
print("Chatbot: Hi there! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
