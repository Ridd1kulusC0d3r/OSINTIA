# Critérios de curadoria

OSINTia é um catálogo de fontes e links para investigação com IA. Não executa investigações nem instala automaticamente os projetos listados.

## Escopo

- Núcleo: MCPs, skills e agentes explicitamente aplicáveis à investigação, CTI, pesquisa pública e análise de evidências.
- Apoio: navegação, extração e preservação que podem compor um fluxo OSINT com IA.
- Índices: fontes para descobrir novos projetos, contabilizadas separadamente.

Cada repositório aparece uma única vez, mesmo quando combina MCP, skill e agente. A categoria representa seu uso principal nesta curadoria. Implementações diferentes do mesmo serviço são alternativas, não fontes independentes de confirmação.

## O que significa verificado

`documentation-retrieved`: o README primário foi recuperado por HTTP, seu conteúdo foi inspecionado para caracterização e o catálogo registra URL, horário e hash SHA-256 do documento recuperado. Isso confirma acesso à documentação naquele instante, não segurança, manutenção, qualidade ou funcionamento.

`runtime_tested: false`: nenhuma ferramenta do catálogo foi instalada ou executada nesta edição. Não houve benchmark, auditoria de dependências ou comprovação de todas as alegações dos mantenedores. A data não é selo de atualização do código. Branches são mutáveis; o hash permite identificar o conteúdo recuperado, mas não disponibiliza uma cópia histórica.

## Requisitos para inclusão

1. Repositório público e documentação primária acessível.
2. Aplicação concreta em uma etapa de pesquisa ou investigação com IA.
3. Descrição objetiva em português e ressalva específica.
4. Sem duplicação de URLs, forks sem diferenciação ou contagem de cada skill interna como projeto distinto.
5. Custo desconhecido permanece desconhecido. Código público não significa API gratuita ou autorização de reutilização.

## Custos e licenças

Os campos de ressalva apontam dependências conhecidas. Os planos comerciais não foram auditados individualmente. Consulte os termos atuais do provedor e a licença de cada projeto antes de implantação, redistribuição ou uso comercial. Esta lista não atribui uma licença aos projetos de terceiros.

## Comparar projetos de verdade

Use casos sintéticos ou dados próprios com resposta conhecida. Registre versão, configuração, fonte, horário, custo e entradas. Meça:

| Métrica | Pergunta |
|---|---|
| Precisão de entidades | Quantas associações são corretas? |
| Cobertura | Quantos itens conhecidos foram recuperados? |
| Proveniência | Cada alegação aponta para trecho e fonte recuperáveis? |
| Independência | As confirmações são independentes ou cópias da mesma notícia? |
| Temporalidade | O achado é atual, histórico ou sem data? |
| Calibração | A confiança declarada acompanha a taxa real de acerto? |
| Reprodutibilidade | Outra execução permite reconstruir o resultado? |
| Custo | Quanto se gasta por achado útil e verificado? |

Um HTTP 200, uma estrela, um hash ou uma citação isolada não comprovam a verdade de uma alegação.

## Descoberta e atribuição

Os índices [Awesome OSINT MCP Servers](https://github.com/soxoj/awesome-osint-mcp-servers) e [Awesome OSINT Repositories / Agentic](https://github.com/osintshifu/awesome-osint-repos/blob/main/AGENTIC.md), além de buscas web, ajudaram a descobrir candidatos. As descrições do OSINTia foram redigidas para esta curadoria; a referência de cada entrada é a documentação primária do próprio projeto, disponível no JSON e CSV.
