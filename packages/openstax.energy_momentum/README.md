# Work, energy and momentum

`openstax.energy_momentum@0.1.0` · `urn:openstax:clir:energy-momentum`

A selected educational reasoning model. Conclusions are conditional on its rules, supplied facts, units and source edition. They do not establish empirical truth or complete textbook formalization.

Install the published npm CLI from the [repository README](../../README.md).

From the repository root, run the selected suite:

```sh
law test packages/openstax.energy_momentum --file tests/01-work-energy-power.lawtest --json
```

Dependencies: `units.si`, `bipm.si_brochure`, `openstax.measurement`, `openstax.kinematics`, `openstax.dynamics`. See [law.toml](law.toml) for exact requirements and [law.lock](law.lock) for the delivered closure.

Read the `.law` files here for the executable definitions; [tests/](tests/) for original scenarios; [sources/](sources/) for pinned publisher bytes. [Depth and boundaries](../../README.md#depth-and-boundaries) records measured and unmeasured scope.

Independent Arxo code uses [Apache-2.0](../../LICENSE). Captured/adapted publisher texts retain the separate conditions in [NOTICE](../../NOTICE), including copies embedded in CLIR. No publisher endorsement is implied.
