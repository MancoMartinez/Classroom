const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

// Resolve all asset paths relative to the skill root (one level up from scripts/)
const SKILL_ROOT = path.resolve(__dirname, "..");
const asset = (...parts) => path.join(SKILL_ROOT, "assets", ...parts);
const bg = (file) => asset("backgrounds", file);

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.3" x 7.5"

// ── Brand colors (no # prefix) ──────────────────────────────────────────────
const C = {
  raisin:      "1E1531",
  green:       "7DE2DD",  // Primary Green
  greenDark:   "007971",  // Darker Green
  brightBlue:  "1F59BD",
  midBlue:     "528DF5",
  paleBlue:    "DBE5FD",
  deepRed:     "7D0748",  // Deep Red (was cherry FA505F -- corrected per SKILL.md)
  gold:        "FBC521",
  bgGray:      "F4F6F9",  // Background Gray — also body text on dark slides
  gray:        "6D7580",  // Text gray
  white:       "FFFFFF",
  darkNavy:    "0D2535",  // PB-Dark-1 approximation
};

const W = 13.3;
const H = 7.5;
const M = 0.75; // margin

// ── Helpers ──────────────────────────────────────────────────────────────────
function makeShadow() {
  return { type: "outer", color: "000000", blur: 10, offset: 3, angle: 135, opacity: 0.10 };
}

// Simulate vertical line columns on right side (line background effect)
function addLineAccents(slide, baseColor) {
  const cols = [
    { x: 9.2,  w: 0.55, t: 92 },
    { x: 9.9,  w: 0.45, t: 88 },
    { x: 10.5, w: 0.7,  t: 84 },
    { x: 11.3, w: 0.5,  t: 80 },
    { x: 11.9, w: 0.65, t: 74 },
    { x: 12.65,w: 0.65, t: 66 },
  ];
  cols.forEach(col => {
    slide.addShape(pres.shapes.RECTANGLE, {
      x: col.x, y: 0, w: col.w, h: H,
      fill: { color: baseColor, transparency: col.t },
      line: { color: baseColor, width: 0 },
    });
  });
}

// Official logo files provided by Kristen
const LOGO_W   = asset("appriss-logo-white.png");   // white on dark
const LOGO_D   = asset("appriss-logo-dark.png");     // dark on light
const LOGO_AR  = 4.8780; // width / height ratio (800×164 dark; white is 1137×233 — same ratio)
const CROWN    = asset("appriss-crown-gray.png");

// Footer bar dimensions — exact match to slideMaster3 in ApprissRetail_theme.thmx
const FOOTER_Y = 7.002;
const FOOTER_H = 0.498;

function addLogoLight(slide) {
  // Full wordmark — dark version — bottom-right, above footer bar
  slide.addImage({ path: LOGO_D, x: W - M - 1.8, y: FOOTER_Y - 0.1 - 1.8 / LOGO_AR, w: 1.8, h: 1.8 / LOGO_AR });
}
function addLogoDark(slide) {
  // Full wordmark — white version — bottom-right, above footer bar
  slide.addImage({ path: LOGO_W, x: W - M - 1.8, y: FOOTER_Y - 0.1 - 1.8 / LOGO_AR, w: 1.8, h: 1.8 / LOGO_AR });
}

// ── Theme footer ──────────────────────────────────────────────────────────────
function addThemeFooter(slide) {
  // 1. Background rectangle — line fully transparent so no border renders
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: FOOTER_Y, w: W, h: FOOTER_H,
    fill: { color: C.white, transparency: 76 },
    line: { color: C.white, transparency: 100, width: 0 },
  });
  // 2. Top border line — thin rectangle, also no outer border
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: FOOTER_Y, w: W, h: 0.008,
    fill: { color: "A5ABB3", transparency: 30 },
    line: { color: "A5ABB3", transparency: 100, width: 0 },
  });
  // 3. Crown icon — left side, vertically centred in bar
  slide.addImage({
    path: CROWN,
    x: 0.280, y: 7.136, w: 0.470, h: 0.268,
  });
  // 4. Copyright text — right-aligned, color A5ABB3
  slide.addText("©2026 Appriss Retail  —  Confidential", {
    x: 8.373, y: 7.153, w: 4.781, h: 0.234,
    fontFace: "Poppins", fontSize: 8,
    color: "A5ABB3", align: "right", margin: 0,
  });
}

// ── SLIDE 1: Cover (dark, line background) ───────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("cover-dark1.png") };

  // Logo — white, no ®, top-left
  s.addImage({
    path: LOGO_W,
    x: M, y: 0.55, w: 2.2, h: 2.2 / LOGO_AR,
  });

  // Title
  s.addText("Appriss Retail brand overview", {
    x: M, y: 2.8, w: 8.2, h: 1.0,
    fontFace: "Poppins SemiBold", fontSize: 36, bold: false,
    color: C.white, align: "left", margin: 0,
  });

  // Subtitle — #6D7580 on cover dark per spec
  s.addText("Stop losses from checkout to return", {
    x: M, y: 4.0, w: 8.2, h: 0.5,
    fontFace: "Poppins", fontSize: 14,
    color: C.gray, align: "left", margin: 0,
  });
  // No footer on cover/title slides
}

// ── SLIDE 2: Light content slide ─────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-light-01.png") };

  // H1
  s.addText("How Appriss Engage works", {
    x: M, y: M, w: 10, h: 0.8,
    fontFace: "Poppins SemiBold", fontSize: 34, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  // H2
  s.addText("Reducing return fraud at every touchpoint", {
    x: M, y: 1.75, w: 10, h: 0.5,
    fontFace: "Poppins SemiBold", fontSize: 20, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  // H3
  s.addText("How it connects across channels", {
    x: M, y: 2.45, w: 10, h: 0.4,
    fontFace: "Poppins SemiBold", fontSize: 14, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  // Body bullets
  s.addText([
    { text: "Connects shopper identity across all touchpoints in real time", options: { bullet: true, breakLine: true } },
    { text: "Flags high-risk return behavior before the transaction completes", options: { bullet: true, breakLine: true } },
    { text: "Rewards loyal customers with frictionless experiences", options: { bullet: true, breakLine: true } },
    { text: "Integrates with your existing POS and e-commerce systems", options: { bullet: true } },
  ], {
    x: M, y: 2.95, w: 8.5, h: 2.2,
    fontFace: "Poppins", fontSize: 12,
    color: C.gray, align: "left", paraSpaceAfter: 8,
  });

  // Caption
  s.addText("Trusted by 60+ of the top 100 U.S. retailers", {
    x: M, y: 5.35, w: 8.5, h: 0.4,
    fontFace: "Poppins", fontSize: 12, italic: true,
    color: C.greenDark, align: "left", margin: 0,
  });

  addThemeFooter(s);
}

// ── SLIDE 3: Dark content slide ───────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-dark-02.png") };

  // H1
  s.addText("Proven results across omnichannel retail", {
    x: M, y: M, w: 10.5, h: 0.8,
    fontFace: "Poppins SemiBold", fontSize: 34, bold: false,
    color: C.white, align: "left", margin: 0,
  });

  // H2
  s.addText("What our customers see after implementing Engage", {
    x: M, y: 1.75, w: 10.5, h: 0.5,
    fontFace: "Poppins SemiBold", fontSize: 20, bold: false,
    color: C.white, align: "left", margin: 0,
  });

  // Body bullets
  s.addText([
    { text: "Average 8–12% reduction in return rate within the first quarter", options: { bullet: true, breakLine: true } },
    { text: "10x ROI demonstrated across 270+ global retail clients", options: { bullet: true, breakLine: true } },
    { text: "99.99% shopper linking accuracy using consortium data", options: { bullet: true, breakLine: true } },
    { text: "Fraud flagged before the refund is issued — not after", options: { bullet: true } },
  ], {
    x: M, y: 2.5, w: 9.0, h: 2.2,
    fontFace: "Poppins", fontSize: 12,
    color: C.bgGray, align: "left", paraSpaceAfter: 8,
  });

  // Accent stat
  s.addText("40% of U.S. retail transactions run through the Appriss Retail consortium", {
    x: M, y: 5.3, w: 9.0, h: 0.45,
    fontFace: "Poppins", fontSize: 12, italic: true,
    color: C.green, align: "left", margin: 0,
  });

  addThemeFooter(s);
}

// ── SLIDE 4: Stats — no cards, numbers 40pt, reduced label spacing ────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-light-02.png") };

  // H1 title
  s.addText("The numbers speak for themselves", {
    x: M, y: M, w: W - M * 2, h: 0.7,
    fontFace: "Poppins SemiBold", fontSize: 34, bold: false,
    color: C.raisin, align: "center", margin: 0,
  });

  const stats = [
    { num: "270+",  label: "Global retail clients"       },
    { num: "10x",   label: "Average ROI"                 },
    { num: "8–12%", label: "Average decrease in returns" },
  ];

  const colW3 = (W - M * 2) / 3;
  // Vertically center the stat block in the space below the title
  const statY = 3.4;

  stats.forEach((stat, i) => {
    // All stat numbers same color — greenDark on light bg
    s.addText(stat.num, {
      x: M + i * colW3, y: statY, w: colW3, h: 1.0,
      fontFace: "Poppins", fontSize: 40, bold: false,
      color: C.greenDark, align: "center", margin: 0,
    });

    s.addText(stat.label, {
      x: M + i * colW3, y: statY + 0.95, w: colW3, h: 0.55,
      fontFace: "Poppins", fontSize: 12, bold: false,
      color: C.raisin, align: "center", margin: 0,
    });
  });

  addThemeFooter(s);
}

// ── SLIDE 5: Closing (dark, line background) ─────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("cover-dark3.png") };

  s.addImage({
    path: LOGO_W,
    x: M, y: 3.2, w: 2.8, h: 2.8 / LOGO_AR,
  });

  s.addText("Stop losses from checkout to return", {
    x: M, y: 4.15, w: 8.2, h: 0.45,
    fontFace: "Poppins", fontSize: 14,
    color: C.gray, align: "left", margin: 0,
  });
  // No footer on closing slides
}

// ── SLIDE 6: Co-branded cover — Alo Yoga customer meeting ─────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("cover-dark2.png") };

  // Appriss logo — top left, no ®
  s.addImage({ path: LOGO_W, x: M, y: 0.55, w: 2.2, h: 2.2 / LOGO_AR });

  // Vertical divider — dark green, 0.5pt weight
  s.addShape(pres.shapes.RECTANGLE, {
    x: 3.6, y: 0.5, w: 0.007, h: 0.72,
    fill: { color: C.greenDark },
    line: { color: C.greenDark, width: 0 },
  });

  // Customer logo placeholder
  s.addText("ALO YOGA", {
    x: 3.85, y: 0.52, w: 3.5, h: 0.7,
    fontFace: "Poppins", fontSize: 18, bold: true, charSpacing: 4,
    color: C.white, align: "left", margin: 0,
  });

  // Title
  s.addText("Protecting revenue while rewarding loyal customers", {
    x: M, y: 2.65, w: 8.2, h: 1.1,
    fontFace: "Poppins SemiBold", fontSize: 34, bold: false,
    color: C.white, align: "left", margin: 0,
  });

  // Subtitle
  s.addText("Prepared for Alo Yoga  ·  April 2026", {
    x: M, y: 3.95, w: 8.2, h: 0.45,
    fontFace: "Poppins", fontSize: 13,
    color: C.gray, align: "left", margin: 0,
  });
  // No footer on cover/title slides
}

// ── SLIDE 7: Section divider ──────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("cover-dark4.png") };

  // Section number — reduced to 32pt
  s.addText("01", {
    x: M, y: 1.9, w: 3, h: 0.7,
    fontFace: "Poppins", fontSize: 32, bold: false,
    color: C.green, align: "left", margin: 0,
  });

  // Section title (no green divider rectangle)
  s.addText("How Engage works", {
    x: M, y: 2.75, w: 8.2, h: 0.85,
    fontFace: "Poppins SemiBold", fontSize: 38, bold: false,
    color: C.white, align: "left", margin: 0,
  });

  addThemeFooter(s);
}

// ── SLIDE 8: Two-column — full-height dark card, no logo ──────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-light-01.png") };

  // H1 (left column area)
  s.addText("Engage at a glance", {
    x: M, y: M, w: 5.2, h: 0.72,
    fontFace: "Poppins SemiBold", fontSize: 28, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  const colW = 5.2, gap = 0.45, colY = 1.65;
  const rx = M + colW + gap; // = 6.4
  const rw = W - rx;         // = 6.9

  // Left — bullets
  s.addText("What it does", {
    x: M, y: colY, w: colW, h: 0.42,
    fontFace: "Poppins SemiBold", fontSize: 16, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });
  s.addText([
    { text: "Identifies shoppers across all channels using consortium data", options: { bullet: true, breakLine: true } },
    { text: "Flags high-risk return and claims behavior before approval", options: { bullet: true, breakLine: true } },
    { text: "Rewards loyal customers with frictionless experiences", options: { bullet: true, breakLine: true } },
    { text: "Integrates with your existing POS, e-commerce, and OMS systems", options: { bullet: true } },
  ], {
    x: M, y: colY + 0.52, w: colW, h: 2.6,
    fontFace: "Poppins", fontSize: 12,
    color: C.gray, align: "left", paraSpaceAfter: 10,
  });

  // Right — full-height dark card, no padding on outer edges
  const IM = 0.75; // internal margin inside card
  s.addShape(pres.shapes.RECTANGLE, {
    x: rx, y: 0, w: rw, h: H,
    fill: { color: C.raisin },
    line: { color: C.raisin, width: 0 },
  });
  s.addText("Why it works", {
    x: rx + IM, y: 1.2, w: rw - IM * 2, h: 0.5,
    fontFace: "Poppins SemiBold", fontSize: 18, bold: false,
    color: C.white, align: "left", margin: 0,
  });
  [
    { num: "40%",  label: "of U.S. retail transactions flow through the Appriss consortium" },
    { num: "270+", label: "retail clients globally across 40+ countries" },
    { num: "10x",  label: "average ROI demonstrated within 12 months" },
  ].forEach((st, i) => {
    const sy = 1.9 + i * 1.4;
    s.addText(st.num, {
      x: rx + IM, y: sy, w: rw - IM * 2, h: 0.62,
      fontFace: "Poppins", fontSize: 36, bold: false,
      color: C.green, align: "left", margin: 0,
    });
    s.addText(st.label, {
      x: rx + IM, y: sy + 0.6, w: rw - IM * 2, h: 0.5,
      fontFace: "Poppins", fontSize: 11, bold: false,
      color: C.bgGray, align: "left", margin: 0,
    });
  });

  // No logo on this slide per spec
  addThemeFooter(s);
}

// ── SLIDE 9: Quote / callout ──────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-dark-01.png") };

  // Opening quotation mark
  s.addText("\u201C", {
    x: M, y: 1.0, w: 1.2, h: 1.2,
    fontFace: "Poppins", fontSize: 96, bold: true,
    color: C.green, align: "left", margin: 0,
  });

  // Quote body
  s.addText("We've seen a consistent 11% reduction in return fraud since deploying Engage. The ROI paid for itself in under 90 days.", {
    x: M + 0.15, y: 1.85, w: 10.8, h: 2.2,
    fontFace: "Poppins", fontSize: 24, bold: false,
    color: C.white, align: "left", margin: 0, lineSpacingMultiple: 1.35,
  });

  // Attribution
  s.addText("— VP of Loss Prevention, Top 10 U.S. Retailer", {
    x: M + 0.15, y: 4.3, w: 9, h: 0.4,
    fontFace: "Poppins", fontSize: 13, italic: true,
    color: C.green, align: "left", margin: 0,
  });

  addThemeFooter(s);
}

// ── SLIDE 10: Table ───────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-light-02.png") };

  // H1
  s.addText("How Appriss Engage compares", {
    x: M, y: M, w: W - M * 2, h: 0.72,
    fontFace: "Poppins SemiBold", fontSize: 28, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  const border  = { pt: 1, color: "DBE5FD" };
  const hdrFill = { color: C.raisin };
  const altFill = { color: "F4F6F9" };
  const whtFill = { color: C.white };
  const hOpts   = { bold: true, color: C.white,  fontSize: 11, fontFace: "Poppins", align: "center", valign: "middle" };
  const cOpts   = { bold: false, color: "1E1531", fontSize: 11, fontFace: "Poppins", align: "center", valign: "middle" };
  const lOpts   = { bold: false, color: "1E1531", fontSize: 11, fontFace: "Poppins", align: "left",   valign: "middle" };

  const rows = [
    [
      { text: "Capability",                     options: { ...hOpts, align: "left", fill: hdrFill, border } },
      { text: "Appriss Engage",                 options: { ...hOpts, fill: hdrFill, border } },
      { text: "Point solution",                 options: { ...hOpts, fill: hdrFill, border } },
      { text: "Manual review",                  options: { ...hOpts, fill: hdrFill, border } },
    ],
    [
      { text: "Real-time risk scoring",         options: { ...lOpts, fill: whtFill, border } },
      { text: "✓",                              options: { ...cOpts, bold: true, color: C.greenDark, fill: whtFill, border } },
      { text: "Partial",                        options: { ...cOpts, fill: whtFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: whtFill, border } },
    ],
    [
      { text: "Cross-retailer consortium data", options: { ...lOpts, fill: altFill, border } },
      { text: "✓",                              options: { ...cOpts, bold: true, color: C.greenDark, fill: altFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: altFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: altFill, border } },
    ],
    [
      { text: "Omnichannel identity linking",   options: { ...lOpts, fill: whtFill, border } },
      { text: "✓",                              options: { ...cOpts, bold: true, color: C.greenDark, fill: whtFill, border } },
      { text: "Partial",                        options: { ...cOpts, fill: whtFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: whtFill, border } },
    ],
    [
      { text: "POS + e-commerce integration",   options: { ...lOpts, fill: altFill, border } },
      { text: "✓",                              options: { ...cOpts, bold: true, color: C.greenDark, fill: altFill, border } },
      { text: "✓",                              options: { ...cOpts, bold: true, color: C.greenDark, fill: altFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: altFill, border } },
    ],
    [
      { text: "Proven 10x ROI",                 options: { ...lOpts, fill: whtFill, border } },
      { text: "✓",                              options: { ...cOpts, bold: true, color: C.greenDark, fill: whtFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: whtFill, border } },
      { text: "✗",                              options: { ...cOpts, color: C.deepRed, fill: whtFill, border } },
    ],
  ];

  s.addTable(rows, {
    x: M, y: 1.65, w: W - M * 2,
    rowH: 0.58, colW: [4.0, 2.55, 2.55, 2.55],
    fontFace: "Poppins", fontSize: 11,
  });

  addThemeFooter(s);
}

// ── SLIDE 11: Speaker / Meet the team ────────────────────────────────────────
{
  const s = pres.addSlide();
  // Background set as s.background (layer, not separate image)
  s.background = { path: bg("primary-light-01.png") };

  // Section eyebrow
  s.addText("YOUR APPRISS RETAIL TEAM", {
    x: M, y: 0.55, w: W - M * 2, h: 0.28,
    fontFace: "Poppins", fontSize: 10, bold: true,
    color: C.greenDark, charSpacing: 2, align: "center",
  });

  // Slide title (no accent line beneath)
  s.addText("Meet your team", {
    x: M, y: 0.9, w: W - M * 2, h: 0.6,
    fontFace: "Poppins SemiBold", fontSize: 30, bold: false,
    color: C.raisin, align: "center",
  });

  // ── Speaker card positions ──
  const photoSize = 2.0;
  const cardW = 4.2;
  const cardGap = 0.8;
  const totalW = cardW * 2 + cardGap;
  const startX = (W - totalW) / 2;
  const photoY = 2.05;
  const nameY = photoY + photoSize + 0.25;

  const speakers = [
    {
      name: "Pedro Ramos",
      title: "VP of Sales",
      email: "pramos@apprissretail.com",
      photo: asset("headshots", "pedro-circle.png"),
      cardX: startX,
    },
    {
      name: "Sarah Cascone",
      title: "Director of Sales",
      email: "scascone@apprissretail.com",
      photo: asset("headshots", "cascone-circle.png"),
      cardX: startX + cardW + cardGap,
    },
  ];

  for (const sp of speakers) {
    const photoX = sp.cardX + (cardW - photoSize) / 2;

    // Circular headshot — no drop shadow (skip if file missing)
    if (fs.existsSync(sp.photo)) {
      s.addImage({
        path: sp.photo,
        x: photoX, y: photoY, w: photoSize, h: photoSize,
        rounding: true,
      });
    } else {
      // Placeholder circle when headshot is unavailable
      s.addShape(pres.shapes.OVAL, {
        x: photoX, y: photoY, w: photoSize, h: photoSize,
        fill: { color: C.bgGray },
        line: { color: C.paleBlue, width: 1 },
      });
    }

    // Name
    s.addText(sp.name, {
      x: sp.cardX, y: nameY, w: cardW, h: 0.38,
      fontFace: "Poppins SemiBold", fontSize: 18, bold: false,
      color: C.raisin, align: "center",
    });

    // Title
    s.addText(sp.title, {
      x: sp.cardX, y: nameY + 0.38, w: cardW, h: 0.3,
      fontFace: "Poppins", fontSize: 13,
      color: C.gray, align: "center",
    });

    // Email
    s.addText(sp.email, {
      x: sp.cardX, y: nameY + 0.7, w: cardW, h: 0.28,
      fontFace: "Poppins", fontSize: 11,
      color: C.greenDark, align: "center",
    });
  }

  addThemeFooter(s);
}

// ── SLIDE 12: 3-column product comparison ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-light-02.png") };

  s.addText("The total loss solution", {
    x: M, y: M, w: W - M * 2, h: 0.65,
    fontFace: "Poppins SemiBold", fontSize: 28, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  const products = [
    {
      name: "Engage",
      color: C.brightBlue,
      tagline: "Returns & claims intelligence",
      bullets: [
        "Identify serial returners and claims abusers",
        "Score risk in real time — before the refund is issued",
        "Reward loyal shoppers with frictionless experiences",
        "Integrates with POS, e-commerce, and OMS",
      ],
    },
    {
      name: "Secure",
      color: C.greenDark,
      tagline: "Transaction loss prevention",
      bullets: [
        "Detect fraud and abuse at the point of sale",
        "Real-time risk decisioning across all channels",
        "Protect against coupon and promotion abuse",
        "Powered by 40% of U.S. retail transaction data",
      ],
    },
    {
      name: "Incident",
      color: C.deepRed,
      tagline: "Case & incident management",
      bullets: [
        "Centralize loss events and investigations",
        "Manage cases end-to-end in one platform",
        "Build rich evidence files tied to shopper data",
        "Drive team accountability and reporting",
      ],
    },
  ];

  const cardW = 3.73;
  const cardGap = 0.22;
  const cardY = 1.6;
  const cardH = FOOTER_Y - cardY - 0.1;
  const accentH = 0.06;
  const innerM = 0.28;

  products.forEach((p, i) => {
    const cx = M + i * (cardW + cardGap);

    // Card background
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: cardY, w: cardW, h: cardH,
      fill: { color: C.white },
      shadow: makeShadow(),
      line: { color: C.paleBlue, width: 1 },
    });

    // Colored top accent bar
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: cardY, w: cardW, h: accentH,
      fill: { color: p.color },
      line: { color: p.color, width: 0 },
    });

    // Product name
    s.addText(p.name, {
      x: cx + innerM, y: cardY + accentH + 0.22, w: cardW - innerM * 2, h: 0.48,
      fontFace: "Poppins SemiBold", fontSize: 20, bold: false,
      color: C.raisin, align: "left", margin: 0,
    });

    // Tagline
    s.addText(p.tagline, {
      x: cx + innerM, y: cardY + accentH + 0.76, w: cardW - innerM * 2, h: 0.36,
      fontFace: "Poppins", fontSize: 11, italic: true,
      color: p.color, align: "left", margin: 0,
    });

    // Divider
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx + innerM, y: cardY + accentH + 1.18, w: cardW - innerM * 2, h: 0.006,
      fill: { color: C.paleBlue }, line: { color: C.paleBlue, width: 0 },
    });

    // Bullets
    s.addText(p.bullets.map(b => ({ text: b, options: { bullet: true, breakLine: true } })), {
      x: cx + innerM, y: cardY + accentH + 1.28, w: cardW - innerM * 2, h: cardH - accentH - 1.38,
      fontFace: "Poppins", fontSize: 10.5,
      color: C.gray, align: "left", paraSpaceAfter: 6,
    });
  });

  addThemeFooter(s);
}

// ── SLIDE 13: Stats — dark background ────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("primary-dark-03.png") };

  s.addText("The numbers speak for themselves", {
    x: M, y: M, w: W - M * 2, h: 0.65,
    fontFace: "Poppins SemiBold", fontSize: 28, bold: false,
    color: C.white, align: "center", margin: 0,
  });

  const dStats = [
    { num: "270+",  label: "Global retail clients"       },
    { num: "10x",   label: "Average ROI"                 },
    { num: "8–12%", label: "Average decrease in returns" },
  ];
  const dColW = (W - M * 2) / 3;
  const dY = 3.4;

  dStats.forEach((stat, i) => {
    s.addText(stat.num, {
      x: M + i * dColW, y: dY, w: dColW, h: 1.0,
      fontFace: "Poppins", fontSize: 40, bold: false,
      color: C.green, align: "center", margin: 0,
    });
    s.addText(stat.label, {
      x: M + i * dColW, y: dY + 0.95, w: dColW, h: 0.55,
      fontFace: "Poppins", fontSize: 12, bold: false,
      color: C.bgGray, align: "center", margin: 0,
    });
  });

  addThemeFooter(s);
}

// ── SLIDE 14: Agenda ──────────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("bg-cover-dark-05.png") };

  s.addText("Today's agenda", {
    x: M, y: M, w: 7, h: 0.72,
    fontFace: "Poppins SemiBold", fontSize: 34, bold: false,
    color: C.white, align: "left", margin: 0,
  });

  const items = [
    "The state of retail loss today",
    "How Appriss Engage works",
    "Proven results and ROI",
    "Product deep dive",
    "Implementation and integrations",
    "Q&A",
  ];

  items.forEach((item, i) => {
    const rowY = 1.7 + i * 0.72;
    // Number
    s.addText(`0${i + 1}`, {
      x: M, y: rowY, w: 0.7, h: 0.5,
      fontFace: "Poppins", fontSize: 13, bold: false,
      color: C.green, align: "left", margin: 0,
    });
    // Item text
    s.addText(item, {
      x: M + 0.75, y: rowY, w: 8, h: 0.5,
      fontFace: "Poppins", fontSize: 15, bold: false,
      color: C.white, align: "left", margin: 0,
    });
    // Divider
    if (i < items.length - 1) {
      s.addShape(pres.shapes.RECTANGLE, {
        x: M, y: rowY + 0.58, w: 9, h: 0.006,
        fill: { color: C.white, transparency: 75 }, line: { width: 0 },
      });
    }
  });

  addThemeFooter(s);
}

// ── SLIDE 15: 2×2 Feature grid ────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("bg-plain-light-01.png") };

  s.addText("Why retailers choose Appriss", {
    x: M, y: M, w: W - M * 2, h: 0.65,
    fontFace: "Poppins SemiBold", fontSize: 28, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  const features = [
    { title: "Consortium data at scale",   body: "40% of U.S. retail transactions flow through our network — giving you cross-retailer visibility no point solution can match.", accent: C.greenDark },
    { title: "Real-time decisioning",      body: "Risk scores are returned in milliseconds at the moment of return or claim — before the refund is issued, not after.", accent: C.brightBlue },
    { title: "Omnichannel identity",       body: "Link shoppers across store, e-commerce, and mobile channels with 99.99% accuracy using our patented identity resolution.", accent: C.greenDark },
    { title: "Rapid time to value",        body: "Most customers go live in under 90 days. Pre-built integrations with major POS and OMS platforms reduce implementation effort.", accent: C.brightBlue },
  ];

  const tileW = (W - M * 2 - 0.3) / 2;
  const tileH = 2.3;
  const tileGap = 0.3;
  const tileStartY = 1.6;

  features.forEach((f, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const tx = M + col * (tileW + tileGap);
    const ty = tileStartY + row * (tileH + 0.2);

    s.addShape(pres.shapes.RECTANGLE, {
      x: tx, y: ty, w: tileW, h: tileH,
      fill: { color: C.white }, shadow: makeShadow(),
      line: { color: C.paleBlue, width: 1 },
    });
    // Accent bar left edge
    s.addShape(pres.shapes.RECTANGLE, {
      x: tx, y: ty, w: 0.045, h: tileH,
      fill: { color: f.accent }, line: { width: 0 },
    });
    s.addText(f.title, {
      x: tx + 0.22, y: ty + 0.22, w: tileW - 0.32, h: 0.42,
      fontFace: "Poppins SemiBold", fontSize: 14, bold: false,
      color: C.raisin, align: "left", margin: 0,
    });
    s.addText(f.body, {
      x: tx + 0.22, y: ty + 0.7, w: tileW - 0.32, h: tileH - 0.85,
      fontFace: "Poppins", fontSize: 11,
      color: C.gray, align: "left", margin: 0,
    });
  });

  addThemeFooter(s);
}

// ── SLIDE 16: Hero stat — single centered number ──────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("bg-plain-dark-01.png") };

  s.addText("40%", {
    x: 0, y: 2.2, w: W, h: 1.8,
    fontFace: "Poppins", fontSize: 120, bold: false,
    color: C.green, align: "center", margin: 0,
  });

  s.addText("of all U.S. retail transactions run through the Appriss Retail consortium", {
    x: 2.5, y: 4.2, w: W - 5, h: 0.8,
    fontFace: "Poppins", fontSize: 16, bold: false,
    color: C.bgGray, align: "center", margin: 0,
  });

  s.addText("That's more than 7 billion transactions across 270+ global retail clients.", {
    x: 2.5, y: 5.1, w: W - 5, h: 0.5,
    fontFace: "Poppins", fontSize: 12, italic: true,
    color: C.green, align: "center", margin: 0,
  });

  addThemeFooter(s);
}

// ── SLIDE 17: Light cover — alternative cover style ───────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("bg-cover-light-blue.png") };

  s.addImage({ path: LOGO_D, x: M, y: 0.55, w: 2.2, h: 2.2 / LOGO_AR });

  s.addText("Smarter returns.\nHappier customers.\nStronger profits.", {
    x: M, y: 2.2, w: 8, h: 2.8,
    fontFace: "Poppins SemiBold", fontSize: 40, bold: false,
    color: C.raisin, align: "left", margin: 0, lineSpacingMultiple: 1.2,
  });

  s.addText("Stop losses from checkout to return", {
    x: M, y: 5.2, w: 7, h: 0.45,
    fontFace: "Poppins", fontSize: 14,
    color: C.gray, align: "left", margin: 0,
  });
  // No footer on cover/title slides
}

// ── SLIDE 18: Process steps ───────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("bg-plain-light-01.png") };

  s.addText("How Engage works in three steps", {
    x: M, y: M, w: W - M * 2, h: 0.65,
    fontFace: "Poppins SemiBold", fontSize: 28, bold: false,
    color: C.raisin, align: "left", margin: 0,
  });

  const steps = [
    { num: "01", title: "Identify",   body: "Shopper arrives at return counter or initiates an online claim. Appriss Engage links their identity across all channels using consortium data in real time." },
    { num: "02", title: "Evaluate",   body: "Our AI scores the transaction for risk based on return history, behavior patterns, and cross-retailer signals — all within milliseconds." },
    { num: "03", title: "Decide",     body: "Your team or system receives a risk recommendation. Approve, flag, or decline — with full confidence and a complete audit trail." },
  ];

  const stepW = (W - M * 2 - 0.4) / 3;
  const stepY = 1.7;
  const stepH = 4.5;

  steps.forEach((step, i) => {
    const sx = M + i * (stepW + 0.2);

    // Step number circle background
    s.addShape(pres.shapes.RECTANGLE, {
      x: sx, y: stepY, w: stepW, h: stepH,
      fill: { color: C.white }, shadow: makeShadow(),
      line: { color: C.paleBlue, width: 1 },
    });

    // Number pill at top
    s.addShape(pres.shapes.RECTANGLE, {
      x: sx + 0.25, y: stepY + 0.3, w: 0.65, h: 0.42,
      fill: { color: C.raisin }, line: { width: 0 },
    });
    s.addText(step.num, {
      x: sx + 0.25, y: stepY + 0.3, w: 0.65, h: 0.42,
      fontFace: "Poppins", fontSize: 13, bold: false,
      color: C.green, align: "center", margin: 0,
    });

    // Connector arrow between steps
    if (i < steps.length - 1) {
      s.addText("→", {
        x: sx + stepW + 0.01, y: stepY + stepH / 2 - 0.2, w: 0.2, h: 0.4,
        fontFace: "Poppins", fontSize: 16,
        color: C.greenDark, align: "center", margin: 0,
      });
    }

    s.addText(step.title, {
      x: sx + 0.25, y: stepY + 0.88, w: stepW - 0.5, h: 0.48,
      fontFace: "Poppins SemiBold", fontSize: 18, bold: false,
      color: C.raisin, align: "left", margin: 0,
    });
    s.addText(step.body, {
      x: sx + 0.25, y: stepY + 1.45, w: stepW - 0.5, h: stepH - 1.65,
      fontFace: "Poppins", fontSize: 11,
      color: C.gray, align: "left", margin: 0,
    });
  });

  addThemeFooter(s);
}

// ── SLIDE 19: Thank You — conclusion slide ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { path: bg("cover-dark1.png") };

  // "Thank You" — large, centered
  s.addText("Thank You", {
    x: 0, y: 2.4, w: W, h: 1.6,
    fontFace: "Poppins SemiBold", fontSize: 64, bold: false,
    color: C.white, align: "center", margin: 0,
  });

  // White horizontal logo — centered below text
  const logoW = 3.2;
  const logoH = logoW / LOGO_AR;
  s.addImage({
    path: LOGO_W,
    x: (W - logoW) / 2, y: 4.3,
    w: logoW, h: logoH,
  });

  // Subtle copyright line — no footer bar on closing slide
  s.addText("©2026 Appriss Retail", {
    x: 0, y: 7.1, w: W, h: 0.28,
    fontFace: "Poppins", fontSize: 8,
    color: C.gray, align: "center", margin: 0,
  });
  // No footer bar on closing/last slides
}

// ── Write file then always apply theme + layouts (nonnegotiable) ─────────────
const { execSync } = require("child_process");

const OUTPUT_DIR = path.join(SKILL_ROOT, "output");
const BASE_PPTX = path.join(OUTPUT_DIR, "brand-test.pptx");
const LAYOUTS_PPTX = path.join(OUTPUT_DIR, "brand-test-layouts.pptx");
const INJECT_SCRIPT = path.join(SKILL_ROOT, "scripts", "inject-layouts.py");

// Ensure output directory exists
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

pres.writeFile({ fileName: BASE_PPTX })
  .then(() => {
    console.log("Done: brand-test.pptx");
    execSync(`python3 "${INJECT_SCRIPT}" "${BASE_PPTX}" "${LAYOUTS_PPTX}"`, { stdio: "inherit" });
    console.log("Done: brand-test-layouts.pptx (theme + layouts applied)");
  })
  .catch(e => console.error(e));
