from io import StringIO


class InputStream(StringIO):
    """
    StringIO that blocks on readline, as sys.stdout does
    """

    def readline(self):
        line = ''
        while '\n' not in line:
            line += self.read()
        return line


class FakeConsole:
    """
    Fakes sys.stdout
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.stdin = InputStream()
        self.stdout = InputStream()
        self.stderr = InputStream()
