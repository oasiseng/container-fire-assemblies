<p align="center">
  <img src="assets/oasis-logo.svg" alt="Oasis Engineering" width="220">
</p>

# Container Fire-Rated Wall Assemblies

**1-hour and 2-hour fire-rated wall assemblies for shipping container construction — UL-listed, code-compliant, and openly published.**

Built on **UL Design V497** (GA File **WP 1297**), a one-sided steel-stud partition that covers both 1HR and 2HR ratings under a single UL design number. Direct application per **IBC §703.2.2(1)**. No alternative-means submittal required for the typical case.

Maintained by **[Oasis Engineering](https://oasisengineering.com)** · Engineer of record: Enrique Lairet, PE.

---

## Why this exists

For fifteen years, container projects have stalled at plan review on a single question: *what is the fire-resistance rating of the wall?* The folklore in the industry says no UL-listed assembly works for containers. **That folklore is wrong.** UL Design V497 is a *one-sided* tested assembly — the unprotected side is bare studs in the test. When V497 is applied to the interior face of a container, the corrugated steel container skin takes the place of that unprotected side. The skin is unambiguously *more* protective than nothing. The rating holds. The whole industry has been looking for a symmetric tested assembly when an asymmetric one was sufficient.

This repo publishes the framework openly so any container builder, architect, AHJ, or owner can use it.

---

## What's in this repo

| File | What it is |
|---|---|
| [`docs/white-paper.md`](docs/white-paper.md) | Full engineering white paper — code basis, all five assembly variants, equivalency analysis, references, permit-submittal guide |
| [`details/CFW-Detail-Sheet.pdf`](details/CFW-Detail-Sheet.pdf) | One-sheet ANSI B drawing with section views, materials callouts, and code basis block — sized to drop into a permit set |
| [`details/V497-NGC-Blog-Details.pdf`](details/V497-NGC-Blog-Details.pdf) | National Gypsum reference detail set showing all three V497 variants |
| [`details/V497-NGC-WPU-007-Bulletin.pdf`](details/V497-NGC-WPU-007-Bulletin.pdf) | National Gypsum technical bulletin for the 3-layer V497 variant |
| [`details/V497-NGC-2018048-Acoustic.pdf`](details/V497-NGC-2018048-Acoustic.pdf) | NGC sound transmission test report (STC 42, ASTM E90) |
| [`LICENSE`](LICENSE) | MIT License with engineering-use notice |

---

## The assemblies at a glance

All five assemblies are built from a V497 steel-stud partition applied to the interior face of the container. They differ in how the gypsum is layered and whether an exterior intumescent coating is added.

| Assembly | Rating | Direction | Code basis | Construction summary |
|---|---|---|---|---|
| **CFW-1A** | 1 HR | Interior | §703.2.2(1) — direct V497 | 2 layers 5/8" Type X + ProForm Quick-Set, on 3-5/8" steel studs at 24" o.c. |
| **CFW-1B** | 1 HR | Interior | §703.2.2(1) — direct V497 | 3 layers 5/8" Type X on 3-5/8" steel studs at 24" o.c. |
| **CFW-2** | 2 HR | Interior | §703.2.2(1) — direct V497 | 4 layers 5/8" Type X on 3-5/8" steel studs at 24" o.c. |
| **CFW-1E** | 1 HR | Both sides | §703.2.2(4) — analysis | CFW-1B + UL-listed 1HR intumescent coating on container exterior |
| **CFW-2E** | 2 HR | Both sides | §703.2.2(4) — analysis | CFW-2 + UL-listed 2HR intumescent coating on container exterior |

For typical V-B / R-3 / B occupancies (single-family, ADUs, small commercial, food service), **CFW-1A or CFW-1B is what you want.** For occupancy separations or 2HR fire walls, **CFW-2.** For symmetric ratings (both-sides), **CFW-1E or CFW-2E.**

Insulation per V497 is **optional**. For container thermal/air-seal performance, spray closed-cell polyurethane foam directly against the container skin *outboard* of the V497 stud cavity — see white paper §5.

---

## Code basis (the short version)

> **IBC §703.2.2 Analytical Methods.** The fire resistance of building elements established by an analytical method shall be by any of the methods listed in this section… (1) Fire-resistance designs documented in approved sources… (4) Engineering analysis based on a comparison of building element… designs having fire-resistance ratings as determined by the test procedures set forth in ASTM E119 or UL 263.

CFW-1A, CFW-1B, and CFW-2 are direct applications of V497 under §703.2.2(1). CFW-1E and CFW-2E use §703.2.2(4) to add UL-listed intumescent coating protection on the container exterior.

For full citations, equivalency arguments, and limits/caveats, see the [white paper](docs/white-paper.md).

---

## Using this on a real project

1. Read the [white paper](docs/white-paper.md) (especially §7 — Limits and §8 — Permit Submittal).
2. Pick the assembly that matches your project's rating requirement and direction.
3. Drop [`details/CFW-Detail-Sheet.pdf`](details/CFW-Detail-Sheet.pdf) into your architectural set, referenced from the wall type schedule.
4. Get a project-specific PE-stamped letter from a PE licensed in the project jurisdiction.
5. Pre-coordinate with the AHJ before submittal.

**Oasis Engineering offers project-specific PE letters and stamping based on these assemblies.** Email or visit [oasisengineering.com](https://oasisengineering.com) to start a project.

---

## Contributing

If you find an error in the analysis, the citations, or the assemblies, please open an issue. If you use this on a project, we want to hear about it — file an issue or send us a note. If a manufacturer would like to fund an actual ASTM E119 burn of a container assembly so the industry can graduate from §703.2.2 analysis to a project-specific UL listing, get in touch.

---

## License

MIT License with engineering-use notice. See [`LICENSE`](LICENSE).

The fire-resistance analyses, assemblies, and details in this repository are published for educational and reference purposes. Project use requires site-specific PE review, AHJ acceptance, and verification of installed material thicknesses against the listed UL designs. **This repository is not a substitute for project-specific engineering.**

---

## Maintainer

**Oasis Engineering, PLLC**
Engineer of record: Enrique Lairet, PE
Web: [oasisengineering.com](https://oasisengineering.com)
GitHub: [github.com/oasiseng](https://github.com/oasiseng)
