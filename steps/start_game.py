from behave import given, when, then
from expects import expect, contain

from unit_test_tools import FakeConsole

from codebreaker import Codebreaker


@given(u'the game is not running')
def step_impl(context):
    # Not running is the initial state
    pass


@when(u'the user types "python -m codebreaker"')  # noqa: F811
def step_impl(context):
    # When the user types this text, the module gets loaded
    context.fake_console = FakeConsole()
    context.game = Codebreaker(console=context.fake_console)
    context.game.start()


@then(u'the game displays "Welcome to Code Breaker"')  # noqa: F811
def step_impl(context):
    actual = context.fake_console.stdout.readline()
    expect(actual).to(contain('Welcome to Code Breaker'))
