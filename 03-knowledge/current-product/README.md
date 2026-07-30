# Current Product

Store or index verified evidence of what the deployed Conative product currently
does. This layer supports regression and implementation comparison. It does not
prove that the observed behavior satisfies intended business requirements.

## Contents

- `product-docs/`: normalized QA knowledge derived from current user-visible behavior documented from code or runtime verification.
- `architecture/`: current system, module, dependency, data-flow, and environment maps.
- `api-specs/`: deployed or versioned OpenAPI, GraphQL, event, and integration contracts.
- `reference-data/`: current master data, allowed values, role matrices, and fixture catalogs.
- `mappings/source-reconciliation-field-map.md`: legacy Conative-to-source field
  mappings extracted from the supplied QA comparison guide; review freshness
  before relying on endpoint or field names.

Record environment, organization, role, build/version, and verification date for
behavior that can vary by deployment or tenant.

Start product-behavior lookup at `product-docs/README.md`.
