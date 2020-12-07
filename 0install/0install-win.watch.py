import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from github import releases

releases = [{
    'version': release['tag_name'],
    'released': release['published_at'][0:10]
} for release in releases('0install/0install-win')]
