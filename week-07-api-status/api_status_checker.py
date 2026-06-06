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

def verificar_servicios(urls):
    resultados = []
    for url in urls:
        resultado = verificar_url(url)
        resultados.append(resultado)
    return resultados

if __name__ == "__main__":
    print(verificar_servicios([
        "https://www.google.com",
        "https://www.facebook.com",
        "https://url-que-no-existe-123456.com"
    ]))