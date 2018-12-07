import subprocess


class BackEnd:
    def __init__(self, code):
        self.code = code

    def run_code(self):
        with open("file.py", "w") as file:
            file.write(self.code)

        command = ['python3', 'file.py']
        out = subprocess.Popen(command, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

        std, _ = out.communicate()
        return std.decode('utf-8').strip()
