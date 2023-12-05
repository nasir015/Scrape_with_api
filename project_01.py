import requests
data = []
for i in range(1, 10):
    url = f"https://bikroy.com/data/serp?top_ads=2&spotlights=5&sort=date&order=desc&buy_now=0&urgent=0&categorySlug=mobiles&locationSlug=bangladesh&category=101&page={i}&filter_json=[]"
    req = requests.get(url)
    response = req.json()

    for product in range(0, 25):
        
        try:
            title = response['ads'][product]['title']
        except:
            title = None
        try:
            description = response['ads'][product]['description']
        except:
            description = None
        try:
            imgUrl = response['ads'][product]['imgUrl']
        except:
            imgUrl = None
        try:
            price = response['ads'][product]['price']
        except:
            price = None
        try:
            location = response['ads'][product]['location']
        except:
            location = None

        data.append({
            'title': title,
            'description': description,
            'imgUrl': imgUrl,
            'price': price,
            'location': location
        })

        print('--'*20)
        print(title)
        print(description)
        print(imgUrl)
        print(price)
        print(location)
        print('--'*20)
