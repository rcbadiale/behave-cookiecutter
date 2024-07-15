from datetime import datetime

class Profiler:
    """
    Object for profiling scenario execution.
    """
    execution_start: datetime
    data: dict[str, dict]
    execution_end: datetime

    def __init__(self) -> None:
        self.execution_start = datetime.now()
        self.data = {}

    def start(self, name: str) -> None:
        """
        Records the start time of a given scenario.

        Args:
            name (str): Name of the scenario.
        """
        self.data[name] = {}
        self.data[name]['start'] = datetime.now()

    def end(self, name: str) -> None:
        """
        Records the end time of a given scenario.

        Args:
            name (str): Name of the scenario.
        """
        self.data[name]['end'] = datetime.now()

    def report(self, full: bool = False) -> str:
        """
        Generates the final execution report.

        Args:
            full (bool, optional): If True, returns the execution time of each
                scenario. If False, returns only the overall execution time
                of the tests. Default = False.

        Returns:
            str: Execution time report.
        """
        self.execution_end = datetime.now()

        delta = (self.execution_end - self.execution_start).seconds
        runtime = (
            f'{"*" * 21} RUNTIME {"*" * 21}\n'
            f'Started at {self.execution_start.isoformat()}\n'
            f'Ended at {self.execution_end.isoformat()}\n'
            f'Time passed: {delta}s\n'
            f'{"*" * 51}\n'
        )

        if not full:
            return runtime

        profile = f'{"*" * 21} PROFILE {"*" * 21}\n'
        for scenario, times in self.data.items():
            delta = (times["end"] - times["start"]).seconds
            profile += f'({delta}s) {scenario}\n'

        return profile + runtime
