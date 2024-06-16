import os
from openai import OpenAI # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore
import subprocess
import sys

class Recursive_GPT:
    no_markdown =  "Return only the raw working code. Do not include any text or comments, just the raw code. Strictly output the working code only with no markdown. Just the raw code. ' \
                    Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just working code. The reason is that it will be executed dynamically so any broken code will cause an execution failiure."

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

    def read_file(self, filepath, filename, ext):
        with open(f"{filepath}/{filename}.{ext}", 'r') as file:
            file_content = file.read()
        return(file_content)

    def clean_filename(self, name):
        # Remove any trailing whitespace including newline character
        filename = name.strip()
        # Convert to lowercase
        lower_case_filename = filename.lower()
        # Replace spaces with dashes
        dash_filename = lower_case_filename.replace(" ", "-")
        return dash_filename

    def run_python_script(self, script_content):
        print(self.test_method)
        if self.test_method == "static":
            # Static testing
            try:
                # Attempt to compile the script content
                compile(script_content, '<string>', 'exec')
                print("Script is syntactically correct.")
                return 1
            except SyntaxError as e:
                # Handle the syntax error
                print(f"Script has a syntax error:\n{e}")
                self.fix_code(script_content, e)
                return 0
        else:
            # Dynamic testing
            try:
                result = subprocess.run([sys.executable, '-c', script_content], capture_output=True, text=True, check=True, timeout=50)
                print(result.stdout)
                print("Script executed successfully")
                return 1
            except subprocess.CalledProcessError as e:
                print("Error: Script execution failed with exit code", e.returncode)
                print("Output:", e.output)
                print("Script failed with error:\n", e.stderr)
                self.fix_code(script_content, e.stderr)
                return

    def fix_code(self, broken_code, e):
        analyse_error = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You analyse error messages in code and provide solutions."},
                {"role": "assistant", "content": f"The user provided code has an error when executed.: \n{e}\n. Access the internet and then suggest a fix."},
                {"role": "user", "content": broken_code},
            ],
            temperature=1,
            max_tokens=200
        )

        error_analysis = analyse_error.choices[0].message.content
        print("-----------------------------")
        print(e)
        print(error_analysis)

        fix_code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You fix code based on an error message"},
                {"role": "assistant", "content": f"The code has an error: \n{e}\n. the analysis of this error is: {error_analysis}"},
                {"role": "user", "content": f"Based on the error anlaysis: {error_analysis} - Fix the error in the code: \n{broken_code}\n .{self.no_markdown}"},
            ],
            temperature=1.2,
            max_tokens=1200
        )

        fixed_code = fix_code.choices[0].message.content
        print("-----------------------------")
        print(fixed_code)
        self.run_python_script(fixed_code)

    gen_code_it = 0
    def gen_code(self, c, guidance, o, n):
        package_list = self.read_file("./", "requirements", "txt")
        enhancements = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "assistant", "content": f"{guidance}"},
                {"role": "assistant", "content": f"If importing Python modules use only the following modules: \n{package_list}\n"},
                {"role": "user", "content": f"Code idea is: {o}. Suggest 3 enhancements to the following code to achieve the idea: \n {c}"}
            ],
            temperature=1.3,
            max_tokens=250
        )

        code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You engineer improvements to code, based on provided feedback."},
                {"role": "assistant", "content": f"The feedback is: \n{enhancements}\n. {guidance}"},
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
            max_tokens=50
        )

        e = enhancements.choices[0].message.content
        print(e)
        c = code.choices[0].message.content
        
        # Test script
        success_exec = self.run_python_script(c)
        # File operations
        m = self.clean_filename(meta.choices[0].message.content) # clean and add dashes to filename
        print(m)
        n+=1

        script_path = f"gen_code/{self.clean_filename(o)}"
        self.save_file(c, script_path, f"{n}-{m}", "py")

        return e,c,m

    def recursive_gpt(self, c, o, n, pl):
        print(c)
        e,c,m = self.gen_code(f"Code idea is: {o}. Language is: {pl}. The current code is \n{c}\n .Enhance the code based on provided feedback. Always demo the code working", f"{self.no_markdown}", o, n) # raw code
        n+=1
        self.recursive_gpt(c, o, n, pl)
        pass

def main():
    recgpt = Recursive_GPT()
    # Enter code to generate here:
    ###################################################################
    pl = "Linux GUI"
    code_idea = "2 bots playing pong"
    """
    Test method
    Scripts can either be executed to test for errors, or compiled to test. 
    In general if you are generating scripts that take a long time or do not close it is best to only compile.
    Scripts that end by themselves can be tested dynamically for greater accuracy.
    Select:
    dynamic: for short running scripts E.G. scan network
    static: for running scripts E.G. launch a GUI
    """
    recgpt.test_method = "static" # dynamic | static
    ###################################################################
    # Modify the following only for existing code upload
    regenerate_existing = 0 # 1 to load code, 2 to generate new code
    filename = "5-bot-feel" # file to load
    ext = "py"
    ###################################################################

    code_idea_dir = recgpt.clean_filename(code_idea)

    if not os.path.exists(f"gen_code/{code_idea_dir}"):
        os.makedirs(f"gen_code/{code_idea_dir}")

    # Set to 1 to continue with exisiting code
    if regenerate_existing == 1:
        try:
            n = int(filename[0]) # Continue from current file number
        except:
            n = 0
        existing_code = recgpt.read_file("gen_code/" + code_idea_dir, filename, ext) # read file
        recgpt.recursive_gpt(existing_code, code_idea, n, pl)
    else:
        n=0# current code generation iteration
        recgpt.recursive_gpt(code_idea, code_idea, n, pl) # passed in twice to retain context during recursion

if __name__ == "__main__":
    main()