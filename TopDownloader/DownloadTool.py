from __future__ import print_function
from pytube import YouTube
import os
from sys import argv
import requests
import time

#added feature

def GetYouTubeID(youtubelink):
	try:
		startid = youtubelink.index('=')
		vidid = ''
		for i in range(startid+1, startid+12):
			vidid += youtubelink[i]
		return vidid
	except IndexError:
		addtolog('ID error with ' + str(youtubelink))
		return 'IdError'

def process_lines(lines):
	linklist = []
	for i in range(len(lines)):
		link = lines[i].rstrip('\n')
		link = link[link.find("http"):]
		linklist.append(link)
	return linklist

def read_file(path):
	linelist = []
	with open(path, 'r') as file:
		for line in file:
			linelist.append(line)
	return process_lines(linelist)

def download(url, local_filename):
    r = requests.get(url, stream=True)
    with open(os.getcwd() + "/" + local_filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename

def download_insta(url, filename):
    r = requests.get(url, params={'__a': 1})
    if r.json()['graphql']['shortcode_media']["__typename"] =="GraphVideo":
        print('Saved as ' + download(r.json()['graphql']['shortcode_media']["video_url"],
                                    '\\insta_videos\\' + filename + '.mp4') + '!')
    else:
        print('Not A Video')

def download_yt_videos(links, path):
	for i in range(len(links)):
		try:
			print('Downloading YT Video ' + str(i))
			yt_vid = YouTube(links[i])
			vidid = str((i+1)) + '.. ' + GetYouTubeID(links[i])
			stream = yt_vid.streams.filter(file_extension='mp4').first()
			stream.download(path, vidid)
		except:
			erormsg = str(links[i]) + ' failed to download, moving on...'
			addtolog(errormsg)
			print('%d failed to download, moving on.' % GetYouTubeID(links[i]))

def download_insta_videos(links, path):
	for i in range(len(links)):
		try:
			print('Downloading Insta Video ' + str(i))
			download_insta(links[i], str(i))
		except:
			erormsg = str(links[i]) + ' failed to download, moving on...'
			addtolog(errormsg)
			print('video %d failed to download, moving on.' % i)


def addtolog(message : str):
	if not os.path.isfile(os.getcwd() + '\\log.txt'):
		with open('log.txt', 'w') as fileouput:
			fileoutput.write(message)
	else:
		with open('log.txt', 'a') as fileoutput:
			fileoutput.write('\n')
			fileoutput.write(message)



def shutdown():
	print('Finished downloading! Thanks for using this DownloadTool!')
	amountofinsta = len(os.listdir(os.getcwd()+'\\insta_videos\\'))
	amountofyt = len(os.listdir(os.getcwd()+'\\yt_videos\\'))
	print('Downloaded %d YouTube video(s)' % amountofyt)
	print('Downloaded %d Instagram video(s)' % amountofinsta)
	print('\n')
	print('Lourens Touwen - © 2018, based on pyTube')
	print('\n')
	print('You can close this window.')
	while True:
		time.sleep(60)

def init_filepaths():
	if not os.path.isdir(str(os.getcwd())+'\\yt_videos'):
		os.makedirs(str(os.getcwd())+'\\yt_videos')
	if not os.path.isdir(str(os.getcwd())+'\\insta_videos'):
		os.makedirs(str(os.getcwd())+'\\insta_videos')


yt_path = 'links_youtube.txt'
insta_path = 'links_instagram.txt'
print('Amount Of YT Videos: ' + str(len(read_file(yt_path))))
print('Amount Of Instagram Videos: ' + str(len(read_file(insta_path))))

init_filepaths()
download_yt_videos(read_file(yt_path), str(os.getcwd())+'\\yt_videos')
download_insta_videos(read_file(insta_path), str(os.getcwd())+'\\insta_videos\\')
shutdown()
