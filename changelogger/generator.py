from typing import List
from datetime import datetime, timezone
from .parser import CommitInfo

def generate_changelog(version: str, commits: List[CommitInfo]) -> str:
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = [f"## [{version}] - {today_str}\n"]

    breaking = [c for c in commits if c.is_breaking]
    features = [c for c in commits if c.commit_type == "feat" and not c.is_breaking]
    fixes = [c for c in commits if c.commit_type == "fix" and not c.is_breaking]
    others = [c for c in commits if c.commit_type not in ["feat", "fix"] and not c.is_breaking]

    if breaking:
        out.append("### ⚠️ Breaking Changes")
        for c in breaking:
            scope_prefix = f"**{c.scope}:** " if c.scope else ""
            out.append(f"- {scope_prefix}{c.description}")
        out.append("")

    if features:
        out.append("### ✨ Features")
        for c in features:
            scope_prefix = f"**{c.scope}:** " if c.scope else ""
            out.append(f"- {scope_prefix}{c.description}")
        out.append("")

    if fixes:
        out.append("### 🐛 Bug Fixes")
        for c in fixes:
            scope_prefix = f"**{c.scope}:** " if c.scope else ""
            out.append(f"- {scope_prefix}{c.description}")
        out.append("")

    if others:
        out.append("### 🔧 Maintenance & Improvements")
        for c in others:
            scope_prefix = f"**{c.scope}:** " if c.scope else ""
            out.append(f"- {scope_prefix}{c.description}")
        out.append("")

    return "\n".join(out).strip()
