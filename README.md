# Assets Checker
Aquire assets data from brokerage accounts in JP.

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

### Monex
For Monex
```
Monex = MonexHandler()
Monex.update()
Monex.close()

Monex.df_currency
> DataFrame for Foreign Stock
Monex.df_foreign
> DataFrame for Currency
```

### bitFlyer
For bitFlyer
Before you run this code, you have to acquire `api_key` and `api_secret` from [bitFlyer Lightning API](https://lightning.bitflyer.com/docs?lang=ja&_gl=1*t1rrjv*_ga*NzU1MzkzODkzLjE2NDg3OTU3MTg.*_ga_3VYMQNCVSM*MTY0OTc1Njc5OC40LjEuMTY0OTc1ODI0OS41MA..).
Check `資産残高を取得` and `証拠金の状態を取得` in allowance page.
```
bitFlyer = bitFlyerHandler()
bitFlyer.update(api_key, api_secret)
bitFlyer.close()

bitFlyer.df
> DataFrame for All
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
* [x] SBI証券 (国内株、米国株)
* [x] マネックス証券 (米国株)
* [ ] 楽天証券
* [x] bitFlyer
* [ ] Coincheck

## File IO
Handle numbers with currency units.

* ECSV.
* Python configuration file.

## Forked from
* [ymotongpoo/parvenu](https://github.com/ymotongpoo/parvenu)

## See Also
* [python:keyringによるパスワード管理 - Qiita](https://qiita.com/hidelafoglia/items/cf84870dd7939524e3e9)
* [【Python入門】プログラミングで自分だけの株価データを手に入れよう | CodeCampus](https://blog.codecamp.jp/programming-python-stockprice)
* [PythonでSBI証券に自動ログインして株価チェックする（Mechanize編） | ねほり.com](https://nehori.com/nikki/2020/08/25/post-18003/)

## LICENSE
Copyright 2017 Yoshi Yamaguchi<br/>
Copyright 2022 Yoiduki \<y-muen\>

Licensed under the Apache License, Version 2.0 (the "License")