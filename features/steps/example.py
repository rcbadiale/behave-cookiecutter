# pylint: disable=missing-function-docstring
from behave import step  # pylint: disable=no-name-in-module
from behave.runner import Context


@step('I have a "{arg}"')
@step('I execute the "{arg}"')
@step('the "{arg}" is executed successfully')
def example_step(context: Context, arg: str):
    pass
