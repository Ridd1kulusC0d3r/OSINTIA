"""Renderiza a seção do README e o CSV a partir do JSON, sem rede."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'skills': 'Skills e método investigativo',
    'mcp-osint': 'MCPs de OSINT e SOCMINT',
    'mcp-cti': 'MCPs de threat intelligence',
    'mcp-corporate': 'MCPs de empresas e registros públicos',
    'mcp-search': 'MCPs de busca e pesquisa documental',
    'agents': 'Agentes e workbenches',
    'support': 'Infraestrutura complementar',
    'directories': 'Índices para descobrir novas fontes',
}


def render(data):
    counts = Counter(x['category'] for x in data)
    core = sum(v for k, v in counts.items() if k not in ('support', 'directories'))
    out = [f'**{len(data)} repositórios únicos · {core} no núcleo · {counts["support"]} de apoio · {counts["directories"]} índices.**', '',
           'Contagem por repositório, sem multiplicar skills internas ou contar o mesmo projeto em várias categorias.', '',
           '| Categoria | Fontes |', '|---|---:|']
    out += [f'| [{name}](#{key}) | {counts[key]} |' for key, name in CATEGORIES.items()]
    out += ['', '> **Verificação documental em 17/10/2026. Nenhum projeto foi testado em execução nesta edição.** URLs e hashes das fontes estão no [JSON](data/sources.json) e no [CSV](data/sources.csv). Código público pode depender de serviços pagos; licenças e planos devem ser conferidos no projeto original.', '']
    for key, name in CATEGORIES.items():
        out += [f'<a id="{key}"></a>', '', f'## {name}', '', '| Projeto / fonte primária | Aplicação | Limitação ou dependência |', '|---|---|---|']
        for x in data:
            if x['category'] == key:
                out.append(f'| [{x["repository"]}]({x["url"]}) | {x["description"]} | {x["caveat"]} |')
        out += ['', '[↑ Voltar ao início](#osintia)', '']
    return '\n'.join(out)


def main():
    data = json.loads((ROOT / 'data/sources.json').read_text())
    path = ROOT / 'README.md'
    before, rest = path.read_text().split('<!-- CATALOG:START -->')
    _, after = rest.split('<!-- CATALOG:END -->')
    path.write_text(before + '<!-- CATALOG:START -->\n\n' + render(data) + '\n<!-- CATALOG:END -->' + after)
    with (ROOT / 'data/sources.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(data)
    print(f'Catálogo e CSV atualizados: {len(data)} fontes.')


if __name__ == '__main__':
    main()
