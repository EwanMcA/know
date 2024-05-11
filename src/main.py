import wikipedia


def get_random_wikipedia_article():
    """Fetch a random Wikipedia article."""
    try:
        random_title = wikipedia.random(pages=1)
        page = wikipedia.page(random_title)
        summary = wikipedia.page(random_title)
        return random_title, page.content
    except wikipedia.exceptions.WikipediaException as e:
        print("Error fetching Wikipedia content:", e)
        return None


def main():
    title, content = get_random_wikipedia_article()
    print(title)
    print(content[:1000])


if __name__ == "__main__":
    main()

