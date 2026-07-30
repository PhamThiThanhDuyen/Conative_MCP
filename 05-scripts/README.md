# Scripts

Shared scripts live here when they apply across multiple skills.

## Kit Setup

Run the portability and validator checks after cloning:

```powershell
powershell -ExecutionPolicy Bypass -File 05-scripts/verify_kit.ps1
```

Install all bundled Skills into the current user's Codex skill directory:

```powershell
powershell -ExecutionPolicy Bypass -File 05-scripts/install_skills.ps1
```

The installer does not overwrite an existing Skill unless `-Force` is supplied.
It copies only self-contained Skill folders and does not install Goals or runtime
evidence.

## Skill Size Validator

For an existing skill, run before editing to capture its baseline and run again
after editing:

```powershell
python 05-scripts/validate_skill_size.py 02-skills/<capability>/<skill>
```

Do not introduce a new warning or increase the size of a skill that was already
warning. For a new skill, validate after creating the initial `SKILL.md` and
again after completing it. Run without a path to audit every skill in the kit.

The validator measures the `SKILL.md` body without YAML frontmatter.

| Result | Threshold | Exit code |
|---|---|---:|
| `PASS` | At most 800 words and 150 lines | 0 |
| `WARN` | Over 800 words or 150 lines | 0 |
| `FAIL` | Over 5,000 words or 500 lines | 1 |

Use `--fail-on-warning` in a strict CI job; warnings then return exit code `2`.
Move detailed rules and examples into `references/`, output material into
`assets/`, and deterministic operations into `scripts/`.

Current skill-local validators:

- `02-skills/test-design/testcase-matrix-design/scripts/validate_testcase_design.py`
- `02-skills/api-verification/qa-api-verification/scripts/validate_api_verification_report.py`

Add root-level scripts here only when at least two skills need the same deterministic
logic, for example:

- contract diff parser
- evidence package validator
- go/no-go report validator
- demo artifact generator
