from unittest import TestCase, main

from expects import expect, contain

from codebreaker import Codebreaker
from unit_test_tools import FakeConsole


class TestStartGame(TestCase):

    def setUp(self):
        self.console = FakeConsole()
        self.sut = Codebreaker(console=self.console)

    def test_displays_welcome_message(self):
        self.sut.start()
        expect(
            self.console.stdout.readline()).to(
                contain('Welcome to Code Breaker'))


if '__main__' == __name__:
    main()
