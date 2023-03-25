# api_key =  2bf6f6301f924a82b621b3aec134747f
import requests


def get_news(country, api_key='2bf6f6301f924a82b621b3aec134747f'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n', {article['title']}, '\nDESCRIPTION', {article['description']}")
        return results


print(get_news(country='Kenya'))
