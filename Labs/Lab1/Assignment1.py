from __future__ import print_function
import subprocess
import re

hosts = ["us-east-1 [23.23.255.255]",
         "us-west-1 [13.52.0.2]",
         "eu-west-1 [34.240.0.253]",
         "ap-northeast-1 [13.112.63.251]",
         "us-west-2 [34.208.63.251]",
         "ap-northeast-2 [13.124.63.251]",
         "ap-southeast-1 [13.228.0.251]",
         "eu-central-1 [18.194.0.252]",
         "eu-west-2 [35.176.0.252]",
         "ap-southeast-2 [13.54.63.252]",
         "eu-west-3 [35.180.0.253]",
         "us-gov-west-1 [52.61.0.254]",
         "us-east-2 [13.58.0.253]",
         "ca-central-1 [35.182.0.251]",
         "sa-east-1 [18.231.0.252]"]

latency_dict = {}

for i in range(len(hosts)):
 ping = subprocess.Popen(
    ["ping", "-n", "3", re.findall(r"\[([0-9.]+)\]" , hosts[i])[0] ],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)
 out, error = ping.communicate()
 avg_time = int(re.findall('\d+', str(out))[-1])
 key = hosts[i]
 latency_dict[key] = avg_time
    
print("The sorted results for average latency of various regions :")
i=1
for key,value in sorted(latency_dict.items(), key=lambda latency_dict: latency_dict[1]):
    print (str(i)+"."+key+" - "+str(value)+"ms")
    i=i+1
