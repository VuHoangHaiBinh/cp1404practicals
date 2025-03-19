"""
Estimated time: 15 minutes
Actual time: 12 minutes
"""
from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"


class Project:
    def __init__(self, name: str, start_date: str, priority: int, estimated_cost: float,
                 completion: float):
        """Initialize class constructor with parameters."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimated_cost = estimated_cost
        self.completion = completion

    def __str__(self) -> str:
        """Get formatted class information."""
        return f"{self.name}, start: {self.start_date},  priority {self.priority}, estimate: ${self.estimated_cost:.2f}, completion: {self.completion}%"

    def __lt__(self, other) -> bool:
        """Get class comparison feature."""
        return self.priority < other.priority

    def is_after_date(self, date: str) -> bool:
        """Get if class start_time is after the passed in time."""
        return datetime.strptime(self.start_date, DATE_FORMAT) > datetime.strptime(date, DATE_FORMAT)


def test():
    project1 = Project("test", "11/11/2020", 2, 20.0, 0)
    print(project1)  # Expect: test, start: 11/11/2020, priority 2, estimated: $20.00, completion: 0%
    print(project1.is_after_date("10/11/2020"))  # Expect: True

    project2 = Project("test", "10/11/2020", 1, 20.0, 0)
    projects = [project1, project2]
    projects.sort()  # Expect: project 2 first then 1
    for project in projects:
        print(project)


if __name__ == "__main__":
    test()
