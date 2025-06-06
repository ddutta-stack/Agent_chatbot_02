import requests
import gradio as gr
## Deepset API URL
ollama_url = "http://localhost:11434/api/generate"

## Create a sample FAQ Database 
FAQ_DB = {

    "order tracking": "You can track your order by logging into your account and navigating to 'My Orders'.",
    "return policy": "We accept returns within 30 days. Visit our Returns page to initiate a return.",
    "customer support contact": "You can reach customer support at support@example.com or call us at +1-800-555-1234.",
    "payment methods": "We accept Visa, MasterCard, PayPal, and Apple Pay for secure transactions.",
    "shipping details": "Orders are processed within 24 hours. Standard shipping takes 3-5 business days."
}
## Function to handle user queries
def chatbot_response(user_query):
    # Check if the query matches any FAQ Else look out for the best match and respond
    prompt = f'Find the best answer to the following question based on the {user_query}\n'
    f'The list of FAqs are: {FAQ_DB.keys()}\n'
    f'Try to find the best match for the question and respond with the answer based on the matching FAQ from {FAQ_DB.keys()}.\n'
    f'If the answer cannot be found even from the FAQ, respond with "I am not sure about that. Please contact our customer support for further assistance."'
    payload={
        "model":"deepseek-r1:1.5b",
        "prompt":prompt,
        "stream":False
    }
    response= requests.post(ollama_url, json=payload)

    if response.status_code == 200:
        ai_response = response.json().get("response", "I am sorry and not sure about that.")
        return FAQ_DB.get(ai_response.lower(),ai_response)
    else:
        return "I am sorry, I could not process your request at the moment. Please try again later."
    
#Test the chatbot_response function
if __name__ == "__main__":
    # interface = gr.Interface(
    #     fn=chatbot_response,
    #     inputs=gr.Textbox(label="User Query", placeholder="Type your question here..."),
    #     outputs=gr.Textbox(label="Chatbot Response"),
    #     title="Customer Support Chatbot",
    #     description="Ask questions related to order tracking, return policy, customer support, payment methods, and shipping details."
    # )
    # interface.launch()

    test_query = "How can I track my order?"
    print("User Query:", test_query)
    print("Chatbot Response:", chatbot_response(test_query))
