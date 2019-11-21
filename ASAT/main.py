from asat_usage_extractor import ASATUsageExtractor
from downloader import RepoDownloader
from db import DB

DB_PATH = 'projects.sqlite3'
REPOS_PATH = 'repos'

db = DB(DB_PATH)
asats = db.get_ASATs()
projects = db.get_projects()

asat_usage_extractor = ASATUsageExtractor(asats)
downloader = RepoDownloader(REPOS_PATH)

for project in projects:
    repo_path = downloader.download(project.url)
    project.asat_usages = asat_usage_extractor.extract(repo_path)
    print(project)