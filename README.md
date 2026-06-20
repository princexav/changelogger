# ChangeLogger 📝

> An automated Semantic Versioning and Conventional Commit changelog generator.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 What is ChangeLogger?

Manually writing release notes and figuring out whether a release is a `MAJOR`, `MINOR`, or `PATCH` is error-prone. 

**ChangeLogger** inspects your Git commit history and automates the release lifecycle:
- **Conventional Commit Parsing:** Recognizes `feat:`, `fix:`, `perf:`, `refactor:`, `docs:`, and breaking changes (`BREAKING CHANGE:` or `feat!:`).
- **SemVer Calculation:** Automatically calculates the next semantic release number based on commits since the last git tag.
- **Markdown Changelog Generation:** Categorizes commits into structured, readable sections for `CHANGELOG.md` or GitHub Releases.

---

## 📦 Usage

```bash
git clone https://github.com/princexav/changelogger.git
cd changelogger
pip install -e .
```

Generate changelog preview:
```bash
python -m changelogger.cli generate
```

Calculate next version bump:
```bash
python -m changelogger.cli next-version --current 1.2.0
```

---

## 🧪 Testing

```bash
python -m unittest discover -s tests
```

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for 20+ hours of planned engineering milestones (monorepo support, GitHub Releases API integration).

## 📄 License

MIT License - see [LICENSE](LICENSE).
