"""Valida integridade, unicidade, referências locais e sincronização. Sem rede."""
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from build_catalog import CATEGORIES, ROOT, render

data = json.loads((ROOT / 'data/sources.json').read_text())
assert len(data) >= 60, 'Escopo mínimo desta edição: 60 repositórios'
assert len({x['url'].lower().rstrip('/') for x in data}) == len(data), 'URL duplicada'
assert len({x['repository'].lower() for x in data}) == len(data), 'Repositório duplicado'
for x in data:
    assert x['category'] in CATEGORIES
    assert x['url'] == 'https://github.com/' + x['repository']
    assert x['http_status'] == 200
    assert re.fullmatch('[0-9a-f]{64}', x['readme_sha256'])
    assert x['source_url'].startswith('https://raw.githubusercontent.com/')
    assert x['validation'] == 'documentation-retrieved'
    assert isinstance(x['runtime_tested'], bool)
    assert datetime.fromisoformat(x['checked_at']).tzinfo
    assert x['description'] and x['caveat']
readme = (ROOT / 'README.md').read_text()
generated = readme.split('<!-- CATALOG:START -->')[1].split('<!-- CATALOG:END -->')[0].strip()
assert generated == render(data).strip(), 'README fora de sincronia'
with (ROOT / 'data/sources.csv').open() as f:
    csv_rows = list(csv.DictReader(f))
assert csv_rows == [{k: str(v) for k, v in row.items()} for row in data], 'CSV fora de sincronia'
for path in ROOT.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if '://' not in target and not target.startswith('#'):
            assert (path.parent / target.split('#')[0]).exists(), (path, target)
print(f'OK: {len(data)} fontes únicas; JSON, CSV, README e referências locais consistentes.')
