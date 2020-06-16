#!/usr/bin/env python3
"""
Copyright 2020, Delta Wolf
Released under the Creative Commons Attribution-ShareAlike 4.0 license

6/14/20
"""
import json, os, shutil, time
from datetime import datetime

import vrcpy, requests

def main():
	client = vrcpy.Client()
	log_file = open("VRChat_Avatar_Collector.log", mode='a+', encoding='utf-8', errors='ignore', buffering=1)

	def end():
		client.logout()
		log_file.close()
		exit()

	def log(text):
		log = datetime.now().strftime("%m/%d/%y - %H:%M:%S")
		con = datetime.now().strftime("%H:%M:%S") #console doesn't need day
		log_file.write("["+log+"] "+text+'\n')
		print("["+con+"] "+text)

	def create_dirs():
		if not os.path.exists(DIR):
			log("No directory named "+config["avatarFolder"]+", making one")
			os.mkdir(DIR)
		else:
			log("Using existing avatar directory '"+config["avatarFolder"]+"'")

	try:
		config = json.load(open('config.json'))
		captureCount = int(config["captureCount"]) #default 16 enough to collect all your current favorites in one go
		captureFrequency = int(config["captureFrequency"]) #default 60 seconds to meet vrchat api guidelines
	except Exception as e:
		log("Error opening config.json")
		log(str(e))
		end()

	DIR = os.path.join(os.getcwd(), config["avatarFolder"])

	client.login(config["username"], config["password"])
	b = client.fetch_me()
	log("Logged in as "+b.displayName)

	def avtr_grab():
		b = client.fetch_me() #refresh user object
		avtr_name = b.currentAvatar.name
		avtr_id = b.currentAvatar.id
		img = b.currentAvatar.thumbnailImageUrl #sometimes gets api.vrchat.cloud img link instead of cloudfront thumbnail png
		log("-"*24)
		log("Name: "+avtr_name)
		log("ID: "+avtr_id)
		log("Img: "+img)
		outputFile = os.path.join(DIR, avtr_id+".png")
		log(outputFile)

		if not os.path.exists(outputFile):
			r = requests.get(img, allow_redirects=True, stream=True, headers={'User-Agent': ""}) #stopped by cf if useragent is missing, fine if empty, https://i.gifer.com/72nt.gif
			r.raw.decode_content = True
			with open(outputFile,'wb') as f:
				shutil.copyfileobj(r.raw, f)
			log("Got: "+avtr_name+":"+avtr_id)
		else:
			log("Avatar " + avtr_name+":"+avtr_id+" has already been downloaded")
			log("Skipping")

	create_dirs()
	for x in range(0, captureCount):
		avtr_grab()
		time.sleep(captureFrequency)
	end()

if __name__ == "__main__":
	main()