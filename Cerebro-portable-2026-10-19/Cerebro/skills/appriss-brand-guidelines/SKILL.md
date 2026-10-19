---
name: appriss-brand-guidelines
description: Appriss Retail brand guidelines for creating presentations, documents, and branded content. MANDATORY TRIGGERS - Use when creating PowerPoint presentations, Word documents, PDFs, HTML files, one-pagers, reports, marketing materials, or any content requiring Appriss Retail branding including logos, colors (Raisin #1E1531, Primary Green #7DE2DD, #7D0748, Mid-Blue #528DF5, sub-head dark #EBEEF2), Poppins typography, and visual design standards.
---

# Appriss Retail Brand Guidelines

## Overview

When creating presentations, documents, or any branded content for Appriss Retail, apply the following brand guidelines automatically. Always maintain visual consistency with these specifications.

**Color fidelity is non-negotiable.** Always use the exact hex values defined in this document. Never substitute, approximate, or drift toward similar hues — no generic blues, grays, greens, or reds in place of the brand palette. If a color is needed and isn't in the palette, default to the closest approved color rather than inventing one.

---

## Brand Identity

**Company:** Appriss Retail
**Industry:** Retail Loss Prevention / AI-Powered Fraud Detection
**Tagline:** *Stop Losses From Checkout To Return*
**Positioning:** The total loss solution for omnichannel retail

### Products

| Product | Color accent | Description |
|---------|-------------|-------------|
| **Engage** | Bright Blue #1F59BD | Returns & claims intelligence |
| **Secure** | Darker Green #007971 | Transaction loss prevention |
| **Incident** | #7D0748 | Case & incident management |

---

## Logo Assets

### Approved Logo Files

```
appriss-logo-dark.png           ← Raisin crown + wordmark — use on light backgrounds
appriss-logo-white.png          ← All white — use on dark backgrounds
appriss-logo-white-stacked.png  ← White stacked (crown over wordmark) — limited horizontal space
appriss-crown-gray.png          ← Gray crown only — footer bar use only
```

Logo aspect ratio (horizontal): **4.878** (800×164 dark; 1137×233 white — same ratio)
Stacked logo aspect ratio: **1.333** (800×600)

> All previous logo variants are retired — including any file with "small", "fullcolor", "nocr", or a ® symbol. Only use the four files above.

### Logo Rules

- **Logo appears on title/cover slides and closing slides only — NEVER on content slides.**
- Cover slides: white logo (`appriss-logo-white.png`), top-left, x: 0.75", y: 0.55", w: 2.2", h: 0.451"
- Closing slides: white logo (`appriss-logo-white.png`), left-aligned, vertically centered
- Co-branded covers: Appriss logo top-left, customer logo to its right
- Never stretch, rotate, or recolor logos
- Never use a logo with a ® or © symbol attached to it
- Never use the full-color (pink/teal crown) logo variant

### Product Sub-Brand Icons

| Product | Icon Description | Background |
|---------|-----------------|------------|
| **Engage** | Two curved sync arrows | Purple circle |
| **Secure** | Four compass arrows | Purple circle |
| **Incident** | Six-pointed burst | White circle, Deep Red accent |

---

## Color Palette

### Primary Colors

```
Raisin (Primary Dark)       #1E1531   Headlines on light bg, dark slide backgrounds
Primary Green               #7DE2DD   Stat numbers on dark bg, accents, buttons
Darker Green                #007971   Stat numbers on light bg, hover, captions on light
White                       #FFFFFF   Text on dark, reversed elements
```

### Accent Colors

```
Bright Blue                 #1F59BD   Emphasis, charts, stat numbers, Engage product
Mid-Blue                    #528DF5   Data viz, secondary accents
Pale Blue                   #DBE5FD   Light fills, card borders, subtle highlights
Deep Red                    #7D0748   Alerts, Incident product accent, UI elements only — NEVER for copy or body text in PPT or PDF
Gold                        #FBC521   Data visualization, warm accents
```

### Neutral Colors

```
Background Gray             #F4F6F9   Slide/page backgrounds
Sub-head on dark            #EBEEF2   Sub-heads and supporting headlines on dark backgrounds (decks + PDFs)
Gray (text)                 #6D7580   Body text and captions on light backgrounds
Footer gray                 #A5ABB3   Footer copyright text only
```

---

## Typography

### Font Family
**Poppins only.** Fallback: Arial.

- **Semi-Bold (600):** All headers (H1, H2, H3) — use `fontFace: "Poppins SemiBold", bold: false`
- **Regular (400):** All body copy, captions, stat labels

> Never use `bold: true` for headers. Always use `fontFace: "Poppins SemiBold"` with `bold: false` to achieve the correct semi-bold weight.

### Text Case
- Sentence case for all text unless otherwise specified
- Always capitalize: product names (Engage, Secure, Incident, Sidekick), proper nouns, acronyms (AI, ROI, POS)

### Header Colors
- Light backgrounds: Raisin (#1E1531)
- Dark backgrounds: White (#FFFFFF)

### Color restrictions on copy
- **Never use #7D0748 for any copy** — headlines, body text, captions, labels, or bullets — in PPT or PDF/HTML. Deep Red is for UI accents and product iconography only (e.g., table X marks, Incident product color bar).

### Type Scale — Presentations (pptxgenjs)

Slide dimensions: **W: 13.3", H: 7.5"**
Slide margins: **M: 0.75" on all sides**

| Element | fontFace | fontSize | bold | Color — Light bg | Color — Dark bg |
|---------|----------|----------|------|-----------------|-----------------|
| H1 | Poppins SemiBold | 32–36pt | false | Raisin #1E1531 | White #FFFFFF |
| H2 | Poppins SemiBold | 20–28pt | false | Raisin #1E1531 | White #FFFFFF |
| H3 | Poppins SemiBold | 14–16pt | false | Raisin #1E1531 | White #FFFFFF |
| Sub-head | Poppins SemiBold | 16–20pt | false | Raisin #1E1531 | #EBEEF2 |
| Body / Bullets | Poppins | 10–14pt | false | Gray #6D7580 | Bg Gray #F4F6F9 |
| Captions | Poppins | 10–12pt | false | Gray #6D7580 | #EBEEF2 |
| Section number | Poppins | 32pt | false | Green #7DE2DD | Green #7DE2DD |
| Eyebrow / label | Poppins | 10pt | true | GreenDark #007971 | Green #7DE2DD |

### Stat / Metric Blocks

- **No card boxes behind stat numbers.** Numbers render directly on the slide background — no white rectangle, no shadow box.
- Default size: **28pt Regular**
- Stats-only slide (no other body content): increase to **40pt**
- Tight vertical spacing — label immediately below number with minimal gap (~0.55" between number y and label y for a 40pt number)

**Light background:**
- Number: Darker Green #007971 or Bright Blue #1F59BD
- Label: Raisin #1E1531, 12pt

**Dark background:**
- Number: Primary Green #7DE2DD
- Label: White #FFFFFF, 10.5pt

### Type Scale — Documents

| Element | Weight | Size |
|---------|--------|------|
| H1 | Semi-Bold 600 | 32px |
| H2 | Semi-Bold 600 | 24px |
| H3 | Semi-Bold 600 | 18px |
| Body | Regular 400 | 16px |
| Caption | Regular 400 | 14px |

---

## Slide Backgrounds

**Always use the exact asset files below. Never recreate backgrounds programmatically.**

All backgrounds are in `assets/backgrounds/`.

### Category 1: Primary Content Backgrounds
Default for all content slides.

**Light variants** (Raisin headers):

| File | Description |
|------|-------------|
| `primary-light-01.png` *(default)* | White base, subtle teal hint at bottom-right. Cleanest. |
| `primary-light-02.png` | White base, soft mint-teal blooms at corners. Slightly more color. |
| `primary-light-03.png` | Light blue top fading to warm white. Most saturated. |

**Dark variants** (White headers):

| File | Description |
|------|-------------|
| `primary-dark-01.png` *(default)* | Deep teal-navy, bright glow from upper-right. |
| `primary-dark-02.png` | Dark navy/indigo, blue-to-teal diagonal sweep. |
| `primary-dark-03.png` | Very dark, concentrated teal-cyan glow. Most dramatic. |

### Category 2: Plain Gradients
Cleaner linear fades. Use for lower-emphasis slides. Available in `assets/backgrounds/`.

### Category 3: Cover / Divider Backgrounds (Line Backgrounds)
For cover slides and section dividers only. Semi-transparent vertical column overlays are baked in.

**Dark variants** (White headers):

| File | Description |
|------|-------------|
| `cover-dark1.png` *(default cover)* | Dark raisin-navy, bright teal glow, prominent column lines right. |
| `cover-dark2.png` | Dark navy-indigo, soft teal-blue columns across right half. |
| `cover-dark3.png` | Dark teal gradient, subtle column overlays right. |
| `cover-dark4.png` | Dark navy-indigo, sharply defined teal columns. High contrast. |
| `cover-dark5.png` | Very dark Raisin-navy, teal-cyan columns at right edge. |

**Light variants** (Raisin headers):

| File | Description |
|------|-------------|
| `cover-light1.png` | Light teal-mint to white, soft blue-purple columns right. |
| `cover-light2.png` | White base, soft teal columns at right edge. |

---

## Slide Footer — INTERIOR SLIDES ONLY

The footer is a frosted semi-transparent overlay applied **only to interior content slides**. It must **never** appear on cover/title slides or the closing/Thank You slide.

**Rule:** First slide (cover), last slide (Thank You/closing), and any co-branded or alternative cover = **no footer**. All interior slides = **footer required**.

The footer must always extend edge-to-edge (x: 0, w: 13.3). Never clip or indent it.

```javascript
const FOOTER_Y = 7.002;
const FOOTER_H = 0.498;

function addThemeFooter(slide) {
  // 1. Background rectangle — line fully transparent (width:0 alone still renders in some hosts)
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: FOOTER_Y, w: 13.3, h: FOOTER_H,
    fill: { color: "FFFFFF", transparency: 76 },
    line: { color: "FFFFFF", transparency: 100, width: 0 },
  });
  // 2. Top border only — separate thin rectangle, also no outer border
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: FOOTER_Y, w: 13.3, h: 0.008,
    fill: { color: "A5ABB3", transparency: 30 },
    line: { color: "A5ABB3", transparency: 100, width: 0 },
  });
  // 3. Gray crown icon — left side
  slide.addImage({ path: "assets/appriss-crown-gray.png",
    x: 0.280, y: 7.136, w: 0.470, h: 0.268 });
  // 4. Copyright text — right-aligned, color #A5ABB3
  slide.addText("©2026 Appriss Retail  —  Confidential", {
    x: 8.373, y: 7.153, w: 4.781, h: 0.234,
    fontFace: "Poppins", fontSize: 8,
    color: "A5ABB3", align: "right", margin: 0,
  });
}
```

> The footer bar is a **frosted semi-transparent overlay** (24% opacity). The top border is a separate thin rectangle — no stroke/outline around the main background rectangle. Never use a solid white fill or an all-sides border.

---

## Slide Templates

### Cover Slide
- Background: Line background, Category 3 (`cover-dark1.png` default)
- Logo: `appriss-logo-white.png` top-left — x: 0.75", y: 0.55", w: 2.2", h: 0.451"
- H1: Poppins SemiBold, 34–36pt, White
- Subtitle: Poppins Regular, 13–14pt, **color #6D7580** (NOT white or light gray — always use gray on cover dark)
- **No footer** — cover/title slides never include the footer bar
- **Logo required** — Appriss logo always present on first/cover slides
- No body text or bullets

### Co-branded Cover Slide
- Background: Line background, Category 3 (`cover-dark2.png` default)
- Appriss logo (`appriss-logo-white.png`) at top-left
- Divider between logos: **Darker Green #007971, narrow rectangle (~0.007" wide)** — NOT white or semi-transparent
- Customer logo/wordmark to the right of the divider
- H1: Poppins SemiBold, 34pt, White
- Subtitle: Poppins Regular, 13pt, **color #6D7580**
- **No footer** — treated as a cover/title slide
- **Logo required**

### Section Divider
- Background: Line background, Category 3 (`cover-dark4.png` default)
- Section number (e.g., "01"): Poppins Regular, **32pt**, Primary Green #7DE2DD, left-aligned
- Section title directly below: Poppins SemiBold, 38pt, White
- **No decorative accent lines or rectangles** between number and title
- Footer: `addThemeFooter` (interior slide)
- No logo

### Content Slide — Light
- Background: `primary-light-01.png` (default)
- H1: Poppins SemiBold, 34pt, Raisin
- H2: Poppins SemiBold, 20pt, Raisin
- H3: Poppins SemiBold, 14pt, Raisin
- Body bullets: Poppins Regular, 12pt, Gray #6D7580
- Caption/accent: Poppins Regular italic, 12pt, Darker Green #007971
- **No logo**
- Footer: `addThemeFooter`

### Content Slide — Dark
- Background: `primary-dark-01.png` or `primary-dark-02.png`
- H1: Poppins SemiBold, 34pt, White
- H2: Poppins SemiBold, 20pt, White
- Body bullets: Poppins Regular, 12pt, Background Gray #F4F6F9
- Accent: Poppins Regular italic, 12pt, Primary Green #7DE2DD
- **No logo**
- Footer: `addThemeFooter`

### Stats Slide
- Background: Primary light or dark
- H1 title: centered, Poppins SemiBold
- **No card boxes, borders, or shadows behind stat numbers** — text directly on background
- Stat number: 40pt if stats are the only content on the slide; 28pt if stats accompany other content
- Tight spacing: label y = stat number y + ~0.95" (minimal gap)
- **No logo**
- Footer: `addThemeFooter`

### Two-Column Slide
- Background: Primary light (`primary-light-01.png`)
- Left column: header + bullets, standard light content rules
- Right column: **dark card (Raisin #1E1531), full slide height (y: 0, h: 7.5"), extending to right edge of slide (no right margin)**
  - Internal text margins: **0.75" on all sides within the card**
  - Card stat numbers: Primary Green, 36pt
  - Card body: Background Gray #F4F6F9
  - Footer renders on top of the card (correct behavior)
- **No logo**
- Footer: `addThemeFooter`

### Quote / Callout Slide
- Background: Primary dark
- Large opening quote mark: Poppins, 96pt, Primary Green, top-left
- Quote body: Poppins Regular, 24pt, White, lineSpacingMultiple: 1.35
- Attribution: Poppins Regular italic, 13pt, Primary Green
- **No logo**
- Footer: `addThemeFooter`

### Table / Comparison Slide
- Background: Primary light (`primary-light-02.png`)
- H1: Poppins SemiBold, 28pt, Raisin
- Table header row: Raisin fill, White bold text
- Alternating rows: White and Background Gray #F4F6F9
- Border: 1pt, Pale Blue #DBE5FD
- Check marks: Darker Green #007971, bold
- X marks: #7D0748
- **No logo**
- Footer: `addThemeFooter`

### 3-Column Product Comparison Slide
- Background: Primary light
- H1 title: Poppins SemiBold, 28pt, Raisin
- Three equal-width cards (white fill, Pale Blue border, subtle shadow)
- Each card has a **colored top accent bar** matching its product color:
  - Engage → Bright Blue #1F59BD
  - Secure → Darker Green #007971
  - Incident → #7D0748
- Product name: Poppins SemiBold, 20pt, Raisin
- Tagline: Poppins Regular italic, 11pt, product accent color
- Thin divider line below tagline: Pale Blue #DBE5FD
- Bullets: Poppins Regular, 10.5pt, Gray #6D7580
- **No logo**
- Footer: `addThemeFooter`

### Speaker / Meet the Team Slide
- Background: set via `s.background = { path: "..." }` — **never** use `s.addImage` for a full-slide background
- Eyebrow label: Poppins Bold, 10pt, Darker Green, charSpacing: 2, centered, ALL CAPS
- Title: Poppins SemiBold, 30pt, Raisin, centered
- **No decorative accent lines under the title**
- Headshot images: circular crop (`rounding: true`), **no drop shadow**
- Name: Poppins SemiBold, 18pt, Raisin, centered
- Title/role: Poppins Regular, 13pt, Gray
- Email: Poppins Regular, 11pt, Darker Green
- **No logo**
- Footer: `addThemeFooter`

### Closing Slide (intermediate)
- Background: Line background, Category 3 (`cover-dark3.png` default)
- Logo: `appriss-logo-white.png`, left-aligned, vertically centered in content area
- Tagline: Poppins Regular, 14pt, **color #6D7580**
- **No footer** — closing slides never include the footer bar
- **Logo required**

### Thank You / Final Slide (last slide)
- Background: Dark cover with column lines (`cover-dark1.png` or `cover-dark2.png`)
- "Thank You": Poppins SemiBold, 64pt, White, horizontally centered (`x: 0, w: 13.3`)
- `appriss-logo-white.png`: horizontally centered below the text — w: ~3.2", h: w / 4.878
- Optional: subtle copyright line at bottom center, Poppins Regular, 8pt, #6D7580
- **No footer bar** — last slide never includes the footer
- **Logo required** — centered horizontal logo or stacked logo beneath "Thank You"

```javascript
// Thank You slide example
{
  const s = pres.addSlide();
  s.background = { path: "assets/backgrounds/cover-dark1.png" };

  s.addText("Thank You", {
    x: 0, y: 2.4, w: 13.3, h: 1.6,
    fontFace: "Poppins SemiBold", fontSize: 64, bold: false,
    color: "FFFFFF", align: "center", margin: 0,
  });

  const logoW = 3.2;
  s.addImage({
    path: "assets/appriss-logo-white.png",
    x: (13.3 - logoW) / 2, y: 4.3,
    w: logoW, h: logoW / 4.878,
  });

  s.addText("©2026 Appriss Retail", {
    x: 0, y: 7.1, w: 13.3, h: 0.28,
    fontFace: "Poppins", fontSize: 8,
    color: "6D7580", align: "center", margin: 0,
  });
  // No addThemeFooter — closing slide
}
```

---

## pptxgenjs Implementation Notes

### Slide constants
```javascript
const W = 13.3, H = 7.5, M = 0.75;
const FOOTER_Y = 7.002, FOOTER_H = 0.498;
const LOGO_W = "assets/appriss-logo-white.png";
const LOGO_D = "assets/appriss-logo-dark.png";
const LOGO_AR = 4.878; // width ÷ height
```

### Semi-Bold headers — correct implementation
```javascript
// CORRECT
s.addText("Heading", { fontFace: "Poppins SemiBold", bold: false, fontSize: 34 });

// WRONG — do not use bold: true
s.addText("Heading", { fontFace: "Poppins", bold: true, fontSize: 34 });
```

### Background images — always use s.background
```javascript
// CORRECT
s.background = { path: "assets/backgrounds/primary-light-01.png" };

// WRONG — creates a separate image layer instead of true background
s.addImage({ path: "...", x: 0, y: 0, w: W, h: H });
```

### Logo placement on cover slides
```javascript
s.addImage({ path: LOGO_W, x: M, y: 0.55, w: 2.2, h: 2.2 / LOGO_AR });
```

### Supporting / body copy color on copy-heavy slides
When a slide has a significant amount of body or supporting text (more than 2–3 short lines), use color `#6D7580` for that text. This applies to light backgrounds especially. Dark background slides may use `#F4F6F9` (Background Gray) for body copy.

### Title visibility — never obscured
Slide titles must always be fully visible. No shape, card, or background element should overlap or clip the title text. If a full-height card or dark panel is present on the slide, set the title above or outside the card bounds.

### Never add text blocks labeled "APPRISS RETAIL" in slide corners
The footer crown + copyright line is sufficient brand identification on content slides.

---

## Named Slide Layouts (inject-layouts.py)

After generating a PPTX with pptxgenjs, run `inject-layouts.py` to:
1. Inject 12 named layouts into the slide master → appear in PowerPoint's "Add New Slide" panel
2. Replace the deck's `theme1.xml` with `assets/appriss-theme1.xml` → Appriss brand colors appear in PowerPoint's color picker

**Theme application is nonnegotiable.** `brand-test.js` automatically calls `inject-layouts.py` and copies the output on completion — never skip this step. The final deliverable is always `brand-test-layouts.pptx`, never `brand-test.pptx`.

Generation workflow (single command):
```
node brand-test.js
```
This generates the base PPTX, injects all layouts, applies the Appriss theme XML, and copies to outputs automatically.

| # | Layout name | Background |
|---|-------------|-----------|
| 1 | Cover Dark | `cover-dark1.png` |
| 2 | Light Content | `primary-light-01.png` |
| 3 | Dark Content | `primary-dark-02.png` |
| 4 | Stats Light | `primary-light-02.png` |
| 5 | Closing Dark | `cover-dark3.png` |
| 6 | Co-branded Cover | `cover-dark2.png` |
| 7 | Section Divider | `cover-dark4.png` |
| 8 | Two Column | `primary-light-01.png` |
| 9 | Quote Callout | `primary-dark-01.png` |
| 10 | Data Table | `primary-light-02.png` |
| 11 | Speaker | `primary-light-01.png` |
| 12 | Product Comparison | `primary-light-02.png` |

---

## Standard Deck Structure

When generating a full deck from scratch, follow this slide order. Not every section is required for every deck, but this is the canonical sequence:

| Position | Slide type | Notes |
|----------|-----------|-------|
| 1 | **Cover** | Dark line background, logo top-left, title + subtitle |
| 2 | **Agenda** | Light background, numbered list of sections |
| 3+ | **Speakers / Meet the Team** | Include when deck is customer-facing or a kickoff |
| Next | **Section Divider** | One per major section — dark line background, section number + title |
| Next | **Content slides** | Light or dark, as appropriate to content density |
| ... | *(repeat section divider → content as needed)* | |
| Second to last | **Thank You** | Dark line background, "Thank You" centered, logo centered below |
| Last | **Closing logo slide** | Dark line background, logo centered or left-aligned, tagline |

> The Thank You slide and Closing logo slide are both closing slides — neither gets a footer bar or any body content. The Closing logo slide is the final brand impression; keep it clean.

---

## PDF / Document Design Guidelines

### Always reference the PPT theme
The PowerPoint theme is the canonical design reference. When creating any document, PDF, one-pager, HTML, or other design asset, match it as closely as the format allows — same colors, typography, backgrounds, and visual hierarchy. When uncertain about any design decision, check the PPT theme first.

### Logo placement
- Logo goes in the **upper right corner** of the header/cover area in PDFs and HTML documents.
- Use `appriss-logo-white.png` on dark backgrounds, `appriss-logo-dark.png` on light backgrounds.

### Backgrounds — use approved image assets
- All backgrounds must use one of the approved image files from `assets/backgrounds/`. Do not generate or approximate backgrounds with CSS gradients or programmatic fills.
- Light background documents: use `primary-light-01.png` or `primary-light-02.png` — **white or very light gray base**. Never use a light green or teal tint as a background.
- Dark background documents/headers: use a `cover-dark` or `primary-dark` variant.

### Header typographic treatment — dark backgrounds
The header line follows a specific format: **H1 + em dash (no line break) + H2 (white)**

- Em dash: no line break before or after it — sits inline on the same line as both H1 and H2
- H2 text (after the em dash): white — `#FFFFFF`
- Sub-head / supporting headline on dark backgrounds: **`#EBEEF2`** — applies to both decks and PDFs

Example: `Appriss Retail — Stop losses from checkout to return`
where "Stop losses from checkout to return" is `#FFFFFF`, all on one line.

> Sub-head color on dark backgrounds is `#EBEEF2` everywhere — decks, PDFs, and HTML. This replaces Background Gray `#F4F6F9` for sub-heads on dark.

### Stroke / border use — remove by default
- **No stroke in PDFs.** Do not apply borders to any element — cards, containers, sections, tables, or layout blocks — unless explicitly required.
- The one exception: a thin **top accent bar** (approx. 3–4pt) on a card, in the card's accent color. This is a filled rectangle, not a CSS/SVG border.
- Do not use gray separator lines in PDFs or HTML. Use whitespace to create visual separation between sections.
- CSS default: `border: none`. Only exception: `border-top` for a card's top accent bar.

### Buttons — reduced corner radius, no dead links
- Button corner radius: **4px**. Do not use large pill/rounded buttons.
- **Do not render CTA buttons that have no destination link** — especially in hero sections. If a button has no URL, omit it entirely. A non-functional button is worse than no button.

### Bullet alignment — consistent hang indent
- Bullet text must hang-indent so **all wrapped lines align with the first character of text**, not with the bullet symbol.
- Apply this consistently across every list — no mixing of aligned and non-aligned bullets.
- CSS: `padding-left: 1.2em; text-indent: -1.2em`, or `list-style-position: outside` with matching `padding-left`. ReportLab: `leftIndent` + `firstLineIndent` as a negative offset.

### Margins — consistent throughout
- Define a single page margin and use it uniformly. Do not vary margins between sections or pages.
- All content blocks, headers, body copy, and lists must align to the same left edge.
- Standard margin: **0.75"** on all sides. Inner card padding: **0.28" / 20px**.
- Full-bleed backgrounds must still inset their text content by 0.75".

### Layout orientation — prefer top/bottom over left/right
- Most multi-element layouts should stack **vertically** rather than splitting side-by-side.
- Side-by-side columns only when content is structurally parallel and roughly equal in length.
- When in doubt: top/bottom.

### Section spacing — HTML deliverables
- When producing HTML files, increase space between sections. Sections should feel visually separated — not compressed. Use a minimum of `padding: 64px 0` between major sections.

### Poppins font loading — HTML deliverables
Always load Poppins from Google Fonts in every HTML file. Place this in the `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
```

Then set the base font in CSS:
```css
body {
  font-family: 'Poppins', Arial, sans-serif;
}
```

Never rely on system fonts or omit the import — without it, Poppins will silently fall back to Arial.

### Paragraph spacing
- Visible breathing room between paragraphs and list items — not a wall of text.
- Target: ~1.4–1.5× line spacing; ~0.5–0.75 line gap between paragraphs/bullets.
- CSS: `line-height: 1.5; margin-bottom: 0.6em`. ReportLab: `leading` ~1.5× font size, `spaceBefore`/`spaceAfter` ~6–8pt.

---

## Visual Design Elements

### Cards & Containers
- Background: White (#FFFFFF) or Pale Blue (#DBE5FD)
- Border: 1pt solid Pale Blue #DBE5FD
- Shadow: subtle outer shadow (color: 000000, blur: 10, offset: 3, opacity: 10%)
- Padding: 24px / 0.28" internal margin

### Divider Lines
- Section divider slides: **no decorative lines** between number and title
- Co-branded logo divider: Darker Green #007971, ~0.007" wide rectangle
- Card internal dividers: Pale Blue #DBE5FD, ~0.006" high rectangle

### Tables
- Header: Raisin fill, White text, Poppins Semi-Bold (use `bold: true` within table cells only)
- Alternating rows: White / Background Gray #F4F6F9
- Border: 1pt, Pale Blue #DBE5FD
- Body: Gray #6D7580, Poppins Regular

### Photography / Headshots
- Headshots: always circular crop (`rounding: true` in pptxgenjs)
- **No drop shadows** on headshots
- Photography: Bright modern retail environments, diverse professionals

### Icons
- Style: Line icons, 2px stroke
- Colors: Primary Green, Raisin, or White on dark
- Source: Lucide, Feather, or similar

### Data Visualization
- Primary: Raisin #1E1531
- Secondary: Primary Green #7DE2DD
- Tertiary: Bright Blue #1F59BD
- Additional: Mid-Blue #528DF5, Gold #FBC521, #7D0748

---

## Voice & Tone

### Brand Personality
- Confident — industry leaders, calm authority
- Intelligent — AI-powered, data-driven
- Approachable — technical but accessible
- Results-focused — lead with outcomes

### Writing Style
- Sentence case throughout
- Active voice, concise sentences
- Lead with benefits and measurable results
- Use specific numbers ("8–12% decrease" not "significant decrease")
- Avoid jargon

### Key Messages
- "Stop losses from checkout to return"
- "AI-powered loss reduction across every channel"
- "Smarter returns. Happier customers. Stronger profits."
- "The total loss solution for omnichannel"
- "Reward loyal customers while stopping fraud and abuse"

### Proof Points
- 270+ Global Retail Clients
- 60+ Top 100 U.S. Retailers
- 40% of U.S. Retail Transactions
- 8–12% average decrease in returns
- 10x ROI
- 99.99% linking accuracy

---

## Quick Reference

| Element | Value |
|---------|-------|
| Font | Poppins (fallback: Arial) |
| Header weight | Poppins SemiBold, `bold: false` |
| Body weight | Poppins Regular |
| Text case | Sentence case |
| Slide W × H | 13.3" × 7.5" |
| Slide margins | 0.75" all sides |
| Footer Y | 7.002" |
| Footer H | 0.498" |
| Raisin | #1E1531 |
| Primary Green | #7DE2DD |
| Darker Green | #007971 |
| Deep Red | #7D0748 |
| Bright Blue | #1F59BD |
| Mid-Blue | #528DF5 |
| Pale Blue | #DBE5FD |
| Background Gray | #F4F6F9 |
| Gray (body text) | #6D7580 |
| Footer text | #A5ABB3 |
| Gold | #FBC521 |
| H1 (pptx) | 32–36pt, Poppins SemiBold |
| H2 (pptx) | 20–28pt, Poppins SemiBold |
| H3 (pptx) | 14–16pt, Poppins SemiBold |
| Body (pptx) | 10–14pt, Poppins Regular |
| Stat number (default) | 28pt Regular, no card behind it |
| Stat number (stats-only slide) | 40pt Regular |
| Section number | 32pt Regular, Primary Green |
| Logo — dark bg | `appriss-logo-white.png`, AR 4.878 |
| Logo — light bg | `appriss-logo-dark.png`, AR 4.878 |
| Logo placement | Title/cover + closing slides ONLY |
| Footer | Semi-transparent white bar (24% opacity), crown left, copyright right |
| Footer border | Top edge only — thin `h:0.008"` rectangle in `#A5ABB3`. NO border around the rectangle itself. |
| Footer line removal | Always use `line: { color: "FFFFFF", transparency: 100, width: 0 }` — `width: 0` alone still renders in some hosts |
| Background method | `s.background = { path: ... }` always |
| Header bold | NEVER `bold: true` — always `fontFace: "Poppins SemiBold", bold: false` |
| Stat cards | NEVER — no boxes behind stat numbers |
| Deep Red for copy | NEVER — #7D0748 is UI/accent only, not for any text |
| Headshot shadow | NEVER — no drop shadows on photos |
| Accent lines | NEVER under slide titles or section numbers |
| Corner text blocks | NEVER add "APPRISS RETAIL" text in slide corners |
| Card borders (PDF) | Top accent bar only — no 4-sided border (PDF/HTML only) |
| Stroke (PDF/HTML) | None by default — `border: none`; top accent bar only (PDF/HTML only) |
| Divider lines (PDF/HTML) | None — use whitespace for section separation |
| Logo placement (PDF) | Upper right corner of header/cover area |
| Backgrounds (PDF) | Always use approved `assets/backgrounds/` images — never CSS gradients |
| Light bg color | White or very light gray — NEVER light green or teal tint |
| Header on dark (PDF) | H1 + em dash (inline, no line break) + H2 in `#FFFFFF` |
| Sub-head on dark | `#EBEEF2` — all formats (decks, PDFs, HTML). Replaces `#F4F6F9`. |
| Button corners | 4px border-radius — no pill/rounded buttons |
| CTA buttons (PDF/HTML) | NEVER render buttons with no destination URL — omit entirely |
| Layout orientation | Top/bottom preferred — left/right only for truly parallel content |
| Bullet alignment | Hang indent throughout — wrapped lines align with first text character, not bullet |
| Margins (PDF) | 0.75" all sides, consistent across every page and section |
| Card padding (PDF) | 0.28" / 20px inner padding — uniform on all cards |
| Section spacing (HTML) | Minimum `padding: 64px 0` between major sections |
| Paragraph spacing | 1.4–1.5× line spacing; 0.5–0.75 line gap between paragraphs/bullets |
| Design reference | Always refer to PPT theme for all design decisions |
| Color fidelity | Always use exact hex values — never approximate or substitute hues |

---

*Apply these guidelines to all Appriss Retail branded content including presentations, documents, one-pagers, reports, and marketing materials.*
