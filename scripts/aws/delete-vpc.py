#!/usr/bin/python3
import sys
import boto3

ec2 = boto3.resource('ec2')
vpc_id = sys.argv[1]

print("Deleting ", vpc_id, "...") 
vpc = ec2.Vpc(vpc_id)

def detach_internet_gateway(vpc):
    internet_gateway_iterator = iter(vpc.internet_gateways.all())
    while gateway_iterator:
        try:
            internet_gateway = next(internet_gateway_iterator)
            response = internet_gateway.detach_from_vpc(
                DryRun=False,
                VpcId=vpc_id
            )
        except StopIteration:
            break


def remove_routes():
    route_table_iterator = iter(vpc.route_tables.all())
    while route_table_iterator:
        try:
            route_table = next(route_table_iterator)
            # route = ec2.Route(route_table.route_table_id, '0.0.0.0/0')
            # route.delete()
            route_table.delete()
        except StopIteration:
            break

def remove_subnets():
    subnet_iterator = iter(vpc.subnets.all())
    while subnet_iterator:
        try:
            subnet = next(subnet_iterator)
            subnet.delete()
        except StopIteration:
            break

remove_subnets
remove_routes()
detach_internet_gateway(vpc)
vpc.delete()
