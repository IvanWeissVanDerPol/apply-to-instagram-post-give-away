from instapy import InstaPy
from instapy.util import smart_run
from credentials import username , password
session = InstaPy(username, password,headless_browser=True, show_logs=True)


with open(r'followers.txt', 'r') as f:
    follower_lines = ["@" + line.strip() for line in f]
followers = follower_lines

with open(r'urls.txt', 'r') as f:
    urls_lines = [line.strip() for line in f]
urls = urls_lines


with smart_run(session):
    """Comment util"""
    session.login()
    session.set_do_comment(enabled=True, percentage=100)
    session.set_comments(comments='Nice shot!')
    session.interact_by_URL(urls, amount=1, randomize=False)

    