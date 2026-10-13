# Delivery record

This is a selected public consumer export, not corpus Git history. The source pin identifies exact captured bytes, original CLIR and fresh published-CLI lowerings. Public README/metadata transformations are recorded separately. Executable .law and .lawtest bytes were preserved. Five OpenStax roots plus units.si, bipm.si_brochure and la.newton.principia form the closure.

Examples are lowered directly from existing .lawtest fixtures using `law engine lower-test --lawtest-list --program`; the complete canonical case, context and query are preserved. Arithmetic, units, interpretation and source edition selection stay in the models/runtime. The checker compares all captured test expectations; it contains no subject evaluator.

The existing boundaries.depth implementation classifies Newton's declared source divisions. Its applicability helper uses a recorded import-only snapshot from the prior Wohngeld measurement because the corpus runtime pin is unpublished. That is not corpus runtime acceptance. CNXML divisions are not admitted, so OpenStax structural completeness is not_measured. SI and BIPM also have no admitted denominator. Source hashes and own node inventories remain available.

Observed CLI limitation: evaluation sourceAnchors are empty in these examples, while applied rule IDs, model anchor references and native unfold locators remain available. Resolved CNXML quotes can be element opening tags. This limitation is documented rather than counted as passed propagation. Scientific conclusions are conditional on modeled assumptions, not empirical validation or full textbook completeness.

The package metadata for rotation_equilibrium was absent in the captured authoring source. This export uses its original manifest, source declarations and executable bytes, plus a consumer README and license map. No model semantics were supplied from missing metadata.

Licensing maps captured/adapted publisher texts separately from independent Arxo code. NOTICE retains source URLs, dates, hashes and publisher conditions, including embedded copies. OpenStax NC/SA conditions remain active. Original source graphics are not supplied as new artwork.

Rebuild the exact allowlisted artifact into a new directory:

```sh
python3.12 tools/canon_publication.py export --source . --config publication.toml --out /tmp/arxo-openstax-mechanics-artifact
python3.12 tools/canon_publication.py verify --artifact /tmp/arxo-openstax-mechanics-artifact
```

No model npm package, private authoring materials, source-history export, full corpus gate, MCP host, SDK change or central catalog update is part of this delivery. Caches, .law directories, machine paths and node_modules are outside the allowlist. Public runtime comes from npm. releaseVerified is false and corpus is not_checked.
