import requests
import xml.etree.ElementTree as ET
import notify2
import time
import threading

def Fifaworldcup2018():

    url = 'https://www.scorespro.com/rss2/live-soccer.xml'

    res = requests.get(url)

    with open('topnewsfeed.xml', 'wb') as f:

        f.write(res.content)

    tree = ET.parse('topnewsfeed.xml')

    root = tree.getroot()

    newsitem = []

    for item in root.findall('./channel/item'):

        news = {}

        for child in item:

            if child.text is not None:

                news[child.tag] = child.text.encode('utf8')

        newsitem.append(news)

    notify2.init("news notifier")

    n = notify2.Notification(None)

    n.set_urgency(notify2.URGENCY_NORMAL)

    n.set_timeout(1000)

    n.update(newsitem[2]['description'], newsitem[2]['pubDate'])

    n.show()

    time.sleep(5)

    threading.Timer(5.0, Fifaworldcup2018).start()

Fifaworldcup2018()

#https://www.foxsports.com.au/content-feeds/fifa-world-cup/ - another feed rss

#this program has a potential flaw that the index of newsitem[index] keeps on changing-
#because there is no reliable rss feed for the fifa world cup. so sadly you have to-
#manually look up for the index where the world cup scores are being.

# For simplicity you may have to change the index of newsitem to 1,2,3 exmaple: newsitem[1] or
# newsitem[2] or newsitem[3]