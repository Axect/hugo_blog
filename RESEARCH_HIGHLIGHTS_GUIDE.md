# Research Highlights Guide

## What are Research Highlights?

Research Highlights are blog posts that translate your academic publications into accessible, engaging content for a broader audience. They follow the "Inverted Pyramid" style—starting with impact and working down to technical details.

## Why Create Research Highlights?

1. **Faculty Hiring**: Committees Google you. Show them you can communicate complex ideas clearly.
2. **Collaboration**: Make your work discoverable to potential collaborators outside your immediate subfield.
3. **Teaching Signal**: Demonstrates your ability to explain research—a key faculty skill.
4. **SEO**: Indexed by Google Scholar and search engines, increasing your paper's visibility.

## Creating a New Research Highlight

### Command

```bash
# For English (default)
hugo new posts/research-highlights/neural-hamilton.en.md --kind research-highlight

# For Korean
hugo new posts/research-highlights/neural-hamilton.kr.md --kind research-highlight
```

### Template Structure

The archetype provides a structured template with 6 main sections:

#### 1. 🎯 The Big Picture (2-3 sentences)
- **Goal**: Hook the reader immediately
- **Focus**: The "so what?" — why this matters
- **Style**: Plain English, no jargon
- **Example**: "Black holes in the early universe might be factories for dark matter particles—and our work shows we can detect their signatures in gamma-ray observations."

#### 2. 💡 What We Did (2-3 sentences)
- **Goal**: Clearly state YOUR contribution
- **Focus**: Active voice, specific actions
- **Avoid**: Passive constructions like "it was shown that..."
- **Example**: "We developed a neural operator that learns Hamiltonian mechanics from data, achieving 10x speedup over traditional RK4 solvers while maintaining physical consistency."

#### 3. 📊 Key Result (Visual + 2-3 sentences)
- **Goal**: Show, don't just tell
- **Focus**: Your single most important figure
- **Format**: Use Hugo shortcodes for images
```markdown
{{< img src="/images/research/neural-hamilton-accuracy.png" caption="Neural Hamilton achieves comparable accuracy to RK4 while being 10x faster" >}}
```

#### 4. 🔬 Technical Approach (200-300 words)
- **Goal**: Satisfy readers who want depth
- **Include**:
  - Mathematical/computational framework
  - Novel methodologies
  - Validation benchmarks
- **Subsections**: Methodology, Validation

#### 5. 🚀 Impact & Future Directions (2-3 sentences)
- **Goal**: Forward-looking, connects to bigger picture
- **Focus**: Implications, applications, next steps
- **Example**: "This framework opens the door to real-time inverse problems in cosmology, potentially enabling live parameter inference from gravitational wave observations."

#### 6. 📄 Publication & Resources
- Full citation
- Collapsible BibTeX (with Copy button!)
- Links to paper, code, slides

## Writing Tips

### The Inverted Pyramid

```
┌─────────────────────────────────┐
│    Impact & Conclusion          │  ← Start here (what matters?)
├─────────────────────────────────┤
│    Your Contribution            │  ← What did YOU do?
├─────────────────────────────────┤
│    Key Visual Result            │  ← Show it
├─────────────────────────────────┤
│    Technical Details            │  ← For experts
└─────────────────────────────────┘
```

**Why this works**: Busy readers (hiring committees!) can stop at any level and still get value.

### Target Length
- **Minimum**: 500 words (shows effort)
- **Ideal**: 500-800 words (comprehensive but skimmable)
- **Maximum**: 1000 words (avoid dissertation-length posts)

### Voice & Style
- ✅ Active voice: "We developed", "I discovered"
- ✅ Plain English first, technical terms second
- ✅ Visual hierarchy with headers and emojis
- ❌ Passive voice: "It was shown that..."
- ❌ Wall of equations without context
- ❌ Jargon without explanation

### Visuals
- **Always include at least one figure**
- Options:
  - Key plot from your paper
  - Schematic diagram
  - Animated GIF of simulation
  - "Visual abstract" infographic
- Store in: `static/images/research/`

## Example Workflow

### 1. Choose a Paper
Pick your most impactful publication or recent preprint.

### 2. Create the Post
```bash
hugo new posts/research-highlights/neural-hamilton.en.md --kind research-highlight
```

### 3. Fill in Frontmatter
```yaml
title: "Can AI Truly Understand Physics? Neural Hamilton Learns Hamiltonian Mechanics"
description: "We developed a neural operator that learns Hamiltonian dynamics from data, achieving 10x speedup while maintaining physical interpretability"
paper_title: "Neural Hamilton: Can A.I. Understand Hamiltonian Mechanics?"
paper_arxiv: "https://arxiv.org/abs/2410.20951"
paper_github: "https://github.com/Axect/Neural_Hamilton"
images: ["/images/research/neural-hamilton-cover.png"]
```

### 4. Write Following the Template
Use the template structure. Each section has inline comments explaining what to write.

### 5. Add Visuals
Export key figure from your paper, place in `static/images/research/`, embed with `{{< img >}}` shortcode.

### 6. Test Locally
```bash
hugo serve -t hello-friend-ng
```
Visit `http://localhost:1313/` and check:
- Does the visual hierarchy work?
- Is the BibTeX copy button working?
- Does it render correctly on mobile?

### 7. Publish
```bash
hugo -t hello-friend-ng
./build_local.sh
cd ../axect.github.io && git add . && git commit -m "Add research highlight: Neural Hamilton" && git push
```

## Recommended Posts to Write

Based on your publications, prioritize these:

### High Priority (Write First)
1. **Neural Hamilton** (arXiv 2024) — Your frontier work, shows AI4Science leadership
2. **DeeLeMa** (PRR 2023) — Published impact, demonstrates research reach
3. **PBH Axion Factory** (PTEP 2023) — Dark matter phenomenology core

### Medium Priority
4. **Learning Hamiltonian with Bayesian DA** (arXiv 2025) — Recent collaboration
5. **HyperbolicLR** (arXiv 2024) — Shows optimization expertise

### Future Content
- Tutorial: "Implementing Hamiltonian Neural Networks in Rust"
- Tutorial: "From Physics Equations to Neural Operators: A Practical Guide"
- Behind-the-scenes: "Building Peroxide: Lessons in Scientific Computing"

## SEO Best Practices

1. **Title**: Include key concepts (e.g., "Neural Operators", "Dark Matter", "AI4Science")
2. **Description**: One-sentence summary (appears in search results)
3. **Tags**: Add relevant tags (research, highlight, + domain-specific terms)
4. **Images**: Always set a cover image (improves social media sharing)
5. **Internal Links**: Link to your Research page, related blog posts

## Measuring Success

After publishing, track:
- Google Scholar citations of the paper (does the blog post correlate with increased citations?)
- Social media engagement (shares, likes on Twitter/LinkedIn)
- Hiring committee feedback ("We read your blog post about...")

---

**Remember**: The goal is not to recreate your paper—it's to make someone care enough to read your paper.
