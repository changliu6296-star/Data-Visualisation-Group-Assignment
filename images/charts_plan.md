# Visualisation Plan — Global Data on Sustainable Energy

## Part 1 — Energy Equity (6 charts)

### Chart 1 — How has the geographic distribution of electricity access changed globally from 2000 to 2020?
- **Type:** Animated Choropleth Map (Plotly)
- **Columns:** `country`, `year`, `electricity_access_pct`
- **Notes:** Animate over all 21 years. Use `locationmode='country names'` with ISO-3 codes for reliable matching. 2020 has 175/176 countries. Strong narrative: Sub-Saharan Africa still lags in 2020.
- **Web:** ✅ Plotly map — satisfies "at least one Plotly map" requirement.

### Chart 2 — Have global average electricity access and clean cooking fuel access risen in tandem over 20 years?
- **Type:** Two-Line Chart (Matplotlib)
- **Columns:** `year`, `electricity_access_pct`, `clean_fuels_pct` — grouped by year, global mean
- **Notes:** Both columns have full 2020 data. The persistent gap between the two lines (electricity access > clean fuels) is the key story.
- **Web:** ✅ Matplotlib — also the designated **Datawrapper** chart. Export the aggregated two-column CSV (year, avg_electricity_access, avg_clean_fuels) to Datawrapper and recreate as a polished line chart. Datawrapper handles this format natively and produces a clean interactive version for the web page.

### Chart 3 — In 2020, does having electricity imply having clean cooking energy? What is the correlation?
- **Type:** Scatter Plot + Regression Line (Seaborn `regplot`)
- **Columns:** `electricity_access_pct`, `clean_fuels_pct`, year = 2020
- **Notes:** Both columns have strong 2020 coverage (175 and 167 countries). Expect a positive but non-linear correlation — countries at 100% electricity access cluster at varied clean-fuel levels. Color by continent for context.

### Chart 4 — How has average electricity access evolved by continent over 20 years? Which continent grew fastest?
- **Type:** Small Multiples Line Chart (Matplotlib, 1 subplot per continent)
- **Columns:** `year`, `electricity_access_pct`, `continent` — grouped mean per continent per year
- **Notes:** Requires continent column (added in §1). Africa will show the steepest absolute growth; Europe/Americas near 100% throughout. 2020 data available.

### Chart 5 — Has within-continent variation in electricity access narrowed as mean access improved (2000–2020)?
- **Type:** Box Plot (Seaborn)
- **Columns:** `electricity_access_pct`, `continent`, `year` — use 4 snapshot years: 2000, 2007, 2014, 2020
- **Notes:** Requires continent column. Narrowing IQR over time = convergence. Africa is the most interesting continent to examine. 4 snapshots keeps the chart readable.

### Chart 6 — In 2020, where are the 20 countries with lowest electricity access, and what do they have in common?
- **Type:** Bubble Chart (Seaborn)
- **Columns:** `gdp_per_capita` (x), `electricity_access_pct` (y), `pop_density` (size), `continent` (color), year = 2020
- **Notes:** 2020 has 175 countries for `electricity_access_pct`. `gdp_per_capita` has 159 countries in 2020 — verify that none of the bottom-20 countries are missing GDP (most are in Sub-Saharan Africa where World Bank data exists). Filter to bottom 20 by `electricity_access_pct`. Small bubble = low density.

---

## Part 2 — Energy Structure (7 charts)

### Chart 7 — How has the global electricity mix (fossil / nuclear / renewables) evolved over 20 years?
- **Type:** Stacked Area Chart (Matplotlib)
- **Columns:** `year`, `elec_fossil_twh`, `elec_nuclear_twh`, `elec_renewables_twh` — global sums per year
- **Notes:** All three TWh columns are complete across all years including 2020. Compelling story: renewables share growing visibly from ~2010. No data caveats needed.
- **Web:** ✅ Strong Matplotlib candidate.

### Chart 8 — How does the 2020 electricity mix differ by continent? Who is most fossil-dependent?
- **Type:** Stacked Bar Chart (Matplotlib, one bar per continent)
- **Columns:** `continent`, `elec_fossil_twh`, `elec_nuclear_twh`, `elec_renewables_twh` — summed per continent, year = 2020
- **Notes:** Requires continent column. TWh columns are complete for 2020. Normalise to 100% share per continent for fair comparison.

### Chart 9 — Which Top 10 countries have the highest renewable electricity share in 2020?
- **Type:** Horizontal Bar Chart (Matplotlib)
- **Columns:** `country`, `renew_elec_share_pct` (derived: `elec_renewables_twh / elec_total_twh × 100`), year = 2020
- **Notes:** Apply a minimum generation threshold of **≥ 1 TWh** to exclude micro-states that are technically 100% renewable but generate negligible electricity (e.g. Central African Republic 0.15 TWh, Lesotho 0.50 TWh). With the filter, the top 10 becomes meaningful: Albania, Bhutan, Iceland, Nepal, Ethiopia, Paraguay, Norway, Costa Rica, Uganda, Namibia.
- **Web:** ✅ Clean, readable Matplotlib chart.

### Chart 10 — How has energy intensity changed by continent over 20 years? Is efficiency improving?
- **Type:** Line Chart (Matplotlib, one line per continent)
- **Columns:** `year`, `energy_intensity`, `continent` — grouped mean per continent, **years 2000–2019 only** (2020 has 1/176 countries)
- **Notes:** Requires continent column. Declining energy intensity = improving efficiency per unit GDP. Asia's decline is the most dramatic story.

### Chart 11 — Does higher renewable energy share correlate with lower energy intensity in 2019?
- **Type:** Scatter Plot + Regression Line (Seaborn `regplot`)
- **Columns:** `renew_energy_share_pct` (x), `energy_intensity` (y), `continent` (color), **year = 2019**
- **Notes:** Both columns use 2019 (energy_intensity: 171 countries; renew_energy_share_pct: 174 countries). Using `renew_energy_share_pct` (economy-wide share) rather than `renew_elec_share_pct` is more appropriate here since energy intensity is also an economy-wide metric.

### Chart 12 — How has the distribution of international clean energy financial flows to developing countries changed over 20 years?
- **Type:** Stacked Bar Chart (Matplotlib, x = year, stacked by continent)
- **Columns:** `year`, `financial_flows_usd`, `continent` — summed per continent per year, **2000–2019 only**
- **Notes:** Requires continent column. Only developing countries have data (~94 countries in a good year); state explicitly that high-income donor nations are excluded by design. Exclude 2020 (1 country only).

### Chart 13 — In 2020, is renewable electricity capacity per capita positively correlated with renewable electricity share?
- **Type:** Scatter Plot + Regression Line (Seaborn `regplot`)
- **Columns:** `renew_elec_cap_per_capita` (x), `renew_elec_share_pct` (y, derived column), **year = 2020**
- **Notes:** Using derived `renew_elec_share_pct` (electricity-only share, 173/176 in 2020) rather than `renew_energy_share_pct` (1/176 in 2020). `renew_elec_cap_per_capita` has 130 countries in 2020 — sufficient. Both measure electricity specifically, so the comparison is conceptually consistent.

---

## Part 3 — Carbon Emissions (7 charts)

### Chart 14 — How has the geographic distribution of total CO₂ emissions changed from 2000 to 2019?
- **Type:** Animated Choropleth Map (Plotly)
- **Columns:** `country`, `year`, `co2_emissions_kt`, **years 2000–2019** (2020 has 0 countries)
- **Notes:** Use **log scale** on the colour axis — China and the US are so dominant on a linear scale that most other countries appear near-zero. 2019 is the last complete year.
- **Web:** ✅ Plotly map — satisfies second Plotly interactive chart requirement.

### Chart 15 — Which 15 countries had the highest total CO₂ emissions in 2019?
- **Type:** Horizontal Bar Chart (Matplotlib)
- **Columns:** `country`, `co2_emissions_kt`, **year = 2019** (2020 unavailable)
- **Notes:** Label the chart "2019" explicitly. 159 countries have 2019 data. Annotate bars with values in Mt (= kt / 1000) for readability.
- **Web:** ✅ Also a candidate for **Datawrapper** if chart 2 is chosen for Plotly instead.

### Chart 16 — In 2019, does a larger economy mean more CO₂ emissions?
- **Type:** Scatter Plot + Regression Line (Seaborn `regplot`)
- **Columns:** `gdp_per_capita` (x), `co2_emissions_kt` (y, total emissions), `continent` (color), **year = 2019**
- **Notes:** `gdp_per_capita` (per capita) vs `co2_emissions_kt` (total) mixes scales, but this is intentional — the question is whether richer countries in per-capita terms also emit more in total. Acknowledge the unit mix in the caption. Alternative framing: x = `gdp_per_capita`, y = estimated CO₂ per capita (see notes on population proxy above) — cleaner but requires the proxy caveat.

### Chart 17 — In 2019, does higher GDP per capita mean higher energy consumption per capita?
- **Type:** Scatter Plot + Regression Line (Seaborn `regplot`)
- **Columns:** `gdp_per_capita` (x), `primary_energy_per_capita` (y), `continent` (color), **year = 2019**
- **Notes:** Both columns use per-capita measures — consistent and clean. 2019 has 161 countries for GDP and 175 for energy. Strong positive correlation expected; Gulf states and Nordic countries are interesting outliers.

### Chart 18 — How has per-capita CO₂ by continent evolved over 20 years? Which continents have reduced emissions?
- **Type:** Line Chart (Matplotlib, one line per continent)
- **Columns:** `year`, estimated CO₂ per capita (`co2_emissions_kt × 1000 / (pop_density × land_area_km2)`), `continent` — mean per continent, **2000–2019**
- **Notes:** Requires continent column. Population estimate is static across years (pop_density does not vary by year in this dataset) — this means per-capita trends directly mirror total CO₂ trends. State this limitation. Europe's declining trend and Asia's rise are the key stories.

### Chart 19 — Do countries with higher renewable energy share have lower per-capita CO₂ emissions? Does the green transition reduce emissions?
- **Type:** Scatter Plot + Regression Line (Seaborn `regplot`)
- **Columns:** `renew_energy_share_pct` (x), estimated CO₂ per capita (y), `continent` (color), **year = 2019**
- **Notes:** 2019 has 174 countries for `renew_energy_share_pct` and 159 for `co2_emissions_kt`. Expected negative correlation. Note that correlation ≠ causation — controlling for development level would be needed for causal claims.

### Chart 20 — In 2019, what is the overall pattern between per-capita energy consumption, per-capita GDP, and per-capita CO₂?
- **Type:** Bubble Chart (Plotly, interactive)
- **Columns:** `gdp_per_capita` (x), estimated CO₂ per capita (y), `primary_energy_per_capita` (bubble size), `continent` (color), `country` (hover label), **year = 2019**
- **Notes:** Requires continent column. Uses 2019 for CO₂. Using estimated per-capita CO₂ on y (with pop proxy caveat) keeps all three axes per-capita and comparable. Rich/high-energy/high-CO₂ countries cluster top-right; clean-energy outliers (France, Switzerland) visible.
- **Web:** ✅ Interactive Plotly — strong web piece, satisfies Plotly requirement.

---

## Web presentation chart selection

| Requirement | Chart(s) |
|---|---|
| ≥ 4 Matplotlib/Seaborn | Charts 3, 5, 7, 9, 11, 15, 17, 19 (pick 4+) |
| ≥ 2 Plotly (interactive) | Charts 1, 14, 20 (pick 2+) |
| ≥ 1 Plotly map | Charts 1 and/or 14 |
| ≥ 1 Datawrapper | Chart 2 (two-line global trend) — export aggregated CSV, recreate in Datawrapper |

**Datawrapper workflow for Chart 2:**
1. In notebook: `df.groupby('year')[['electricity_access_pct','clean_fuels_pct']].mean().to_csv('chart2_datawrapper.csv')`
2. Upload to Datawrapper → Line chart → publish → embed iframe in web page
