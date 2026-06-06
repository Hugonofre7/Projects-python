from verificar_url import verificar_url

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