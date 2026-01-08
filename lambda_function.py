import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')

    SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:570959644631:EC2-Stop-Alert-Topic"

    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    instances_to_stop = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_stop.append(instance['InstanceId'])

    if instances_to_stop:
        message = (
            "⚠️ The following EC2 instances will be stopped:\n\n"
            + "\n".join(instances_to_stop)
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Alert: EC2 Instances Stopping",
            Message=message
        )

        ec2.stop_instances(InstanceIds=instances_to_stop)

        print("Email sent and stopping instances:", instances_to_stop)
    else:
        print("No running EC2 instances found.")
