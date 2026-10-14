# Delivery record

This is a selected public consumer export, not corpus Git history. The source pin identifies exact captured bytes, original CLIR and fresh published-CLI lowerings. Public README/metadata transformations are recorded separately. Executable .law and .lawtest bytes were preserved. Five OpenStax roots plus units.si, bipm.si_brochure and la.newton.principia form the closure.

Examples are lowered directly from existing .lawtest fixtures using `law engine lower-test --lawtest-list --program`; the complete canonical case, context and query are preserved. Arithmetic, units, interpretation and source edition selection stay in the models/runtime. The checker compares all captured test expectations; it contains no subject evaluator.

Release 0.1.1 adds CNXML support to the existing boundaries.depth implementation. Both module snapshots and exact addressable CNXML elements in content/glossary are measured from original bytes; 86 module snapshots and 13,154 addressable elements are enumerated. Classifier levels remain structural, not complete scientific formalization. Exact hashed publication editions are isolated, and absent/duplicate/stale element identifiers refuse measurement. No authoring .law, .lawtest, CLIR or runtime semantics changed.

The public snapshot of the common classifier and source-division reader is under tools/depth. Python 3.12 plus the standard library reproduces the five measurements without a private checkout or runtime helper. Applicability is imported lazily only for the pre-existing text-edition grouping; CNXML uses exact publication editions. The earlier Newton measurement retains its separate implementation hashes and recorded import-only applicability snapshot. SI and BIPM keep not_measured because no admitted source-division denominator was added for them.

Observed CLI limitation: evaluation sourceAnchors are empty in these examples, while applied rule IDs, model anchor references and native unfold locators remain available. Resolved CNXML quotes can be element opening tags. This limitation is documented rather than counted as passed propagation. Scientific conclusions are conditional on modeled assumptions, not empirical validation or full textbook completeness.

The package metadata for rotation_equilibrium was absent in the captured authoring source. This export uses its original manifest, source declarations and executable bytes, plus a consumer README and license map. No model semantics were supplied from missing metadata.

Licensing maps captured/adapted publisher texts separately from independent Arxo code. NOTICE retains source URLs, dates, hashes and publisher conditions, including embedded copies. OpenStax NC/SA conditions remain active. Original source graphics are not supplied as new artwork.

Rebuild the exact allowlisted artifact into a new directory:

```sh
python3.12 tools/canon_publication.py export --source . --config publication.toml --out /tmp/arxo-openstax-mechanics-artifact
python3.12 tools/canon_publication.py verify --artifact /tmp/arxo-openstax-mechanics-artifact
```

No model npm package, private authoring materials, source-history export, full corpus gate, MCP host, SDK change or central catalog update is part of this delivery. Caches, .law directories, machine paths and node_modules are outside the allowlist. Public runtime comes from npm. releaseVerified is false and corpus is not_checked.

Public Ubuntu/Node 20 CI passed at commit `8d2be5dd09bb5c39f896ac53def4d1e434e8e19b`: https://github.com/arxohq/arxo-openstax-mechanics/actions/runs/38479699988. Later changes record delivery evidence and clarify snapshot counts/boundaries only; model and example bytes are unchanged. Anonymous HTTPS clone and the README example passed.

The 0.1.1 change ran 24 addressed measurement tests (16 existing regressions plus eight new CNXML tests), then recomputed all five packages from hash-checked immutable inputs. Reader execution evidence from 0.1.0 remains applicable: no executable model or example bytes changed. No full corpus or runtime suites were repeated for this measurement/documentation update.

The addressed [0.1.1 Linux depth CI](https://github.com/arxohq/arxo-openstax-mechanics/actions/runs/38548881032) passed at `9d4dbdae1b1843fe038dcc5ce7758a9c69b2d8e8`: eight CNXML regression tests and exact five-package recomputation. Subsequent changes record this evidence and strengthen required delivery files; classifier, models and measurement rows remain unchanged.
