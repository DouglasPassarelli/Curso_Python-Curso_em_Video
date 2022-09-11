import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim nao esta acessivel no momento\033[m')
else:
    print('\033[33mO Site Pudim esta acessivel\033[m')
    print(site.read())
