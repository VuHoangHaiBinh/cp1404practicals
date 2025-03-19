"""
Estimated time: 30 minutes
Actual time:
"""
from datetime import datetime

from project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = get_valid_name("Filename: ")
            projects = load_projects(filename)

        elif choice == 'd':
            incomplete_projects, completed_projects = categorize_project(projects)
            print("Incomplete projects:")
            for project in incomplete_projects: 
                print(f"\t{project}")
            print("Completed projects:")
            for project in completed_projects: 
                print(f"\t{project}")

        elif choice == 'f':
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = filter_projects(date, projects)
            print(project for project in filtered_projects)

        elif choice == 'u':
            for index, project in enumerate(projects):
                print(f"{index} {project}")
            project_choice = int(get_valid_number("Project choice: ", lower_bound=0, upper_bound=len(projects) - 1))
            choosen_project = projects[project_choice]
            print(choosen_project)
            completion = get_valid_number("New Percentage: ", lower_bound=0, upper_bound=100, none_allowed=True)
            priority = get_valid_number("New Priority: ", lower_bound=1, upper_bound=None, none_allowed=True)
            choosen_project.completion = int(completion) if completion is not None else choosen_project.completion
            choosen_project.priority = int(priority) if priority is not None else choosen_project.priority

        elif choice == 'a':
            print("Let's add a new project")
            name = get_valid_name("Name: ")
            start_date = get_valid_date("Start date (dd/mm/yy): ")
            priority = int(get_valid_number("Priority: ", lower_bound=1, upper_bound=None))
            estimated_cost = get_valid_number("Cost estimate: $", lower_bound=0, upper_bound=None)
            completion = int(get_valid_number("Percent complete: ", lower_bound=0, upper_bound=100))
            projects.append(Project(name, start_date, priority, estimated_cost, completion))

        elif choice == 's':
            filename = get_valid_name("Filename: ")
            write_projects(filename, projects)

        else:
            print("Invalid choice!! Please try again!!")

        print(MENU)
        choice = input(">>> ").lower()


def test():
    name = get_valid_name("Name: ")  # Expect: input ' ' -> retry
    print(name)
    projects = load_projects("a.txt")  # Expect: 0 entries
    print(len(projects))
    projects = load_projects(FILENAME)  # Expect: 5 entries
    print(len(projects))
    for project in projects:
        print(project)
    incomplete_projects, completed_projects = categorize_project(projects)
    print(len(incomplete_projects))  # Expect: 4
    print(len(completed_projects))  # Expect: 1
    print(get_valid_date("Date: "))  # Expect: input - 41/2/2020 -> retry - input - 20/2/2020 -> pass
    filtered_projects = filter_projects("1/1/2022", projects)  # Expect 20/07/2022, 31/10/2022, 01/12/2022
    for project in filtered_projects:
        print(project)
    print(get_valid_number("Num: "))  # Expect: all number valid, letter retry
    print(get_valid_number("Num: ", lower_bound=0,
    upper_bound=100))  # Expect: all number within 0 to 100 valid, other retry
    print(get_valid_number("Num: ", lower_bound=0, upper_bound=100,
    none_allowed=True))  # Expect: all number within 0 to 100 valid and nothing, other retry
    write_projects("test.txt", projects)  # Expect: same as FILENAME content


def get_valid_name(prompt: str) -> str:
    """Repeatedly ask for name until valid."""
    name = input(prompt).strip()
    while name == '':
        print("Name cannot be blank")
        name = input(prompt).strip()
    return name


def load_projects(filename: str) -> list[Project]:
    """Open filename and return loaded data into list - empty if file does not exist."""
    projects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1::]  # Get every row except header
            for line in lines:
                parameters = line.split('\t')
                name = parameters[0]
                start_date = parameters[1]
                priority = int(parameters[2])
                estimated_cost = float(parameters[3])
                completion = int(parameters[4])
                projects.append(Project(name, start_date, priority, estimated_cost, completion))
    except FileNotFoundError:
        print("Filename was not found!! Please enter another valid filename")
    return projects


def categorize_project(projects: list[Project]) -> tuple[list[Project], list[Project]]:
    """Categorize passed in projects to incomplete or completed and sort them based on priority."""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        completed_projects.append(project) if project.completion == 100 else incomplete_projects.append(project)
    completed_projects.sort()
    incomplete_projects.sort()
    return incomplete_projects, completed_projects


def get_valid_date(prompt: str) -> str:
    """Ask for date string and convert it to date format until valid and return."""
    date = ""
    is_valid = False
    while not is_valid:
        try:
            date = input(prompt)
            _ = datetime.strptime(date, "%d/%m/%Y")  # _ means for unsed variable
            is_valid = True
        except ValueError:
            print("Invalid date format!! Please try again!!")
    return date


def filter_projects(date: str, projects: list[Project]) -> list[Project]:
    """Filter a list of projects that was created after a specified date and sorted."""
    filtered_projects = [project for project in projects if project.is_after_date(date)]
    filtered_projects.sort()
    return filtered_projects


def get_valid_number(prompt: str, lower_bound: float | None = None, upper_bound: float | None = None,
                     none_allowed: bool = False) -> float | None:
    """Repeatedly ask for a valid number based on passed in parameters until satisfied."""
    is_valid = False
    valid_number = None
    while not is_valid:
        try:
            number = input(prompt).strip()
            if not (none_allowed and number == ""):
                number = float(number)
                if lower_bound is not None and number < lower_bound:
                    print("Number must be bigger than " + str(lower_bound))
                elif upper_bound is not None and number > upper_bound:
                    print("Number must be smaller than " + str(upper_bound))
                else:
                    valid_number = number
                    is_valid = True
            else:
                is_valid = True
        except ValueError:
            print("Please enter a valid number!!")
    return valid_number


def write_projects(filename, projects):
    """Read all data from projects and save them to specified file with tab as seperator."""
    with open(filename, 'w') as file:
        for project in projects:
            file.write("\t".join(str(data) for data in
                                 [project.name, project.start_date, project.priority, project.estimated_cost,
                                  project.completion]) + "\n")


if __name__ == "__main__":
    main()
    # test()
