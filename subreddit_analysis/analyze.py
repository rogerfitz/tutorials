import sys
import utils

if __name__=='__main__':
    opts=sys.argv
    if len(opts)>1:
        if opts[1]=="subreddit":
            utils.analyze_subreddit(opts[2])
        elif opts[1]=="user":
            utils.analyze_user(opts[2])
        else:
            raise Exception("Invalid  options, check analyze.py")
