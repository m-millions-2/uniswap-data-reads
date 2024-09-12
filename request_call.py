import configparser
import json
import requests


URI = 'https://gateway.thegraph.com/api/[INSERT API KEY HERE]/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV'


def get_config_values():
    '''
    This function reads in global variables from a configuration file
    '''
    config = configparser.ConfigParser()
    config.sections()

    config.read('config.ini')
 
    DAYS = config['Time Series Length']['DAYS']
    TOKENS = config['Tokens']['TOKENS']
    
    return DAYS, TOKENS


def query_subgraph_day_data(Token):
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
    # ToDo: There is a small bug in this error checking logic,
    #       which will be addressed in a later commit
    if response.status_code == 200:
        print(response)
        return response.json()
    else:
        print("Error:", response.text)
        return None


def query_subgraph_timeseries(Token, Days):
    '''
    This function queries a Uniswap Subgraph.  The original Curl construct and expected response struct
    can be found in the read-me file
    '''
    json_data = { 
                 "query": "{ tokenDayDatas(first: " + Days + ", where: {token: \"" + Token + "\"}, orderBy: date,\
                                                                                                   orderDirection: asc )\
                                                                                                   { date volumeUSD token { id symbol\
                                                                                                   } } }",                                           
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
    '''
    This is the point of ingress for the application and launches two distinct 
    Subgraph search queries, each returning a JSON payload
  
    ToDo: Update calls for asychronous processing and DAYS variable pass-through
    '''

    DAYS, TOKENS = get_config_values()
    TOKENS = TOKENS.split()

    for Token in TOKENS:
        result = query_subgraph_day_data(Token)
        if result:
            print(json.dumps(result, indent=4))

        result = query_subgraph_timeseries(Token, DAYS)
        if result:
            print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()