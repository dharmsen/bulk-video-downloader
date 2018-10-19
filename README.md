# bulk-video-downloader
Tool for bulk downloading videos from video sharing platforms (e.g YouTube, instagram)

At the moment, only YouTube and Instagram downloading is supported.

Uses <a href="https://python-pytube.readthedocs.io/en/latest/">pytube</a> module for YouTube handling

## Setup:
1. ```install python 3.7.0```
2. ```pip install requests```
3. ```pip install pytube```

## How to use:
1. Copy the direct video links from YouTube to the 'youtube_links.txt' file

2. Copy the direct video links from Instagram to the 'instagram_links.txt' file <br>
<b>NOTE:</b> YouTube links should be in the form of: https://www.youtube.com/watch?v=XXXXXXXXXXX <br>
<b>NOTE:</b> Every link should be on a separate line <br>
<b>NOTE:</b> Every link should be on a seperate line <br>

3. Run the ```run.bat``` file. This will install the needed modules and run the downloadtool

4. Wait untill the command prompt closes. The downloaded videos from YouTube and Instagram should be in their respective folders.

## Error Handling:
After the first run, a log file will be created that will show you all YouYube and Instagram videos that failed to download. Check for typing mistakes, if this isn't the problem, rerunning the tool most likely won't solve the issue.
