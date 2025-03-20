"""
Estimated time: 30 minutes
Actual time: 90 minutes
"""
from datetime import datetime
from operator import attrgetter

from project import DATE_FORMAT
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
    """Load projects, show ui to update, add, display, filter, save, load new until quit."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            projects = load_projects(get_valid_name("Filename: "))

        elif choice == 'd':
            incomplete_projects, completed_projects = categorize_project(projects)
            print("Incomplete projects:")
            print(f"{'\n'.join('\t'+str(project) for project in incomplete_projects)}")
            print("Completed projects:")
            print(f"{'\n'.join('\t'+str(project) for project in completed_projects)}")

        elif choice == 'f':
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ", DATE_FORMAT)
            filtered_projects = filter_projects(date, projects)
            for project in filtered_projects:
                print(project)

        elif choice == 'u':
            for index, project in enumerate(projects):
                print(f"{index} {project}")
            project_choice = int(get_valid_number("Project choice: ",
                                                  lower_bound=0,
                                                  upper_bound=len(projects) - 1))
            chosen_project = projects[project_choice]
            print(chosen_project)
            completion = get_valid_number("New Percentage: ",
                                          lower_bound=0,
                                          upper_bound=100,
                                          none_allowed=True)
            priority = get_valid_number("New Priority: ",
                                        lower_bound=1,
                                        upper_bound=None,
                                        none_allowed=True)
            chosen_project.completion = int(completion) if completion is not None \
                else chosen_project.completion
            chosen_project.priority = int(priority) if priority is not None \
                else chosen_project.priority

        elif choice == 'a':
            print("Let's add a new project")
            name = get_valid_name("Name: ")
            start_date = get_valid_date("Start date (dd/mm/yy): ", DATE_FORMAT)
            priority = int(get_valid_number("Priority: ",
                                            lower_bound=1,
                                            upper_bound=None))
            estimated_cost = get_valid_number("Cost estimate: $",
                                              lower_bound=0,
                                              upper_bound=None)
            completion = int(get_valid_number("Percent complete: ",
                                              lower_bound=0,
                                              upper_bound=100))
            projects.append(Project(name, start_date, priority, estimated_cost, completion))

        elif choice == 's':
            write_projects(get_valid_name("Filename: "), projects)

        else:
            print("Invalid choice!! Please try again!!")

        print(MENU)
        choice = input(">>> ").lower()
    choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if choice not in ("n", "no"):
        write_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def test():
    """Test for all bugs of individual modules."""
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
    print(get_valid_date("Date: ", DATE_FORMAT))  # Expect: input - 41/2/2020 -> retry
    filtered_projects = filter_projects(datetime.strptime("1/1/2022", DATE_FORMAT),
                                        projects)  # Expect 20/07 31/10 01/12
    for project in filtered_projects:
        print(project)
    print(get_valid_number("Num: "))  # Expect: all number valid, letter retry
    print(get_valid_number("Num: ",
                           lower_bound=0,
                           upper_bound=100))  # Expect: 0->100 -> valid
    print(get_valid_number("Num: ",
                           lower_bound=0,
                           upper_bound=100,
                           none_allowed=True))  # Expect: 1->100 and blank -> valid
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
        with open(filename, 'r', encoding="utf-8") as file:
            lines = file.readlines()[1::]  # Get every row except header
            for line in lines:
                parameters = line.split('\t')
                name = parameters[0]
                start_date = datetime.strptime(parameters[1], DATE_FORMAT)
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
        if project.completion == 100:
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    completed_projects.sort()
    incomplete_projects.sort()
    return incomplete_projects, completed_projects


def get_valid_date(prompt: str, date_format: str) -> datetime:
    """Ask for date string and convert it to date format until valid and return."""
    is_valid = False
    while not is_valid:
        try:
            date = input(prompt)
            date = datetime.strptime(date, date_format)
            is_valid = True
        except ValueError:
            print("Invalid date format!! Please try again!!")
    return date


def filter_projects(date: datetime, projects: list[Project]) -> list[Project]:
    """Filter a list of projects that was created after a specified date and sorted."""
    filtered_projects = [project for project in projects if project.is_after_date(date)]
    filtered_projects.sort(key=attrgetter("start_date"))
    return filtered_projects


def get_valid_number(prompt: str,
                     lower_bound: float | None = None,
                     upper_bound: float | None = None,
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
    with open(filename, 'w', encoding="utf-8") as file:
        for project in projects:
            attributes = [project.name,
                          project.start_date,
                          project.priority,
                          project.estimated_cost,
                          project.completion]
            file.write("\t".join(str(data) for data in attributes) + "\n")


if __name__ == "__main__":
    main()
    # test()
