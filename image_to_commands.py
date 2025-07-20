# aim is to convert an image into position and command
import os
import re
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from on_screen_actions import click_a_spot, take_screenshot

load_dotenv()
client = genai.Client()

take_screenshot()

with open('screenshot.png', 'rb') as file:
    image_bytes = file.read()

prompt = f"""
    You are given a screenshot of a macbook air 13 inch running macOS with resolution 1470x956.

    Task: minimise the current screen click the mail box symbol button in the bottom part of the screen.

    1. Return its **center coordinates** in pixels (X, Y).
    2. Suggest the action to take — click if it's a button, fill if it's a textbox.

    Respond ONLY in the following JSON format:
    ```json
    {{
    "x": <X coordinate>,
    "y": <Y coordinate>,
    "action": "click" // or "fill"
    }}
    ```
"""

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png'
        ),
        prompt
    ]
)
output = response.text
pattern = r'```json\n([\s\S]*?)\n```'
formatted_output = re.search(pattern, output)
json_output = formatted_output.group(1).strip()
json_output = json.loads(json_output)
print(json_output)
click_a_spot(json_output["x"], json_output["y"])



