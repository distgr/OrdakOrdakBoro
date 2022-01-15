import bs4
import requests

class DuckDuckGo():
    def __init__(self, headers=None) -> None:
        self.headers = {
            'User-Agent': ' '.join([
                'Mozilla/5.0',
                '(X11; Linux x86_64; rv:96.0)',
                'Gecko/20100101 Firefox/96.0'
            ])
        } if not headers else headers

    def search(self, query):
        output = list()
        ddg = requests.get(
            'https://html.duckduckgo.com/html/?q={}'.format(query),
            headers=self.headers)
        soup = bs4.BeautifulSoup(ddg.text, 'html.parser')
        
        for r in soup.find('div', {'class': 'results'}).find_all(
                'div', {'class': 'result'}):
            try:
                output.append({
                    'title': r.a.text,
                    'href': r.a.get('href'),
                    'desc': r.find('a', {'class': 'result__snippet'}).text
                })
            except:
                continue

        return output