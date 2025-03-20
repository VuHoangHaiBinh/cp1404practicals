"""
Estimated time: 15 minutes
Actual time: 12 minutes
"""
from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"


class Project:
    """Project class for storing project information."""

    def __init__(self, name: str, start_date: datetime, priority: int, estimated_cost: float,
                 completion: int):
        """Initialize class constructor with parameters."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion = completion

    def __str__(self) -> str:
        """Get formatted class information."""
        return (f"{self.name},"
                f" start: {self.start_date.strftime(DATE_FORMAT)},"
                f" priority {self.priority},"
                f" estimate: ${self.estimated_cost:.2f},"
                f" completion: {self.completion}%")

    def __lt__(self, other) -> bool:
        """Get class comparison feature."""
        return self.priority < other.priority

    def is_after_date(self, date: datetime) -> bool:
        """Get if class start_time is after passed in time."""
        return self.start_date >= date


def test():
    """Test for bugs or unwanted behaviors."""
    project1 = Project("test", datetime.strptime("11/11/2020", DATE_FORMAT), 2, 20.0, 0)
    print(project1)  # Expect test, start: 11/11/2020, priority 2, estimated: $20.00, completion: 0%
    print(project1.is_after_date(datetime.strptime("12/11/2020", DATE_FORMAT)))  # Expect: True

    project2 = Project("test", datetime.strptime("10/11/2020", DATE_FORMAT), 1, 20.0, 0)
    projects = [project1, project2]
    projects.sort()  # Expect project 2 first then 1
    for project in projects:
        print(project)


if __name__ == "__main__":
    test()
