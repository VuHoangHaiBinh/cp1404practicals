import wikipedia


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            search_result = wikipedia.page(title, auto_suggest=False)
            print(search_result.title)
            print(search_result.content)
            print(search_result.url)

        except wikipedia.exceptions.DisambiguationError as suggestion:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(suggestion.__dict__["options"])

        except wikipedia.exceptions.PageError:
            pass

        title = input("Enter page title: ").strip()
    print("Thank you")

main()
