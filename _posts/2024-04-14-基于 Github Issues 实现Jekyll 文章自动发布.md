---
layout: default
date: 2024-04-14
title: 基于 Github Issues 实现Jekyll 文章自动发布
permalink: /2024/04/issue-to-Jekyll.html
---



参考 [https://github.com/ninehills/blog/issues/100](https://github.com/ninehills/blog/issues/100)

实现靠两个文件
[https://github.com/YixiaoOrg/blog.yixiao.org/blob/gh-pages/.github/workflows/main.yml](https://github.com/YixiaoOrg/blog.yixiao.org/blob/gh-pages/.github/workflows/main.yml)

和

[https://github.com/YixiaoOrg/blog.yixiao.org/blob/gh-pages/generate.py](https://github.com/YixiaoOrg/blog.yixiao.org/blob/gh-pages/generate.py)

GitHub Actions is not permitted to create or approve pull requests.报错需要去https://github.com/[YixiaoOrg/blog.yixiao.org]/settings/actions 的最下面设置允许 GitHub Actions 创建和批准拉取请求
`YixiaoOrg/blog.yixiao.org` 部分需要参考自己的项目


generate.py最主要的代码解释一下

```py
for issue in issues:
    r = subprocess.check_output(f"gh issue view {issue['number']} --json title,url,author,number,labels,createdAt,updatedAt,body",
                       shell=True, timeout=TIMEOUT)

    issue = json.loads(r)
    logging.info("process issue: %s", issue)
    date = datetime.strptime(issue['createdAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    title, permalink = issue['title'].split('[url]')
    title = title.replace(' ', '-')
    permalink = permalink.replace(' ', '-')
    with open(f"{ARTICLES_DIR}/{date}-{title}.md", "w") as f:
        f.write("---\n")
        f.write(f"layout: default\n")
        f.write(f"date: {date}\n")
        f.write(f"title: {title}\n")
        f.write(f"permalink: /{date[:7].replace('-', '/')}/{permalink}.html\n")
        f.write("---\n\n")
        f.write("\n\n")
        f.write(issue['body'])
```


1. `title, permalink = issue['title'].split('[url]')`：将问题的标题分割为两部分，前半部分作为文章的标题，后半部分作为文章的permalink。

2. `title = title.replace(' ', '-')` 和 `permalink = permalink.replace(' ', '-')`：将标题和permalink中的空格替换为破折号。

3. `with open(f"{ARTICLES_DIR}/{date}-{title}.md", "w") as f:`：创建一个新的Markdown文件，文件名由文章目录、日期和标题组成。

4. `f.write("---\n")` 等：在Markdown文件中写入文章的元数据，包括布局、日期、标题和permalink。

4. `f.write(issue['body'])`：将问题的正文作为文章的正文写入Markdown文件。
