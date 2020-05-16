#!/bin/bash
date
echo  -e "\nOpening Camera..."
python3 llvaslocal.py
echo -e "\nSending images to cloud \n"
scp -i k30.pem ~/llvaslocal/attendance/*gray.jpg ubuntu@ec2-54-163-35-10.compute-1.amazonaws.com:/home/ubuntu/llvascloud/attendance/
echo -e "\nFinding faces in each image (in cloud)...\n"
ssh -i k30.pem ubuntu@ec2-54-163-35-10.compute-1.amazonaws.com
echo -e "\nSending attendance graph back to laptop..."
scp -i k30.pem ubuntu@ec2-54-163-35-10.compute-1.amazonaws.com:/home/ubuntu/llvascloud/attendance/* /home/pankaj/llvaslocal/attendance
date

