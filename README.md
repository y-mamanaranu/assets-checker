# Assets Checker
Aquire assets data from brokerage accounts.

## Usage
### SBI
For SBI
```
handler = SBIHandler()
handler.update()
handler.close()

handler.df_domestic
> DataFrame for Domestic Stock
handler.df_foreign
> DataFrame for Foreign Stock
handler.df_currency
> DataFrame for Currency
```

### Options
If you use Chromium browser but not Chrome, use `binary_location`.
```
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
```

If you use browser extentions, setting profile via `--user-data-dir` is covininet.
```
options.add_argument(f"--user-data-dir=/Users/USERNAME/.config/selenium/cache")
```

Pass the option at initialization.
```
handler = SBIHandler(options)
```

## Expected User
* SBI証券.
* マネックス証券.
* 楽天証券.
* bitFlyer.
* Coincheck.

## File IO
Handle numbers with currency units.

* ECSV.
* Python configuration file.

## Forked from
* (ymotongpoo/parvenu)[https://github.com/ymotongpoo/parvenu]

## See Also
* [python:keyringによるパスワード管理 - Qiita](https://qiita.com/hidelafoglia/items/cf84870dd7939524e3e9)
* [【Python入門】プログラミングで自分だけの株価データを手に入れよう | CodeCampus](https://blog.codecamp.jp/programming-python-stockprice)
* [PythonでSBI証券に自動ログインして株価チェックする（Mechanize編） | ねほり.com](https://nehori.com/nikki/2020/08/25/post-18003/)
