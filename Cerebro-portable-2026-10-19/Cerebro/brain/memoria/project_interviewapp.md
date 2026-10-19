---
name: InterviewApp project
description: Overview of the InterviewApp project — a macOS interview assistant at ~/Desktop/InterviewApp; currently at Phase 0 (context only, no code).
type: project
originSessionId: e659ac04-506c-48af-a9d8-3f5c72ae08ad
---
**InterviewApp** at `/Users/MancoMenStudio/Desktop/InterviewApp` — a macOS-only, Apple-Silicon-only interview assistant (ParakeetAI-like). Captures system audio via ScreenCaptureKit, transcribes with whisper.cpp, detects questions, answers via a local MLX LLM or the free GitHub Models tier, and displays the answer in an `NSWindow` with `sharingType = .none` (invisible to screen-capture).

**Why:** The user conducts remote job interviews on a MacBook Air M4 and wants a private, free assistant that stays off screen-share.

**How to apply:**
- Language is **Swift 6** with strict concurrency. SwiftPM, no `.xcodeproj`.
- The non-negotiables live in `CLAUDE.md` and `docs/01-constraints.md`: free-only, local-first, invisible to capture, no telemetry, ≤ 2 s end-of-silence→first-token.
- Allowed dependencies are enumerated in `docs/02-tech-stack.md` — adding anything else requires approval.
- Phase 0 (planning docs) is done. Next step is **Phase 1** in `docs/10-roadmap.md`: SwiftPM skeleton + invisible overlay + `InvisibilityTests`. Do not skip phases.
- When implementing, always read `CLAUDE.md` and `docs/01-constraints.md` first and treat them as contracts, not suggestions.
