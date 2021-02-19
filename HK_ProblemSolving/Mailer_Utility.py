from pyspark.sql import SparkSession
from pandas import ExcelWriter
import IP2Location
from pyspark.sql.types import *
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import requests
import datetime
from datetime import timedelta
import time
import sqlalchemy
from sqlalchemy import *
import pymysql
import sys
#import reverse_geocode
#reload(sys)
#sys.setdefaultencoding('utf8')

print(datetime.timedelta())
previous_date = str(datetime.date.today()-datetime.timedelta(1))
year = previous_date.split("-")[0]
month = previous_date.split("-")[1]
day = previous_date.split("-")[2]
print(previous_date)

'''
Connect to Vitune DB
'''
###################################
# -- Noida Prod Connection creden--
##################################
host = '192.168.200.15'
user = 'ie'
password = 'Spark@123#'
database='jet_revenue_mis'
mySqlConfig = "mysql+pymysql://"+user+':'+password+'@'+host+'/'+database
engine = sqlalchemy.create_engine(mySqlConfig)
connection = engine.connect()

print("-------------------------------------------------------------------------------------------------------------")
print("------------------------------->>>>>>>>>>>>>>>>>>Connection to mapr DB<<<<<<<<<<<<<<<<-----------------------")
print("-------------------------------------------------------------------------------------------------------------")




#############################################################################################################################################
####################################################################################Spark Context Creation###################################
#############################################################################################################################################
'''
Create Spark Context To Extract Data
'''
spark = SparkSession.builder.appName("CMI data aggregation and Dump bahrain").enableHiveSupport().getOrCreate()
sc = spark.sparkContext
spark.sql("use app_billing_mis")



#############################################################################################################################################
#############################Aggregation which will consolidate data as per logic and Dump###################################################
#############################################################################################################################################

query="""
select
min(acq_dt) as acq_dt,
msisdn,
lower(store) as store,
operator,
promoid,
req_mode,
case
when ma_base_price like '%1%' then 'Daily' else ma_base_price end as plan_type,
sum(acq_count) as acq_count,
sum(acq_rev) as acq_rev,
sum(acq_rev_in_INR) as acq_rev_in_INR,
sum(jspl_acq_rev_in_INR) as jspl_acq_rev_in_INR,
sum(ren_count) as ren_count,
sum(ren_rev) as ren_rev,
sum(ren_rev_in_INR) as ren_rev_in_INR,
sum(jspl_ren_rev_in_INR) as jspl_ren_rev_in_INR,
country ,
jspl,
jspl_share  
from
(
select
min(acq_date) as acq_dt,
msisdn,
matx_id,
store,
operator,
promoid,
req_mode,
ma_base_price,
sum(acq_count) as acq_count,
sum(acq_rev) as acq_rev,
sum(acq_rev)*currency_value as acq_rev_in_INR,
sum(acq_rev*currency_value*jspl_share) as jspl_acq_rev_in_INR,
sum(ren_count) as ren_count,
sum(ren_rev) as ren_rev,
sum(ren_rev)*currency_value as ren_rev_in_INR,
sum(ren_rev*currency_value*jspl_share) as jspl_ren_rev_in_INR,
country,
jspl,
jspl_share
from
(

-- ######################################2
select
min(dt) as acq_date,
ma_year,
case when ma_year>'2010' then '198.34' else '198.34' end as currency_value,
msisdn,
matx_id as matx_id,
ma_app_user as store,
ma_opt_name as operator,
promoid as promoid,
ma_base_price ,
ma_req_mode as req_mode,
sum(acq_count) as acq_count,
sum(acq_rev) as acq_rev,
sum(ren_count) as ren_count,
sum(ren_rev) as ren_rev,
dim_tab.country as country,
jspl,
dim_tab.jspl_share as jspl_share
from
(
-- #######################################1
select
to_date(ma_date) dt,
year(ma_date) as ma_year,
ma_msisdn as msisdn,
ma_tranx_id as matx_id,
ma_req_mode,
ma_app_user,
ma_opt_name,
ma_base_price,
case when to_date(ma_date)<='2018-05-31' then '0' else '0' end as jspl,
case when lower(ma_tokencall)='notoken' or lower(ma_tokencall)=' ' or lower(ma_tokencall) like
'z_%' then 0 when lower(ma_tokencall) like '%-%'
then SUBSTRING_INDEX( SUBSTRING_INDEX(lower(ma_tokencall),'-',3) ,'-',-1)else
SUBSTRING_INDEX(SUBSTRING_INDEX(lower(ma_tokencall),'#',3) , '#',-1) end as promoid,
sum(case when upper(ma_req_type)='ACTIVATION' and ma_amount <> 0 then 1 else 0 end) acq_count,
sum(case when upper(ma_req_type)='ACTIVATION' and ma_amount = 0 then 1 else 0 end) parking_count,
sum(case when upper(ma_req_type)='ACTIVATION' then ma_amount else 0 end) acq_rev,
sum(case when upper(ma_req_type)='RENEWAL' and ma_amount <> 0 then 1 else 0 end) ren_count,
sum(case when upper(ma_req_type)='RENEWAL' and ma_amount = 0 then 1 else 0 end) grace_count,
sum(case when upper(ma_req_type)='RENEWAL' then ma_amount else 0 end) ren_rev,
sum(case when upper(ma_user_status)='ACTIVE' then 1 else 0 end) active_users,
count(distinct ma_tranx_id) attempts
from
mis_activation_renewal
where lower(ma_app_user) in
('100mb_bh',
'comedyclub_viva_bh',
'comedyclub_batelco_bh',
'100mb_batelco_bh',
'droid_batelco_bh')
and to_date(ma_date)<= date_sub(to_date(current_date),1)
group by to_date(ma_date),ma_app_user,ma_opt_name,ma_msisdn,ma_tranx_id,ma_base_price,ma_req_mode,year(ma_date),
case when lower(ma_tokencall)='notoken' or lower(ma_tokencall)=' ' or lower(ma_tokencall)
like 'z_%' then 0 when lower(ma_tokencall) like '%-%'
then SUBSTRING_INDEX( SUBSTRING_INDEX(lower(ma_tokencall),'-',3) ,'-',-1)else
SUBSTRING_INDEX(SUBSTRING_INDEX(lower(ma_tokencall),'#',3) , '#',-1) end
-- #######################################1
)as temp_1
left outer join
(select app,operator,country,jspl_share from product_operator) dim_tab
on (lower(temp_1.ma_app_user)=lower(dim_tab.app) and lower(temp_1.ma_opt_name)=lower(dim_tab.operator))
group by temp_1.matx_id,temp_1.msisdn,ma_app_user,ma_opt_name,promoid,ma_req_mode,ma_base_price,ma_year,jspl,
dim_tab.country,dim_tab.jspl_share,jspl
) as temp
-- ######################################2
group by temp.matx_id,temp.msisdn,store,operator,promoid,req_mode,ma_base_price,ma_year,currency_value,country,jspl_share,jspl
)as temp2
group by msisdn,matx_id,store,operator,promoid,req_mode,ma_base_price,country,jspl_share,jspl
"""


df_3=spark.sql(query).toPandas()

df_3.columns=['acq_dt','msisdn','store','operator','promoid','req_mode','plan_type','acq_count','acq_rev','acq_rev_in_INR','jspl_acq_rev_in_INR','ren_count','ren_rev','ren_rev_in_INR','jspl_ren_rev_in_INR','country','jspl','jspl_share']
df_3.reset_index(drop=True,inplace=False)
df_3.to_sql('tbl_campro_bahrain_agg',con=connection,if_exists='replace',index=False)





print("-------------------------------------------------------------------------------------------------------------")
print("---------------------->>>>>>>>>>>>>>>>>> Bahrain Task Done Successfully<<<<<<<<<<<<<<<<----------------------")
print("-------------------------------------------------------------------------------------------------------------")