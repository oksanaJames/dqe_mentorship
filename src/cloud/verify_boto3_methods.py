import boto3

# At first, 'aws configure' command needs to be executed to configure 'default' profile
# session = boto3.Session(profile_name='default')

if __name__ == '__main__':
    # list S3 buckets with boto3 s3 client
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Bucket List: %s" % buckets)

    # list EC2 instances with boto3 ec2 client
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)

    # list cloudwatch metrics with boto3 cloudwatch client
    cloudwatch = boto3.client('cloudwatch')
    paginator = cloudwatch.get_paginator('list_metrics')
    metrics = [response['Metrics'] for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                       MetricName='IncomingLogEvents',
                                       Namespace='AWS/Logs')]
    print("CloudWatch metrics: %s" % metrics)
