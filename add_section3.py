import json, uuid

with open('DV.ipynb') as f:
    nb = json.load(f)

def M(src):
    return {'cell_type': 'markdown', 'id': uuid.uuid4().hex[:10], 'metadata': {}, 'source': src}

cells = [
    M([
        '---\n',
        '## Section 3 — Conclusion\n',
    ]),
    M([
        '### 3.1 Key Findings\n',
        '\n',
        'Twenty charts across three themes surface a consistent set of patterns in the data.\n',
        '\n',
        '**Energy equity.** Electricity access improved across all continents from 2000 to 2020, but the gains were uneven. Sub-Saharan Africa made the largest absolute progress yet still contains every country in the bottom-20 access ranking by 2020. Critically, electricity access and clean cooking fuel access did not converge — the gap between the two global averages widened over the period, meaning electrification alone has not translated into broader household energy access.\n',
        '\n',
        '**Energy structure.** The global electricity mix shifted noticeably toward renewables after about 2010, driven largely by solar and wind expansion, but fossil fuels still accounted for the majority of generation in 2020. Asia remains the most fossil-dependent region; Europe holds the highest nuclear share; hydro-dominated nations in Africa and South America punch above their weight on renewable share despite modest absolute capacity. Energy intensity fell across all continents, most sharply in Asia, though the rate of improvement varies widely by region and industrial structure.\n',
        '\n',
        '**Carbon emissions.** CO₂ emissions are heavily concentrated — the top 3 emitters in 2019 (China, the US, India) together exceeded all other countries combined. Europe showed a clear declining trend over the two decades while Asia rose sharply through the early 2010s before plateauing. Across countries, GDP per capita, energy consumption per capita, and CO₂ per capita move together strongly, but notable outliers (France, Switzerland, Sweden) demonstrate that high income does not necessarily require high emissions.',
    ]),
]

nb['cells'].extend(cells)

with open('DV.ipynb', 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f'Added {len(cells)} cells. Total cells: {len(nb["cells"])}')
