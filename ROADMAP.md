# ChangeLogger Roadmap (20+ Hours Planned Work)

This roadmap tracks engineering goals and planned improvements for `ChangeLogger`.

---

## 📍 Phase 1: Git Provider Integrations (6–8 Hours)
- [ ] **GitHub Releases API:** Automatically publish changelogs and create GitHub Releases via API token.
- [ ] **PR & Author Attribution:** Query commit metadata to append `(@contributor)` and PR numbers `#123` to release lines.
- [ ] **Signed Git Tagging:** Automatically run `git tag -s` with GPG signing for released versions.

---

## 📍 Phase 2: Monorepo & Scoped Packages (6–8 Hours)
- [ ] **Package Path Filtering:** Generate independent changelogs for subpackages based on commit file diff paths.
- [ ] **Cross-package Dependency Bumps:** Detect when core package bumps require bumping dependent workspace packages.
- [ ] **Config File (`.changelogger.toml`):** Support custom commit type aliases, header titles, and ignored scopes.

---

## 📍 Phase 3: Templating & Formats (6–8 Hours)
- [ ] **Jinja2 Template Engine:** Support custom user templates for Slack release announcements and HTML newsletters.
- [ ] **Keep-a-Changelog Format Conformance:** Ensure 100% compliance with keepachangelog.com standard format.
- [ ] **GitLab & Gitea Support:** Add web release dispatchers for self-hosted GitLab and Gitea instances.
