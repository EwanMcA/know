import wikipedia
from openai import OpenAI


def get_random_wikipedia_article():
    """Fetch a random Wikipedia article."""
    try:
        title = wikipedia.random(pages=1)
        page = wikipedia.page(title)
        return title, page.summary, page.content
    except wikipedia.exceptions.WikipediaException as e:
        print("Error fetching Wikipedia content:", e)
        return None


def generate_trivia_questions(content, n_questions=5, multiple_choice=True):
    client = OpenAI()
    prompt = (
        f"Generate {n_questions} trivia questions based on the following text: {content}\n"
        "Keep in mind that the reader will not have access to the text when answering the questions."
        "So please provide any necessary context.\n"
        "If there isn't enough context in the text, please provide additional context.\n"
    )

    if multiple_choice:
        prompt += (
            "Please provide multiple-choice answers for each question.\n"
            "For example:\n"
            "Q: What is the capital of France?\n"
            "CORRECT: Paris\n"
            "WRONG: London\n"
            "WRONG: Berlin\n"
            "WRONG: Rome\n"
        )
    else:
        prompt += (
            "Give the questions along with the answers, in the following format:\n"
            "Q: What is the capital of France?\n"
            "A: Paris\n"
        )

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
      ],
      temperature=1.2,
    )

    print(completion.choices[0].message.content)


def main():
    title, summary, content = get_random_wikipedia_article()
    print(f"title: {title}")
    print(f"summary: {summary}")
    print(content[:1000], end="...\n\n")

    print("#" * 20)
    print("QUIZ")
    print("#" * 20)
    print(generate_trivia_questions(content[:1000], 3))


if __name__ == "__main__":
    main()
