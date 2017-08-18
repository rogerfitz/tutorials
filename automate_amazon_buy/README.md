### Automate Amazon Purchases
Next time amazon has a price glitch you can be ready. [Writeup Here](https://www.ergosum.co/scraping-draft-kings-contests/)

The script:  

1. Goes to the product page you entered
2. Signs in
3. Adds the product to cart.
4. Uses your default payment and shipping options
5. And finally, checks the total price to make sure it is $0 or whatever you've set as your MAX_BUY_PRICE.


To install: 

- download the [Chrome Web Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Install python 3.6
- Run `pip install -r requirements.txt`
- Configure your username and password in a config.py file.
