import configparser


class GCV:
    def read_config_file(self):
        config = configparser.ConfigParser()
        config.sections()

        config.read('config_test.ini')
 
        API_KEY = config['Secret']['API_KEY'] 
        DAYS = config['Time Series Length']['DAYS']
        TOKENS = config['Tokens']['TOKENS']

        return API_KEY, DAYS, TOKENS

