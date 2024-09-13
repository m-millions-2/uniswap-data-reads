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

