"""
Estimated time: 30mins
Actual time:
"""
from project import Project

FILENAME = "projects.txt"
MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

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
            display_projects(projects)

        elif choice == 'f':
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = filter_projects(date, projects)
            print(project for project in filtered_projects)

        elif choice == 'u':
            for index, project in enumerate(projects): 
                print(f"{index} {project}")
            project_choice = get_valid_number("Project choice: ", lower_bound=0, upper_bound=len(projects)-1)
            choosen_project = projects[project_choice]
            print(choosen_project)
            completion = get_valid_number("New percent: ", lower_bound=0, upper_bound=100, none_allowed=True)
            priority = get_valid_number("New percent: ", lower_bound=1, upper_bound=None, none_allowed=True)
            choosen_project.completion = completion if not completion else choosen_project.completion
            choosen_project.priority = priority if not priority else choosen_project.priority

        elif choice == 'a':
            print("Let's add a new project") 
            name = get_valid_name("Name: ")
            start_date = get_valid_date("Start date (dd/mm/yy): ")
            priority = int(get_valid_number("Priority: ", lower_bound=1, upper_bound=None))
            estimated_cost = get_valid_number("Cost estimate: $", lower_bound=0, upper_bound=None) 
            completion = get_valid_number("Percent complete: ", lower_bound=0, upper_bound=100)
            projects.append(Project(name, start_date, priority, estimated_cost, completion))
        
        elif choice == 's': 
            filename = get_valid_name("Filename: ")
            write_projects(filename, projects)

        else:
            print("Invalid choice!! Please try again!!")

        print(MENU)
        choice = input(">>> ").lower()



def test():
    name = get_valid_name("Name: ") # Expect: input ' ' -> retry
    print(name)
    projects = load_projects(FILENAME) # Expect: 5 entries
    print(len(projects))
    projects = load_projects("a.txt") # Expect: 0 entries
    print(len(projects))



def get_valid_name(prompt): 
    """Repeatedly ask for name until valid."""
    name = input(prompt).strip()
    while name == '':
        print("Name cannot be blank")
        name = input(prompt).strip()
    return name


def load_projects(filename) -> list[Project]:
    """Open filename and return loaded data into list - empty if file does not exist."""
    projects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1::] # Get every rows except header
            for line in lines:
                parameters = line.split('\t')
                projects.append(Project(*parameters))
    except FileNotFoundError:
        print("Filename was not found!! Please enter another valid filename")
    return projects


if __name__ == "__main__":
    # main()
    test()
