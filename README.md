**INTRODUCTION**

This Python script provides a service that queries pricing data for various Web3 tokens via Uniswap’s V3 open subgraph - thus allowing for the powering of GraphQL charts.


**APPROACH**

The approach to this solution is as follows:
(1) Creat three (3) distinct API end-points, which consume data for each token
(2) Persist and store token data to a PostgreSQL database, or any additional store a necessary
(3) Expose a time-series API end-point that allows a GraphQL engine to consume the data for graphing purposes


**CAVEATS**

(1) Uniswaps Subgraph `TokenHourData` appears to be deprecated and `TokenDayData` will be used instead
(2) The requirements call for data persistence to a relational database (i.e. PostgreSQL), however for some use-cases, a cached, time-series
    data store might be more appropriate
(3) No security requirements have been specified, but appropriate notes, recommendatios will be noted in the documentation and code-base


**PROPOSED DATA ARCHITECTURE**

```
 --------           -------------             ------------------
|Token   |         |Token_History|           |Token_Timeseries_7|
|token_id|<------->|token_id     |<--------->|token_id          | 

```

Please note: The above architecture is not meant to be a fully realized database scheema, but rather is meant to represent the primary keys, which will serve in connecting the proposed tables in the data stores.  It is also possible that `Token_TimeSeries_7` may be implemented as a rolling, flat-file, datastore indepented of the relational database tables - futher consideration needs to be given at this point to this matter.


**KEY CORE VARIABLES FOR CONNECTIVITY** 

The following are the key component variables that power the API endpoints:
```
API KEY: 
   [INSERT API KEY HERE]
```   
  - Please note that the API KEY is being exposed in this documentation for the sake of this example so that the reader can run this code easily.
  - This API KEY would normally be encrypted and salted and not included in any type of documentation, nor hard-coded anywhere in the code, if this was a component of a production-ready system.

```
SUBGRAPH ID: 
  5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV
```

```
TESTED ON:
   https://gateway.thegraph.com/api/[INSERT API KEY HERE/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV
```

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

