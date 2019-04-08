#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
import torrent_parser as tp
import sys
import md5
import re


def md5_string(val):
	m = md5.new()
	matchObj = re.match(r'^(.*)\.(.*?)$', val)
	if matchObj:
		val = matchObj.group(1)
		m.update(val)
		return m.hexdigest() + '.' +  matchObj.group(2)
	else:
		m.update(val)
		return m.hexdigest()


data = tp.parse_torrent_file(sys.argv[1])

data['info']['name'] = md5_string(data['info']['name'].encode('utf-8'))
data['info']['publisher'] = md5_string(data['info']['publisher'].encode('utf-8'))
if 'name.utf-8' in data['info']:
	data['info']['name.utf-8'] = md5_string(data['info']['name.utf-8'].encode('utf-8'))
if 'publisher.utf-8' in data['info']:
	data['info']['publisher.utf-8'] = md5_string(data['info']['publisher.utf-8'].encode('utf-8'))

for i in range(0, len(data['info']['files'])):
	data['info']['files'][i]['path'][0] = md5_string(data['info']['files'][i]['path'][0].encode('utf-8'))
	if 'path.utf-8' in data['info']['files'][i]:
		data['info']['files'][i]['path.utf-8'][0] = md5_string(data['info']['files'][i]['path.utf-8'][0].encode('utf-8'))

tp.create_torrent_file(sys.argv[2], data)
