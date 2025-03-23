import gradio as gr
from transformers import pipeline

# Load Transformer-based chatbot model
chatbot_pipeline = pipeline("text-generation", model="gpt2", trust_remote_code=True)

def get_ai_response(user_input):
    """
    Generates an AI response based on user input.
    """
    response = chatbot_pipeline(user_input, max_length=100, do_sample=True)
    return response[0]['generated_text']

# Create a Gradio UI
def chat_interface(user_input):
    return get_ai_response(user_input)

# Define Gradio Interface
chatbot_ui = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(lines=2, placeholder="Type your message..."),
    outputs="text",
    title="AI Chatbot 🤖",
    description="Chat with an AI-powered bot using Transformers!",
)

if __name__ == "__main__":
    chatbot_ui.launch()