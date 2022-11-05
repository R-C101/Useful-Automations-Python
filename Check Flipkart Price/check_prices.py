import bs4
import requests

producturl = str(input("Enter the Product URL: "))

def get_flipkart_price(producturl):
    res = requests.get(producturl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d')
    return elems[0].text.strip()
    
    
price = get_flipkart_price(producturl)
print(price)