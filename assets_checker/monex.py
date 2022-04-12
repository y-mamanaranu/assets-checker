""" for Monex
"""
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time
import numpy as np

from .handler import InvestmentTrustSiteHandler

class MonexHandler(InvestmentTrustSiteHandler):
    """ MonexHandler is a handler for Monex
    """
    
    __url_home = "https://mxp1.monex.co.jp/pc/servlet/ITS/home/Announce"
    __url_login = "https://www.monex.co.jp/"
    __url_foreign = "https://mxp1.monex.co.jp/pc/servlet/ITS/asset/AmountListForeign?attrSrcKey=bd3b399ac43efca011"
    __url_currency = "https://mxp1.monex.co.jp/pc/servlet/ITS/asset/AmountListSummary?attrSrcKey=68cd51bccc47140582"
    
    def __init__(self, options:Options=None):
        options = options or Options()
        options.headless = False
        super().__init__(
            options=options
        )
        
        self.login_check()
        
    def login_check(self):
        self.browser.get(self.__url_home)
        if urlparse(self.browser.current_url).path == '/pc/common/err/SessionTimeOut.jsp':
            self.browser.get(self.__url_login)
            input("Please login and press Key")
            
    def update(self):
        self.browser.get(self.__url_foreign)
        time.sleep(0.5)
        html = self.browser.page_source
        html = html.replace("<br>", ";")
        self.soup_foreign = BeautifulSoup(html, 'html.parser')
        
        self.browser.get(self.__url_currency)
        time.sleep(0.5)
        html = self.browser.page_source
        self.soup_currency = BeautifulSoup(html, 'html.parser')
        
        self.update_currency()
        self.update_foreign()
        
    def update_foreign(self):
        res = self.soup_foreign.find(id="fstock-list-usa")
        res = res.find_parent("table")
        
        df, = pd.read_html(str(res))
        df = df.rename(columns={
            "銘柄": "ticker", 
            "保有株数;売却可能数量;注文済数量": "amount",
            "概算簿価単価;（参考値）": "acquisition",
            "直近株価;株価日付": "price_USD",
            "概算評価損益（円）": "valuation"
        })
        df[["ticker", "name"]] = df["ticker"].str.split(";", expand=True)
        df["amount"] = df["amount"].str.extract("(.+?);")
        df["price_USD"] = df["price_USD"].str.extract("(.+?)US\$;")
        df = df[["ticker", "name", "amount", "acquisition", "price_USD", "valuation"]].copy()
        df = df.apply(pd.to_numeric, errors="ignore")
        df["valuation_USD"] = df.amount * df.price_USD
        self.df_foreign = df
        
    def update_currency(self):
        res = self.soup_currency.find(text="お預り金・MRF残高")
        res = res.find_parent("table")

        df1, = pd.read_html(str(res))
        df1 = df1.iloc[[0], :]
        df1.iloc[0, 0] = "円"
        df1 = df1.rename(columns={"お預り金・MRF残高": "name", "資産額（円）": "valuation"})

        res = res.find_next_sibling("div")

        df2, = pd.read_html(str(res))
        df2 = df2.rename(columns={0: "name", 1: "valuation"})

        df_ammount = pd.concat([df1, df2])
        df_ammount = df_ammount.reset_index()
        del df_ammount["index"]

        res = self.soup_currency.find(text="為替レート（基準日）")
        res = res.find_parent("table")

        df, = pd.read_html(str(res))

        df1 = pd.DataFrame({"name": ["円"], "price": [1]})

        df2 = df.iloc[:, [0,1]].copy()
        df2 = df2.rename(columns={"通貨": "name", "為替レート（基準日）": "price"})
        df2.price = df2.price.str.extract("(.+?)\（.+?\）")

        df3 = df.iloc[:, [2,3]].copy()
        df3 = df3.rename(columns={"通貨.1": "name", "為替レート（基準日）.1": "price"})
        df3.price = df3.price.str.extract("(.+?)\（.+?\）")

        df_price = pd.concat([df1, df2, df3])
        df_price = df_price.reset_index()
        del df_price["index"]

        df = pd.merge(df_price, df_ammount)
        df = df.apply(pd.to_numeric, errors="ignore")
        df["ammount"] = df.valuation / df.price
        df.iloc[0, -1] = df.iloc[0, -1].astype(int)
        df.iloc[1, -1] = np.round(df.iloc[1, -1],decimals=2)
        self.df_currency = df