import json

with open('DV.ipynb') as f:
    nb = json.load(f)

UPDATES = {
    '27u7i1nbli1': [
        '### Section 2.0 — Correlation Overview (2019 cross-section)\n',
        '\n',
        'Before diving into the three themes, a Pearson correlation heatmap across 10 key numeric variables gives a sense of which relationships are strong and which are weak. The 2019 cross-section is used because it has the best coverage across the columns of interest.\n',
        '\n',
        'Dark red (r close to +1) means a strong positive relationship; dark blue (r close to −1) means a strong negative one; near-white means little to no linear link. The upper triangle is hidden — it is a mirror image of the lower.\n',
        '\n',
        'A few patterns stand out immediately. GDP per capita moves closely with both energy consumption per capita and CO₂ per capita, and more modestly with electricity and clean-fuel access — wealthier countries tend to use more energy and emit more. Electricity access and clean-fuel access track each other reasonably well, but the relationship is far from perfect, which is the core story in Part 1. Renewable share shows a mild negative link with energy intensity, suggesting — but not proving — that cleaner energy systems tend to be somewhat more efficient. These broad signals motivate the specific charts that follow.',
    ],

    'zvp49i5jo9j': [
        '### Part 1 — Energy Equity\n',
        '\n',
        '**Chart 1 — How has the geographic distribution of electricity access changed globally from 2000 to 2020?**\n',
        '\n',
        'An animated choropleth maps `electricity_access_pct` for all 176 countries across 21 years, making the spatial pattern and its change over time immediately visible. By 2020, most of Europe, the Americas, and East Asia sit at or near universal access, while large parts of sub-Saharan Africa remain well below 50%.',
    ],

    'bjn3vtcdc18': [
        '**Chart 2 — Have global average electricity access and clean cooking fuel access risen in tandem over 20 years?**\n',
        '\n',
        'Both metrics improved over the period, but at very different rates. Electricity access climbed steadily and pulled well ahead; clean cooking fuel access lagged behind and the gap between the two widened rather than closed — meaning that gaining a power connection did not reliably translate into gaining access to clean fuels for cooking. The shaded area between the two lines makes this divergence visible at a glance. The aggregated data is also exported as a CSV for the Datawrapper version of this chart.',
    ],

    'lu78ctbk92t': [
        '**Chart 5 — Has within-continent variation in electricity access narrowed as mean access improved?**\n',
        '\n',
        'Four snapshot years (2000, 2007, 2014, 2020) are shown as grouped box plots, one group per continent. When the boxes shrink over time, it means the gap between the best- and worst-served countries in that region is closing — countries that once lagged are catching up with their regional neighbours. When the boxes stay wide, the region is still deeply divided internally despite any improvement in the average.',
    ],

    'd5w0m2hvb04': [
        '**Chart 6 — In 2020, where are the 20 countries with the lowest electricity access, and what do they have in common?**\n',
        '\n',
        'All 20 sit in sub-Saharan Africa. The bubble chart places each country by GDP per capita (x) and electricity access rate (y), with bubble size encoding population density. The tight clustering near the bottom-left — low income, low access — makes the pattern hard to miss: across this group, poverty and lack of electricity go hand in hand, and higher population density does not appear to help.',
    ],

    'c21c25392d': [
        '**Chart 8 — How does the 2020 electricity mix differ by continent? Who is most fossil-dependent?**\n',
        '\n',
        'Each bar shows one continent\'s total 2020 generation normalised to 100%. Asia is the most fossil-heavy, with coal and gas making up the large majority of its output. Europe stands out for its nuclear share. Africa benefits from significant hydropower. The Americas figure spans a wide internal range — fossil-heavy North America on one end and hydro-rich South America on the other — which is why the continent sits in the middle of the fossil ranking rather than near either extreme.',
    ],

    'f9a7d90ece': [
        '**Chart 10 — How has energy intensity changed by continent from 2000 to 2019? Is efficiency improving?**\n',
        '\n',
        'Energy intensity (MJ per dollar of PPP GDP) falls as economies produce more output per unit of energy, whether through technological improvements or a shift away from heavy industry. 2020 is excluded (near-complete data gap for this column). Asia\'s decline is the steepest — a combination of rapid industrial modernisation and a growing services sector. Africa\'s intensity remains the highest of any continent, partly because many of its economies are concentrated in energy-intensive primary industries and partly because lower PPP GDP figures mechanically push the ratio up.',
    ],

    '618be5fbef': [
        '**Chart 11 — Does higher renewable energy share correlate with lower energy intensity in 2019?**\n',
        '\n',
        'Economy-wide renewable share (`renew_energy_share_pct`) is used rather than the electricity-only share, because energy intensity covers the full economy — transport, heating, and industry — not just electricity. Pairing two economy-wide metrics keeps the comparison on the same footing. A mild negative correlation is expected: countries deriving more of their total energy from renewables tend to use somewhat less energy per dollar of output, though development level and industrial structure also play a large role.',
    ],

    '0dfa0dafdd': [
        '**Chart 12 — How have international clean energy financial flows to developing countries changed over 20 years?**\n',
        '\n',
        'The chart stacks annual totals by recipient continent (2000–2019; 2020 excluded due to near-complete data absence). `financial_flows_usd` records inflows to developing countries only — high-income donor nations show no value for this column by design. Asia receives the largest cumulative flows, with Africa growing as a share from the mid-2010s onward. Total flows roughly tripled over the two decades, though they remain concentrated in a handful of large recipient countries.',
    ],

    '144dfc97e3': [
        '**Chart 17 — In 2019, does higher GDP per capita mean higher primary energy consumption per capita?**\n',
        '\n',
        'Both axes are per-capita and use 2019 data. The positive relationship is clear and spans a wide range — from countries consuming under 20 GJ per person to Gulf states consuming over 300 GJ. That said, the relationship is not deterministic: France and the UK sit noticeably below the regression line for their income level, while Iceland, Qatar, and the UAE sit far above it. Industry structure, climate, and energy prices all pull countries away from the central trend.',
    ],
}

updated = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown' and cell.get('id') in UPDATES:
        cell['source'] = UPDATES[cell['id']]
        updated += 1

print(f'Updated {updated} cells')

with open('DV.ipynb', 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Done.')
