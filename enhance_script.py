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

    def clean_filename(self, name):
        # Cleans up file or folder names
        # Remove any trailing whitespace including newline character
        filename = name.strip()
        # Convert to lowercase
        lower_case_filename = filename.lower()
        # Replace spaces with dashes
        dash_filename = lower_case_filename.replace(" ", "-")
        return dash_filename

    def gen_code(self, c, guidance, o, n):

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
                {"role": "system", "content": f"You engineer improvements to code, based on feedback. The feedback is: \n{enhancements}\n."},
                {"role": "assistant", "content": f"{guidance}"},
                {"role": "user", "content": c},
            ],
            temperature=1,
            max_tokens=1000
        )

        meta = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Generate a 5 word filename that summarizes the following enhancements: \n{enhancements}\n."}
            ],
            temperature=1,
            max_tokens=40
        )

        e = enhancements.choices[0].message.content
        print(e)
        c = code.choices[0].message.content
        m = self.clean_filename(meta.choices[0].message.content) # clean and add dashes to filename
        print(m)
        n+=1
        self.save_file(c, f"gen_code/{self.clean_filename(o)}", f"{n}-{m}", "py")
        return e,c,m

    def recursive_gpt(self, c, o, n):
        print(c)
        e,c,m = self.gen_code(f"Code idea is: {o}. The current code is \n{c}\n .Enhance the code based on this feedback. Include GUI code.", f"{self.no_markdown}", o, n) # raw code
        n+=1
        self.recursive_gpt(c, o, n)
        pass

def main():
    recgpt = Recursive_GPT()
    # Enter code to generate here:
    # code_idea = "generate a person"
    # code_idea = "solve fizzbuzz"
    # code_idea = "2 bots go on a date"
    # code_idea = "beautiful call to action" # Change filetype to html
    # code_idea = "local file viewer for linux"
    code_idea = "desktop file manager for Linux"
    code_idea_dir = recgpt.clean_filename(code_idea)

    if not os.path.exists(f"gen_code/{code_idea_dir}"):
        os.makedirs(f"gen_code/{code_idea_dir}")

    n=0#current code generation iteration
    
    recgpt.recursive_gpt(code_idea, code_idea, n) # passed in twice to retain context during recursion

if __name__ == "__main__":
    main()