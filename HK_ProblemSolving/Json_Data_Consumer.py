import requests
import datetime
import sqlalchemy
from pandas.io.json import json_normalize
import pandas as pd

time_data = datetime.datetime.now()
current_date = str(time_data.date())
previous_date = str(datetime.date.today() - datetime.timedelta(2))
print(previous_date)
since = previous_date
until = previous_date


##################################################################################################
#########################Currency_Conversion_Rate#################################################
##################################################################################################
def currency_database_connection():
    '''
    Credential for email_id and Mysql Table
    '''
    username = 'ie'
    password = 'Spark@123#'
    hostname = '192.168.200.15'
    database = 'jet_revenue_mis'
    table = 'currency_details'
    ###################################################################################################
    ##################################DataBase_Connection_Cred#########################################
    ###################################################################################################

    mySqlConfig = "mysql+pymysql://" + username + ':' + password + '@' + hostname + '/' + database

    engine = sqlalchemy.create_engine(mySqlConfig)
    connection = engine.connect()
    query = "select to_inr from " + database + "." + table + " where currency_code='USD' and date='" + previous_date + "';"
    print(query)
    result = connection.execute(query)
    rows = result.fetchall()
    try:
        if rows:
            currency_value = rows[0][0]
            print("--->>>>>>", currency_value)
            return currency_value
        else:
            print("Data Set is Empty !!!")
            return None
    except Exception as e:
        print("Error in currency conversion !!", e)


def get_appwise_spend_via_camp_id(campaign_id, app_name, finaldf):
    currency_rate = currency_database_connection()
    base_url = "https://graph.facebook.com/v7.0/" + campaign_id + "/insights/"
    json_param = {'time_range': str({'since': since, 'until': until}),
                  'access_token': 'EAAZApSJ1mUYYBAKEJ09nOqnVjZBZAgtLqDKeEs6Bj8OLWC4EGo8DkodGlmNh8xtAQJDbmz8oijjlwiZAfkSyx0ZB36qWqUx6ROotWuQZCUTmu7Rax7S9DzsLmqzJB24LlCcCZBoeSVoVmvVGkkcN9B4ZCcMKPMVuihMu4ZAsxzXZCxIeRJmyO95YZCDh1uvhnXHnWUVpGZBzw9yXTwZDZD'
                  }
    HEADERS = {
        'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/45.0.2454.101 Safari/537.36'),
    }
    # Make the same request we did earlier, but with the coordinates of San Francisco instead.
    response = requests.get(base_url, params=json_param)
    print(response)
    print("#####################################")
    # Get the response data as a python object. Verify that it's a dictionary.
    dict = {'Date': "", 'Source': "", 'App_name': "", 'UA_cost_INR': "", 'UA_cost_in_USD': "", '1_USD_to_INR': ""}

    data = response.json()
    pd = json_normalize(data)
    print(pd['data'][0])
    # exit()
    dataframedata = pd['data'][0]

    if dataframedata:
        data = pd['data'][0][0]
        dict['Date'] = data['date_start']
        dict['Source'] = 'Facebook'
        dict['App_name'] = app_name
        dict['UA_cost_INR'] = data['spend']
        #######################################################################################################################################
        ################--------UA COST CALCULATION(TotalSpend=Spend+6%(PaymentmodeExtraCharges CreditCard Payment)---------###################
        #######################################################################################################################################
        #######################################################################################################################################
        ################--------UA COST CALCULATION(Mode Changed 10oct onwrds Post-Paid Payment)---------######################################
        #######################################################################################################################################

        if app_name == 'SSCC':
            dict['UA_cost_in_USD'] = float(data['spend']) / float(currency_rate)
        else:
            dict['UA_cost_in_USD'] = float(data['spend']) / float(currency_rate)

        dict['1_USD_to_INR'] = currency_rate
        finaldf = finaldf.append(dict, ignore_index=True)

    return finaldf


def get_campaign_list(parameters, baseurl):
    base_url = baseurl
    HEADERS = {
        'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/45.0.2454.101 Safari/537.36'),
    }
    # Make the same request we did earlier, but with the coordinates of San Francisco instead.
    response = requests.get(base_url, params=parameters)
    print(response)
    # Get the response data as a python object. Verify that it's a dictionary.
    data = response.json()
    # print(data['data'])
    campaign_list = data['data']
    return campaign_list


###################################################################################################
##################################DataBase Date CrossCheck#########################################
###################################################################################################
def insert_into_db(dataframe, app_name, tablename, spendsource):
    try:
        ###################################################################################################
        ###################################################################################################
        '''
        Credential for email_id and Mysql Table
        '''
        username = 'ie'
        password = 'Spark@123#'
        hostname = '192.168.200.15'
        database = 'Jet_auto_db'
        table = tablename
        '''
        Creating MYSql Engine
        '''
        ###################################################################################################
        ##################################DataBase Connection Cred#########################################
        ###################################################################################################

        mySqlConfig = "mysql+pymysql://" + username + ':' + password + '@' + hostname + '/' + database

        engine = sqlalchemy.create_engine(mySqlConfig)
        connection = engine.connect()
    except Exception as e:
        print(e)
    try:
        ###################################################################################################
        ##################################DataBase Date CrossCheck#########################################
        ###################################################################################################
        select_query = ""
        print(spendsource)
        if spendsource == 'Facebook':
            select_query = "Select distinct Date from " + database + '.' + table + " where Source='" + spendsource + "' and App_name='" + app_name + "';"
            print(select_query)

        result = connection.execute(select_query)
        rows = result.fetchall()
        if not rows:
            print(rows)
            print('Empty set returned')
            dataframe.to_sql(table, if_exists='append', con=engine, index=False)
            print('If Block first time data insertion')
            print('Data inserted successfully!!!')
        else:
            result = connection.execute(select_query)
            date_df = pd.DataFrame(result.fetchall())
            date_df.columns = result.keys()
            print(date_df.columns)
            table_date = date_df['Date'].unique()
            # print('table_date--->>>>>>>>', table_date)
            file_date = dataframe['Date'].unique()
            dates_notexist = set(file_date) - set(table_date)
            print('IAP_EXCEL_Date-------->>>>>', file_date)
            print('Table_date------------>>>>>', table_date)
            print('Dates_notexist_intable-------->>>>>', dates_notexist)
            final_df = dataframe[dataframe['Date'].isin(dates_notexist)]
            print(final_df['Date'].unique())
            '''
            Inserting Data into Mysql Table
            '''
            final_df.to_sql(table, if_exists='append', con=engine, index=False)
            print('else Block data vailidation and insertion')
            print('Data inserted successfully!!!')
    except Exception as e:
        print(e)


def callurl(app_name):
    #############################################################################################
    #############################################################################################

    json_param = {'since': since, 'until': until,
                  # 'time_range': str({'since': since, 'until': until}),
                  'fields': 'name,status',
                  'limit': 100,
                  'access_token': 'EAAZApSJ1mUYYBAKEJ09nOqnVjZBZAgtLqDKeEs6Bj8OLWC4EGo8DkodGlmNh8xtAQJDbmz8oijjlwiZAfkSyx0ZB36qWqUx6ROotWuQZCUTmu7Rax7S9DzsLmqzJB24LlCcCZBoeSVoVmvVGkkcN9B4ZCcMKPMVuihMu4ZAsxzXZCxIeRJmyO95YZCDh1uvhnXHnWUVpGZBzw9yXTwZDZD'
                  }

    campainid_list = get_campaign_list(json_param,
                                       'https://graph.prod.facebook.com/v8.0/act_379096755862514/campaigns/')

    finaldf = pd.DataFrame(columns=['Date', 'Source', 'App_name', 'UA_cost_INR', 'UA_cost_in_USD', '1_USD_to_INR'])
    for camp_name in campainid_list:
        if str(camp_name['name']).lower().__contains__(app_name.lower()):
            print(str(camp_name['name']).lower())
            finaldf = get_appwise_spend_via_camp_id(camp_name['id'], app_name, finaldf)

    newdf = finaldf.groupby(['Date', 'Source', 'App_name', '1_USD_to_INR'])['UA_cost_in_USD', 'UA_cost_INR'].apply(
        lambda x: x.astype(float).sum()).reset_index()
    print(finaldf)
    newdf = newdf[['Date', 'Source', 'App_name', 'UA_cost_INR', 'UA_cost_in_USD', '1_USD_to_INR']]
    return newdf


ssccnewdf = callurl('SSCC')
insert_into_db(ssccnewdf, 'SSCC'.lower(), 'tbl_spend_data', 'Facebook')
print(ssccnewdf)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
ludonewdf = callurl('LUDO')
insert_into_db(ludonewdf, 'LUDO'.lower(), 'tbl_spend_data', 'Facebook')
print(ludonewdf)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
