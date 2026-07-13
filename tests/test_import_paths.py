import importlib
import sys
from pathlib import Path
import unittest


class SetupPathsTests(unittest.TestCase):
    def test_setup_paths_falls_back_when_framework_helpers_are_unavailable(self):
        repo_root = Path(__file__).resolve().parents[1]
        sys.path.insert(0, str(repo_root))

        main_module = importlib.import_module("main")
        ext_base = main_module.setup_paths()

        self.assertEqual(ext_base, repo_root)
        self.assertIn(str(repo_root), sys.path)
        self.assertIn(str(repo_root / "src"), sys.path)


if __name__ == "__main__":
    unittest.main()
