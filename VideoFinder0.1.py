
#import vlc
import urllib.request
import re
import urllib

# YouTube URL search test
Search = input("What word would you like to learn? ")
Search = Search.replace(" ","+")
signSearch = (Search + "+asl+dictionary")
URL = f'https://youtube.com/results?search_query={signSearch}'

#print(URL)

html = urllib.request.urlopen(URL)
videoIds = re.findall(r"watch\?v=(\S{11})", html.read().decode())
videoURL = ("https://youtube.com/watch?v=" + videoIds[0])

linkFile = open("URLLinks.txt", "a")
linkFile.write(videoURL)
linkFile.close()



#player = vlc.MediaPlayer(videoURL)
#player.play()

#print(htmlContent)
#above print leads to literal hundreds of lines of class \n
#i think its the full HTML of the search page
