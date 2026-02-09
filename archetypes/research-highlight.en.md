---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
toc: true
tags: ["research", "highlight"]
images: []
description: "Brief one-sentence summary of the research"
# Paper metadata
paper_title: ""
paper_authors: ""
paper_journal: ""
paper_arxiv: ""
paper_doi: ""
paper_github: ""
---

<!--
# Research Highlight Template (English Version)

This template follows the "Inverted Pyramid" style for maximum impact.
Target length: 500-800 words
Audience: Faculty hiring committees, potential collaborators, international peers

Structure:
1. Impact First: Start with the "so what?" - why does this matter?
2. Your Contribution: What did YOU specifically do?
3. Key Results: Show the most compelling finding (with visual)
4. Context & Approach: Technical details for interested readers
5. Future Directions: Where is this heading?
-->

## 🎯 The Big Picture

<!--
Start with the impact and motivation in plain English.
Answer: "Why should a busy faculty member care about this?"
Example: "Black holes in the early universe might be producing dark matter particles—and we can detect them."
-->

[Write 2-3 sentences explaining the core problem and why it matters to physics/AI/science]

## 💡 What We Did

<!--
Clearly state YOUR unique contribution.
Use active voice: "I developed...", "We discovered...", "This work demonstrates..."
Avoid: "It was shown that..." or passive constructions
-->

[Write 2-3 sentences describing your specific contribution and approach]

## 📊 Key Result

<!--
Feature the single most important figure or finding from your paper.
Use the {{< img >}} shortcode for figures with captions.
Example: {{< img src="/images/research/paper_key_figure.png" caption="Caption explaining the significance" >}}
-->

[Insert your most compelling visual here - a plot, diagram, or animation]

[Write 2-3 sentences explaining what the figure shows and why it's significant]

## 🔬 Technical Approach

<!--
Now add technical depth for readers who want details.
This section can be longer (200-300 words).
Include:
- The mathematical/computational framework you used
- Novel methodologies or algorithms
- Validation against benchmarks or previous work
-->

### Methodology

[Describe your technical approach]

### Validation

[How did you verify your results? What benchmarks did you use?]

## 🚀 Impact & Future Directions

<!--
End with forward-looking statements.
Connect to:
- Broader implications for your field
- Future research directions
- Potential applications
-->

[Write 2-3 sentences about what comes next and the broader implications]

---

## 📄 Publication

**Full Citation:**
[Author list]. *[Paper title]*. [Journal/Conference] ([Year]). [DOI/arXiv link]

<!--
Add BibTeX using collapsible details:

<details>
<summary>📋 BibTeX</summary>

```bibtex
@article{key2024,
  title={Paper Title},
  author={Your Name and Others},
  journal={Journal Name},
  year={2024}
}
```
</details>
-->

{{< note >}}
This work was presented at [Conference Name] and published in [Journal Name].
{{< /note >}}

## 🔗 Resources

- 📄 [Paper (arXiv)]()
- 📄 [Paper (Journal)]()
- 💻 [Code Repository]()
- 📊 [Supplementary Materials]()

---

## Related Posts

- [Link to related blog post or tutorial]

