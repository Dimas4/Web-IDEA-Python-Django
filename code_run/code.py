from .backend.backend import BackEnd


class Code:
    def __init__(self, code):
        self.code = code

        self.backend = BackEnd(code)

    def check_code(self):
        return self.backend.run_code()
