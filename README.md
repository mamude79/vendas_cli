# vendas-cli

**vendas-cli**: Ferramenta de linha de comando para análise e relatórios de vendas.


## 🛠️ Instalação das Dependências com `uv`

O projeto utiliza [`uv`](https://github.com/astral-sh/uv) para gerenciar dependências:

```bash
# Sincronizar todas as dependências declaradas no pyproject.toml
uv sync
```

### Exemplos de como executar o projeto

```bash
python main.py --input produtos.csv --format text
```
```bash
python main.py --input produtos.csv --format json
```
```bash
python main.py --input produtos.csv --format text --start 2026-01-01 --end 2026-06-01
```

```bash
python main.py --input produtos.csv --format json --start 2026-01-01 --end 2026-06-01
```

## 🧪 Executar os Testes

Para rodar todos os testes unitários:

```bash
# Rodar todos os testes
uv run pytest
```

### Executar um teste específico

Para rodar apenas um módulo de teste:

```bash
uv run pytest tests/test_main.py::TestMain
```

## 📊 Gerar o Coverage em HTML

Para gerar o relatório de cobertura com visualização no navegador:

```bash
# Gerar o relatório e abrir automaticamente no navegador
uv run pytest --cov=. --cov-report=html
```

### Acessar o relatório manualmente

1. Execute o comando acima para gerar a cobertura
2. Abra o arquivo `coverage/html_report/index.html` em seu navegador
3. Navegue pelas abas "Class coverage" e "Function coverage" para ver os detalhes
4. Clique nos links azuis (classes, funções) para expandir e ver quais linhas estão cobertas ou não
5. Use a barra lateral de filtros à esquerda para focar em classes específicas
6. O relatório é atualizado automaticamente sempre que você roda `uv run pytest --cov=...
