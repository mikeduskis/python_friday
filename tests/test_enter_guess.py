from threading import Thread
from unittest import TestCase, main

from expects import expect, match

from codebreaker import Codebreaker
from unit_test_tools import FakeConsole


class TestEnterGuess(TestCase):

    def setUp(self):
        self.console = FakeConsole()
        self.sut = Codebreaker(console=self.console)
        game_thread = Thread(target=self.sut.start, daemon=True)
        game_thread.start()
        # Read "Welcome to Codebreaker"
        self.console.stdout.readline()

    def test_returns_4_valid_chars_on_enter_guess(self):
        # Enter a guess
        self.console.stdin.write('1234\n')
        expect(self.console.stdout.readline()).to(
            match('^[0\+\-]{4}$'))


if '__main__' == __name__:
    main()
