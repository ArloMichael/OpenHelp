import requests
from bs4 import BeautifulSoup


def find_question(query):
    """
    Finds the top 5 Stack Overflow questions related to the query.
    """
    url = 'https://api.stackexchange.com/2.3/search'
    params = {
        'order': 'desc',
        'sort': 'votes',
        'site': 'stackoverflow',
        'pagesize': 5,
        'intitle': query
    }

    # Make the API request and check for errors
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Use a generator expression instead of a list comprehension
    question_ids = (x["question_id"] for x in data["items"])
    return question_ids


def find_best_answers(question_ids):
    """
    Yields the best answer to each question in the list of IDs.
    """
    url = "https://api.stackexchange.com/2.3/questions/{}/answers"

    for question_id in question_ids:
        params = {
            "order": "desc",
            "sort": "votes",
            "site": "stackoverflow",
            "filter": "withbody"
        }
        response = requests.get(url.format(question_id), params=params)
        response.raise_for_status()
        data = response.json()

        # Yield the first answer body string
        for answer in data["items"]:
            yield answer["body"]
            break


def extract_text(html):
    """
    Extracts the text from the given HTML using BeautifulSoup.
    """
    soup = BeautifulSoup(html, "lxml")
    return soup.get_text()


def find(query):
    """
    Returns a list of the best answer texts for the given query.
    """
    question_ids = find_question(query)
    best_answer_texts = find_best_answers(question_ids)

    # Extract the text from each answer
    return [extract_text(answer_text) for answer_text in best_answer_texts]