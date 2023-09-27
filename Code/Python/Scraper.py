#Scraper
a = ""
b = "-v1-a1.ts"
for x in range(1, 134):
    url = "https://embed-cloudfront.wistia.com/deliveries/a9cad323e15084fd0b4efc01f3aadf3952e27e6e.m3u8/seg-" + str(x) + b
    url = url.replace(" ", "")  # Remove spaces from the URL
    print(url)