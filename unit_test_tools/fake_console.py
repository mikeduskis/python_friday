from time import sleep


class InputStream:
    """
    StringIO that blocks on readline, as sys.stdout does
    """

    def __init__(self):
        self._buf = ''

    def read(self):
        s = self._buf
        self._buf = ''
        return s

    def readline(self):
        while True:
            eol = self._buf.find('\n')
            if -1 == eol:
                sleep(0.05)  # Don't burn CPU
            else:
                line = self._buf[:eol]
                self._buf = self._buf[eol + 1:]
                return line

    def write(self, s):
        self._buf += s


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
