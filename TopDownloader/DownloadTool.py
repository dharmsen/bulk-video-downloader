from __future__ import print_function
from pytube import YouTube
import os
from sys import argv
import requests
import time

def GetYouTubeID(youtubelink):
	startid = youtubelink.index('=')
	vidid = ''
	for i in range(startid+1, startid+12):
		vidid += youtubelink[i]
	return vidid

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
		print('Downloading YT Video ' + str(i))
		yt_vid = YouTube(links[i])
		try:
			vidid = str((i+1)) + '.. ' + GetYouTubeID(links[i])
		except IndexError:
			vidid = str((i+1))
		stream = yt_vid.streams.filter(file_extension='mp4').first()
		stream.download(path, vidid)

def download_insta_videos(links, path):
	for i in range(len(links)):
		print('Downloading Insta Video ' + str(i))
		download_insta(links[i], str(i))

def shutdown():
	print('Finished downloading all videos! Thanks for using this DownloadTool!')
	print('By Lourens Touwen - 2018, based on pyTube')
	print('\n')
	print('Shutting down in 5 seconds')
	time.sleep(5)


yt_path = 'links_youtube.txt'
insta_path = 'links_instagram.txt'
print('Amount Of YT Videos: ' + str(len(read_file(yt_path))))
print('Amount Of Instagram Videos: ' + str(len(read_file(insta_path))))

download_yt_videos(read_file(yt_path), str(os.getcwd())+'\\yt_videos')
download_insta_videos(read_file(insta_path), str(os.getcwd())+'\\insta_videos\\')

shutdown()
