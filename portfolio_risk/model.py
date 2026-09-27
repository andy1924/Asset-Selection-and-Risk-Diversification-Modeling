"""Set-counting and Boolean policy checks for the portfolio example.

The 50 records reconstruct the aggregate counts supplied in the source PDF.
They are synthetic records, not downloaded market observations.
"""

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Asset:
    identifier: str
    tech: bool
    high_volatility: bool
    foreign_exposure: bool


# The seven disjoint regions implied by the source's marginal/intersection counts.
# Key order: Tech, High Volatility, Foreign Exposure.
REGION_COUNTS = {
    (True, False, False): 8,
    (False, True, False): 7,
    (False, False, True): 7,
    (True, True, False): 4,
    (True, False, True): 3,
    (False, True, True): 1,
    (True, True, True): 3,
    (False, False, False): 17,
}


def make_assets() -> list[Asset]:
    """Construct a reproducible 50-row witness for the published counts."""
    assets = []
    for flags, count in REGION_COUNTS.items():
        for _ in range(count):
            assets.append(Asset(f"A{len(assets) + 1:02}", *flags))
    return assets


def count_sets(assets: list[Asset]) -> dict[str, int]:
    """Compute marginal, intersection, and direct union cardinalities."""
    a = {x.identifier for x in assets if x.tech}
    b = {x.identifier for x in assets if x.high_volatility}
    c = {x.identifier for x in assets if x.foreign_exposure}
    return {
        "universe": len(assets),
        "A": len(a), "B": len(b), "C": len(c),
        "AB": len(a & b), "AC": len(a & c), "BC": len(b & c),
        "ABC": len(a & b & c),
        "union_direct": len(a | b | c),
    }


def inclusion_exclusion(counts: dict[str, int]) -> int:
    return (counts["A"] + counts["B"] + counts["C"]
            - counts["AB"] - counts["AC"] - counts["BC"]
            + counts["ABC"])


def policy(p: bool, q: bool, r: bool) -> bool:
    """(Q implies not P) and (R or (not Q and P))."""
    return ((not q) or (not p)) and (r or ((not q) and p))


def policy_cnf(p: bool, q: bool, r: bool) -> bool:
    """Equivalent CNF: (not Q or not P) and (R or not Q) and (R or P)."""
    return ((not q) or (not p)) and (r or (not q)) and (r or p)


def truth_table() -> list[tuple[bool, bool, bool, bool]]:
    return [(p, q, r, policy(p, q, r)) for p, q, r in product((False, True), repeat=3)]


def main() -> None:
    assets = make_assets()
    counts = count_sets(assets)
    exact = inclusion_exclusion(counts)
    naive = counts["A"] + counts["B"] + counts["C"]
    assert exact == counts["union_direct"] == 33
    assert all(policy(p, q, r) == policy_cnf(p, q, r)
               for p, q, r, _ in truth_table())

    print("50 synthetic assets reconstructed from the PDF's aggregate counts")
    print("|A|=18 |B|=15 |C|=14 |AB|=7 |AC|=6 |BC|=4 |ABC|=3")
    print(f"Naive tag incidences: {naive}")
    print(f"PIE unique tagged assets: {exact}")
    print(f"Direct set union: {counts['union_direct']}")
    print(f"Assets with no tag: {counts['universe'] - exact}")
    print(f"Incidence inflation relative to union: {(naive - exact) / exact * 100:.2f}%")
    valid = sum(accepted for _, _, _, accepted in truth_table())
    print(f"Policy satisfying assignments: {valid}/8")
    print("Policy and CNF agree on all 8 assignments")


if __name__ == "__main__":
    main()
