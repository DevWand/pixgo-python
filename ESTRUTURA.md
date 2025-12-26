# 📦 Estrutura do Pacote PixGo Python

## Visão Geral

```
PacotePixGo/
│
├── 📁 pixgo/                      # Código principal do pacote
│   ├── __init__.py               # Exports e versão
│   ├── client.py                 # Cliente da API
│   ├── models.py                 # Modelos (Payment, PaymentStatus, etc)
│   └── exceptions.py             # Exceções personalizadas
│
├── 📁 examples/                   # Exemplos de uso
│   ├── exemplo_basico.py         # Uso básico da API
│   ├── exemplo_webhook.py        # Servidor Flask com webhooks
│   ├── exemplo_ecommerce.py      # Sistema e-commerce completo
│   └── exemplo_env.py            # Uso com variáveis de ambiente
│
├── 📁 tests/                      # Testes unitários
│   ├── __init__.py               
│   └── test_client.py            # Testes do cliente
│
├── 📄 README.md                   # Documentação principal ⭐
├── 📄 QUICKSTART.md              # Guia de início rápido
├── 📄 INSTALL.md                 # Guia de instalação
├── 📄 CONTRIBUTING.md            # Guia de contribuição
├── 📄 CHANGELOG.md               # Histórico de mudanças
│
├── 📄 setup.py                   # Configuração de instalação (setup tradicional)
├── 📄 pyproject.toml             # Configuração moderna (PEP 518)
├── 📄 requirements.txt           # Dependências
├── 📄 MANIFEST.in                # Arquivos incluídos na distribuição
│
├── 📄 LICENSE                    # Licença MIT
├── 📄 .gitignore                 # Arquivos ignorados pelo Git
├── 📄 .env.example               # Exemplo de configuração
│
└── 📄 test_install.py            # Script para testar instalação
```

## Componentes Principais

### 1. Core (`pixgo/`)

#### `client.py`
- **PixGoClient**: Cliente principal da API
- Métodos:
  - `create_payment()`: Criar pagamento
  - `get_payment_status()`: Consultar status
  - `get_payment()`: Detalhes completos
  - `check_payment()`: Verificar se foi pago

#### `models.py`
- **Payment**: Modelo de pagamento
- **PaymentStatus**: Enum de status
- **WebhookEvent**: Evento de webhook

#### `exceptions.py`
- **PixGoException**: Base
- **PixGoAPIError**: Erros da API
- **PixGoValidationError**: Validação
- **PixGoAuthenticationError**: Autenticação
- **PixGoRateLimitError**: Rate limit

### 2. Exemplos (`examples/`)

| Arquivo | Descrição |
|---------|-----------|
| `exemplo_basico.py` | Uso básico de todas as funcionalidades |
| `exemplo_webhook.py` | Servidor Flask completo com webhooks |
| `exemplo_ecommerce.py` | Sistema e-commerce com fluxo completo |
| `exemplo_env.py` | Configuração via variáveis de ambiente |

### 3. Testes (`tests/`)

- Testes unitários com pytest
- Mocks para não fazer chamadas reais
- Cobertura de código

### 4. Documentação

| Arquivo | Propósito |
|---------|-----------|
| `README.md` | Documentação completa com exemplos |
| `QUICKSTART.md` | Guia de 5 minutos |
| `INSTALL.md` | Instruções de instalação detalhadas |
| `CONTRIBUTING.md` | Como contribuir |
| `CHANGELOG.md` | Histórico de versões |

### 5. Configuração

| Arquivo | Propósito |
|---------|-----------|
| `setup.py` | Instalação tradicional (setuptools) |
| `pyproject.toml` | Configuração moderna (PEP 518) |
| `requirements.txt` | Dependências de produção |
| `MANIFEST.in` | Arquivos extras na distribuição |

## Dependências

### Produção
- **requests** (>=2.25.0): Cliente HTTP

### Desenvolvimento
- **pytest** (>=7.0.0): Testes
- **pytest-cov** (>=3.0.0): Cobertura
- **black** (>=22.0.0): Formatação
- **flake8** (>=4.0.0): Linting
- **mypy** (>=0.950): Type checking

## Comandos Úteis

### Instalação
```bash
# Produção
pip install -e .

# Desenvolvimento
pip install -e ".[dev]"
```

### Testes
```bash
# Executar testes
pytest

# Com cobertura
pytest --cov=pixgo --cov-report=html
```

### Qualidade de Código
```bash
# Formatação
black pixgo/

# Linting
flake8 pixgo/

# Type checking
mypy pixgo/
```

### Execução
```bash
# Testar instalação
python test_install.py

# Exemplos
python examples/exemplo_basico.py
python examples/exemplo_ecommerce.py
python examples/exemplo_webhook.py  # requer Flask
```

### Publicação (PyPI)
```bash
# Build
python -m build

# Upload
python -m twine upload dist/*
```

## Recursos Implementados

### ✅ Funcionalidades
- [x] Criação de pagamentos PIX
- [x] Consulta de status
- [x] Detalhes completos de pagamentos
- [x] Suporte a webhooks
- [x] Validação de dados
- [x] Tratamento de erros robusto
- [x] Context manager
- [x] Type hints completo

### ✅ Qualidade
- [x] Testes unitários
- [x] Documentação completa
- [x] Exemplos práticos
- [x] Code style (PEP 8)
- [x] Tratamento de exceções
- [x] Logs e debug

### ✅ Infraestrutura
- [x] Setup moderno (pyproject.toml)
- [x] Setup tradicional (setup.py)
- [x] CI/CD ready
- [x] Git configurado
- [x] Licença MIT

## Próximos Passos

1. **Testar**: `python test_install.py`
2. **Documentar**: Adicionar sua API key
3. **Executar**: Testar exemplos
4. **Publicar**: Fazer upload para PyPI (opcional)

## Suporte

- 📖 Documentação: [README.md](README.md)
- 🌐 API Docs: https://pixgo.org/api/v1/docs
- 📧 Email: contato@pixgo.org
- 💬 Telegram: Disponível no dashboard

## Licença

MIT License - Veja [LICENSE](LICENSE)

---

**Pacote pronto para uso e distribuição! 🎉**
