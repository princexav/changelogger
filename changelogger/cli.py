import sys
import argparse
import subprocess
from .parser import parse_commit
from .semver import calculate_next_version
from .generator import generate_changelog

def get_git_commits() -> list:
    try:
        out = subprocess.check_output(
            ["git", "log", "--pretty=format:%B%x00"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")
        raw_msgs = [m.strip() for m in out.split("\x00") if m.strip()]
        commits = []
        for msg in raw_msgs:
            parsed = parse_commit(msg)
            if parsed:
                commits.append(parsed)
        return commits
    except Exception:
        return []

def main():
    parser = argparse.ArgumentParser(prog="changelogger", description="Semantic release changelog generator.")
    subparsers = parser.add_subparsers(dest="command")

    gen_p = subparsers.add_parser("generate", help="Generate changelog from git history")
    gen_p.add_argument("--version", default="0.1.0", help="Release version")

    next_p = subparsers.add_parser("next-version", help="Calculate next semver bump")
    next_p.add_argument("--current", default="0.1.0", help="Current version")

    args = parser.parse_args()
    commits = get_git_commits()

    if args.command == "next-version":
        next_ver = calculate_next_version(args.current, commits)
        print(next_ver)
    elif args.command == "generate":
        print(generate_changelog(args.version, commits))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
