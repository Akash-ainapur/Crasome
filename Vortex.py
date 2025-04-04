import textwrap
from flask import Flask, render_template, request
import google.generativeai as genai
import markdown2  # Import the markdown2 library

app = Flask(__name__)

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def markdown_to_html(markdown_text):
    return markdown2.markdown(markdown_text)  # Convert Markdown to HTML

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate_response():
    data = request.json
    prompt_parts = [
        data['part1'],
        data['part2'],
        data['part3']
    ]

    # Configure Generative AI
    genai.configure(api_key="AIzaSyDhJL7mLlFmwNQv-RHO0yyIxfPoIPyA8jU")

    # Set up the model and generation configurations
    generation_config = {
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        # Your safety settings here
    ]

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    # Generate content based on the received prompt parts
    response = model.generate_content(prompt_parts)
    
    # Process the response as needed before sending it back
    generated_response = to_markdown(response.text)
    # Convert Markdown to HTML
    html_response = markdown_to_html(generated_response)
    # Return the generated response (HTML) to the frontend
    return html_response

if __name__ == '__main__':
    app.run(debug=True)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 

@app.route('/generate_response', methods=['POST'])
def generate_response():
    data = request.json
    prompt_parts = [
        data['part1'],
        data['part2'],
        data['part3']
    ]
    
    # Configure Generative AI
    genai.configure(api_key="AIzaSyDhJL7mLlFmwNQv-RHO0yyIxfPoIPyA8jU")

    # Set up the model and generation configurations
    generation_config = {
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        # Your safety settings here
    ]

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    # Generate content based on the received prompt parts
    response = model.generate_content(prompt_parts)
    
    # Process the response as needed before sending it back
    generated_response = to_markdown(response.text)
    # Return the generated response to the frontend
    html_response = Markup(generated_response)
    return str(html_response)

if __name__ == '__main__':
    app.run(debug=True)
