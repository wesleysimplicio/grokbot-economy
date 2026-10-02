import csv, os, subprocess, sys, tempfile, unittest
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "scripts", "token_log.py")
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import token_log  # noqa: E402


def run(*args):
    return subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)


class TokenLogTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.f = os.path.join(self.tmp.name, "t.csv")

    def tearDown(self):
        self.tmp.cleanup()

    def add(self, *extra, path="api", tokens="1"):
        return run("add", "--agent", "a", "--task", "t", "--path", path, "--tokens", tokens, "--file", self.f, *extra)

    def assertCleanError(self, r):
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("token_log: error:", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_selftest(self):
        r = run("--selftest")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("selftest ok", r.stdout)

    def test_cli_add_and_summary(self):
        for p, n in (("mcp", "10"), ("browse", "90")):
            self.assertEqual(self.add(path=p, tokens=n).returncode, 0)
        tot = token_log.summary(self.f)
        self.assertEqual(tot["browse"]["tokens"], 90)
        self.assertEqual(sum(v["tasks"] for v in tot.values()), 2)

    def test_template_header_matches(self):
        with open(os.path.join(HERE, "..", "templates", "token-log.csv"), encoding="utf-8") as fh:
            self.assertEqual(fh.readline().strip(), ",".join(token_log.FIELDS))

    def test_negative_tokens_clean_error(self):
        self.assertCleanError(self.add(tokens="-5"))

    def test_nan_and_inf_cost_rejected(self):
        for c in ("nan", "inf", "-inf"):
            self.assertCleanError(self.add(f"--cost={c}"))
        self.assertFalse(os.path.exists(self.f))

    def test_missing_directory_clean_error(self):
        r = run("add", "--agent", "a", "--task", "t", "--path", "api", "--tokens", "1",
                "--file", os.path.join(self.tmp.name, "nope", "x.csv"))
        self.assertCleanError(r)

    def test_malformed_csv_clean_error(self):
        with open(self.f, "w", encoding="utf-8") as fh:
            fh.write("a,b,c\n1,2,3\n")
        self.assertCleanError(run("summary", "--file", self.f))
        with open(self.f, "w", encoding="utf-8") as fh:
            fh.write(",".join(token_log.FIELDS) + "\nd,a,t,api,lots,0,n\n")
        self.assertCleanError(run("summary", "--file", self.f))

    def test_no_trailing_newline(self):
        self.add()
        with open(self.f, "a", encoding="utf-8") as fh:
            fh.write("2026-01-01T00:00+00:00,h,t,api,5,0.0000,last")
        self.add(path="mcp", tokens="7")
        tot = token_log.summary(self.f)
        self.assertEqual(tot["api"]["tasks"], 2)
        self.assertEqual(tot["mcp"]["tokens"], 7)

    def test_formula_values_escaped(self):
        r = run("add", "--agent", '=HYPERLINK("http://x")', "--task", "+1", "--path", "api",
                "--tokens", "1", "--notes", "@sum", "--file", self.f)
        self.assertEqual(r.returncode, 0, r.stderr)
        with open(self.f, newline="", encoding="utf-8") as fh:
            row = list(csv.DictReader(fh))[0]
        self.assertEqual(row["agent"], "'=HYPERLINK(\"http://x\")")
        self.assertEqual(row["task"], "'+1")
        self.assertEqual(row["notes"], "'@sum")
        self.assertEqual(token_log.clean_text("-x"), "'-x")
        self.assertEqual(token_log.clean_text("a\r\nb"), "a b")

    @unittest.skipIf(token_log.fcntl is None, "POSIX only")
    def test_parallel_writes_with_lock(self):
        with ThreadPoolExecutor(max_workers=16) as ex:
            results = list(ex.map(lambda i: self.add("--lock", "--notes", "x" * 300, tokens=str(i)), range(40)))
        self.assertTrue(all(r.returncode == 0 for r in results))
        with open(self.f, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        self.assertEqual(lines.count(",".join(token_log.FIELDS)), 1)
        self.assertEqual(len(lines), 41)
        self.assertEqual(token_log.summary(self.f)["api"]["tasks"], 40)


if __name__ == "__main__":
    unittest.main()
