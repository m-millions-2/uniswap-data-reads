import configparser
import json
import requests

import config_values


URI1 = 'https://gateway.thegraph.com/api/'
URI2 = '/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV'


def query_subgraph_day_data(Token, URL):
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

    response = requests.post(URL, json=json_data)  
    
    # Check if the request was successful
    # ToDo: There is a small bug in this error checking logic,
    #       which will be addressed in a later commit
    if response.status_code == 200:
        print(response)
        return response.json()
    else:
        print("Error:", response.text)
        return None


def query_subgraph_timeseries(Days, Token, URL):
    '''
    This function queries a Uniswap Subgraph.  The original Curl construct and expected response struct
    can be found in the read-me file
    '''
    json_data = { 
                 "query": "{ tokenDayDatas(first: " + Days + ", where: {token: \"" + Token + "\"},\
                                                                                                   orderBy: date,\
                                                                                                   orderDirection: asc )\
                                                                                                   { date volumeUSD token \
                                                                                                   { id symbol\
                                                                                                   } } }",                                           
                 "operationName": "Subgraphs", 
                 "variables": {} 
                }  

    response = requests.post(URL, json=json_data)  
    
    # Check if the request was successful
    # ToDo: There is a small bug in this error checkin logic,
    #       which will be addressed in a later committ
    if response.status_code == 200:
        print(response)
        return response.json()
    else:
        print("Error:", response.text)
        return None


def run_day_data_query():
    '''
    This function fetches daily data from a Subgraph - fetching the configuration values
    here seems like a repetative task, but it is architected as an individual call based on 
    scheduler and other system considerations and with the assumptions that on call time, the 
    configurations values could have changed - so though it looks like an over-sight, it's 
    actually structured this way by design
    '''
    config_values = config_values.GCV()
    API_KEY, DAYS, TOKENS = config_values.read_config_file()
    TOKENS = TOKENS.split()
    URL = URI1 + API_KEY + URI2

    for Token in TOKENS: 
        result = query_subgraph_day_data(Token, URL)
        if result:
            print(json.dumps(result, indent=4))


def run_timeseries_query():
    '''
    This function fetches timeseries data from a Subgraph - fetching the configuration values
    here seems like a repetative task, but it is architected as an individual call based on 
    scheduler and other system considerations and with the assumptions that on call time, the 
    configurations values could have changed - so though it looks like an over-sight, it's 
    actually structured this way by design
    '''
    config_values = config_test.GCV()
    API_KEY, DAYS, TOKENS = config_values.read_config_file()
    TOKENS = TOKENS.split()
    URL = URI1 + API_KEY + URI2

    for Token in TOKENS:
        print(Token)
        result = query_subgraph_timeseries(DAYS, Token, URL)
        if result:
            print(json.dumps(result, indent=4))


def main():
    '''
    This is the point of ingress for the application and launches two distinct 
    Subgraph search queries, each returning a JSON payload. Arbritary run-times 
    are used in this example...
    '''
    #Run job every day at the 11:33am - Time Zone not specefied
    schedule.every().day.at("11:33").do(run_timeseries_query)
    
    #Run job every day at the 11:00pm - Time Zone not specefied
    schedule.every().day.at("23:00").do(run_day_data_query)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
  main()

