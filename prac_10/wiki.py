import wikipedia


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            search_result = wikipedia.page(title, auto_suggest=False)

        except wikipedia.exceptions.DisambiguationError as suggestion:
            pass

        except wikipedia.exceptions.PageError:
            pass

        title = input("Enter page title: ").strip()
    print("Thank you")

main()
