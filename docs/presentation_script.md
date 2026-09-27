# Presentation script

For `output/DM_PPT.pptx`, 13 slides. Presenter order: **Devaansh, Sarvesh, Arnav**.

Aim for **6 minutes**, excluding questions. Speak conversationally, at roughly 120–130 words per minute, with short pauses for the diagrams and equations. Directions in square brackets are cues, not spoken text. The timestamps are rehearsal targets, not rigid deadlines.

| Presenter | Slides | Section | Time |
| --- | --- | --- | --- |
| Devaansh Devnani | 1–4 | The overlap problem and its mathematical proof | 0:00–2:00 |
| Sarvesh Nimbalkar | 5–8 | Reconstructed data, code verification and Boolean rules | 2:00–4:00 |
| Arnav Deshpande | 9–13 | Policy examples, demonstration and conclusion | 4:00–6:00 |

## Devaansh: slides 1–4

### Slide 1: The overlap problem

**0:00–0:25 · 25 seconds**

[Point briefly to 47 and 33.]

> Good morning. We’re Devaansh, Sarvesh and Arnav. Our project applies discrete mathematics to asset selection. Here’s the question: if a stock belongs to several categories, how do we count it correctly? We’ll explain why a total of forty-seven becomes thirty-three, then use Boolean logic to check whether an asset meets a selection policy.

### Slide 2: One stock, three entries

**0:25–0:55 · 30 seconds**

[Trace STOCK-07 across the three lists.]

> Set A contains technology stocks, B contains stocks tagged as high volatility, and C contains stocks with foreign exposure. Notice STOCK-07: it appears in every list. Adding the list sizes counts this one asset three times. The labels tell us different things about the same stock. To count distinct assets, we need the union of the sets.

### Slide 3: Why the correction works

**0:55–1:30 · 35 seconds**

[Pause after each membership case.]

> Inclusion–exclusion corrects those repeated counts. An asset in one set contributes one. An asset in two sets contributes two initially, then we subtract its overlap once, leaving one. An asset in all three contributes three, loses three through the pairwise subtractions, and gains one through the triple intersection. Every tagged asset therefore contributes exactly one. That explains why the formula works.

### Slide 4: The inclusion–exclusion ledger

**1:30–2:00 · 30 seconds**

[Follow the ledger downward. Hand over after the last sentence.]

> Applying it to our example, the category sizes add to forty-seven. The three pairwise intersections total seventeen, and the triple intersection contains three assets. So forty-seven minus seventeen plus three gives thirty-three distinct tagged assets. We corrected the arithmetic in the original material using these inputs. Sarvesh will now show how the dataset and code check this result.

## Sarvesh: slides 5–8

### Slide 5: All fifty assets, accounted for

**2:00–2:30 · 30 seconds**

[Point to ABC, then AB only, then No tag. Don’t read every number.]

> Each dot represents one of fifty synthetic assets. We reconstructed these records from the supplied aggregate counts, rather than downloading market data. The regions do not overlap. For example, the seven assets in A intersection B include the three in all categories, leaving four in AB only. The tagged regions total thirty-three, and seventeen assets have none of these tags.

### Slide 6: Fourteen extra incidences

**2:30–2:55 · 25 seconds**

[Point to the subtraction and percentage.]

> The difference between forty-seven and thirty-three is fourteen extra category incidences. Dividing fourteen by the correct count, thirty-three, gives forty-two point four two percent inflation. This percentage describes the counting error. It doesn’t measure portfolio risk, and it doesn’t mean fourteen individual stocks each appeared exactly twice.

### Slide 7: Verification in six lines

**2:55–3:25 · 30 seconds**

[Point to the union operator and assertion. Do not read the code character by character.]

> The Python program builds sets of asset identifiers from those records. The union operator combines them and removes repeated identifiers. We compare that direct count with inclusion–exclusion, and the assertion checks that both equal thirty-three. Scanning n assets across k tags takes order n times k. With many categories, direct set operations avoid writing the exponentially growing inclusion–exclusion expansion.

### Slide 8: The rulebook has four passing cases

**3:25–4:00 · 35 seconds**

[Identify P, Q and R. Point to the two rules, then the S column.]

> Next, we check selection rules. P means high dividend, Q is the example’s high-volatility tag, and R means ESG compliant. The first rule says a high-volatility asset cannot also have the high-dividend tag. The second requires ESG compliance, or a dividend payer without the high-volatility tag. Both rules must hold. Across eight possible truth assignments, four pass. Arnav will explain what a pass actually means.

## Arnav: slides 9–13

### Slide 9: A policy can have a solution and still reject a stock

**4:00–4:40 · 40 seconds**

[Contrast the two examples. Point to the first CNF clause.]

> Consider an asset with a high dividend, no high-volatility tag, and no ESG tag. It satisfies both rules, so it passes. Now give it all three tags. It fails the first rule, even though it is ESG compliant. This separates two questions: does any valid combination exist, and does this particular asset qualify? The CNF expression below rewrites the same policy as an AND of OR clauses. Our code checks that both forms agree on every assignment.

### Slide 10: Run the proof

**4:40–5:20 · 40 seconds**

[Use the displayed output, or run the two prepared commands below. Avoid typing explanations into the terminal.]

> Here’s the program output. Direct union and inclusion–exclusion both return thirty-three, with seventeen assets outside the categories. The policy check finds four passing assignments and confirms agreement with CNF on all eight. The tests also check the reconstructed membership counts. Everything runs with Python’s standard library. This demonstrates the counting and policy logic on our constructed data. Real market use would need validated asset data and a clearly defined investment mandate.

### Slide 11: A count you can audit

**5:20–5:45 · 25 seconds**

[Pause on 33.]

> Our main result is thirty-three distinct tagged assets. Set theory explains the count, and Boolean logic makes each selection decision traceable. However, these tags alone cannot establish diversification or predict losses. Measuring financial risk would also require portfolio weights and relationships between asset returns. Our project provides a verified counting and screening foundation.

### Slide 12: References

**5:45–5:55 · 10 seconds**

[Let the slide remain visible briefly. Don’t read the bibliography.]

> The references cover the set theory, Python implementation and portfolio-risk context. Our repository contains the code and tests for reproducing the example.

### Slide 13: Thank you

**5:55–6:00 · 5 seconds**

[Face the audience.]

> Thank you. We’re happy to take your questions.

## Demo preparation

Open a terminal in the project directory before presenting. Use:

```sh
python3 portfolio_demo.py
python3 -m unittest discover -s tests -v
```

For a six-minute presentation, the output already on slide 10 is enough. If you demonstrate live, run the commands while Arnav explains the output. Keep a successful run ready as a backup.

## Adjusting the length

- **Five-minute version:** shorten slides 3, 5, 7, 8 and 9 by about ten seconds each. Omit slide 7’s complexity explanation, slide 9’s CNF explanation and the live demo. Keep the synthetic-data disclosure and the financial-risk limitation.
- **Seven-minute version:** use the extra minute for a live run and one truth-table example. Ask the audience whether P=1, Q=1, R=1 should pass, pause briefly, then explain the conflicting first rule.
- Rehearse the two handovers without introductions or repeated summaries. The next speaker should start directly with their slide.

## Deck consistency notes for the presenters

The current deck has a few legacy labels. These notes do not change the PPT:

- Slides 11–12 mention `test_portfolio_demo.py`. The uploaded repository now uses `tests/test_model.py`. Use the discovery command above.
- Reference [1] on slide 12 now points to the team’s GitHub project, while earlier slide footnotes still cite page numbers from the original supplied PDF. Those page references belong to the PDF. Keep this distinction clear if asked about the source of the aggregate counts.
- The four passing truth assignments are possible combinations, not four selected assets or evidence that half the fifty assets qualify.
