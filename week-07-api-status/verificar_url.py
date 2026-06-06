import requests

def verificar_url(url):
    try:
        response = requests.get(url)
        return {
            'url': url,
            'status_code': response.status_code,
            'disponible': response.status_code == 200
        }
    except requests.exceptions.ConnectionError:
        return {
            'url': url,
            'status_code': None,
            'disponible': False
        }
        
print(verificar_url("https://url-que-no-existe-123456.com"))
