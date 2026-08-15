import json
import re
import unittest
from pathlib import Path

from scripts.render_post import load_config, render


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml"}
PROHIBITED_PATH_TERMS = {"resume", "resumes", "curriculum-vitae", "candidate-documents"}
SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
]
PERSONAL_DATA_PATTERNS = [
    re.compile(r"\b\d{6}-[1-4]\d{6}\b"),
    re.compile(r"\b01[016789][ -]?\d{3,4}[ -]?\d{4}\b"),
]


def public_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name == ".DS_Store":
            continue
        yield path


class PublicRepositoryTests(unittest.TestCase):
    def test_configuration_requires_human_approval(self):
        config = load_config(ROOT / "config" / "workflow.example.json")
        self.assertTrue(config["automation"]["human_approval_required"])
        self.assertFalse(config["automation"]["external_messages_enabled"])

    def test_candidate_example_uses_non_identifying_id(self):
        profile = json.loads((ROOT / "examples" / "candidate-profile.example.json").read_text())
        self.assertRegex(profile["candidate_id"], r"^candidate-\d{3}$")
        self.assertNotIn("name", profile)
        self.assertNotIn("email", profile)
        self.assertNotIn("birth_date", profile)
        self.assertNotIn("address", profile)

    def test_role_post_is_deterministic(self):
        config = load_config(ROOT / "config" / "workflow.example.json")
        output = render(config, "Synthesize cited sources.", "Traceable research evidence.")
        self.assertIn(config["project_title"], output)
        self.assertIn("accountable human decision-makers", output)

    def test_no_candidate_document_is_tracked(self):
        violations = []
        for path in public_files():
            lowered_parts = {part.lower() for part in path.relative_to(ROOT).parts}
            if lowered_parts & PROHIBITED_PATH_TERMS or path.suffix.lower() in {".pdf", ".doc", ".docx"}:
                violations.append(str(path.relative_to(ROOT)))
        self.assertEqual([], violations)

    def test_no_obvious_secret_or_personal_identifier(self):
        violations = []
        for path in public_files():
            if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore"}:
                continue
            text = path.read_text(encoding="utf-8")
            for pattern in SECRET_PATTERNS + PERSONAL_DATA_PATTERNS:
                if pattern.search(text):
                    violations.append(f"{path.relative_to(ROOT)}: {pattern.pattern}")
        self.assertEqual([], violations)

    def test_public_material_is_english(self):
        hangul = re.compile(r"[\uac00-\ud7a3]")
        violations = []
        for path in public_files():
            if path.suffix.lower() in TEXT_SUFFIXES or path.name == ".gitignore":
                if hangul.search(path.read_text(encoding="utf-8")):
                    violations.append(str(path.relative_to(ROOT)))
        self.assertEqual([], violations)


if __name__ == "__main__":
    unittest.main()
