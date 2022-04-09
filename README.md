# APIStock

## Intro

APIStock will use [Finnhub](https://finnhub.io/) API for viewing current stock values.

This app will work with another project called [APIStockServer](https://github.com/MateuszKon/APIStockServer).
Server is for controlling configured stock allerts, (including asking API for current stock prices for parameters 
calculation of alerts). 
Server is also for wrapping listing all stocks from Finnhub, as Finnhub API does not allow limiting requested data 
(using limit and page parameters).  

## What do you need to do to start your own server?

- get authentication-key from [finnhub](https://finnhub.io/dashboard) (you need to register an account) and put it into a file (as a text).
- set environment variable APISTOCK_KEY_FILE with path to created file containing authentication-key (absolut path or relative to project working directory)

## Used frameworks/modules

- Flask
- API requests (requests)