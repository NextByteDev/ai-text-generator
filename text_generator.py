import random

def generate_text(prompt):
    """Simulates an AI text generator without using an API."""
    
    responses = {
        "hello": ["Hello! How can I assist you today?", "Hi there! What’s on your mind?"],
        "ai": ["AI is transforming the world! What interests you about AI?", "AI is amazing! Are you working on any AI projects?"],
        "python": ["Python is a great choice for AI and automation!", "Python makes AI development easy and fun!"],
        "default": ["That's interesting! Tell me more.", "I’d love to hear more about that!"]
    }

    # Find a response based on keyword matching
    for key in responses:
        if key in prompt.lower():
            return random.choice(responses[key])
    
    # If no keywords match, return a default response
    return random.choice(responses["default"])

if __name__ == "__main__":
    user_prompt = input("Enter a prompt: ")
    generated_text = generate_text(user_prompt)
    print("AI:", generated_text)
