import os
from openai import OpenAI # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore
import subprocess
from subprocess import TimeoutExpired
import sys
import getpass

class Recursive_GPT:
    no_markdown =  "Return only the raw working code. Do not include any text or comments, just the raw code. Strictly output the working code only with no markdown. Just the raw code. ' \
                    Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just working code. The reason is that it will be executed dynamically so any broken code will cause an execution failiure."
    enhance_protocol = "You develop code, if you are provided code then your objective is to enhance the code by adding new design and functionality."
    sudo_password = 0
    use_sudo = 0

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

    def get_debug_info(self):
        info = []
        
        # Current working directory
        cwd = os.getcwd()
        info.append(f"Current working directory: {cwd}")
        
        # Home directory
        home_dir = os.path.expanduser("~")
        info.append(f"Home directory: {home_dir}")
        
        # Python executable location
        python_executable = sys.executable
        info.append(f"Python executable: {python_executable}")
        
        # List all files and directories in the current working directory
        cwd_contents = os.listdir(cwd)
        info.append(f"Contents of the current working directory: {cwd_contents}")
        
        return "\n".join(info)

    def clean_filename(self, name):
        # Remove any trailing whitespace including newline character
        filename = name.strip()
        # Convert to lowercase
        lower_case_filename = filename.lower()
        # Replace spaces with dashes
        dash_filename = lower_case_filename.replace(" ", "-")
        return dash_filename
    
    def helpful_assistant(self, pl, idea):
        first_run = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a software developer."},
                {"role": "assistant", "content": f"Develop a {pl} script that implements the provided idea. The code should not require any user input and should run automatically. {self.no_markdown}"},
                {"role": "user", "content": f"Develop a {pl} script that implements the following product idea: {idea}. Do not use path placeholders, Use real paths as per the following: {self.get_debug_info()}. "}
            ],
            temperature=1,
            max_tokens=800
        )

        res = first_run.choices[0].message.content
        print(res)
        return res

    def run_python_script(self, script_content):
        print(self.test_method)
        print("Running script...")
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
                if self.use_sudo:
                    print("Using sudo")
                    sudo_command = f"sudo -S {sys.executable} -c {script_content}"
                    result = subprocess.run(sudo_command, shell=True, capture_output=True, text=True, check=True, timeout=5)
                else:
                    print("Not using sudo")
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
                if "ModuleNotFoundError" in e.stderr:
                    self.install_actions(e.stderr)
                else:
                    broken_code, error_analysis_res = self.error_analysis(script_content, e.stderr)
                    self.fix_code(broken_code, error_analysis_res)
                return 0

    def install_actions(self, e):
        # if script requires install:
        shell_install = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You convert error messages to raw shell commands"},
                {"role": "assistant", "content": f"You will be provided and error message. The message will indicate a missing package or library. Find the correct install command for the environment. {self.no_markdown}"},
                {"role": "user", "content": f"The error message is \n{e}\n. Return only the raw bash shell command without sudo to resolve this error. E.G. pip install jq, or apt install. {self.no_markdown}"},
            ],
            temperature=1.1,
            max_tokens=200
        )

        shell_command = shell_install.choices[0].message.content
        print("-------------INSTALL SHELL COMMAND:----------------")
        print(e)
        print(shell_command)
        self.install_package(shell_command)
        return

    def install_package(self, install_command):
        confirm = input(f"\nThis script wants to install: {install_command}. \n y or n\n")
        if confirm.lower() == "y":
            self.sudo_password = getpass.getpass("Enter your sudo password: ")
            sudo_command = f"echo {self.sudo_password} | sudo -S {install_command}"
            try:
                subprocess.check_call(install_command, shell=True)
                print("Package has been installed successfully.")
            except subprocess.CalledProcessError as e:
                try:
                    print(f"Failed to install the package without sudo. Error: {e}. \n Trying with sudo...")
                    subprocess.check_call(sudo_command, shell=True)
                except subprocess.CalledProcessError as e:
                    print(f"Failed to install the package. Error: {e}")
        else: 
            print(f"please manually install: \n{install_command}\n")
            exit(0)
        return

################################################################

    def error_analysis(self, broken_code, e):
        advanced_error = ""
        if "FileNotFoundError" in e:
            print("The path could not be found, implementing local path fix...")
            debug_info = self.get_debug_info()
            advanced_error = f"There is a path error. Replace any placeholder paths in the script with real working values based on: {debug_info}"
        elif "PermissionError" in e or "root" in e or "sudo" in e or "Operation not permitted" in e:
            advanced_error = "There is a permissions error. Try sudo...."
            self.use_sudo = input("Allow root access? Y or N: ")
            if self.use_sudo.lower() == "y":
                self.use_sudo=1
    
        analyse_error = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You analyse error messages in code and provide solutions."},
                {"role": "assistant", "content": f"You will be provided some code. This code is broken and generates the following error when executed: \n{e}\n. Find the solution to fix the code. {self.no_markdown}"},
                {"role": "user", "content": f"broken code is: {broken_code}. Error is: {e}. {advanced_error}"},
            ],
            temperature=1.2,
            max_tokens=600
        )

        error_analysis = analyse_error.choices[0].message.content
        print("--------------ERROR ANALYSIS---------------")
        print(e)
        print(error_analysis)
        return broken_code, error_analysis

########################################################################

    def fix_code(self, broken_code, e):
        fix_code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You fix broken code. {self.no_markdown}"},
                {"role": "assistant", "content": f"You will be provided with a broken script, along with the error causing the script to fail. {self.no_markdown}"},
                {"role": "user", "content": f"The code is: \n{broken_code}\n. Fix the error in the line of code based on the error anlaysis: {e}. Return only the fixed the line of code. {self.no_markdown}"},
            ],
            temperature=1.2,
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
                {"role": "assistant", "content": f"You will be provided with a broken script, along with the solution code. Return the fixed script. {self.no_markdown}. Do not use path placeholders, Use real paths as per the following: {self.get_debug_info()}."},
                {"role": "user", "content": f"The code is: \n{broken_code}\n. The error is: \n{e}\n Merge the fix to fix the broken code. Do not use path placeholders, Use real paths as per the following: {self.get_debug_info()}. The error has been analysed and the provided fix is: \n{fixed_code}\n. Return the full working script. {self.no_markdown}"},
            ],
            temperature=1.1,
            max_tokens=1400
        )

        merged_code = merge_fix.choices[0].message.content
        print("-----------------------------")
        print("Code merged:")
        print(merged_code)
        print("-----------------------------")
        if self.use_sudo == 0:
            self.run_python_script(merged_code)
        else:
            self.use_sudo=1
            self.run_python_script(merged_code)

##########################################################################

    def gen_code(self, c, guidance, o, n):
        enhancements = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": c},
                {"role": "assistant", "content": f"Output as a succint plain text list."},
                {"role": "user", "content": f"Code idea is: {o}. Propose 3 features that can be added to the following code to enhance the functionality:\n {c}"}
            ],
            temperature=1.3,
            max_tokens=500
        )

        code = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You make improvements to code, based on provided feedback."},
                {"role": "assistant", "content": f"The feedback is: \n{enhancements}\n Always include a main method to output the working code. {guidance} {self.enhance_protocol}. Do not use path placeholders, Use real paths as per the following: {self.get_debug_info()}."},
                {"role": "user", "content": f"Provided code is: {c}. Output instructions: {self.no_markdown}. Do not use path placeholders, Use real paths as per the following: {self.get_debug_info()}."},
            ],
            temperature=1.1,
            max_tokens=1400
        )

        meta = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Generate a succint filename that summarizes the following enhancements: \n{enhancements}\n."}
            ],
            temperature=1,
            max_tokens=50
        )

        e = enhancements.choices[0].message.content
        print("Enhancements: ")
        print(e)
        print("-------------------------------------")
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
                {"role": "user", "content": f"Product idea is: {ci}. Language is {pl}. Provide a succint list of the core requirements for this product."}
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
                              The code should not require any user input and should run automatically. \
                              The outputted code must meet each item listed in the product requirements: \n{pr}\n \
                              Always include a main method to output the working code.", f"{self.no_markdown} {self.enhance_protocol}", o, n)
        n+=1
        # print(pr) # Product requirements
        self.recursive_gpt(c, o, n, pl, pr)

def main():
    recgpt = Recursive_GPT()
    # Enter code to generate here:
    ###################################################################
    pl = "Python"
    code_idea = "chroot"
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
    filename = "" # file to load
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
        first_run = recgpt.helpful_assistant(pl, code_idea)
        recgpt.recursive_gpt(first_run, code_idea, n, pl, pr)

if __name__ == "__main__":
    main()