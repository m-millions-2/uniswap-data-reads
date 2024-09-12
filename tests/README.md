**UNISWAP QUERY - TOKEN WBTC, GENERAL DATA:**  

```
{
 token(id: "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"){
   symbol
   name
   symbol
   totalSupply
   volumeUSD
   decimals
   tokenDayData {
     id 
     open
     close
     high
     low
     priceUSD
   }
 }
}
```

**Token WBTC - CURL COMMAND:**
``` 
 curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "{ token(id: \"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599\") { id name symbol totalSupply volumeUSD decimals tokenDayData{ id open close high low priceUSD } } }", "operationName": "Subgraphs", "variables": {}}' \
  https://gateway.thegraph.com/api/[INSERT API KEY HERE]/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV
```

**TOKEND WBTC - SAMPLE SUMMARIZED OUTPUT:**

```
{
  "data":{
  "token":{
    "decimals":"8",
    "id":"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "name":"Wrapped BTC",
    "symbol":"WBTC",
    "tokenDayData":[{
      "close":"0",
      "high":"0",
      "id":"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599-18751",
      "low":"0",
      "open":"0",
      "priceUSD":"0"
      },{
        "close":"58338.53440207575247331913887502708",
        "high":"58553.1908023713332712389966567129",
        "id":"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599-18752",
        "low":"0",
        "open":"0",
        "priceUSD":"58338.53440207575247331913887502708"
        },
...

                    {
        "close":"45797.85164312075190869882520134988",
        "high":"46614.22293500136975059740373694383",
        "id":"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599-18850",
        "low":"45329.42398245743787093475826281843","open":"45385.49424284112396310281374575781",
        "priceUSD":"4579785164312075190869882520134988"
        }],
      "totalSupply":"18240",
      "volumeUSD":"132659142365.5401549028363719898432"}}}

```


**UNISWAP QUERY - TOKEN WBTC, 24HR AGGREGATE, 7 DAY HISTORY:** 
```
{
  tokenDayDatas(first: 7, where: {token: "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"}, orderBy: date, orderDirection: asc) {
    date
    token {
      id
      symbol
    }
    volumeUSD
  }
}
```

**TOKEN WBTC - CURL COMMAND:**
``` 
 curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "{ tokenDayDatas(first: 7, where: {token: \"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599\"}, orderBy: date, orderDirection: asc ) { date volumeUSD token { id symbol } } }", "operationName": "Subgraphs", "variables": {}}' \
  https://gateway.thegraph.com/api/[INSERT API KEY HERE]/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV
```

**TOKEND WBTC - SAMPLE SUMMARIZED OUTPUT - 7 DAY TIMESERIES:**
```
{
  "data": {
    "tokenDayDatas": [
      {
        "date": 1620086400,
        "token": {
          "id": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
          "symbol": "UNI"
        },
        "volumeUSD": "0"
      },
      
      ...

      {
        "date": 1620604800,
        "token": {
          "id": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
          "symbol": "UNI"
        },
        "volumeUSD": "20174456.32972813854113988751821221"
      }
    ]
  }
```