import praw
from praw.models import MoreComments
import csv


commentlist = []

reddit = praw.Reddit(
    client_id='loOZRpSx5xd9lQ',
    client_secret='2ay9Nek2l5BPRhoJxGBZKBZOYxg',
    user_agent='quiet_learning'
)

all_posts = reddit.subreddit('all').hot(limit=3)

for each_post in all_posts:
    subreddits = reddit.subreddit(str(each_post.subreddit)).hot(limit=1)

    for subreddit in subreddits:
        if subreddit.num_comments != 0:
            submission = reddit.submission(str(subreddit.id))
            submission.comments.replace_more(limit=None)

            for comment in submission.comments.list():
                if comment.author != None:
                    commentsdata = {}
                    commentsdata['subreddit'] = str(each_post.subreddit)
                    commentsdata['title'] = subreddit.title
                    commentsdata['id'] = comment.id
                    commentsdata['author']= str(comment.author)
                    commentsdata['body'] = str(comment.body).replace('\n', '\s')
                    commentsdata['parent_id'] = comment.parent_id

                    commentlist.append(commentsdata)
keys = commentlist[0].keys()

with open('reddit-fetch.csv', 'w', encoding='utf_8_sig') as output_file:
    dict_writer = csv.DictWriter(output_file, keys, dialect='excel', delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(commentlist)
