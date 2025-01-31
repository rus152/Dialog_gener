import openai
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=3000
    )
    result = response.choices[0].message['content'].strip()
    # Удаление пустых строк
    result = "\n".join([line for line in result.split("\n") if line.strip() != ""])
    return result

if __name__ == "__main__":
    with open('prompt.txt', 'r', encoding='utf-8') as file:
        prompt = file.read().replace('\n', '\\n')
    response = generate_response(prompt)
    print(response)
    
    # Запись результата в файл
    os.makedirs('results', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    with open(f'results/response_{timestamp}.txt', 'w', encoding='utf-8') as file:
        file.write(response)