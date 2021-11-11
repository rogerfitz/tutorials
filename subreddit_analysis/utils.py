from praw.models import MoreComments
from urllib.parse import urlparse  #https://docs.python.org/3/library/urllib.parse.html
import re #Regex is generally available in all programming languages

from secret_services import reddit

from collections import defaultdict

def extract_link_information(text):
    #Notice that this function works off of text, it can be used other data scraping projects too!
    #In general make functions as reusable as makes sense
    root_domains=defaultdict(int)
    if text:
        urls=re.findall(r'(https?://[^\s\)\]]+)', text)#starts with https and not strip out )] in case markdown
        for url in urls:
            parsed_url=urlparse(url)
            root_domains[parsed_url.netloc]+=1
    return root_domains

def get_post_text(post):
    if post.selftext:
        return post.selftext
    else:
        return post.url

#Improved version that fixes the MoreComments bug
def traverse_post(post):
    comments=[]
    for comment in post.comments:
        comments+=recursive_replies(comment, level=1)
    return comments

def recursive_replies(reply,level):
    #Also return level in case we want to stop after level 3 comments and for ease of the printing
    comments=[]
    #Funky MoreComments code checked manually with permalinks and seems right
    if isinstance(reply, MoreComments):#https://praw.readthedocs.io/en/stable/code_overview/models/more.html
        replies=reply.comments()
        level-=1
    else:
        replies=reply.replies
        comments+=[(reply, level)]
    for r in replies:
        comments+=recursive_replies(r,level+1)
    return comments

def get_domains(post):
    all_domains=defaultdict(int)
    comments=traverse_post(post)
    texts=[get_post_text(post)]+[comment.body for comment,level in comments]
    for text in texts:
        domains=extract_link_information(text)
        for k,v in domains.items():
            all_domains[k]+=v
    return all_domains

def analyze_subreddit(subreddit_name, how="all",limit=10):
    subreddit=reddit.subreddit(subreddit_name)

    all_domains=defaultdict(int)
    #Can change window size(s) to compare top links over tiem
    for post in subreddit.top("all",limit=limit):#1000
        domains=get_domains(post)
        for k,v in domains.items():
            all_domains[k]+=v
    all_domains=dict(sorted(all_domains.items(), key=lambda x:-x[1]))
    return {"domains": all_domains}

def analyze_user(user_name, limit=10):
    raise NotImplementedError