---
name: project-moscu-second-brain
description: Moscú second-brain vision + Phase 1-3 roadmap and the Microsoft Graph decision that overrides a CLAUDE.md non-negotiable
metadata: 
  node_type: memory
  type: project
  originSessionId: 9e1517f7-1260-4428-a144-8f8ab8d39b24
---

Moscú's true goal (user-stated 2026-05-27): a **second brain + personal assistant** that grows and learns over time. Stores chat, live transcript, and documents; auto-organizes them; gives grounded (not generic) answers anchored to the user's role/company/profile.

**Roadmap agreed (2026-05-27):**
- **Phase 1 (bugs) — DONE (2026-05-28):** C4 meeting context selector (`LiveInterviewViewModel.meetingContextId`, no more stale `activeContext`); C2 items split into Importantes vs collapsible Capturas + signalScore ranking; C1 instrumented 11/14 `MetricsCollector` ops; C3a category auto-org.
- **Phase 2 (intelligence) — DONE (2026-05-28):** `KnowledgeOrganizer` corpus analysis proposes categories (C3a) and folder splits (C3b), user approves via shared `ReviewSheet`; `ChunkDeduplicator` (exact + semantic cosine ≥0.94) wired into `vm.createChunk`; `EmbeddingClient` in-memory cache (SHA256 key, FIFO 512); `RetrievalCoverage` (strong/partial/novel) via `HybridSearchEngine.assessCoverage`, injected into chat RAG block to steer grounding.
- **Phase 3 (visual) — DONE (2026-05-28):** C6 interactive Mermaid panorama on Dashboard (`MermaidView` gained `theme` + `interactive` pan/zoom; `ScrollPassthroughWebView` so it doesn't trap page scroll — zoom is ⌘+wheel/buttons). C5 structured visual `WeeklyDigest` (Pulso metrics+deltas / atención bars / decisiones / aprendizajes / lo que pesa / síntesis) — user OK'd dropping the rigid new/advanced/overcome/forgotten scheme for this data-driven one. A1 calendar **BLOCKED for the user (2026-05-28): their work tenant requires admin consent** for Graph Calendars.Read, which they cannot grant — Graph code stays dormant/ready for if they ever get consent. **EventKit IMPLEMENTED (2026-05-28) as the active calendar path** — `EventKitCalendar` actor reads macOS Calendar.app locally (TCC permission only, no admin/OAuth); VM prefers it over Graph (`calendarAuthorized`, `hasCalendar`); Settings has "Calendario de macOS (recomendado)" with "Permitir acceso"; Info.plist (build-app.sh) gained `NSCalendarsFullAccessUsageDescription`. Works IF the user's Outlook account is synced into macOS Calendar (System Settings → Internet Accounts). A1 Graph path code-complete, pending user's Entra app registration to light up: `MicrosoftGraphAuth` (PKCE OAuth via ASWebAuthenticationSession), `MicrosoftGraphClient` (calendarView), Settings connect UI, "Reuniones de hoy" dashboard card. Redirect URI `moscu-auth://auth`, scopes `offline_access User.Read Calendars.Read`, tenant default `common`, client id in UserDefaults, tokens in Keychain.

**Why:** the bugs make the app feel like a junk drawer, contradicting "second brain." Fix trust before adding features.

**How to apply:** work one item at a time, build+verify each before moving on (user preference — see [[feedback-build-and-verify]]).

**STANDING DECISION — local-first dropped project-wide (user, 2026-05-28):** "no debe ser local first, eso ya no lo usamos, necesito algo funcional." Local-first (CLAUDE.md non-negotiables #2/#3 and #6) **no longer applies** — prioritize functional/working features over on-device purity. BUT "100% free stack" (#1) and no-telemetry STILL hold (user actively checks cost). When A1 starts, update CLAUDE.md to formally retire the local-first rules.

**Microsoft Graph for calendar (A1) — confirmed FREE (2026-05-28):** Graph API has no per-call charge for calendar read/write; Entra ID app registration is free (no paid Azure sub); native auth = OAuth2 auth-code + PKCE (public client, no secret). Personal MS accounts self-consent; work/M365 accounts may need tenant admin consent (a permission gate, not a cost). EventKit remains a zero-OAuth fallback if Outlook is synced into macOS Calendar, but user chose Graph for richer/direct Outlook data.
