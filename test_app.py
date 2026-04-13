import subprocess
import sys
import unittest


def run_app(*args: str) -> str:
    cmd = [sys.executable, "app.py", *args]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


class AppTests(unittest.TestCase):
    def test_default_greeting(self) -> None:
        self.assertEqual(run_app(), "Hello, World!")

    def test_named_greeting(self) -> None:
        self.assertEqual(run_app("Talha"), "Hello, Talha!")


if __name__ == "__main__":
    unittest.main()
