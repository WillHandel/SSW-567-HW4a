import requests


def getGithubInfo(githubUser):
    repos = requests.get(f"https://api.github.com/users/{githubUser}/repos").json()

    info = []
    for repo in repos:
        name = repo["name"]
        commits = requests.get(f"https://api.github.com/repos/{githubUser}/{name}/commits").json()
        commitAmnt = len(commits)
        info.append(f"Repo: {name}, Number of commits: {commitAmnt}")
    return info


    pass


print("Test from within githubGetter.py: ",getGithubInfo("WillHandel"))