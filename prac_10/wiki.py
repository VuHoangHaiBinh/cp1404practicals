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
            pass

        except wikipedia.exceptions.PageError:
            pass

        title = input("Enter page title: ").strip()
    print("Thank you")

main()
