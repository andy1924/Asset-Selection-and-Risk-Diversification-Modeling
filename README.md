# Asset Selection and Risk Diversification Modeling

A small Python project demonstrating **set theory**, **inclusion–exclusion**,
and **propositional logic** through portfolio risk tags and an illustrative
trading policy.

The demo reconstructs 50 synthetic assets, checks a direct set union against
inclusion–exclusion, and evaluates every truth assignment of a three-variable
Boolean policy. It uses only the Python standard library.

## Quick start

Requires **Python 3.10 or newer**. No package installation is necessary.

```sh
git clone https://github.com/andy1924/Asset-Selection-and-Risk-Diversification-Modeling.git
cd Asset-Selection-and-Risk-Diversification-Modeling
python3 -m portfolio_risk
python3 -m unittest discover -s tests -v
```

The presentation's original command also works:

```sh
python3 portfolio_demo.py
```

For an optional installed command, run `python3 -m pip install .`, then
`portfolio-risk-demo`. Packaging uses setuptools; the runtime has no external
dependencies.

## Repository structure

```text
.
├── portfolio_risk/
│   ├── __init__.py       # Package metadata
│   ├── __main__.py       # python3 -m portfolio_risk
│   └── model.py          # Asset reconstruction, set counts, and policy logic
├── tests/
│   ├── __init__.py
│   └── test_model.py     # Set counts and exhaustive policy checks
├── docs/
│   └── mathematics.md   # Derivation, truth table, and references
├── portfolio_demo.py    # Presentation-compatible entry point
├── pyproject.toml       # Package metadata and CLI command
├── .gitignore
└── README.md
```

## Expected output

```text
50 synthetic assets reconstructed from the PDF's aggregate counts
|A|=18 |B|=15 |C|=14 |AB|=7 |AC|=6 |BC|=4 |ABC|=3
Naive tag incidences: 47
PIE unique tagged assets: 33
Direct set union: 33
Assets with no tag: 17
Incidence inflation relative to union: 42.42%
Policy satisfying assignments: 4/8
Policy and CNF agree on all 8 assignments
```

## What the project verifies

### Exact asset counting

A is Tech, B is High Volatility, and C is Foreign Exposure. Category sizes
overlap, so the naive sum counts tag incidences rather than distinct assets.

```text
|A ∪ B ∪ C| = 18 + 15 + 14 - 7 - 6 - 4 + 3 = 33
```

The tests reproduce every marginal and intersection count and verify that
inclusion–exclusion agrees with direct set union.

### Boolean policy consistency

P represents high dividend, Q high volatility, and R ESG compliance:

```text
S   = (Q ⇒ ¬P) ∧ (R ∨ (¬Q ∧ P))
CNF = (¬Q ∨ ¬P) ∧ (R ∨ ¬Q) ∧ (R ∨ P)
```

The tests evaluate all eight assignments, find four satisfying assignments,
and verify that the original expression and CNF agree in every case.

Read [the mathematical model](docs/mathematics.md) for the disjoint-region
reconstruction, truth table, complexity discussion, and interpretation.

## Data and limitations

The supplied course presentation provides aggregate counts but no asset-level
market data. This program builds **synthetic records** that reproduce those
counts. It verifies the mathematics, not the presentation's market-data
provenance.

The original presentation reports a union of 29 and inflation of 62.07%.
Its listed inputs instead give **33** and **42.42%**. This project uses the
corrected arithmetic.

A satisfiable policy has at least one passing assignment. Real trade
eligibility requires verified asset attributes. These counts and Boolean
rules do not measure financial diversification, expected losses, or compliance
with a real investment mandate.

## References

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications* (8th ed.).
  McGraw-Hill Education. Sections 1.1, 1.3, and 8.5.
- Python Software Foundation. [Set types: set and frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).
- Nimbalkar, S., Deshpande, A., and Devnani, D. (n.d.). *Discrete Mathematics
  Application Project* [Unpublished course presentation]. Source of the
  aggregate counts and illustrative policy.
- Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1),
  77–91. [doi:10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x).
