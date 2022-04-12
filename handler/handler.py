""" handler is a mobule to provide base handler classes
"""
#    Copyright 2017 Yoshi Yamaguchi
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class InvestmentTrustSiteHandler(object):
    """ InvestmentTrustSiteHandler is a class to provide minimum functions
    for invest trust site

    Attributes:
    :param browser webdriver.WebDriver: WebDriver instance
    :param data dict: data storage
    """

    def __init__(self, url, options:Options=None):
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(url)
        self.data = None

    def close(self):
        """ close closes WebDriver instance
        """
        self.browser.close()
        self.browser.quit()
