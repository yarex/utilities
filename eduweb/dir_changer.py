#!/usr/bin/env python
''' yarex eduweb project directory changer '''

import os
import sys
import shutil

#
try:
	path = sys.argv[1]
except:
	print('No path provided')

#
try:
	newDir = os.path.join(path, 'test')
	if not os.path.exists(newDir):
		os.mkdir(newDir)
except:
	print('Invalid path')

#
try:
	for entry in os.scandir(path):
		if not entry.name.startswith('.') and not entry.is_file():
			directory = os.path.join(path, entry.name)
			for innerEntry in os.scandir(directory):
				if innerEntry.name.lower() == 'start':
					oldName = os.path.join(directory, innerEntry.name)
					newName = os.path.join(directory, entry.name)
					os.rename(oldName, newName)
					newPath = shutil.move(newName, newDir)
					print(newPath)
except:
	print('Invalid path')