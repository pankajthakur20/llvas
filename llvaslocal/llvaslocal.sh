#!/bin/bash
date
echo  -e "\nOpening Camera..."
python3 llvaslocal.py
echo -e "\nSending images to cloud \n"
scp -i k30.pem ~/llvaslocal/attendance/*gray.jpg ubuntu@your-public-dns-ipv4:/home/ubuntu/llvascloud/attendance/
echo -e "\nFinding faces in each image (in cloud)...\n"
ssh -i k30.pem ubuntu@your-public-dns-ipv4
echo -e "\nSending attendance graph back to laptop..."
scp -i k30.pem ubuntu@your-public-dns-ipv4:/home/ubuntu/llvascloud/attendance/* /home/pankaj/llvaslocal/attendance
date

