import os, subprocess, sys, tempfile, unittest
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "scripts", "token_log.py")
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import token_log  # noqa: E402


class TokenLogTest(unittest.TestCase):
    def test_selftest(self):
        out = subprocess.run([sys.executable, SCRIPT, "--selftest"], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("selftest ok", out.stdout)

    def test_cli_add_and_summary(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "t.csv")
            for p, n in (("mcp", 10), ("browse", 90)):
                r = subprocess.run([sys.executable, SCRIPT, "add", "--agent", "a", "--task", "t",
                                    "--path", p, "--tokens", str(n), "--file", f], capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
            tot = token_log.summary(f)
            self.assertEqual(tot["browse"]["tokens"], 90)
            self.assertEqual(sum(v["tasks"] for v in tot.values()), 2)

    def test_template_header_matches(self):
        with open(os.path.join(HERE, "..", "templates", "token-log.csv"), encoding="utf-8") as fh:
            self.assertEqual(fh.readline().strip(), ",".join(token_log.FIELDS))


if __name__ == "__main__":
    unittest.main()
