# A Code-Compliant Fire-Rated Wall Assembly for Shipping Container Construction

**1-Hour and 2-Hour Assemblies — Direct Application of UL Design V497 per IBC §703.2.2(1)**

*An open-source engineering reference published by [Oasis Engineering](https://oasisengineering.com)*

*Version 1.2 — April 2026*

---

## TL;DR

The container construction industry has spent fifteen years arguing about fire-rated wall assemblies as if no listed design existed. **One does. And it covers both 1-hour and 2-hour ratings under the same UL design number.**

**UL Design V497** (GA File **WP 1297**) is a UL-listed, non-loadbearing, *single-sided* steel-stud partition. The same design number covers three tested variants:

- **1HR — 2 layers** of 5/8" Fire-Shield Type X gypsum board with ProForm Quick-Set setting compound between them
- **1HR — 3 layers** of 5/8" Fire-Shield Type X gypsum board
- **2HR — 4 layers** of 5/8" Fire-Shield Type X gypsum board

In all three variants, **gypsum is on one side only.** The opposite side, in the tested assembly, is bare studs. Cavity insulation is **optional** per the listing.

When V497 is applied to the interior face of a shipping container, the corrugated 14-ga steel container skin takes the place of the tested assembly's unprotected side. The steel skin is unambiguously *more* protective than nothing. The fire-resistance rating — 1HR or 2HR — is conferred directly by the listed design. **No alternative-means submittal is required for either case.** Both fall under IBC §703.2.2(1), direct application of an approved listed design.

For projects that additionally require *symmetric* fire resistance from both sides (fire walls between dwelling units, certain fire separation distance conditions), this paper presents an optional engineering analysis under IBC §703.2.2(4) that adds a UL-listed intumescent coating to the container's exterior steel skin.

The detail sheet that accompanies this paper (`details/CFW-Detail-Sheet.pdf`) is sized to drop directly into a permit set. All assemblies use commercially available products. The framework is published openly so AHJs, architects, and builders can vet it, copy it, and use it.

If you are designing or permitting a container build and have hit the "no UL-listed assembly" wall — the wall isn't there. This is the path through it.

---

## 1. The Problem Designers *Think* They Have

Shipping container architecture has been built across all 50 states for decades. Yet at the plan-review desk, container projects routinely stall on the same question: *what is the fire-resistance rating of the wall?* The standard answer for conventional construction is to point to a UL- or GA-listed assembly. The folklore in the container industry is that no such listing exists for a wall assembly that uses the container's corrugated steel skin.

That folklore is half right. There is no listing for an assembly that *integrates* the container skin as a tested face sheet. There *is* a listing — V497 — that is structured in a way that makes integrating the container skin trivial: the tested assembly already includes an unprotected face. Replacing "unprotected studs and cavity" with "unprotected studs, cavity, and a continuous 14-gauge steel skin a few inches further out" cannot reduce the fire-resistance rating. It can only increase it.

The industry has been looking for a *symmetric* tested assembly when a one-sided one was sufficient — and was sitting in the UL catalog the whole time, with both 1HR and 2HR ratings.

---

## 2. The Code Basis

The relevant section of the International Building Code is §703.2.2 — *Analytical Methods.* The full text:

> **703.2.2 Analytical Methods.** The fire resistance of building elements, components or assemblies established by an analytical method shall be by any of the methods listed in this section, based on the fire exposure and acceptance criteria specified in ASTM E119 or UL 263.
>
> 1. Fire-resistance designs documented in approved sources.
> 2. Prescriptive designs of fire-resistance-rated building elements, components or assemblies as prescribed in Section 721.
> 3. Calculations in accordance with Section 722.
> 4. Engineering analysis based on a comparison of building element, component or assemblies designs having fire-resistance ratings as determined by the test procedures set forth in ASTM E119 or UL 263.
> 5. Fire-resistance designs certified by an approved agency.

Two of these methods apply to this paper:

- **§703.2.2(1)** — *Approved sources.* The UL Online Certifications Directory and the Gypsum Association's *Fire Resistance and Sound Control Design Manual* are universally accepted as approved sources. UL Design V497 and GA File WP 1297 are both listed. **All three primary assemblies in this paper (CFW-1A, CFW-1B, CFW-2) are direct applications of V497 and fall under §703.2.2(1).**
- **§703.2.2(4)** — *Engineering analysis based on comparison.* Used here only for the optional enhanced assemblies (CFW-1E and CFW-2E), which add a UL-listed intumescent coating to the container's exterior steel face for symmetric fire resistance.

IBC §104.11 (*Alternative Materials, Design and Methods of Construction and Equipment*) provides the AHJ acceptance pathway for the §703.2.2(4) cases. The §703.2.2(1) cases require no alternative-means submittal — they are direct applications of a listed assembly, the same as specifying any other UL design number on a permit set.

---

## 3. The Tested Assembly: UL V497 / GA File WP 1297

UL Design V497 — also catalogued as Gypsum Association File No. WP 1297 — is a non-loadbearing steel-stud partition with three tested variants under the same design number. The common construction:

| Component | Specification (common to all three variants) |
|---|---|
| Studs | 3-5/8" cold-formed steel studs at 24" o.c. max |
| Top and bottom track | Steel track, mechanically fastened 24" o.c. max |
| Cavity insulation | Glass fiber — **optional** per the listing |
| Joint at top (against deck above) | Firestop sealant required |
| Joint at base | Flexible sealant — optional per the listing |
| Side 2 (rated face) | Type X gypsum, layered as described below per variant |
| Side 1 (unprotected face) | None — bare studs |

The three variants are differentiated only by the gypsum buildup on the rated face:

| Variant | Layers of 5/8" Type X Gypsum | Additional Components | Rating |
|---|---|---|---|
| **V497 — 2-layer** | 2 layers | ProForm Quick-Set setting compound between layers | 1 HR |
| **V497 — 3-layer** | 3 layers | (none beyond standard fastening) | 1 HR |
| **V497 — 4-layer** | 4 layers | (none beyond standard fastening) | 2 HR |

The acceptable gypsum products per the V497 listing include Gold Bond Fire-Shield: FSW, FSW-C, FSW-6, eXP-C, SBWB, FSK, and FSK-C. Acoustic performance for the 3-layer 1HR variant has been independently tested at STC 42 (NGC Test Report 2018048).

Source documents reproduced in this repository:

- `details/V497-NGC-Blog-Details.pdf` — National Gypsum head-of-wall and base-of-wall detail set showing all three V497 variants
- `details/V497-NGC-WPU-007-Bulletin.pdf` — National Gypsum technical bulletin for the 3-layer 1HR variant
- `details/V497-NGC-2018048-Acoustic.pdf` — NGC Testing Services sound transmission loss test report (NGC 2018048), STC 42

**The key fact:** V497 is *asymmetric.* Each rating is conferred by the gypsum face protecting the steel-stud structural element. The unprotected face — bare studs facing the cavity — is not part of what creates the rating. That asymmetry is what makes V497 the right comparison basis for a container wall.

---

## 4. The Assemblies

### 4.1 CFW-1A — 1-Hour Assembly *(V497 2-layer + ProForm Quick-Set)*

**Code basis:** IBC §703.2.2(1) — direct application of an approved listed assembly (V497, 1HR variant).

| Layer (interior → exterior) | Material | Specification |
|---|---|---|
| 1 (interior face) | Type X gypsum, **face layer** | 5/8" Gold Bond Fire-Shield, fastened per V497 listing |
| 2 | ProForm Quick-Set setting compound | Per V497 listing, between gypsum layers |
| 3 | Type X gypsum, **base layer** | 5/8" Gold Bond Fire-Shield, fastened to studs |
| 4 | Steel studs | 3-5/8" deep, 24" o.c. max, with steel top and bottom track mechanically fastened 24" o.c. max |
| 5 | Cavity insulation | Glass fiber, **optional** — see §5 for spray-foam compatibility |
| 6 (exterior) | **Container skin** | Existing 14-ga corrugated COR-TEN A steel container side wall — *no modification or coating required for the 1HR rating* |

Joint conditions: firestop sealant at top against the deck/header above; flexible sealant at base (optional per V497).

**Use case:** Lowest-thickness 1HR assembly. Saves one gypsum layer compared to CFW-1B, at the cost of requiring the ProForm Quick-Set setting compound application step.

---

### 4.2 CFW-1B — 1-Hour Assembly *(V497 3-layer)*

**Code basis:** IBC §703.2.2(1) — direct application of an approved listed assembly (V497, 1HR variant).

| Layer (interior → exterior) | Material | Specification |
|---|---|---|
| 1 (interior face) | Type X gypsum, **face layer** | 5/8" Gold Bond Fire-Shield, fastened 12" o.c. with 2-1/4" Type S screws |
| 2 | Type X gypsum, **middle layer** | 5/8" Gold Bond Fire-Shield, fastened 24" o.c. with 1-5/8" Type S screws, joints staggered 24" V / 12" H from face layer |
| 3 | Type X gypsum, **base layer** | 5/8" Gold Bond Fire-Shield, fastened 24" o.c. with 1" Type S screws, joints staggered from middle layer |
| 4 | Steel studs | 3-5/8" deep, 24" o.c. max (25 ga or heavier), with steel top and bottom track mechanically fastened 24" o.c. max |
| 5 | Cavity insulation | Glass fiber, **optional** — see §5 for spray-foam compatibility |
| 6 (exterior) | **Container skin** | Existing 14-ga corrugated COR-TEN A steel container side wall — *no modification or coating required for the 1HR rating* |

Joint conditions: firestop sealant at top; flexible sealant at base (optional).

**Use case:** All-gypsum 1HR assembly without the additional setting-compound step. Slightly thicker than CFW-1A but simpler trade workflow. Independently tested at STC 42 (NGC 2018048).

---

### 4.3 CFW-2 — 2-Hour Assembly *(V497 4-layer)*

**Code basis:** IBC §703.2.2(1) — direct application of an approved listed assembly (V497, 2HR variant).

| Layer (interior → exterior) | Material | Specification |
|---|---|---|
| 1 (interior face) | Type X gypsum, **outer face layer** (4th) | 5/8" Gold Bond Fire-Shield, fastened per V497 listing, joints staggered |
| 2 | Type X gypsum, layer 3 | 5/8", fastened per listing, joints staggered |
| 3 | Type X gypsum, layer 2 | 5/8", fastened per listing, joints staggered |
| 4 | Type X gypsum, base layer | 5/8", fastened per listing |
| 5 | Steel studs | 3-5/8" deep, 24" o.c. max, with steel top and bottom track mechanically fastened 24" o.c. max |
| 6 | Cavity insulation | Glass fiber, **optional** — see §5 for spray-foam compatibility |
| 7 (exterior) | **Container skin** | Existing 14-ga corrugated COR-TEN A steel container side wall — *no modification or coating required for the 2HR rating* |

Joint conditions: firestop sealant at top; flexible sealant at base (optional).

**Use case:** 2HR rating for occupancy separations, dwelling-unit fire walls, or any project where the AHJ requires 2-hour interior fire resistance. *Same UL design number as the 1HR variants.* No equivalency argument required.

---

### 4.4 CFW-1E and CFW-2E — Optional Symmetric (Both-Sided) Variants

**Code basis:** IBC §703.2.2(4) — engineering analysis by comparison.

CFW-1E and CFW-2E are identical to CFW-1B and CFW-2 respectively, with the addition of a UL-listed intumescent coating on the *exterior* face of the container skin. Use these only when the project requires *symmetric* fire resistance — meaning the rating must be achieved independently from both directions of fire exposure. Typical triggers:

- The wall is a *fire wall* or *fire barrier* requiring rated performance from both sides (IBC Chapter 7).
- The exterior wall must satisfy fire-spread requirements based on fire separation distance (IBC §705.5).
- The AHJ specifically requires symmetric rating.

| Additional layer (exterior) | Material | Specification |
|---|---|---|
| Surface preparation | SSPC-SP6 commercial blast cleaning or coating-manufacturer-approved equivalent |
| Primer | Manufacturer-listed primer per the intumescent's UL design |
| Intumescent coating | UL-listed intumescent for **1HR (CFW-1E)** or **2HR (CFW-2E)** protection of structural steel substrate, applied to the listed dry-film thickness. Acceptable products include Carboline Nullifire SC902, PPG Pitt-Char NX, or equivalent. |
| Topcoat | Manufacturer-listed weather-protective topcoat for exterior exposure |

**Equivalency argument (§703.2.2(4)):** The exterior face consists of a continuous 14-ga steel substrate protected by an intumescent coating that is independently UL-listed (typically per UL Design X771, X772, X791, or product-specific designs) for the relevant duration of structural-steel substrate protection under ASTM E119 / UL 263. The function in those listings — keeping a steel substrate below the critical temperature for the rated time under the E119 time-temperature curve — is identical to the function required here. The intumescent system on the container's steel skin therefore extends its UL-listed protection of steel substrates directly to this application.

Combined with the V497 interior rating, the total assembly provides the rated protection independently from each side.

---

## 5. The Insulation Question (Glass Fiber vs. Closed-Cell Spray Foam)

The V497 listing makes glass fiber cavity insulation **optional**. This is unusual — most rated assemblies tie cavity fill into the listing — and it solves a problem that has otherwise complicated container fire-rating design.

A typical container build wants closed-cell spray polyurethane foam (ccSPF) directly against the container skin for two reasons that have nothing to do with fire resistance: ccSPF is the most reliable air-seal against the corrugated steel surface, and it provides the highest R-value per inch (R-6.5+) for the limited cavity depth. Many designers default to ccSPF for the entire wall cavity.

Because V497 makes cavity insulation *optional*, the listing does not constrain the cavity fill choice. The recommended construction sequence:

1. Spray ccSPF directly against the container skin (interior face of the container) at the desired thickness for thermal/air-seal performance. Typical thickness: 2–3 inches (R-13 to R-19), determined by climate zone and project energy code (e.g., ComCheck).
2. Erect the V497 steel-stud framing inboard of the ccSPF, set off the container skin to provide the ccSPF cavity depth. Use 3-5/8" steel studs at 24" o.c. max (V497 listing).
3. Fill the V497 stud cavity with glass fiber if additional thermal performance is desired (now genuinely optional per the listing) or leave open.
4. Apply gypsum to the room-side face of the studs per the chosen V497 variant (CFW-1A, CFW-1B, or CFW-2).

The result satisfies V497 directly (the listing makes no constraint on what is on the unrated side of the studs) and gives the project the ccSPF air-seal and thermal performance independently. There is no equivalency argument required for this construction.

**What is *not* permitted:** substituting ccSPF *inside* the V497 stud cavity *in place of* the listing's optional glass fiber. The listing tests with glass fiber when insulation is present; substituting a different cavity fill within the rated cavity would require its own §703.2.2(4) analysis. Keep the ccSPF outboard of the studs (against the container skin) and the V497 stud cavity either empty or filled with glass fiber.

---

## 6. Why V497 Is the Right Comparison Basis (and Why Symmetric Designs Aren't)

A common mistake — one this paper avoids — is to start from a symmetric tested assembly such as UL U419 (gypsum both sides) and try to substitute the container skin for one of the gypsum faces. That approach forces an equivalency argument for the *substituted* face: you must demonstrate that 14-ga coated steel performs as well as 5/8" Type X gypsum under E119. The argument is winnable but contested, because it asks the AHJ to accept that two materials with very different failure modes are interchangeable.

The V497 approach inverts the problem. V497 *already includes* an unprotected face in the tested assembly. The CFW substitution doesn't replace the unprotected face — it *adds material on the cold side* of the unprotected face. There is no equivalency claim to dispute. The container skin is, structurally and thermally, surplus to the conditions UL tested.

This is why CFW-1A, CFW-1B, and CFW-2 read as direct applications of an approved listed design under §703.2.2(1), while only CFW-1E and CFW-2E — which add coating-based protection in a direction V497 doesn't address — fall under §703.2.2(4).

---

## 7. Limits, Caveats, and Conditions of Use

Honest scope is part of what makes this defensible.

- **Direction of rating matters.** CFW-1A, CFW-1B, and CFW-2 protect against fires originating *inside* the container. Verify the project's actual rating requirement and direction before specifying. If symmetric rating is required, use CFW-1E / CFW-2E.
- **No deviation from the V497 listing.** The assembly must use 5/8" Type X gypsum from the manufacturers and product lines named in the V497 listing (or substitutions explicitly permitted by UL/GA). Substituting an off-brand or wrong-thickness gypsum voids the listing.
- **Cavity fill rules.** Per §5 above: keep ccSPF outboard of the V497 stud cavity (against the container skin). Inside the V497 stud cavity, use glass fiber or leave empty — both are within the listing.
- **Joints, penetrations, and perimeter conditions** must be detailed using fire-rated sealants per UL 1479 (through-penetrations) and UL 2079 (joint systems). The wall rating does not survive an unsealed penetration.
- **Top of wall.** V497 details show firestop sealant at the head-of-wall against concrete or fluted steel deck. For a container application, the top of the V497 assembly meets the underside of the container roof corrugation. Use a UL-listed head-of-wall firestop system rated for the joint condition.
- **Coating thickness verification is non-negotiable** for CFW-1E and CFW-2E. Wet-film thickness gauging during application and dry-film thickness gauging after cure must be documented. The UL listing on intumescents is specific to the dry-film thickness; under-application voids the rating.
- **Coating compatibility with COR-TEN / weathering steel substrates** must be confirmed in writing by the coating manufacturer. Pre-existing rust, mill scale, paint, and surface contaminants typically require abrasive blast prep (SSPC-SP6 or higher) before primer application.
- **AHJ pre-coordination.** Even the §703.2.2(1) direct-application case benefits from a brief pre-submittal conversation with the building official. Surprising a plan reviewer with an unfamiliar UL design number costs more time than introducing it.
- **Project-specific PE stamp required.** This paper supports the analytical framework. A site- and project-specific stamped letter from a PE licensed in the jurisdiction is required for permit submittal.

---

## 8. How to Use This in a Permit Submittal

For **CFW-1A, CFW-1B, or CFW-2** (interior fire only — the typical case):

1. Reference UL Design V497 / GA File WP 1297 in the wall type schedule, noting the variant (2-layer / 3-layer / 4-layer) and rating.
2. Note the container skin as a non-rated exterior weather barrier on the unprotected side of V497.
3. Include `details/CFW-Detail-Sheet.pdf` and the relevant National Gypsum reference detail (`details/V497-NGC-Blog-Details.pdf`) in the architectural set.
4. Include a brief PE letter confirming the container application is a direct extension of V497 under IBC §703.2.2(1) and that the steel skin substitution is conservative.

For **CFW-1E or CFW-2E** (symmetric 1HR or 2HR):

1. Reference V497 and the relevant intumescent UL design number in the wall type schedule.
2. Include the detail sheet and this white paper as a permit attachment.
3. Submit a PE-stamped §104.11 alternative-means cover letter that adopts the analysis here, confirms the project's fire-rating requirement, and lists the specific products being used.
4. Include the intumescent coating manufacturer's UL listing card and product data sheets.
5. Pre-coordinate with the AHJ before submittal.

Oasis Engineering offers project-specific PE letters and stamping based on these assemblies. Contact information in the README.

---

## 9. Why We Are Publishing This

The container construction industry has had a reputation problem at the building department for fifteen years, and most of it traces back to one piece of folklore: that no UL-listed wall assembly works for containers. V497 has been sitting in the catalog the whole time — covering both 1HR and 2HR ratings under the same design number — and the industry just wasn't looking for asymmetric assemblies.

We could keep this analysis proprietary and bill more hours per project. We think the better business is the opposite: publish the framework, let the industry use it, and become the firm that documented it. If you find an error in the analysis, file an issue on this repository. If you use this on a project, we would like to hear about it.

---

## Appendix A — References

- **IBC 2021** — International Code Council. *International Building Code,* §703.2.2, §721, §722, §104.11, §705.5, Chapter 7.
- **ASTM E119-23** — *Standard Test Methods for Fire Tests of Building Construction and Materials.* ASTM International.
- **UL 263** — *Standard for Fire Tests of Building Construction and Materials.* Underwriters Laboratories.
- **UL Design V497** — *Nonbearing Wall Rating — 1 HR / 2 HR.* UL Online Certifications Directory.
- **GA File No. WP 1297** — Gypsum Association *Fire Resistance and Sound Control Design Manual.*
- **UL X-series designs** (X771, X772, X791, etc.) — Intumescent coating fire-resistance ratings on structural steel substrates.
- **National Gypsum Detail Set — V497** — Head-of-wall and base-of-wall details for all three V497 variants (2-layer 1HR, 3-layer 1HR, 4-layer 2HR). Reproduced in this repo as `details/V497-NGC-Blog-Details.pdf`.
- **National Gypsum Technical Bulletin** — *V497 / WP 1297 — Non-Loadbearing Steel Stud Partition – 1 Hour (3-layer variant).* National Gypsum Services Company, 07/01/2024. Reproduced as `details/V497-NGC-WPU-007-Bulletin.pdf`.
- **NGC Test Report 2018048** — *Sound Transmission Loss Test on Wall Partition,* ASTM E90-09(2016) / E413-16 / E1332-16. NGC Testing Services, 06/06/2018, STC 42 (3-layer V497 variant). Reproduced as `details/V497-NGC-2018048-Acoustic.pdf`.
- **GA-216** — *Application and Finishing of Gypsum Panel Products.* Gypsum Association.
- **GA-600** — *Fire Resistance Design Manual.* Gypsum Association.
- **ASTM C645** — *Standard Specification for Nonstructural Steel Framing Members.*
- **ASTM C1396** — *Standard Specification for Gypsum Board.*
- **ASTM E84** — *Standard Test Method for Surface Burning Characteristics of Building Materials.*
- **ISO 668 / ISO 1496-1** — Series 1 freight containers — classification, dimensions, and ratings.
- **SSPC-SP6** — *Commercial Blast Cleaning.* Society for Protective Coatings.
- **UL 1479 / UL 2079** — Through-penetration firestops and joint systems.
- Carboline Technical Data Sheet, *Nullifire SC902 Intumescent Coating.*
- PPG Protective & Marine Coatings Technical Data Sheet, *Pitt-Char NX Intumescent Coating.*

---

## Appendix B — Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | April 2026 | Initial publication, U419-based equivalency argument | Enrique Lairet, PE — Oasis Engineering |
| 1.1 | April 2026 | Reworked around UL V497 (one-sided tested assembly, 3-layer 1HR variant). CFW-1 reframed as direct §703.2.2(1) application; CFW-1E and CFW-2 retained §703.2.2(4) analysis for symmetric/2HR cases. | Enrique Lairet, PE — Oasis Engineering |
| 1.2 | April 2026 | Added all three V497 variants (2-layer 1HR, 3-layer 1HR, 4-layer 2HR) per NGC blog detail set. CFW-2 reframed as direct §703.2.2(1) application of V497 4-layer variant. Added §5 covering optional ccSPF outboard of V497 cavity to address container thermal/air-seal needs without disturbing the listing. | Enrique Lairet, PE — Oasis Engineering |

---

*This document is published under the MIT License with engineering use restrictions. See `LICENSE` in the repository root.*

*Oasis Engineering, PLLC · [oasisengineering.com](https://oasisengineering.com) · [github.com/oasiseng](https://github.com/oasiseng)*
