from io import StringIO
import re

from behave import given, when, then

from codebreaker import Codebreaker
from unit_test_tools import FakeConsole


@given(u'the game has been started')
def step_impl(context):
    # Instantiate the game
    context.console = FakeConsole()
    context.game = Codebreaker(console=context.console)
    # Start the game
    context.game.start()
    # Reset standard output
    context.console.stdout = StringIO()


@when(u'the player enters a string of four digits')  # noqa: F811
def step_impl(context):
    context.console.stdin = StringIO(initial_value='1234\n')

@then(u'the game displays exactly four zeros, plusses and/or minuses')  # noqa
def step_impl(context):
    # Verify standard output contains the expected text
    expected = re.compile('^[0\-\+]{4}$')
    actual = context.console.stdout.getvalue()
    matched = expected.match(actual)
    assert matched, '"%s" did not match the expected pattern' % actual

@when(u'the player enters a string that is not exactly four digits')  # noqa
def step_impl(context):
    raise NotImplementedError(
        'STEP: When the player enters a string that is not exactly '
        'four digits')


@then(u'the game displays "Please enter four digits."')  # noqa: F811
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the game displays "Please enter four digits."')
