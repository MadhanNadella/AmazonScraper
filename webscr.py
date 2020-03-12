import bs4 as bs
import urllib.request
import pandas as pd

sauce= urllib.request.urlopen("https://www.amazon.in/s?k=headphones&ref=nb_sb_noss_2").read()
soup = bs.BeautifulSoup(sauce, 'lxml')

products= []
prices= []
ratings= []

for d in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
        name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        price = d.find('span', attrs={'class':'a-offscreen'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})


        if name is not None:
            products.append(name.text)
        else:
            products.append("unknown-product")
 
        if price is not None:
            prices.append(price.text)
        else:
            prices.append('$0')
		
        if rating is not None:
            ratings.append(rating.text)
        else:
            ratings.append('-1')

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')


