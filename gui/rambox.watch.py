import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import github

releases = [{
    'version': release['tag_name'].strip('v'),
    'released': release['published_at'][0:10]
} for release in github.releases('ramboxapp/download') if release['tag_name'][:2] != 'v1']
