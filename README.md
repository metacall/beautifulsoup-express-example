# Using BeautifulSoup (Python) mixed with Express (NodeJS) with MetaCall

<div align="center">
  <a href="https://medium.com/@metacall/this-scraping-serverless-polyglot-is-metacall-c13223ae1cb5" target="_blank"><img src="https://raw.githubusercontent.com/metacall/beautifulsoup-express-example/master/resources/scraper.png" alt="Scraping polyglot with MetaCall" style="max-width:100%; margin: 0 auto;" width="600" height="auto"></a>
</div>

In this example we show how to use BeautifulSoup (Python) from an Express server (NodeJS) in order to build a **Polyglot Scrapping API**. Link to the article: https://medium.com/@metacall/this-scraping-serverless-polyglot-is-metacall-c13223ae1cb5 .

## Install

Install MetaCall CLI:

```sh
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
```

Install application dependencies:

```sh
metacall pip3 install beautifulsoup4==4.8.2 certifi==2019.11.28
metacall npm install metacall express
```

## Run the Application

```sh
metacall index.js
```

For testing it, in another terminal, let's scrape all URLs from [NPM](https://www.npmjs.com/):

```sh
curl localhost:3000/?url=https://www.npmjs.com/
```

It should output something like:

```sh
["https://docs.npmjs.com","https://npm.community","https://go.npmjs.com/npm-pkgsafe","https://docs.npmjs.com","https://npm.community","https://www.npmjs.com/advisories","http://status.npmjs.org/","https://blog.npmjs.org/"]
```

## Docker

An alternative version with Docker and automated testing is provided.

```sh
docker build -t metacall/beautifulsoup-express-example .
docker run --rm -p 3000:3000 -it metacall/beautifulsoup-express-example
```

## MetaCall FaaS

<div align="center">
  <a href="https://metacall.io" target="_blank"><img src="https://github.com/metacall/beautifulsoup-express-example/blob/master/resources/dashboard.png?raw=true" alt="Scraping polyglot with MetaCall" style="max-width:100%; margin: 0 auto;" width="600" height="auto"></a>
</div>

After deploying the application into the FaaS https://dashboard.metacall.io, it can be accessed with (change `<your_alias>` by the alias you used to sign up):

```sh
curl -X POST https://api.metacall.io/<your_alias>/metacall-beautifulsoup-express-example/v1/call/links -X POST --data '{ "url": "https://www.npmjs.com/" }'
```
