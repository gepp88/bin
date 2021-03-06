#!/usr/bin/env python
import aiml
import sys
import os

os.chdir('./basic')
sakura = aiml.Kernel()
sakura.setBotPredicate("name","Sakura")
sakura.setBotPredicate("hometown","170.01.5.5")
sakura.setBotPredicate('master', 'gepp')

if os.path.isfile("noise0001.brn"):
	sakura.bootstrap(brainFile = "noise0001.brn")
else:
	#load all AIML files and save a new brain
	sakura.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
	sakura.saveBrain("noise0001.brn")
	
#sakura.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
#sakura.learn("pazienza.aiml")
#sakura.respond('load aiml b')
#Saving loaded patterns into a brain file
#sakura.saveBrain('standard.brn')
while True:
	message = raw_input(">: ")
	if message == "quit":
			exit()
	if message == "exit":
			exit()
	#else message == "save":
	#	sakura.saveBrain("noise0001.brn")
	else:
		bot_response = sakura.respond(message)
	print bot_response
