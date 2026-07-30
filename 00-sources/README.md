# Internal Sources

This directory makes internal source material available to authorized users who
clone the kit from the approved private Conative GitLab repository.

## Contents

- `ba/Conative 3.0 - Services & Use cases.md`: BA-authored source snapshot.
- `product-docs/`: Git submodule linked to the private Conative Product Docs repo.

## Intentionally Excluded Sources

- `Docs_Comparedfield.md` is registered as `SRC-QA-COMPARED-FIELDS` but is not
  copied into this repository because the supplied source contains plaintext
  Shopify and internal API credentials. Only a credential-free normalized
  version is stored under `03-knowledge/`.

## Clone

Clone the kit and its Product Docs submodule together:

```powershell
git clone --recurse-submodules https://gitlab.cbidigital.dev/conative/knowledges/conative-tester-agent.git
```

For an existing clone:

```powershell
git submodule update --init --recursive
```

To update the submodule to the commit recorded by the kit after pulling:

```powershell
git pull --recurse-submodules
git submodule update --init --recursive
```

## Security

These files contain internal project information. Keep the kit in the approved
private Conative GitLab namespace. Do not mirror, publish, or upload this source
material to public or unapproved repositories.
