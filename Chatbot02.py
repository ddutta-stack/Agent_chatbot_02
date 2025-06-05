import requests
import gradio as gr
## Deepset API URL
ollama_url = "https://localhost:11434/chat/completions"

## Create a sample FAQ Database 
FAQ_DB = {

    "order tracking": "You can track your order by logging into your account and navigating to 'My Orders'.",
    "return policy": "We accept returns within 30 days. Visit our Returns page to initiate a return.",
    "customer support contact": "You can reach customer support at support@example.com or call us at +1-800-555-1234.",
    "payment methods": "We accept Visa, MasterCard, PayPal, and Apple Pay for secure transactions.",
    "shipping details": "Orders are processed within 24 hours. Standard shipping takes 3-5 business days."
}
## Function to handle user queries