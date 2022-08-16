from requests_html import HTMLSession

def getPrices(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }

    print(product)
    return product


getPrices('https://www.amazon.co.uk/iPhone-Charger-Cable-Lightning-Compatible/dp/B08F2NDB39?ref_=Oct_d_oup_d_560800&pd_rd_w=TtYu9&content-id=amzn1.sym.cf168abf-8d77-4933-98b1-3151f5974581&pf_rd_p=cf168abf-8d77-4933-98b1-3151f5974581&pf_rd_r=29D7F0H9VJZ4XKR3P81Q&pd_rd_wg=AsMvu&pd_rd_r=dc5ed78e-9d5d-434b-955b-92b1aeaaa3b5&pd_rd_i=B08F2NDB39')