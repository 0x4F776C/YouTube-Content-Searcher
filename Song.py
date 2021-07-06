import os
import pyautogui
import time
import urllib.request
import urllib.parse
import re

class Node:
    def __init__(self, newData = None, nextNode = None):
        self.data = newData
        self.next = nextNode
    
    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, newNode):
        self.next = newNode

class Music:
    def __init__(self, songId, songName, songArtist):
        self.songId = songId
        self.songName = songName
        self.songArtist = songArtist

    def getSongId(self):
        return self.songId

    def getSongName(self):
        return self.songName

    def getSongArtist(self):
        return self.songArtist

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def next(self, newNode):
        self.head = newNode

    def AddMusicToFront(self, newMusic):
        newMusic.setNext(self.head)
        self.head = newMusic
        self.size = self.size + 1

    def AddMusicAtPosition(self, newMusic, n):
        if n == 0:
            self.AddMusicToFront(newMusic)
        else:
            nodeBefore = self.head
            for i in range(0, n - 1):
                nodeBefore = nodeBefore.getNext()
            newMusic.setNext(nodeBefore.getNext())
            nodeBefore.setNext(newMusic)
            self.size = self.size + 1
        
    def RemoveMusicAtPosition(self, n):
        if self.head is None:
            print("List is empty!")
        elif n == 0:
            self.head = self.head.getNext()
        else:
            nodeBefore = self.head
            for i in range(0, n - 1):
                nodeBefore = nodeBefore.getNext()
            nodeBefore.setNext(nodeBefore.getNext().getNext())
            self.size = self.size - 1
            
    def DisplayMusic(self):
        node = self.head
        while node is not None:
            print("ID: {}".format(node.getData().getSongId()))
            print("Song Name: {}".format(node.getData().getSongName()))
            print("Artist Name: {}".format(node.getData().getSongArtist()))
            print("")
            node = node.getNext()

    def SortByArtistName(self):
        for i in range(0, self.size):
            NodeA = self.head
            NodeB = self.head.getNext()
            for j in range(i):
                ArtistA = NodeA.getData().getSongArtist()
                ArtistB = NodeB.getData().getSongArtist()
                for k in range(min(len(ArtistA), len(ArtistB))):
                    if ArtistA[k] < ArtistB[k]:
                        temp = NodeA.getData()
                        NodeA.setData(NodeB.getData())
                        NodeB.setData(temp)
                        break
                    elif ArtistA[k] > ArtistB[k]:
                        break
                NodeA = NodeA.getNext()
                NodeB = NodeB.getNext()

### Insert data into Music ###

s1 = Music(1, "Hello", "Adele")
s2 = Music(2, "Lean On", "Major Lazer")
s3 = Music(3, "Dark Horse", "Katy Perry")
s4 = Music(4, "Counting Stars", "OneRepublic")
s5 = Music(5, "Thinking Out Loud", "Ed Sheeran")
s6 = Music(6, "Bailando", "Enrique Iglesias")
s7 = Music(7, "Roar", "Katy Perry")
s8 = Music(8, "Shake It Off", "Taylor Swift")
s9 = Music(9, "Sugar", "Maroon 5")
s10 = Music(10, "Sorry", "Justin Bieber")

Song = LinkedList()

### Add Music to list at the front ###

Song.AddMusicToFront(Node(s1))
Song.AddMusicToFront(Node(s2))
Song.AddMusicToFront(Node(s3))
Song.AddMusicToFront(Node(s4))
Song.AddMusicToFront(Node(s5))
Song.AddMusicToFront(Node(s6))
Song.AddMusicToFront(Node(s7))

### Add Music to list at position n ###

Song.AddMusicAtPosition(Node(s8), 2)
Song.AddMusicAtPosition(Node(s9), 4)
Song.AddMusicAtPosition(Node(s10), 6)

### Start of Run Line ###

os.system('cls' if os.name == 'nt' else 'clear') # clear the screen
# Song.RemoveMusicAtPosition(1) # remove music at n position



Song.SortByArtistName() # sort the list by artist name (alphabetically)



Song.DisplayMusic() # display the result
time.sleep(3) # stop for 3s to have a clearer view of results

### End of Run Line

### Start of Extra Stuff ###

def searchYoutube(): # function to find video on Youtube
    print("")
    search_input = input("What do you want to search?\n>>> ") # get user choice of video
    vid = urllib.parse.urlencode({"search_query" : search_input}) # encode the video string
    content = urllib.request.urlopen("http://www.youtube.com/results?" + vid) # request and open the site with the vid url
    result = re.findall(r'href=\"\/watch\?v=(.{11})', content.read().decode()) # get the full url
    url = "https://www.youtube.com/watch?v=" + result[0] # getting the full string for later use in automation

    app = pyautogui # dimming pyautogui as app

    app.click(21, 1066) # click position 21, 1066
    time.sleep(1) # stop for 1s for slower systems
    app.typewrite("Chrome") # type Chrome into the search bar
    time.sleep(1) # stop for 1s for slower systems
    app.typewrite(["enter"]) # keydown on enter key
    time.sleep(1) # stop for 1s for slower systems
    app.click(470, 76) # click position 430, 82
    time.sleep(1.5) # stop for 1.5s for slower systems
    app.typewrite("{}".format(url)) # type the url into the Chrome search bar
    time.sleep(1) # stop for 1s for slower systems
    app.typewrite(["enter"]) # keydown on enter key
# print(app.position()) # find mouse position

while True: # infinite loop till break
    q1 = input("Do you want to search a video on Youtube?\n>>> ") # asking if user want to find a video on Youtube

    if q1.lower() not in ('y', 'ye', 'yes'): # checking if user input is True or not, go to else statement if not
        # print("Error")
        break # break out of loop
    else: # break out of loop as user input does not contain 'y', 'ye', 'yes'
        # print("Pass")
        searchYoutube() # run the function searchYoutube()
        break # break out of loop

### End of Extra Stuff ###