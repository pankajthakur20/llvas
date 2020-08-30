#!/bin/bash
date
sudo mv ~/llvaslocal/attendance/* ~/llvaslocal/archive/
echo  -e "\nOpening Camera..."
python3 llvaslocal.py
echo -e "\nUploading gray scale images to cloud"
scp -i k30.pem ~/llvaslocal/attendance/*gray.jpg ubuntu@ip-address:/home/ubuntu/llvascloud/attendance/
echo -e "\nFinding faces in each image (in cloud)...\n"
ssh -i k30.pem ubuntu@ip-address
date
read -n 1 -r -s -p $'and press ENTER Key when ready to upload latency graph on the Web Server\n'
scp ~/latency.svg root@117.240.64.147:/usr/share/nginx/html
