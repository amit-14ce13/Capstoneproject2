import boto3
s3 = boto3.client('s3')
s3.download_file('staging-for-load','adobe_analytics/dtm_data/commercial/01-decommercialresponsive_2021-01-05.tsv.gz','./amit.tsv')
print("file downloaded")
