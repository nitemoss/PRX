import string
import random
import time
import vk
from datetime import datetime

pubList = []
history = []
limitReachedTimes = 0

userSess = vk.Session(access_token = '0ca9a0b3ff1749e6bd8c9734da9542886ef011df93a02e31ffcb11b82b0c17271247b91c5f6ad76404490') # Reserved profile
user = vk.API(userSess)

class Public:
    def __init__(self, gid = None, name = None, auditory = None, views = None, expires = int()):

        if int(gid) < 0:
            gid = int(gid) * -1

        metadata = user.groups.getById(group_id = int(gid), fields = "members_count", v = 5.92)[0]
        postdata = user.wall.get(owner_id = int(gid) * -1, count = 1, offset = 1, v = 5.92)

        self.gid = int(gid)
        self.name = metadata['name']
        self.auditory = metadata['members_count']
        self.views = postdata['items'][0]['views']['count']
        self.priority = (self.auditory + self.views) / 2000
        self.repostsCreated = 0
        self.repostsGetted = 0
        self.postlink = str()
        self.expirationDate = int(time.time()) + expires * 3600

    def printInfo(self):
        print(self.gid,
              self.name,
              self.auditory,
              self.priority)
def getPost(gid = int()):
    pass

 
def distrib():
    repostLimit = 10
   
    for i in pubList:
        #print(i.gid, i.repostsCreated)
        for u in pubList:
            if u.gid != i.gid:
                if u.repostsCreated < repostLimit:
                    # Making repost from I to U
                    
                    postdata = user.wall.get(owner_id = int(i.gid) * -1, count = 1, offset = i.repostsCreated + 1, v = 5.92)
                    postID = postdata['items'][0]['id']


                    

                    u.repostsCreated += 1 #
                    i.repostsGetted += 1

                    repostObj = "wall" + str(i.gid * -1) + "_" + str(postID)
                    #print(repostObj)

                    print("\t Created/Getted reposts {}: {}/{}".format(u.gid, u.repostsCreated, u.repostsGetted))
                    
                    #user.wall.repost(object = repostObj, group_id = u.gid, v = 5.92)                 
                    # try to include technology: i.repost(u.post)    u.repost(i.post)
                    



                    # delay 30-90 sec
                    time.sleep(1.2)
                else:
                    print("\t Interrupted. Reason:", u.gid, "repost limit reached(", i.gid, "->", u.gid, ")")
                    global limitReachedTimes

                    limitReachedTimes += 1
 
                   
            
 
 

 
def id_generator(size = 4, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
def loadList(gidArray = []):
    gidlist = ",".join(str(gidArray))
    data = user.groups.getById(group_ids = gidlist, fields = "members_count", v = 5.92)
    postdata = user.wall.get(owner_ids = gidlist, count = 1, offset = 1, v = 5.92)
    for i in range(len(gidArray)):
        p = Public(gid = gidArray[i],
            name = data[i]['name'],
            auditory = data[i]['members_count'],
            views = postdata[i]['items']['views']['count']
        )
        ###########
 
def loadTestList():
    for i in range(40):
        p1 = Public(gid = random.randint(111111111, 999999999), auditory = random.randint(100,30000), views = random.randint(50,5000))
        pubList.append(p1)
    pubList.sort(key=lambda x: x.priority, reverse = True)


def rankList():
    groupCount = 1
    rankedList = []
    rankedPart = []
    if len(pubList) % 2 == 0:
        groupCount = 2
    elif len(pubList) % 3 == 0:
        groupCount = 3
    elif len(pubList) % 5 == 0:
        groupCount = 5

    print("Applied count: ", groupCount)
    #for i in pubList:


def main():
    ids = [-172323410, -171826699]
    #ids = [-171826699, -44138029, -172840307, -164139178, -170416883, -164380511, -150158703, -175766115, -170267843, -98584661]
    for i in ids:
        p1 = Public(i)
        pubList.append(p1)
        time.sleep(1.2)
    pubList.sort(key = lambda x: x.priority, reverse = True)
    print(pubList[0].name)
 
   
    for i in pubList:
        print(i.auditory, "subs ", i.views, "views  = {}γ ({})".format(i.priority, i.name))
    #p1.printInfo()
 
main()
distrib()
#print(id_generator())
input()
