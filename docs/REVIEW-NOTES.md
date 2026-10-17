# Notas críticas de avaliação

## Projeto fora da seleção principal

[smixs/osint-skill](https://github.com/smixs/osint-skill) foi citado no levantamento inicial, mas não entra na contagem principal desta edição. Seu README consultado em 17/10/2026 reconhece shell injection com entradas não confiáveis e problemas de portabilidade. Também anuncia psicoperfis inferidos de conteúdo. Essas alegações não foram validadas e não devem ser tratadas como diagnóstico ou conclusão psicológica demonstrada.

Reavaliar após correções documentadas e inspeção do código relevante. Referência: seção Known Issues do README do próprio projeto.

## Alegações que não adotamos como garantias

- **OpenOSINT:** versões indexadas do README faziam uma afirmação excessiva sobre impossibilidade de alucinação. O README primário recuperado nesta edição já esclarece que resumos da IA são pistas a verificar, não prova. A curadoria usa essa formulação atual.
- **SYNINT:** a apresentação como API-free não elimina dependências de APIs em módulos opcionais.
- **Skills:** instruções antialucinação não demonstram, por si só, redução mensurada de alucinações.
- **MCP:** acesso padronizado não certifica o coletor nem o conteúdo consultado.
- **Agentes gerais de pesquisa:** úteis como infraestrutura, mas não chegam com validação OSINT universal.

## Antes de integrar

Inspecione comandos, instalação de dependências e permissões de escrita. Prefira versões fixadas e credenciais com escopo mínimo. Conteúdo coletado é dado não confiável: páginas, PDFs e resultados de busca não devem virar instruções de sistema do agente. Preserve o original e mantenha inferências separadas de observações.
