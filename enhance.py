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

    def save_file(self, content, filepath, filename, ext):
        with open(f"{filepath}/{filename}.{ext}", 'a') as file:
            file.write(f"{content}\n")
        print(f"File saved to {filepath}/{filename}.{ext}")

    def gen_code(self, c, guidance):

        enhancements = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Suggest 3 enhancements to the following code: \n {c}"}
            ],
            temperature=1.3,
            max_tokens=300
        )

        code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You engineer improvements to Python code based on feedback. The feedback is: \n{enhancements}\n."},
                {"role": "assistant", "content": f"{guidance}"},
                {"role": "user", "content": c},
            ],
            temperature=1,
            max_tokens=1000
        )

        meta = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Generate a 5 word filename that summarizes the following enhancements: \n{enhancements}\n. Join with dashes -"}
            ],
            temperature=1,
            max_tokens=40
        )

        e = enhancements.choices[0].message.content
        print(e)
        c = code.choices[0].message.content
        m = meta.choices[0].message.content
        print(m)
        self.save_file(c, "gen_code", m, "py")
        return e,c,m

    def recursive_gpt(self, c, o):
        print(c)
        e,c,m = self.gen_code(f"Objective is to {o}. The current code is \n{c}\n .Enhance the code based on this feedback.", f"{self.no_markdown}") # raw code
        self.recursive_gpt(c, o)
        pass

def main():
    recgpt = Recursive_GPT()
    recgpt.recursive_gpt("generate a person", "generate a person")

if __name__ == "__main__":
    main()