from io import StringIO


class FakeConsole:
    """
    Fakes sys.stdout
    """

    def __init__(self):
        self.stdin = StringIO()
        self.stdout = StringIO()
        self.stderr = StringIO()
