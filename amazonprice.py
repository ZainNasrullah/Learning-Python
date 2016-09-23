import bs4, requests, sys


def getAmazonPrice(productUrl):
    #goes to the url provided and stores result in a request object
    res = requests.get(productUrl)
    res.raise_for_status()

    #parses the HTML of the page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #searches for the CSS element that contains the price and selects it
    elems = soup.select('#buyNewSection > div > div > span > span')
    #must take the 0th element because select returns a list type
    return elems[0].text.strip()
    

print('Please input a URL:')
URL = input()
price = getAmazonPrice(URL)
print('The price is ' + price)
