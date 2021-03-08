## Website Blocker
 
import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts"     
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_list = ["www.reddit.com"]    # one can modify the names

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+website+"\n")
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
		content = file.readlines()
		file.seek(0)    # reset the pointer to the top of the text file
		for line in content:
			# overwriting the whole file
			if not any(websites in line for website in web_sites_list):
				file.write(line)
		file.truncate()  # used to delete the trailing lines

		time.sleep(5)
