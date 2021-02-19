def lambda_handler(event, context):
    output = []
    for record in event['records']:
        payload = record["data"]
        if payload[0]['ticker_symbol'] == "DFG":
            output_record = {
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': payload
            }
            output.append(output_record)
    return {'records': output}
