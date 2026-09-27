# Mathematical model

## Overlapping asset tags

Let the universe contain 50 assets. Define A as Tech, B as High Volatility,
and C as Foreign Exposure. The supplied presentation gives:

| Set or intersection | Cardinality |
| --- | ---: |
| A | 18 |
| B | 15 |
| C | 14 |
| A ∩ B | 7 |
| A ∩ C | 6 |
| B ∩ C | 4 |
| A ∩ B ∩ C | 3 |

Pairwise intersections include the triple intersection. Inclusion–exclusion
therefore gives:

```text
|A ∪ B ∪ C| = |A| + |B| + |C|
              - |A ∩ B| - |A ∩ C| - |B ∩ C|
              + |A ∩ B ∩ C|
            = 18 + 15 + 14 - 7 - 6 - 4 + 3
            = 33
```

An asset in one, two, or three sets contributes respectively 1, 2−1, or
3−3+1 to this expression. Each contribution equals one.

The reconstructed disjoint regions are:

| Region | Assets |
| --- | ---: |
| A only | 8 |
| B only | 7 |
| C only | 7 |
| A and B only | 4 |
| A and C only | 3 |
| B and C only | 1 |
| A, B, and C | 3 |
| No tag | 17 |
| Total | 50 |

These are synthetic records reconstructed from summary counts. They are not
downloaded market observations. The program independently computes the direct
set union and checks it against inclusion–exclusion.

The naive sum counts 47 tag incidences. It exceeds the union by 14 incidences,
or `(47 - 33) / 33 × 100 = 42.42%` relative to the unique tagged asset count.
The source presentation's result of 29 and its associated 62.07% figure are
arithmetic errors.

Scanning n assets with k Boolean tags takes O(nk). General inclusion–exclusion
has 2^k−1 nonempty subset terms, before accounting for intersection computation.

## Illustrative trading policy

P denotes high dividend, Q high volatility, and R ESG compliance. The mandate
requires both of these rules:

1. `Q ⇒ ¬P`: high volatility excludes high dividend.
2. `R ∨ (¬Q ∧ P)`: require ESG compliance or a low-volatility dividend payer.

Eliminating implication and applying the distributive law gives equivalent
conjunctive normal form (CNF):

```text
S = (Q ⇒ ¬P) ∧ (R ∨ (¬Q ∧ P))
  = (¬Q ∨ ¬P) ∧ (R ∨ ¬Q) ∧ (R ∨ P)
```

| P | Q | R | S |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

Four assignments satisfy the policy. The test compares the original formula
and CNF for every assignment. This exhaustive check is sufficient for this
three-variable example, so no SAT solver dependency is needed.

Satisfiability means at least one assignment passes. Actual asset eligibility
requires evaluating that asset's verified attributes. P and R values are not
supplied for the 50-asset counting example, so the policy check is separate
from the synthetic asset reconstruction.

## Interpretation

Unique tagged assets and Boolean policy results do not quantify portfolio
diversification, risk exposure, or expected losses. Financial risk depends on
portfolio weights and asset co-movement, among other assumptions.

## References

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications* (8th ed.).
  McGraw-Hill Education. Sections 1.1, 1.3, and 8.5.
- Python Software Foundation. [Set types: set and frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).
- Nimbalkar, S., Deshpande, A., and Devnani, D. (n.d.). *Discrete Mathematics
  Application Project* [Unpublished course presentation]. Supplied source for
  the example counts and mandate, with arithmetic corrected here.
- Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1),
  77–91. [doi:10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x).
