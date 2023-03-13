import sys
import utils

if __name__=='__main__':
    opts=sys.argv
    if len(opts)>1:
        limit=opts[2] if len(opts)==3 else 100
        if opts[1]=="subreddit":
            print(utils.analyze_subreddit(opts[2], limit=limit))
        elif opts[1]=="user":
            print(utils.analyze_user(opts[2]), limit=limit)
        else:
            raise Exception("Invalid  options, check analyze.py")
