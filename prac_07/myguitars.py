from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, 'r') as file:
        lines = file.readlines()

        for line in lines:
            parameters = line.strip().split(',') 
            guitars.append(Guitar(parameters[0], int(parameters[1]), float(parameters[2])))

        for guitar in guitars:
            print(guitar)


main()
