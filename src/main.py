import wikipedia


def get_random_wikipedia_article():
    """Fetch a random Wikipedia article."""
    try:
        title = wikipedia.random(pages=1)
        page = wikipedia.page(title)
        return title, page.summary, page.content
    except wikipedia.exceptions.WikipediaException as e:
        print("Error fetching Wikipedia content:", e)
        return None


def main():
    title, summary, content = get_random_wikipedia_article()
    print(f"title: {title}")
    print(f"summary: {summary}")
    print(content[:1000])


if __name__ == "__main__":
    main()
