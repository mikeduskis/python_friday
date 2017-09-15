class Codebreaker:

    def __init__(self, *, console):
        self._console = console

    def start(self):
        self._console.stdout.write('Welcome to Code Breaker')
