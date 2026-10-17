# Contribua com o OSINTia

Proponha um projeto com URL primária, categoria, aplicação concreta em OSINT com IA, dependências conhecidas e uma limitação verificável. Explique como difere das entradas existentes.

Não inclua forks sem diferenciação, slogans de marketing, contagens de ferramentas como prova de qualidade ou alegações de funcionamento sem teste reproduzível. Não publique chaves, dados pessoais de casos reais ou conteúdo de acesso restrito.

1. Edite `data/sources.json` e preserve o esquema das entradas existentes.
2. Registre a fonte primária e o nível de verificação real; não reutilize datas de uma consulta antiga.
3. Execute `python scripts/build_catalog.py` para atualizar o catálogo e o CSV.
4. Execute `python scripts/validate_catalog.py`.
5. Envie a alteração com a justificativa e evidências de verificação.

O README contém uma seção gerada entre marcadores. Edite a fonte JSON para evitar divergências.
