#!/usr/bin/env bash 
ssh -i ~/auth/bloom_rsa bloomlab@192.168.1.1 "sudo cp /var/log/freeradius/* /home/bloomlab/radiuslogs/; sudo chown -R bloomlab /home/bloomlab/radiuslogs/" 
scp -ri ~/auth/bloom_rsa bloomlab@192.168.1.1:/home/bloomlab/radiuslogs/ /root/infrastructure-automation/lab-ranking/
