from typing import List, Tuple
from .parser import CommitInfo

def parse_semver(version_str: str) -> Tuple[int, int, int]:
    clean = version_str.lstrip("v").strip()
    parts = clean.split(".")
    major = int(parts[0]) if len(parts) > 0 else 0
    minor = int(parts[1]) if len(parts) > 1 else 0
    patch = int(parts[2]) if len(parts) > 2 else 0
    return major, minor, patch

def calculate_next_version(current_version: str, commits: List[CommitInfo]) -> str:
    major, minor, patch = parse_semver(current_version)

    has_breaking = any(c.is_breaking for c in commits)
    has_feat = any(c.commit_type == "feat" for c in commits)
    has_fix = any(c.commit_type in ["fix", "perf", "refactor"] for c in commits)

    if has_breaking:
        return f"{major + 1}.0.0"
    elif has_feat:
        return f"{major}.{minor + 1}.0"
    elif has_fix:
        return f"{major}.{minor}.{patch + 1}"
    else:
        return f"{major}.{minor}.{patch}"
