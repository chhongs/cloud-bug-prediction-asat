from tqdm import tqdm

from parsers.asat_usage_extractor import ASATUsageExtractor
from util.downloader import RepoDownloader
from model.db import DB
from util.statistics import \
    plot_asat_usage_percentages, \
    print_average_number_of_asats, \
    print_asat_arg_usage

DB_PATH = 'data/projects.sqlite3'
REPOS_PATH = 'repos'

db = DB(DB_PATH)
asats = db.get_ASATs()
projects = db.get_projects()

asat_usage_extractor = ASATUsageExtractor(asats)
downloader = RepoDownloader(REPOS_PATH)

for project in tqdm(projects):
    repo_path = downloader.download(project.url)
    project.asat_usages = asat_usage_extractor.extract(repo_path)

plot_asat_usage_percentages(asats, projects)
print_average_number_of_asats(projects)
print_asat_arg_usage(projects)
