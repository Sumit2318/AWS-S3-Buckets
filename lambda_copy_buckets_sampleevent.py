import boto3

#Create a s3 client to make API Calls to AWS s3 Services
s3_client= boto3.client('s3')

#Dictionary containing information about source S3 Bucket
copy_source={
    'Bucket':'demo_source',
    'Key': ''
}

#List all the objects present in the source Bucket    
response=s3_client.list_objects(Bucket="demo_source")
    for each_item in response['Contents']:
        copy_source['Key']=each_item['Key']

        s3_client.copy(copy_source,'demo_dest',"copy_file {}".format(copy_source['Key']))





In this article , I will discuss about how to write a Python Script that will copy all or some specific files from Source S3 Bucket to Destination S3 Bucket.
In order to Execute this Function you need to have an AWS Account , so that you can create two S3 Buckets.
For example, I have created Source Bucket as "demo_source" & Destination Bucket as "demo_dest".
I have hard-coded the Buckets Name in my Script.
You will need to install Boto3 API which is an AWS SDK for Python.
