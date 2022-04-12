""" handler is a mobule to provide base handler classes
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class InvestmentTrustSiteHandler(object):
    """ InvestmentTrustSiteHandler is a class to provide minimum functions
    for invest trust site

    Attributes:
    :param browser webdriver.WebDriver: WebDriver instance
    :param data dict: data storage
    """

    def __init__(self, options:Options=None):
        self.browser = webdriver.Chrome(options=options)

    def close(self):
        """ close closes WebDriver instance
        """
        self.browser.close()
        self.browser.quit()
