# Principia 1687: axiomatic framework

`la.newton.principia@0.1.0` · `urn:la:newton:clir:principia`

A selected educational reasoning model. Conclusions are conditional on its rules, supplied facts, units and source edition. They do not establish empirical truth or complete textbook formalization.

Install the published npm CLI from the [repository README](../../README.md).

From the repository root, run the selected suite:

```sh
law test packages/la.newton.principia --file tests/01-aer-quadruplus.lawtest --json
```

Dependencies: none. See [law.toml](law.toml) for exact requirements and [law.lock](law.lock) for the delivered closure.

Read the `.law` files here for the executable definitions; [tests/](tests/) for original scenarios; [sources/](sources/) for pinned publisher bytes. [Depth and boundaries](../../README.md#depth-and-boundaries) records measured and unmeasured scope.

Independent Arxo code uses [Apache-2.0](../../LICENSE). Captured/adapted publisher texts retain the separate conditions in [NOTICE](../../NOTICE), including copies embedded in CLIR. No publisher endorsement is implied.
