import openai import json

def ai_triple_lock(pdf_image_url, extracted_data): """ OpenAI Vision validation against the source document. Ensures human analysts didn't misread a 6 for an 8. """ client = openai.OpenAI()

prompt = f"""
Analyze the attached mining report image. 
Cross-reference the following extracted data: {json.dumps(extracted_data)}

Tasks:
1. Verify Tonnage (Mt) matches the table.
2. Verify Grade (g/t) matches the table.
3. Ensure Units are consistent.

Return a JSON object with 'verified' (bool) and 'anomalies' (string).
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": pdf_image_url}}
            ]
        }
    ],
    response_format={"type": "json_object"}
)

return response.choices[0].message.content