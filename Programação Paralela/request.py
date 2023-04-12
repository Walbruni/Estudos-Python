
import threading
import urllib3
import time


# exemplo mais pratico de aplicacao de threads

start = time.time()
urls = ["http://www.google.com", "http://www.apple.com",
        "http://www.microsoft.com", "http://www.instagram.com"]


def chama_url(url):
    req = urllib3.request(url)  # para verificar se a url é confiável
    response = urllib3.urlopen(req)  # acessa a url
    the_page = response.read()  # realiza uma leitura
    print("carregado em %s" % {url, (time.time() - start)})
    print(the_page)


# url é um item de cada um dos elementos da lista
threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Elapsed Time: %s" % (time.time() - start))
