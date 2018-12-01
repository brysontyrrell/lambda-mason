def lambda_handler(event, context):
    print(event)
    return {"layer_uri": "s3://python_layer_archive"}
