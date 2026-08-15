# Security and privacy

Please do not open a public issue containing candidate information, credentials, private company information, or security findings with exploitable detail.

## Data boundary

This repository must never contain real candidate documents or operational recruiting records. Store runtime data in an access-controlled system with an appropriate retention policy. The `.gitignore` file provides defense in depth but is not a substitute for reviewing staged changes.

Before committing, run:

```bash
python3 -m unittest discover -s tests -v
git diff --cached
```

If sensitive data is committed, revoke exposed credentials immediately and remove the data from Git history before publishing.
