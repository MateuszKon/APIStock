# APIStock

## Intro

APIStock uses [Finnhub](https://finnhub.io/) API for viewing current stock values.
This app works with another project called APIStockServer. Server is used for controlling configured stock allerts, (including asking Finnhub for current stock prices for that matter). Server is also used as wrapper for listing all stocks from Finnhub, as Finnhub API does not allow limitting requested data (using limit and page parameters).  

## What do you need to do to start your own server?

- get authentication-key from [finnhub](https://finnhub.io/dashboard) (you need to register an account) and put it into a file (as a text).
- set environment variable APISTOCK_KEY_FILE with path to created file containing authentication-key (absolut path or relative to project working directory)

