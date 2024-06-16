import os
from openai import OpenAI # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore
import subprocess
from subprocess import TimeoutExpired
import sys

class Recursive_GPT:
    no_markdown =  "Return only the raw working code. Do not include any text or comments, just the raw code. Strictly output the working code only with no markdown. Just the raw code. ' \
                    Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just working code. The reason is that it will be executed dynamically so any broken code will cause an execution failiure."
    enhance_protocol = "You develop code, if you are provided code then your objective is to enhance the code by adding new design and functionality."
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
                result = subprocess.run([sys.executable, '-c', script_content], capture_output=True, text=True, check=True, timeout=5)
                print(result.stdout)
                print("Script executed successfully")
                return 1
            except TimeoutExpired:
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
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You analyse error messages in code and provide solutions."},
                {"role": "assistant", "content": f"You will be provided some code. This code generates the following error when executed: \n{e}\n. Access the internet and then provide a solution to fix the code."},
                {"role": "user", "content": broken_code},
            ],
            temperature=1,
            max_tokens=200
        )

        error_analysis = analyse_error.choices[0].message.content
        print("-----------------------------")
        print(e)
        print(error_analysis)
        print("Attempting to fix code..........")
        print("-----------------------------")

        fix_code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You fix broken code. {self.no_markdown}"},
                {"role": "assistant", "content": f"You will be provided some code. This code generates the following error when executed: \n{e}\n. the error analysis is: {error_analysis}."},
                {"role": "user", "content": f"The code is: \n{broken_code}\n. Fix the error in the line of code based on the error anlaysis. {self.no_markdown}."},
            ],
            temperature=1,
            max_tokens=600
        )

        fixed_code = fix_code.choices[0].message.content
        print("-----------------------------")
        print("Code fix complete. Fixed code is:")
        print(fixed_code)
        print("-----------------------------")

        merge_fix = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a software developer. {self.no_markdown}"},
                {"role": "assistant", "content": f"You will be provided a broken script along with the solution code. Return the full working code."},
                {"role": "user", "content": f"The code is: \n{broken_code}\n. Merge the fix: {fixed_code}. {self.no_markdown}."},
            ],
            temperature=1,
            max_tokens=1200
        )

        merged_code = merge_fix.choices[0].message.content
        print("-----------------------------")
        print("Code merged:")
        print(merged_code)
        print("-----------------------------")

        self.run_python_script(merged_code)

    def gen_code(self, c, guidance, o, n):
        package_list = self.read_file("./", "requirements", "txt")
        enhancements = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": c},
                {"role": "assistant", "content": f"{guidance}"},
                {"role": "user", "content": f"Code idea is: {o}. Propose 3 features that can be added to the following code to enhance the functionality:\n {c}"}
            ],
            temperature=1.3,
            max_tokens=500
        )

        code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You make improvements to code, based on provided feedback."},
                {"role": "assistant", "content": f"If using Python packages use only the following packages: \n{package_list}\n"},
                {"role": "assistant", "content": f"The feedback is: \n{enhancements}\n Always include a main method to output the working code. {guidance} {self.enhance_protocol}"},
                {"role": "user", "content": c},
            ],
            temperature=1,
            max_tokens=1200
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
    
    def gen_requirements(self, ci, pl):
        requirements = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a product manager"},
                {"role": "assistant", "content": f"You are developing a software product."},
                {"role": "user", "content": f"Product idea is: {ci}. Language is {pl}. Provide a list of the core requirements for this product."}
            ],
            temperature=1.3,
            max_tokens=400
        )

        r = requirements.choices[0].message.content
        print("-----------------------------")
        print("Requirements: ")
        print(r)
        print("-----------------------------")
        return r

    def recursive_gpt(self, c, o, n, pl, pr):
        print(c)
        e,c,m = self.gen_code(f"You are a software developer. You are developing a product. The product idea is: {o}. Language is: {pl}. \
                              The current code is \n{c}\n .Enhance the code based on provided feedback. \
                              The outputted code must meet each item listed in the product requirements: \n{pr}\n \
                              Always include a main method to output the working code.", f"{self.no_markdown} {self.enhance_protocol}", o, n)
        n+=1
        print(pr)
        self.recursive_gpt(c, o, n, pl, pr)

def main():
    recgpt = Recursive_GPT()
    # Enter code to generate here:
    ###################################################################
    pl = "Linux GUI"
    code_idea = "local file manager"
    """
    Test method
    Scripts can either be executed to test for errors, or compiled to test. 
    In general you can leave as dynamic
    To debug persistant scripts that run a long time or do not close naturally you can try staticy
    Scripts that end by themselves can be tested dynamically for greater accuracy.
    Select:
    dynamic: for short running scripts E.G. scan network
    static: for running scripts E.G. launch a GUI
    """
    recgpt.test_method = "dynamic" # dynamic | static
    ###################################################################
    # Modify the following only for existing code upload
    regenerate_existing = 0 # 1 to load code, 2 to generate new code
    filename = "5-bot-feel" # file to load
    ext = "py"
    ###################################################################

    code_idea_dir = recgpt.clean_filename(code_idea)
    pr = recgpt.gen_requirements(code_idea, pl)

    if not os.path.exists(f"gen_code/{code_idea_dir}"):
        os.makedirs(f"gen_code/{code_idea_dir}")

    # Set to 1 to continue with exisiting code
    if regenerate_existing == 1:
        try:
            n = int(filename[0]) # Continue from current file number
        except:
            n = 0
        existing_code = recgpt.read_file("gen_code/" + code_idea_dir, filename, ext) # read file
        recgpt.recursive_gpt(existing_code, code_idea, n, pl, pr)
    else:
        n=0# current code generation iteration
        recgpt.recursive_gpt(code_idea, code_idea, n, pl, pr) # passed in twice to retain context during recursion

if __name__ == "__main__":
    main()