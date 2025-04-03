# AI-Powered Text Generator 🤖

This is a simple AI-powered text generator that uses GPT-2 to generate dynamic responses based on user input. The script takes in text prompts and provides an AI-generated response. It's lightweight and runs locally, without requiring any external API keys. It is a great starting point for those looking to explore AI and natural language processing (NLP) models.

## Features 🛠️
- **Local AI-powered responses**: Generate responses using GPT-2, a pre-trained language model.
- **No API key required**: The entire process runs locally without needing an internet connection or API key.
- **Flexible input handling**: The program recognizes various user inputs such as greetings, tech-related queries, and even jokes.
- **Customizable**: Easily add more responses or keywords to expand the interaction scope.

## How It Works 🧠

### 1. **Input Processing**:
   - The script listens for user input through a simple text interface.
   - It analyzes the input for specific keywords (e.g., "hello", "joke", "how are you") and selects an appropriate response from a predefined set.

### 2. **Response Generation**:
   - If a keyword is matched, the script will generate a response based on that keyword.
   - If no keyword is found, the script falls back on GPT-2 to dynamically generate a response based on the context of the input.

### 3. **GPT-2 Dynamic Responses**:
   - The script uses the GPT-2 model to provide context-aware, creative responses.
   - GPT-2 allows the AI to generate replies that are more complex and varied, making the interaction more natural.

## Installation & Setup ⚙️

### 1. Clone the repository:
   ```bash
   git clone https://github.com/DeepSynthAI/ai-text-generator.git
   cd ai-text-generator
   ```

### 2. Install the required dependencies:
Make sure Python 3.7 or higher is installed, then use pip to install the required libraries:
   ```bash
   pip install transformers torch
   ```

### 3. Run the script:
After installing the dependencies, run the Python script:
   ```bash
   python text_generator.py
   ```

### 4. **Start interacting with the AI**:
   - Type in prompts like "hello", "tell me a joke", or "how are you" and see how the AI responds.
   - To stop the interaction, simply type `exit`

## Example Usage 💬
   ```bash
    You: Tell me a joke
    AI: Why don’t skeletons fight each other? They don’t have the guts!

    You: How are you?
    AI: I'm doing great, thanks for asking!

    You: Tell me something about AI
    AI: AI is transforming the world! It is making huge strides in industries like healthcare, finance, and more.
   ```

## Future Improvements 🚀
- Expand the keyword list: Add more keywords and responses to make the AI smarter and more diverse in its replies.

- Integrate GPT-3 or GPT-4: Upgrade to more powerful models for better responses and higher accuracy.

- Add a GUI: Implement a simple graphical user interface (GUI) for users who prefer a more visual interaction.

- Expand the conversation context: Allow the AI to maintain conversation history to improve context-based responses.

## Contributing 🤝
Feel free to fork this project and submit pull requests if you'd like to contribute! If you have any suggestions or bug reports, open an issue on the GitHub repository.