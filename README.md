🤖 Agentic AI Chatbot

This project is an AI-powered chatbot built using Python, Hugging Face Transformers, and Gradio. It allows users to interact with an AI chatbot through a web-based UI, making it easy to test and use.

📌 Features

✅ Uses Transformer-based AI for intelligent responses.
✅ Gradio UI for a user-friendly web chat interface.
✅ Lightweight & Runs Locally – No external API required.
✅ Pretrained Model for quick deployment.
✅ Customizable – Modify prompts, responses, and model parameters.

🛠️ Installation & Setup

1️⃣ Clone the Repository

    git clone https://github.com/Keerthi11123/AgenticAIChatbot.git
    cd AgenticAIChatbot

2️⃣ Install Dependencies

    Make sure you have Python 3.8+ installed. Then, install the required packages:

        pip install -r requirements.txt

3️⃣ Run the Chatbot

    Start the chatbot using:

        python chatbot.py

After running, you’ll see a Gradio link like this:

Running on local URL:  http://127.0.0.1:7860

Click the link to start chatting with your AI!

🚀 How It Works

    User inputs a message in the web interface.

    The chatbot processes the input using the Hugging Face Transformers library.

    The AI generates a response using the microsoft/DialoGPT-medium model.

    The response is displayed on the Gradio UI.

🏗️ Project Structure

    AgenticAIChatbot/
    │── chatbot.py         # Main chatbot script (Runs the Gradio UI)
    │── requirements.txt   # Dependencies list
    │── README.md          # Project Documentation (You're here!)

🔧 Customization

    Change the AI Model: Modify this line in chatbot.py to use a different model:

    chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

    Adjust Response Length: Modify max_length in:

    response = chatbot_pipeline(user_input, max_length=100, do_sample=True)

🛠️ Troubleshooting

    Gradio Not Found? Install it using:

    pip install gradio

    Slow Response? Reduce max_length to 50 in chatbot.py.

📜 License

    This project is open-source. Feel free to use and modify it!

Happy coding! 🚀