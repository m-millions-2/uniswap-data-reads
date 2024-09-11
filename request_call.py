import requests


def send_graphql_query_to_subgraph():
    '''
    This is the first iteration of a simple function, which queries a Uniswap Subgraph.  

    The original Curl construct is:

    Curl -X POST \
      -H "Content-Type: application/json" \
      -d '{ 
           "query": "{ token(id: \"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599\") { id name symbol } }", 
           "operationName": "Subgraphs", 
           "variables": {} 
          }'
        https://gateway.thegraph.com/api/[INSERT API KEY HERE]/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV

    Expected JSON response:
        {
         'data': {
                  'token': {
                            'id': '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599',
                            'name': 'Wrapped BTC', 
                            'symbol': 'WBTC'
                            }
                  }
        }

    '''

    response = requests.post(uri, json=json_data)  
    
    # Check if the request was successful
    # ToDo: There is a small bug in this error checkin logic,
    #       which will be addressed in a later committ
    if response.status_code == 200:
        print(response)
        return response.json()
    else:
        print("Error:", response.text)
        return None

uri = 'https://gateway.thegraph.com/api/[Insert API KEY Here]/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV'

json_data = { 
       "query": "{ token(id: \"0x2260fac5e5542a773aa44fbcfedf7c193bc2c599\") { id name symbol } }", 
       "operationName": "Subgraphs", 
       "variables": {} 
       }

print(send_graphql_query_to_subgraph())

