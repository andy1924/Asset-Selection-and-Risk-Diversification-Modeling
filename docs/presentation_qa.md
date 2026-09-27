# Likely questions and short answers

For the six-minute presentation. Start with the short answer and expand only if asked. Devaansh handles the counting proof, Sarvesh handles the data and implementation, and Arnav handles policy interpretation and limitations. Anyone may answer if they know the point clearly.

## Core questions

### 1. Why is the answer 33 instead of 47?

**Devaansh:** “Forty-seven adds category memberships, so it repeats assets with multiple tags. Inclusion–exclusion gives 18 + 15 + 14 − 7 − 6 − 4 + 3 = 33 distinct assets. The direct Python union gives the same count.”

### 2. Why do you add the triple intersection back?

**Devaansh:** “An asset in all three sets is counted three times initially and subtracted three times through the pairwise overlaps. That leaves zero. Adding the triple intersection restores its contribution to one.”

### 3. How did you obtain the data? Are these actual stocks?

**Sarvesh:** “The supplied material gives aggregate category and overlap counts. We constructed fifty synthetic asset records consistent with those counts. The demonstration verifies the mathematics and implementation. It does not validate the counts against actual market records.”

If pressed: “Many different datasets could have these same region counts. Our reconstruction is one valid example.”

### 4. What does 42.42% represent?

**Sarvesh:** “It is the overcount relative to the correct distinct count: fourteen divided by thirty-three, multiplied by one hundred. It measures count inflation, not financial risk.”

If the examiner uses 47 as the denominator: “Fourteen divided by forty-seven is about 29.79%, which measures the excess as a share of the reported category total. We explicitly use the correct count as our baseline.”

### 5. Does four out of eight mean 50% of your assets pass?

**Arnav:** “No. Those are the eight possible combinations of three Boolean variables. Four combinations satisfy the policy. We would need each asset’s dividend and ESG tags, alongside its volatility tag, to calculate how many actual assets qualify.”

### 6. Why does an ESG-compliant asset sometimes fail?

**Arnav:** “Both rules must hold. An asset with high dividend and high volatility violates the first rule. ESG compliance satisfies the second rule but cannot cancel a failure of the first.”

### 7. What does this prove about diversification?

**Arnav:** “It proves that we can count tagged assets consistently and evaluate a stated screening policy. It does not prove a reduction in financial risk. That would require return data, portfolio weights and covariance analysis.”

## Technical follow-ups

### 8. Did you use a SAT solver?

**Arnav:** “No external SAT solver. We exhaustively evaluate all eight assignments, which is sufficient for three variables. This establishes that the example policy is satisfiable and identifies its valid assignments.”

### 9. Why convert the policy to CNF?

**Arnav:** “CNF expresses the policy as an AND of OR clauses, a useful form for many SAT methods. Implication becomes `¬Q ∨ ¬P`, and distributing OR over AND gives the other two clauses. Our exhaustive check confirms equivalence for all eight assignments.”

Original policy:

```text
(Q ⇒ ¬P) ∧ (R ∨ (¬Q ∧ P))
```

Equivalent CNF:

```text
(¬Q ∨ ¬P) ∧ (R ∨ ¬Q) ∧ (R ∨ P)
```

### 10. How do you know the code works?

**Sarvesh:** “We check each reconstructed region and the supplied marginal and intersection counts. We compare direct union with inclusion–exclusion. A second test checks the policy and CNF across every possible assignment and confirms four pass.”

If pressed: “The assertion on slide 7 checks this particular example. The membership argument on slide 3 explains the mathematical result more generally.”

### 11. Would this scale to more categories?

**Sarvesh:** “The general inclusion–exclusion formula has 2 to the power k minus one intersection terms. For asset-level data, scanning n assets across k tags and building sets is more practical. Boolean enumeration also grows exponentially, so a larger policy may benefit from a SAT solver.”

The `O(nk)` statement describes scanning the tag data under ordinary constant-time tag access and expected hash-set insertion assumptions. It does not include acquiring or validating market data.

### 12. What do the 17 untagged assets mean?

**Devaansh:** “They are outside A union B union C. They lack these three particular tags in the constructed dataset. That does not establish that they are risk-free or suitable investments.”

### 13. Is the dividend–volatility rule a financial law?

**Arnav:** “No. It is an illustrative selection constraint from the project. Another investment mandate could use different rules. We evaluate the stated policy rather than claim that those asset characteristics are universally incompatible.”

## Last-minute revision

Remember these distinctions:

- **47:** category incidences. **33:** distinct tagged assets. **14:** excess incidences.
- **17:** assets outside the three category sets, not assets proven safe.
- **4/8:** satisfying Boolean combinations, not the acceptance rate of the fifty assets.
- **Synthetic data:** constructed from supplied counts, not downloaded market data.
- **Verification:** direct union agrees with inclusion–exclusion, and policy agrees with CNF.

If a question goes beyond the implementation, say: “We haven’t implemented that part. Our current demonstration covers the counting and Boolean screening, and that would be an extension.”
