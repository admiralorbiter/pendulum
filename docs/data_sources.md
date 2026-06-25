# Data Sources Guide

*When the Pendulum Doesn't Swing — Research Project*

This document catalogs every data source relevant to the project. For each source: what it is, how to access it, which variables it provides, and how it maps to the theory.

---

## Overview Map

| Source | Type | Domain | Theory Variable | Priority |
|---|---|---|---|---|
| NAEP | Achievement outcomes | Education | Outcomes | High |
| Education Next Poll | Public opinion | Education | Mass opinion (backlash) | High |
| PDK Poll | Public opinion | Education | Mass opinion (backlash) | High |
| ESSA State Plans | Policy design | Education | Policy correction | High |
| ECS Legislative Archives | Policy activity | Education | Policy intensity + correction | High |
| GDELT | Media attention | All domains | Elite/media backlash | High |
| Media Cloud | Media attention | All domains | Elite/media backlash | High |
| Google Trends | Search salience | All domains | Attention (A_t) | Medium |
| CRDC | School conditions | Education | Outcomes + discipline | High |
| ANES | Public opinion, political behavior | All domains | N_t norm anchor, controls | Medium |
| CES/CCES | Public opinion (large N) | All domains | State-level controls | High |
| GSS | Social attitudes | All domains | Trust, norm measures | Low |
| NCES Finance | School finance | Education | Controls | Medium |
| ACS | Demographics | All | Controls | Medium |
| BLS LAUS | Unemployment | All | Controls | Medium |
| MIT Election Lab | Election returns | All | Partisanship controls | High |
| Stanford SEDA | District achievement | Education | Outcomes | Medium |
| Common Core of Data | School characteristics | Education | Controls | Medium |

---

## 1. Public Opinion & Perception

### 1.1 Education Next Survey of Public Opinion
- **URL**: https://www.educationnext.org/poll/
- **Official data file**: "Question wording and data over time" downloadable from the site
- **Coverage**: Annual, national, 2007–present
- **Key variables**: Support for federal testing mandate (grades 3–8, HS), support for Common Core, views on teacher evaluation by test scores, school choice attitudes, school quality ratings
- **Theory relevance**: Mass opinion component of backlash index. Most directly tracks the NCLB/Common Core/ESSA sequence.
- **Limitations**: National only — cannot use for state-year panel directly. Use as external validity check for national trend narrative. Questions changed slightly over time; check wording archive carefully.
- **Notes**: The 2015 poll showing ~2/3 support for federal testing mandate even as Common Core support fell sharply is a key data point for the theory (backlash is bundle-specific, not generic anti-testing).

### 1.2 PDK Poll (Phi Delta Kappa / Gallup)
- **URL**: https://pdkpoll.org/
- **Coverage**: Annual, national, 1969–present (longest-running education opinion series in the U.S.)
- **Key variables**: Satisfaction with public schools, views on testing, federal vs. local control, school funding, teacher pay
- **Theory relevance**: Long historical baseline for norm estimation ($N_t$). Useful for establishing pre-NCLB baseline attitudes.
- **Limitations**: National only. Some question wording has changed over decades.
- **Download**: Annual toplines and archived reports downloadable as PDFs; tabular data available on request from PDK.

### 1.3 American National Election Studies (ANES)
- **URL**: https://electionstudies.org/
- **Access**: Free download after registration
- **Coverage**: Biennial (presidential + midterm years), 1948–present
- **Key variables**: Party identification, ideological self-placement, trust in government, issue positions, electoral behavior
- **Theory relevance**: Long-run norm anchor for $N_t$. Electoral behavior context. Institutional trust measures for norm variable operationalization.
- **Limitations**: Not education-specific. Sample size limits state-level disaggregation (use CES instead for state estimates).
- **Download format**: Stata, SPSS, CSV

### 1.4 Cooperative Election Study (CES / CCES)
- **URL**: https://cces.gov.harvard.edu/
- **Access**: Free download (Harvard Dataverse)
- **Coverage**: Annual, 2006–present; very large samples (40,000–80,000 respondents/year)
- **Key variables**: Policy preferences, party ID, ideology, vote choice, state of residence
- **Theory relevance**: Primary source for **state-level opinion estimates**. Large enough to construct state-year public opinion series via multilevel regression and poststratification (MrP) if needed.
- **Download**: Cumulative file available covering 2006–present; also available year-by-year.

### 1.5 General Social Survey (GSS)
- **URL**: https://gss.norc.org/
- **Access**: Free download (SDA browser or bulk download)
- **Coverage**: 1972–present (biennial in recent years)
- **Key variables**: Social trust, institutional confidence, racial attitudes, education spending attitudes
- **Theory relevance**: Secondary norm anchor. Confidence-in-education items. Long-run time series for pre-NCLB baselines.
- **Limitations**: Not education-policy specific. Biennial cadence limits time-series density.

---

## 2. Policy Design & Institutional Variables

### 2.1 ESSA Consolidated State Plans
- **URL**: https://www.ed.gov/essa/implementing/plans/index.html
- **Access**: Public PDFs from the U.S. Department of Education
- **Coverage**: All 50 states + DC, filed 2017–2018; amendments available
- **Key variables**: Accountability indicator weights, school rating systems (A-F, 1-5, etc.), multiple measures vs. single-metric design, teacher evaluation linkage, school improvement strategies
- **Theory relevance**: Primary source for **policy correction score**. Codes the ESSA-era redesign away from test-centric accountability.
- **Coding approach**: Construct indicator weight index, count of non-test indicators, rating system complexity, presence of growth vs. proficiency emphasis. **Pre-register this coding scheme before starting.**
- **Limitations**: Filed once (2017–18), rarely amended. This is **cross-sectional**, not time-varying. Separate from annual legislative revision tracking (see ECS below).

### 2.2 Education Commission of the States (ECS) — Legislative Archives
- **URL**: https://www.ecs.org/
- **Access**: Free; 50-state comparison tools online
- **Key databases**:
  - Assessment and testing legislation (state-by-state)
  - Accountability legislation
  - Standards/curriculum legislation (Common Core adoption/revision)
  - Opt-out legislation
  - Teacher evaluation legislation
- **Theory relevance**: **Primary source for time-varying policy activity** — tracks annual state legislative changes. Complements ESSA plans (which are cross-sectional) with year-by-year legislative action.
- **Download**: Most useful as a manually coded panel; ECS provides legislative summaries and 50-state tables.

### 2.3 NCLB Archive / Federal Policy Timeline
- **URL**: https://www2.ed.gov/nclb/overview/intro/index.html
- **Coverage**: NCLB passage (Jan 8, 2002), waiver program, Common Core-NCLB waiver linkage, ESSA passage (Dec 10, 2015)
- **Theory relevance**: Federal policy phase coding: NCLB implementation, waiver/Common Core expansion, ESSA passage, ESSA-era redesign. Essential for phase-by-phase analysis.

### 2.4 NCES Accountability and ESSA Tables
- **URL**: https://nces.ed.gov/
- **Key files**: State-level accountability and ESSA plan tables; NAEP data explorer
- **Theory relevance**: Pre-ESSA baseline accountability data for constructing the pre-treatment policy intensity index.

---

## 3. Backlash Measurement — Media & Attention

### 3.1 GDELT Project
- **URL**: https://www.gdeltproject.org/
- **Access**: Free; Google BigQuery (recommended for large queries); also bulk download
- **Coverage**: Global news media, 1979–present; near-real-time updates
- **Key variables**: Article counts by keyword and date; tone scores; geographic mention
- **Theory relevance**: **Elite/media backlash component** of backlash index. Track "Common Core," "standardized testing," "opt out testing," "No Child Left Behind," "ESSA" over time.
- **Limitations (CRITICAL from peer review)**: 
  - Over-represents English-language national media
  - Systematic gaps in regional and local coverage
  - Geographic attribution is problematic — a NYT article about opt-out is not evidence of New York State backlash specifically
  - Use for national trend signals; avoid state-level attribution without strong validation
- **Query approach**: GDELT 2.0 GKG via BigQuery; filter by theme codes and keyword mentions

### 3.2 Media Cloud
- **URL**: https://mediacloud.org/
- **Access**: API (registration required); Python client library available
- **Coverage**: Curated media outlet lists, 2008–present
- **Key variables**: Article counts by source, keyword, date; can be filtered by state-level outlets
- **Theory relevance**: Second media attention source; better suited than GDELT for controlled outlet-list analysis. Can filter to state-level outlets for better geographic attribution.
- **Limitations**: Coverage depends on outlet lists that change over time; cross-year comparability requires careful attention.
- **Python library**: `pip install mediacloud`

### 3.3 Google Trends
- **URL**: https://trends.google.com/
- **Access**: `pytrends` Python library for programmatic access
- **Coverage**: 2004–present; weekly data for multi-year queries; daily for short windows
- **Key variables**: Relative search interest (0–100 scale) by keyword and geography
- **Theory relevance**: **Attention (A_t) proxy**. State-level data available by DMA (media market) — better geographic granularity than GDELT. Search terms: "Common Core," "opt out testing," "standardized testing," "school testing," "ESSA"
- **Limitations**: Relative, not absolute, counts. Values are comparable within a query but not across separate queries. Normalize carefully.
- **Code**:
  ```python
  from pytrends.request import TrendReq
  pytrends = TrendReq()
  pytrends.build_payload(["Common Core"], geo="US", timeframe="2010-01-01 2024-01-01")
  df = pytrends.interest_over_time()
  ```

---

## 4. Achievement & Outcomes

### 4.1 NAEP (National Assessment of Educational Progress)
- **URL**: https://www.nationsreportcard.gov/
- **Access**: NAEP Data Explorer (online); bulk download via API
- **Coverage**: State math and reading, grades 4 and 8; biennial 1990/1992–present
- **Key variables**: Mean scale scores, proficiency rates, achievement gap by subgroup (race, income, disability)
- **Theory relevance**: **Primary outcomes variable**. Low-stakes (not tied to state accountability), consistent across states. Use as external outcome series and as "achievement signal" ($AchievementSignal_{s,t-1}$ in the backlash equation).
- **Download**: NAEP Data Explorer → select states, years, subjects, grades → export CSV

### 4.2 Stanford Education Data Archive (SEDA)
- **URL**: https://edopportunity.org/
- **Access**: Free download (Harvard Dataverse)
- **Coverage**: District-level achievement, 2008/09–2019; updated versions available
- **Key variables**: Standardized test score trends by district, demographic covariates, opportunity measures
- **Theory relevance**: District-level extension when state analysis needs more granularity. Useful for within-state variation analysis.

---

## 5. School Conditions & Discipline

### 5.1 Civil Rights Data Collection (CRDC)
- **URL**: https://www2.ed.gov/about/offices/list/ocr/data.html
- **Access**: Free download from OCR
- **Coverage**: All public schools and districts; biennial (2011–12 onward)
- **Key variables**: Suspension/expulsion rates by race and grade, referrals to law enforcement, restraint and seclusion, school-level demographics
- **Theory relevance**: **Primary data source for the school discipline comparison case.** Operationalizes discipline policy intensity and allows testing whether pendulum dynamics generalize beyond testing.
- **Limitations**: Biennial cadence; some early years had data quality issues (flagged by OCR)

### 5.2 NCES School Survey on Crime and Safety (SSOCS)
- **URL**: https://nces.ed.gov/surveys/ssocs/
- **Coverage**: School-level safety, discipline incidents; periodic (not annual)
- **Theory relevance**: Supplement to CRDC for school climate measures

---

## 6. State-Level Covariates & Controls

### 6.1 American Community Survey (ACS)
- **URL**: https://www.census.gov/programs-surveys/acs.html
- **Access**: Census API; `tidycensus` (R) or `census` (Python) wrappers
- **Coverage**: Annual state and county estimates; 2005–present
- **Key variables**: Poverty rate, household income, race/ethnicity composition, educational attainment, population
- **Theory relevance**: Demographic and economic controls in all regression models

### 6.2 BLS Local Area Unemployment Statistics (LAUS)
- **URL**: https://www.bls.gov/lau/
- **Coverage**: Monthly state unemployment rates; 1976–present
- **Theory relevance**: Economic stress controls

### 6.3 MIT Election Data and Science Lab
- **URL**: https://electionlab.mit.edu/data
- **Access**: Free download (Harvard Dataverse)
- **Key variables**: Presidential and gubernatorial vote shares by state and year; legislative composition
- **Theory relevance**: **Primary partisanship controls** — presidential vote share, state legislative party control, governor party. Critical for ruling out partisan cycling as alternative explanation (see empirical design).

### 6.4 NCES / Census School Finance
- **URL**: https://nces.ed.gov/edfin/; Census Annual Survey of School System Finances
- **Coverage**: Annual, district and state level
- **Key variables**: Per-pupil expenditure, revenue sources, state vs. local vs. federal funding shares
- **Theory relevance**: School finance controls; proxy for state education capacity

---

## 7. Notes on the Backlash Index Construction

> [!IMPORTANT]
> **Pre-register all index construction decisions on OSF or EGAP before collecting data.** This is the most critical credibility protection available. Decisions made ad hoc after seeing the data create substantial researcher degrees of freedom.

The composite backlash index should be built from **three distinct sub-indicators**, run separately before combining:

1. **Mass opinion** (Education Next Poll, PDK Poll, CES items) — surveys
2. **Organized mobilization** (opt-out rates, ECS legislative activity, school board election outcomes) — behavioral
3. **Elite/media framing** (GDELT, Media Cloud, Google Trends) — media

**Validation steps:**
1. Examine each indicator separately first — do they show the same directional pattern?
2. Run confirmatory factor analysis (CFA) to test whether they load on one latent "backlash" dimension or multiple
3. If multiple factors, treat them as separate dependent variables with separate theoretical interpretations
4. If combining into composite, use factor scores or PCA weights — document the method in the pre-registration

---

## 8. COVID-Era Data Considerations

> [!WARNING]
> **The 2020–2024 period requires special treatment.** COVID disrupted both policy and outcomes in ways that are not well-described by the pre-COVID pendulum framework. Post-2020 education politics (parent rights movements, curriculum debates, learning loss discourse) introduced new conflict dimensions. Recommended approach:
> - Primary analysis: 2010–2019
> - Robustness check 1: Exclude 2020–2022
> - Robustness check 2: Add pandemic-period interaction
> - Alternative: Treat 2020–2024 as a separate analytical epoch with a separate model

---

## 9. Accessing Data Programmatically

Key Python libraries for this project:
```python
# Google Trends
pip install pytrends

# Census / ACS
pip install census us

# NAEP (via API - check current NCES API status)
# Primarily manual download from nationsreportcard.gov

# GDELT via BigQuery
pip install google-cloud-bigquery pandas-gbq

# Media Cloud
pip install mediacloud

# MIT Election Lab data - download from Dataverse
# https://dataverse.harvard.edu/dataverse/electionscience
```
