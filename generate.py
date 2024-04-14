#!/usr/bin/env python3

import os
import sys
import json
import logging
import subprocess
from datetime import datetime

logging.basicConfig(level=logging.INFO)

GH = "gh"
ARTICLES_DIR = "_posts"
LABELS = set(["blog"])
TIMEOUT = 20

## 1. find all issues with specific labels
issues_json = subprocess.check_output(
    "gh issue list --state open --json title,url,author,number,labels,updatedAt,createdAt",
    shell=True, timeout=TIMEOUT)
logging.info("issues_json: %s", issues_json)

issues = json.loads(issues_json)
issues = [issue for issue in issues if LABELS.intersection(set([label["name"] for label in issue["labels"]]))]
logging.info("issues with filter: %s", issues)


## 3. generate articles
for issue in issues:
    r = subprocess.check_output(f"gh issue view {issue['number']} --json title,url,author,number,labels,createdAt,updatedAt,body",
                       shell=True, timeout=TIMEOUT)
    issue = json.loads(r)
    logging.info("process issue: %s", issue)
    date = datetime.strptime(issue['createdAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    title = issue['title'].replace(' ', '-')
    with open(f"{ARTICLES_DIR}/{date}-{title}.md", "w") as f:
        f.write(f"# {issue['title']}\n\n")
        f.write(f"> Author: **{issue['author']['login']}**  \n")
        f.write(f"> Labels: **{' '.join([label['name'] for label in issue['labels']])}**  \n")
        f.write(f"> Created: **{issue['createdAt']}**  \n")
        f.write(f"> Link and comments: <{issue['url']}>  \n")
        f.write("\n\n")
        f.write(issue['body'])