import unittest
from changelogger.parser import parse_commit
from changelogger.semver import calculate_next_version
from changelogger.generator import generate_changelog

class TestChangeLogger(unittest.TestCase):
    def test_parse_conventional_commits(self):
        c1 = parse_commit("feat(auth): add OAuth2 provider support")
        self.assertIsNotNone(c1)
        self.assertEqual(c1.commit_type, "feat")
        self.assertEqual(c1.scope, "auth")
        self.assertEqual(c1.description, "add OAuth2 provider support")
        self.assertFalse(c1.is_breaking)

        c2 = parse_commit("fix: resolve race condition in worker loop")
        self.assertIsNotNone(c2)
        self.assertEqual(c2.commit_type, "fix")
        self.assertIsNone(c2.scope)

        c3 = parse_commit("feat(api)!: drop legacy v1 endpoints\n\nBREAKING CHANGE: v1 removed")
        self.assertIsNotNone(c3)
        self.assertTrue(c3.is_breaking)

    def test_semver_bumping(self):
        feat = parse_commit("feat: new feature")
        fix = parse_commit("fix: patch bug")
        breaking = parse_commit("feat!: breaking change")

        self.assertEqual(calculate_next_version("1.0.0", [fix]), "1.0.1")
        self.assertEqual(calculate_next_version("1.0.0", [feat, fix]), "1.1.0")
        self.assertEqual(calculate_next_version("1.0.0", [breaking, feat]), "2.0.0")

    def test_generate_changelog(self):
        commits = [
            parse_commit("feat(ui): add dark mode toggle"),
            parse_commit("fix(api): correct 404 response header")
        ]
        log = generate_changelog("1.1.0", commits)
        self.assertIn("## [1.1.0]", log)
        self.assertIn("### ✨ Features", log)
        self.assertIn("add dark mode toggle", log)
        self.assertIn("### 🐛 Bug Fixes", log)

if __name__ == "__main__":
    unittest.main()
