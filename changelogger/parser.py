import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class CommitInfo:
    commit_type: str # feat, fix, perf, docs, etc.
    scope: Optional[str]
    description: str
    is_breaking: bool
    raw_message: str

CONVENTIONAL_PATTERN = re.compile(
    r"^(?P<type>[a-zA-Z]+)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<desc>.+)$"
)

def parse_commit(message: str) -> Optional[CommitInfo]:
    lines = message.strip().splitlines()
    if not lines:
        return None
    
    first_line = lines[0].strip()
    match = CONVENTIONAL_PATTERN.match(first_line)
    if not match:
        return None

    c_type = match.group("type").lower()
    scope = match.group("scope")
    has_exclamation = bool(match.group("breaking"))
    desc = match.group("desc").strip()

    # Check body for BREAKING CHANGE:
    has_breaking_footer = any(
        l.strip().startswith("BREAKING CHANGE:") or l.strip().startswith("BREAKING-CHANGE:")
        for l in lines[1:]
    )

    is_breaking = has_exclamation or has_breaking_footer

    return CommitInfo(
        commit_type=c_type,
        scope=scope,
        description=desc,
        is_breaking=is_breaking,
        raw_message=message
    )
