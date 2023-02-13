import sys
import os
from metrics import *

test_token = os.environ.get('GITHUB_TOKEN')
test_userId = "nullivex"
test_repo = "nodist"
testTotal = 10
testSuccess = 0

def testDownloadsSuccess(test_userId, test_repo, test_token):
    numDownloads = get_downloads(test_userId, test_repo, test_token)
    if numDownloads == '241465':
        return 1
    else:
        return 0

def testDownloadsFail(test_userId, test_repo, test_token):
    numDownloads = get_downloads(test_userId, test_repo, test_token)
    if numDownloads == '241465':
        return 1
    else:
        return 0

def testIssuesSuccess(test_userId, test_repo, test_token):
    numIssues = get_issues(test_userId, test_repo, test_token)
    if numIssues == '193':
        return 1
    else:
        return 0

def testForksSuccess(test_userId, test_repo, test_token):
    numForks = get_forks(test_userId, test_repo, test_token)
    if numForks == '207':
        return 1
    else:
        return 0

def testContributorsSuccess(test_userId, test_repo, test_token):
    num = get_contributors(test_userId, test_repo, test_token)

    if num == 'None':
        return 1
    else:
        return 0

testSuccess += testDownloadsSuccess(test_userId, test_repo, test_token)
testSuccess += testIssuesSuccess(test_userId, test_repo, test_token)
testSuccess += testForksSuccess(test_userId, test_repo, test_token)
testSuccess += testContributorsSuccess(test_userId, test_repo, test_token)

totalScore = (testSuccess / testTotal) * 100
print(totalScore)