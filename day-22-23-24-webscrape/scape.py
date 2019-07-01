import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=&find_loc=Sydney+New+South+Wales%2C+Australia&ns=1'
loc = 'Sydney New South Wales, Australia'
current_page = 0

while current_page < 30:
    print(current_page)
    url = base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div', {'class': 'lemon--div__373c0__1mboc largerScrollablePhotos__373c0__3FEIJ arrange__373c0__UHqhV border-color--default__373c0__2oFDT'})
        for i in businesses:
            title = i.findAll('div', {'class': 'lemon--div__373c0__1mboc businessName__373c0__1fTgn border-color--default__373c0__2oFDT'})[0].text
            print(title)
            try:
                phone = i.findAll('p', {'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})[0].text
            except:
                phone = None
            print(phone)
            try:
                address = i.findAll('div', {'class': 'lemon--div__373c0__1mboc display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'})[0].text
            except:
                address = None
            print(address)
            textfile.write(title+"\n"+phone+"\n"+address+"\n")
    current_page += 10