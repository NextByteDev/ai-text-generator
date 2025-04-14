import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Dictionary of predefined responses
responses = {
    "greetings": ["Hello!", "Hi there!", "Hey!", "Greetings!", "Nice to meet you!"],
    "how_are_you": ["I'm doing great, thanks for asking!", "I'm just a program, but I'm doing fine.", "I'm good, how about you?"],
    "ai": ["AI is transforming the world!", "Machine learning is fascinating!", "Neural networks are powerful tools."],
    "casual": ["I'm just a program, but I'm doing great!", "Not much, just waiting for your input!", "Here's a joke: Why did the AI break up with the CPU? It needed more space!"],
    "tech": ["Python is a great programming language!", "Algorithms are the backbone of computer science.", "Coding is fun and rewarding!"],
    "jokes": ["Why don’t skeletons fight each other? They don’t have the guts!", "Why was the computer cold? It left its Windows open!", "What’s a programmer’s favorite hangout place? The Foo Bar!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "That's interesting! Tell me more."]
}

# Keyword mapping to categories (we'll use GPT-2 for the default category)
keywords = {
    "hello": "greetings", "hi": "greetings", "hey": "greetings", "greetings": "greetings",
    "how are you": "how_are_you", "how are you doing": "how_are_you", "what's up": "casual",
    "machine learning": "ai", "deep learning": "ai", "neural networks": "ai", "AI": "ai",
    "python": "tech", "programming": "tech", "coding": "tech", "algorithms": "tech",
    "joke": "jokes", "tell me a joke": "jokes", "make me laugh": "jokes", "tell a joke": "jokes"
}

# Keep track of previous responses to avoid repetition
previous_responses = []
joke_mode = False  # Flag to prevent unnecessary follow-up after a joke

def generate_response(user_input):
    """Generate a response based on the user input."""
    global joke_mode
    user_input = user_input.lower()  # Convert input to lowercase

    # Check for joke requests
    if any(joke_request in user_input for joke_request in ["joke", "tell me a joke", "make me laugh", "tell a joke"]):
        category = "jokes"
        response = random.choice(responses[category])
        joke_mode = True  # Activate joke mode
        # Ensure response hasn't been given recently
        while response in previous_responses:
            response = random.choice(responses[category])
        previous_responses.append(response)
        if len(previous_responses) > 5:
            previous_responses.pop(0)
        return response

    # Prevent follow-up conversational responses if in joke mode
    if joke_mode:
        joke_mode = False  # Reset joke mode after the joke response
        return "I'm glad you enjoyed the joke! Anything else I can do for you?"

    # Check for greeting inputs
    greeting_keywords = ["hello", "hi", "hey", "greetings"]
    if any(greeting in user_input for greeting in greeting_keywords):
        category = "greetings"
        response = random.choice(responses[category])
        # Ensure response hasn't been given recently
        while response in previous_responses:
            response = random.choice(responses[category])
        previous_responses.append(response)
        if len(previous_responses) > 5:  # Limit the history of responses
            previous_responses.pop(0)
        return response

    # Check for specific "how are you" type queries
    if "how are you" in user_input or "how are you doing" in user_input:
        category = "how_are_you"
        response = random.choice(responses[category])
        # Ensure response hasn't been given recently
        while response in previous_responses:
            response = random.choice(responses[category])
        previous_responses.append(response)
        if len(previous_responses) > 5:
            previous_responses.pop(0)
        return response

    # Check for other keyword matches (e.g., AI, tech, etc.)
    for key in keywords:
        if key in user_input:
            category = keywords[key]
            response = random.choice(responses[category])
            # Ensure response hasn't been given recently
            while response in previous_responses:
                response = random.choice(responses[category])
            previous_responses.append(response)
            if len(previous_responses) > 5:
                previous_responses.pop(0)
            return response

    # If no keyword is matched, use GPT-2 to generate a dynamic response
    return generate_dynamic_response(user_input)

def generate_dynamic_response(user_input):
    """Use GPT-2 to generate a response."""
    # Encode the input text and generate predictions
    inputs = tokenizer.encode(user_input, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)

    # Decode the predicted tokens and return the response
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Ensure GPT-2 doesn’t repeat itself
    return generated_text.strip()

# Main loop for interaction
if __name__ == "__main__":
    print("AI Text Generator with GPT-2 - Type 'exit' to stop.")
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() == "exit":
            print("Goodbye!")
            break
        print("AI:", generate_response(user_prompt))
