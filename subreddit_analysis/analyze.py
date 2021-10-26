import sys
import utils

if __name__=='__main__':
    opts=sys.argv
    if len(opts)>1:
        if opts[1]=="subreddit":
            print(utils.analyze_subreddit(opts[2], limit=None))
        elif opts[1]=="user":
            print(utils.analyze_user(opts[2]))
        else:
            raise Exception("Invalid  options, check analyze.py")
