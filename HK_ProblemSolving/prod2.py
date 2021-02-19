from kafka import KafkaProducer
for i in range(0,10000):
    try:
        print("----------------> ",i)
        producer = KafkaProducer(bootstrap_servers='192.168.1.191:9094,192.168.1.192:9094,192.168.1.193:9094')
        producer.send('sdkanalytics', value=b'''{"server_time":"2020-07-30 14:06:21","ref_id":"51","client_ip":"192.168.3.1","data":{"Events":[{"game_id":"com.apnajob.candidate","session_id":"15960966171131b67f3288aa03dd2_and","device_id":"3","user_code":"871802737-35659-1595240806","time_stamp":"1596098913679","game_version":"1.0","event_name":"Interaction","advid":"4ab4cdbe-174a-4e19-aab8-689ca6b35785","param1":"Profile_Complete_Percentage","param2":"","param3":"","param4":"SCR_Profile","param5":"","param6":"","param7":"","param8":"","param9":"","param10":"","param11":"","param12":"null","param13":"null","param14":"null","param15":"null"}],"Type":"Events"}}''')
    except Exception as e:
        print(e)
    print('done')