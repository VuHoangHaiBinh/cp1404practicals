import wikipedia


def main():
    """Get title until blank and search it up wiki with suggestions."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            search_result = wikipedia.page(title, auto_suggest=False)
            print(search_result.title)
            print(search_result.content)
            print(search_result.url)

        # Print suggestions if search title is too abstract
        except wikipedia.exceptions.DisambiguationError as suggestion:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(suggestion.__dict__["options"])

        # Alert not found id in wiki database
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        title = input("Enter page title: ").strip()
    print("Thank you")

main()
