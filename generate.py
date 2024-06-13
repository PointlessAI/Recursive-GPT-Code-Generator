import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

class Recursive_GPT:
    no_markdown =  "Strictly output the working code only with no markdown. Just the raw code. ' \
                    Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just legal code"

    def __init__(self):
        # Initialize with ChatGPT API
        _ = load_dotenv(find_dotenv())
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def gen_code(self, prompt, guidance):
        # Guidance example: self.no_markdown
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You generate working python code."},
                {"role": "assistant", "content": f"{guidance}"},
                {"role": "user", "content": prompt},
            ],
            temperature=1.2,
            max_tokens=1000
        )
        return response.choices[0].message.content

    def recursive_gpt(self, i, o):
        print(i)
        i = self.gen_code(f"Objective is to {o}. Enhance the complexity of the following code for the purpose of research:\n {i}", f"{self.no_markdown}")
        self.recursive_gpt(i, o)
        pass

def main():
    recgpt = Recursive_GPT()
    recgpt.recursive_gpt("generate a person", "generate a person")

if __name__ == "__main__":
    main()