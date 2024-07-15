# pylint: disable=unused-argument
import logging
import sys

from behave.model import Feature, Scenario, Status, Step
from behave.runner import Context

from helpers.profiler import Profiler

# Setup the logger
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)


def before_all(context: Context) -> None:
    """
    Executes the setup for the test environment.
    """
    context.logger = logger

    # Variables for scenario profiling
    context.profiling = context.config.userdata.get('profiling') != 'false'
    context.profiler = Profiler()


def before_feature(context: Context, feature: Feature) -> None:
    """
    Executes preparations before running a feature.
    """


def before_scenario(context: Context, scenario: Scenario) -> None:
    """
    Executes preparations before running a scenario.
    """
    # Log the start of the scenario
    sys.stdout.write('\n\n' + '*-' * 50 + '\n')
    sys.stdout.flush()
    context.logger.info(f'before_scenario: {scenario.name}')

    # Skip scenarios with the "skip" tag
    if 'skip' in scenario.effective_tags:
        scenario.skip(reason='Skipped')
        return

    # Start profiling for the current scenario
    context.profiler.start(scenario.name)


def before_step(context: Context, step: Step) -> None:
    """
    Executes preparations before running a step.
    """


def after_step(context: Context, step: Step) -> None:
    """
    Executes teardown after running a step.
    """


def after_scenario(context: Context, scenario: Scenario) -> None:
    """
    Executes teardown after running a scenario.
    """
    # Log the completion of the scenario
    sys.stdout.write('\n')
    sys.stdout.flush()
    context.logger.info(f'after_scenario: {scenario.name}')

    # Stop execution if the scenario is skipped
    if scenario.status == Status.skipped:
        return

    # End profiling for the current scenario
    context.profiler.end(scenario.name)


def after_feature(context: Context, feature: Feature) -> None:
    """
    Executes teardown after running a feature.
    """


def after_all(context: Context) -> None:
    """
    Executes teardown for the test environment.
    """
    # Print the profiler report
    sys.stdout.write(context.profiler.report(context.profiling))
    sys.stdout.flush()
