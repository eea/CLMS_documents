#!/usr/bin/env python3
"""Fail unless a promotion PR (into test or main) is approved by someone
other than the person who asked for it.

"Asked for" means either of these:
  - triggered the open-* workflow that opened the PR. Promotion PRs are
    authored by github-actions[bot], so GitHub's own "can't approve your own
    PR" never applies. The workflow leaves REQUESTER_MARKER in a bot comment.
  - clicked Ready for review. On a selective PR that click picks what lands.

A PR opened by a human counts its author as the requester.

Usage: check_independent_approval.py <pr-number> <head-sha>   (needs GH_TOKEN)
"""
import json
import os
import re
import subprocess
import sys

BOT = "github-actions[bot]"
REQUESTER_MARKER = re.compile(r"<!-- promotion-requester: ([A-Za-z0-9-]+) -->")


def gh_items(path):
    out = subprocess.check_output(
        ["gh", "api", "--paginate", path, "--jq", ".[]"], text=True
    )
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def requesters(pr_author, comments, timeline):
    """Logins that may not approve. Empty set means the requester is unknown."""
    who = set()
    if pr_author != BOT:
        who.add(pr_author)
    for c in comments:
        if c["user"]["login"] == BOT:
            who.update(REQUESTER_MARKER.findall(c.get("body") or ""))
    if not who:
        return who  # fail closed: don't count Ready clicks as the whole answer
    for e in timeline:
        if e.get("event") == "ready_for_review" and e.get("actor"):
            who.add(e["actor"]["login"])
    return who


def independent_approvers(reviews, excluded, head_sha):
    """Reviewers whose latest decisive review approves head_sha."""
    latest = {}
    for r in sorted(reviews, key=lambda r: r.get("submitted_at") or ""):
        if r["state"] in ("APPROVED", "CHANGES_REQUESTED", "DISMISSED"):
            latest[r["user"]["login"]] = r
    return sorted(
        login for login, r in latest.items()
        if r["state"] == "APPROVED"
        and r["commit_id"] == head_sha
        and login not in excluded
        and not login.endswith("[bot]")
    )


def main(pr, head_sha):
    repo = os.environ["GITHUB_REPOSITORY"]
    pr_author = json.loads(subprocess.check_output(
        ["gh", "api", f"repos/{repo}/pulls/{pr}"], text=True))["user"]["login"]
    excluded = requesters(
        pr_author,
        gh_items(f"repos/{repo}/issues/{pr}/comments"),
        gh_items(f"repos/{repo}/issues/{pr}/timeline"),
    )
    if not excluded:
        print("::error::No requester recorded on this PR (expected a "
              f"'promotion-requester' comment from {BOT}). Refusing to pass.")
        return 1
    approvers = independent_approvers(
        gh_items(f"repos/{repo}/pulls/{pr}/reviews"), excluded, head_sha)
    print(f"Requested by: {', '.join(sorted(excluded))}")
    if not approvers:
        print("::error::Needs an approval of the current head from someone "
              f"other than {', '.join(sorted(excluded))}.")
        return 1
    print(f"✅ Independently approved by: {', '.join(approvers)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
