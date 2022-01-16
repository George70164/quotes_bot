from urllib import request
import json

def quote():
    hdrs = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,ru-RU;q=0.7',
        'Origin': 'https://forismatic.com',
        'Referer': 'https://forismatic.com/ru/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }

    req = request.Request('http://forismatic.com/api/1.0/', data = 'method=getQuote&format=json&param=ms&lang=ru'.encode('utf-8'), headers=hdrs )
    res = request.urlopen(req)

    quote = json.loads(res.read().decode('utf-8'))

    #print(quote)
    return quote['quoteText']

#new_file = open('Цитаты.txt', 'a')
#new_file.write(quote['quoteText'])
#print("link: " + quote['quoteLink'])
