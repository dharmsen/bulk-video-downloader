# bulk-video-downloader
tool for bulk downloading videos from video sharing platforms (e.g YouTube, instagram)

at the moment, only YouTube and Instagram downloading is supported.

uses pytube module for youtube handling

Setup:
1. install python 3.7.0
2. pip install requests
3. pip install pytube

How to use:
1. copy the direct video links from YouTube to the 'youtube_links.txt' file

2. copy the direct video links from Instagram to the 'instagram_links.txt' file

	NOTE: YouTube links should be in the form of: https://www.youtube.com/watch?v=XXXXXXXXXXX

	NOTE: every link should be on a separate line

	NOTE: every link should be on a seperate line

3. run the 'run.bat' file. This will install the needed modules and run the downloadtool

4. Wait untill the cmd closes. The downloaded videos from YouTube and Instagram should be in their respective folders.

Error Handling:
After the first run, a log file will be created that will show you all youtube and instagram videos that failed to download. 
Check for typing mistakes, if this isn't the problem, rerunning the tool most likely won't solve the issue. 
