import twint
from pandas import *
import re
import os
import urlexpander



c = twint.Config()
c.Search = "cats"
c.Videos = True
c.Limit = 100
c.Store_csv = True
c.Output = "none.csv"
twint.run.Search(c)


data = read_csv("none.csv")

tweet = data['tweet'].tolist()

counter = 1
for t in tweet:
    link = re.search("(?P<url>https?://[^\s]+)", t).group("url")
    exp_link = urlexpander.expand(link)
    print("downloading:",exp_link[:-8])
    exp_link = exp_link[:-8]
    print("\n")

    try:
        os.system("cd C://Users//verma//Desktop//twitter_bot//twitter2mp4 && python twitter2mp4.py {link} -fn {name}".format(link = exp_link, name = "vid"+ str(counter)))
        counter = counter +1
    except ():
        pass

os.system("cd C:/Users/verma/Desktop/twitter_bot && del none.csv")


