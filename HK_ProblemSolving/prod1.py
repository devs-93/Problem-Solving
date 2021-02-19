from kafka import KafkaConsumer
from pymongo import MongoClient
import configparser
import time
import csv
import sys
import json
from pprint import pprint
import logging
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.encoders import encode_base64
from pathlib import Path
import os
import calendar

'''

This Function is Used for Setting
the config properties of different
table in dictionary. It takes run
time argument of the configuration
file


'''
LEVEL = {
    "info": logging.INFO,
    "error": logging.ERROR,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "critical": logging.CRITICAL
}


def log_prop(conf):
    log_path = conf['logging']['log_path']
    log_mode = conf['logging']['log_mode']
    logging.basicConfig(filename=log_path, level=LEVEL[log_mode],
                        format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p'
                        )
    logger = logging.getLogger(__name__)
    return logger


the_dict = {}


def mongo_connection(ipaddr, portnum, db_name):
    try:
        uri_sms = 'mongodb://smsdb:smsdb2k18@{}/{}'.format(ipaddr, db_name[0])
        uri_contacts = 'mongodb://smsdb:smsdb2k18@{}/{}'.format(ipaddr, db_name[1])
        uri_crash = 'mongodb://smsdb:smsdb2k18@{}/{}'.format(ipaddr, db_name[2])
        client_sms = MongoClient(uri_sms)
        client_contacts = MongoClient(uri_contacts)
        client_crash = MongoClient(uri_crash)
        logger.info("mongo coonection established")
        return client_sms, client_contacts, client_crash
    except Exception as e:
        logger.error(e)


def insert_record(client, db_name, coll_name, message):
    try:
        db = client[db_name]
        collection = db[coll_name]
        collection.insert(message)
    except Exception as e:
        logger.error(e)


def as_dict(config):
    for section in config.sections():
        the_dict[section] = {}
        for key, val in config.items(section):
            the_dict[section][key] = val
    return the_dict


def SettingProps():
    if len(sys.argv) == 2:
        print("condition is correct")
        print(sys.argv[1])
        config = configparser.ConfigParser()
        try:
            config.read(sys.argv[1])
            config = as_dict(config)
            return config
        except Exception as e:
            print("Error in Reading the configuration file")
            exit(0)

    else:
        print("Please provide the path of the configuaration file")
        exit(0)


'''

This Function is used to get the properties
used for writing the table to appropriate team

'''


def getProp(authkey, conf, isevent):
    try:
        c = conf[authkey]
        if isevent == 1:
            path = c['path_event']
            partition = c['partition']
            t_name = c['table_event_name']

        else:
            path = c['path_session']
            partition = c['partition']
            t_name = c['table_session_name']

        return path, t_name, partition
    except Exception as e:
        logger.error(e)
        return None, None, None


'''
This Function is used for writing the files
in the concern folder

'''


def write_file(path, message, tablename, partition):
    if partition == "False":

        with open(path + "/" + time.strftime("%d-%m-%Y-%H") + "-json.csv", "a+", newline='') as ef:
            ewriter = csv.writer(ef, quotechar='"', quoting=csv.QUOTE_ALL)
            for line in message:
                ewriter.writerow(line)

        ef.close()


    elif partition == "True":

        with open(path + "/year=" + time.strftime("%Y") + "/month=" + time.strftime("%m") + "/day=" + time.strftime(
                "%d/") + time.strftime("%d-%m-%Y-%H") + "-json.csv", "a+", newline='') as ef:
            ewriter = csv.writer(ef, quotechar='"', quoting=csv.QUOTE_ALL)
            for line in message:
                ewriter.writerow(line)
        ef.close()


'''
This function is used for Creating the
Connection with the kafka

'''


def mailer_Alert(name):
    ###########################################################################
    #####################Sender Address########################################
    me = "analytics@jetsynthesys.com"
    #####################whom to send Address################
    to = "devbrt.shukla@jetsynthesys.com"
    #####################CC Address################
    cc = "devbrt.shukla@jetsynthesys.com"
    rcpt = cc.split(",") + to.split(",")
    ############################################################################
    ############################################################################
    NofilemsgRoot = MIMEMultipart('related')
    NofilemsgRoot['Cc'] = cc
    NofilemsgRoot['To'] = to
    NofilemsgRoot['Subject'] = "Json Consumer Crashed"
    body = " " + name
    ##########################################
    part1 = MIMEText(body, 'plain')

    NofilemsgRoot.attach(part1)
    ################################################
    ################################################
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("mail@jetsynthesys.com", "jet@2015")
    text = NofilemsgRoot.as_string()
    server.sendmail(me, rcpt, text)
    print("Mail Send Successfully")
    server.quit()


def kafkaConnect(boot_server, g_id, topic):
    try:
        consumer = KafkaConsumer(bootstrap_servers=boot_server,
                                 auto_offset_reset='latest',
                                 # Set this property,if auto commit should happen.
                                 enable_auto_commit=False,
                                 # Make Auto commit interval to a big number so that auto commit does not happen,
                                 # we are going to control the offset commit via consumer.commitSync(); after
                                 # processing // message.
                                 #auto_commit_interval_ms=999999999999,
                                 max_poll_records=200,
                                 #session_timeout_ms = 1000,
                                 # This is how to control number of messages being read in each poll
                                 #max_partition_fetch_bytes=1000,
                                 #max_poll_interval_ms=300,
                                 #heartbeat_interval_ms=10000,
                                 #session_timeout_ms=30000,
                                 #consumer_timeout_ms=1000,
                                 group_id=g_id)
        consumer.subscribe([topic])
        print("Connection Created.........")
        logger.info("kafka Connection Created")

        return consumer
    except Exception as e:
        logger.error(e)


'''
This is the main part of the program
which consumes the messages in while
infinite loop

'''

if __name__ == '__main__':

    conf = SettingProps()
    logger = log_prop(conf)
    mongo_ip = conf['mongo']['ip']
    mongo_port = int(conf['mongo']['port'])

    Moconn1, Moconn2, Moconn3 = mongo_connection(mongo_ip, mongo_port, ["SMS_db", "CONTACTS_db", "CRASH_db"])
    print(Moconn1, Moconn2, Moconn3)

    brokerAddress = conf['kafka']['broker_server']
    topicname = conf['kafka']['topic']
    gid = conf['kafka']['gid']
    consumerObj = kafkaConnect(boot_server=brokerAddress, g_id=gid, topic=topicname)

    while (True):
        try:
            a=consumerObj.poll(timeout_ms=5000,max_records=100)
            Commited_offset_value = 0
            for packet in a:
                data_to_consume = list(a.values())
                packet = data_to_consume[0][0]
                Commited_offset_value = packet.offset
                packet = packet.value.decode("utf-8")
                packet = packet.replace(r'\n', " ")
                isevent = 0
                issms = 0
                iscontact = 0

                try:
                    message = json.loads(packet)
                    if message['data']['Type'] == 'Sessions':
                        isevent = 0
                        serv_time = message['server_time']
                        ref_id = message['ref_id']
                        data = message['data']['Sessions']
                        param1 = message.get('client_ip', "")
                        session_chunk = []
                        for i in data:
                            param2 = i.get('param2', "")
                            param3 = i.get('operatorName', "")
                            param4 = i.get('param4', "")
                            param5 = i.get('param5', "")
                            param6 = i.get('param6', "")
                            parsed_messages = [
                                "SESSIONSTART", serv_time, ref_id,
                                i.get('time_stamp', " "), i.get('device_id', " "),
                                i.get('session_id', " "), i.get('user_code', " "),
                                i.get('country', " "), i.get('city', " "),
                                i.get('make_model', " "), i.get('language', " "),
                                i.get('os', " "), i.get('os_version', " "),
                                i.get('game_id', " "), i.get('game_version', " "),
                                i.get('source_of_acquisition', " "), param1,
                                param2, param3, param4, param5, param6]
                            session_chunk.append(parsed_messages)
                        try:
                            path, t_name, partition = getProp(ref_id, conf, isevent)
                            logger.info("get_prop() function executed successfully")
                        except Exception as e:
                            print(e)
                            logger.error(e)
                            pass
                        if path is None or t_name is None or partition is None:
                            continue

                        try:
                            write_file(path, session_chunk, t_name, partition)
                            logger.info("write_file() function executed successfully")
                        except Exception as e:
                            print(e)
                            logger.error(e)
                            pass



                    elif message['data']['Type'] == 'Events':
                        isevent = 1
                        serv_time = message['server_time']
                        ref_id = message['ref_id']
                        data = message['data']['Events']
                        event_chunk = []
                        for i in data:
                            parsed_messages = [
                                "EVENTS", serv_time, ref_id,
                                i.get('time_stamp', " "), i.get('event_name', " "), i.get('device_id', " "),
                                i.get('session_id', " "),
                                i.get('user_code', " "),
                                i.get('game_id', " "), i.get('game_version', " "), i.get('param1', " "),
                                i.get('param2', " "), i.get('param3', " "), i.get('param4', " "), i.get('param5', " "),
                                i.get('param6', " "), i.get('param7', " "), i.get('param8', " "), i.get('param9', " "),
                                i.get('param10', " "),
                                i.get('param11', " "), i.get('param12', " "), i.get('param13', " "),
                                i.get('param14', " "), i.get('param15', " "), i.get('param16', " "),
                                i.get('param17', " "),
                                i.get('param18', " "), i.get('param19', " "), i.get('param20', " "),
                                i.get('advid', " ")]
                            event_chunk.append(parsed_messages)
                        try:
                            path, t_name, partition = getProp(ref_id, conf, isevent)
                            logger.info("get_prop() function executed successfully")
                        except Exception as e:
                            print(e)
                            logger.error(e)
                            pass
                        if path is None or t_name is None or partition is None:
                            continue

                        try:
                            write_file(path, event_chunk, t_name, partition)
                            logger.info("write_file function executed successfully")
                        except Exception as e:
                            print(e)
                            logger.error(e)
                            pass
                    #
                    # elif message['data']['Type'] in ['SMS', "MESSAGES", "Messages"]:
                    #
                    #     # insert_record(Moconn1, "SMS_db", "sms_collection", message)
                    #
                    #
                    # elif message['data']['Type'] == 'Contacts':
                    #     # insert_record(Moconn2, "CONTACTS_db", "contacts_collection", message)
                    #
                    # elif message['data']['Type'] in ['CrashDump', 'crashDump']:
                    #
                    #     # insert_record(Moconn3, "CRASH_db", "crash_collection", message)


                    else:
                        logger.info("no format found")
                        pass

                except Exception as e:
                    print(e)
                    print(('Faulty Json: %s') % packet)
                    logger.error(e)
                    logger.error(packet)
                    pass
            try:
                consumerObj.commit()
                if Commited_offset_value != 0:
                    print('Last Commited_offset_value : ', Commited_offset_value)
            except Exception as e:
                print("----------->while commit",e)
        except Exception as e:
            print('Json Kafka Consumer failed :', e)
            mailer_Alert('Please Do Somthing to Re run this , Suggestion Group Id change and Re Run')
            exit()
