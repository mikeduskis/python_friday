from unittest import TestCase, main

from expects import expect, match

from codebreaker import Codebreaker
from unit_test_tools import FakeConsole


class TestEnterGuess(TestCase):

    def setUp(self):
        self.console = FakeConsole()
        self.sut = Codebreaker(console=self.console)
        self.sut.start()

    def test_returns_4_valid_chars_on_enter_guess(self):
        # Enter a guess
        self.console.stdin.write('1234\n')
        expect(self.console.stdout.getvalue()).to(
            match('[0\+\-]{4}'))


if '__main__' == __name__:
    main()
