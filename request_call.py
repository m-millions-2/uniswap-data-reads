import json
import requests


TOKENS = [
          '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599',
          '0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce',
          '0x6810e776880c02933d47db1b9fc05908e5386b96' 
         ]

URI = 'https://gateway.thegraph.com/api/[INSERT API KEY HERE]/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV'


def query_subgraph(Token):
    '''
    This function queries a Uniswap Subgraph.  The original Curl construct and expected response struct
    can be found in the read-me file
    '''

    json_data = { 
                 "query": "{ token(id: \"" + Token + "\") { id name symbol totalSupply,volumeUSD, \
                                                            decimals tokenDayData{ id, open, close, \
                                                            high, low, priceUSD } } }", 
                 "operationName": "Subgraphs", 
                 "variables": {} 
                }

    response = requests.post(URI, json=json_data)  
    
    # Check if the request was successful
    # ToDo: There is a small bug in this error checkin logic,
    #       which will be addressed in a later committ
    if response.status_code == 200:
        print(response)
        return response.json()
    else:
        print("Error:", response.text)
        return None


def main():
    for Token in TOKENS:
        result = query_subgraph(Token)
        if result:
            print(json.dumps(result, indent=4))


if __name__ == "__main__":
  main()

