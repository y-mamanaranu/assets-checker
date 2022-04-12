""" for bitFlyer
"""
import pybitflyer
import pandas as pd
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from handler.handler import InvestmentTrustSiteHandler

class bitFlyerHandler(InvestmentTrustSiteHandler):
    """ bitFlyerHandler is a handler for bitFlyer
    """
    
    __url_home = "https://bitflyer.com/ja-jp/ex/Home"

    def __init__(self, options:Options=None):
        options = options or Options()
        options.headless = True
        super().__init__(
            options=options
        )

    def update(self, api_key, api_secret):
        api = pybitflyer.API(api_key=api_key, api_secret=api_secret)
        balances = api.getbalance()
        
        df1 = pd.DataFrame(balances)
        df1 = df1.rename(columns={"currency_code":"tikcer"})
        df1 = df1[["tikcer", "amount"]]
        
        self.browser.get(self.__url_home)
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        res = soup.find(id="fundsInfo")
        res = res.findChildren("table")[0]
        
        df2, = pd.read_html(str(res))
        df2 = df2.rename(columns={"Unnamed: 0": "tikcer", "価格": "price"})
        df2 = df2.iloc[1: , :]
        df2 = df2[["tikcer", "price"]].copy()
        df2.iloc[0,1] = 1

        df = df1.merge(df2)
        df = df.apply(pd.to_numeric, errors="ignore")
        df["valuation"] = df["amount"] * df["price"]
        self.df = df