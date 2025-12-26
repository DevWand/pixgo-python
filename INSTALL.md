# Guia de Instalação e Uso - PixGo Python

## Instalação

### Via pip (quando publicado no PyPI)

```bash
pip install pixgo
```

### Instalação local para desenvolvimento

1. Clone ou extraia o pacote:
```bash
cd PacotePixGo
```

2. Instale em modo de desenvolvimento:
```bash
pip install -e .
```

3. Ou instale as dependências manualmente:
```bash
pip install -r requirements.txt
```

## Configuração Inicial

### 1. Obter API Key

1. Acesse [pixgo.org](https://pixgo.org) e crie sua conta
2. Valide suas informações de carteira Liquid
3. Vá para "Checkouts" > "API"
4. Gere sua API key (formato: `pk_...`)

### 2. Primeiro Uso

```python
from pixgo import PixGoClient

# Substitua pela sua API key
client = PixGoClient(api_key="pk_sua_chave_aqui")

# Criar um pagamento simples
payment = client.create_payment(
    amount=25.50,
    description="Meu primeiro pagamento"
)

print(f"QR Code: {payment.qr_code}")
print(f"URL: {payment.qr_image_url}")
```

## Executar os Exemplos

### Exemplo Básico
```bash
cd examples
python exemplo_basico.py
```

### Exemplo de E-commerce
```bash
python exemplo_ecommerce.py
```

### Exemplo com Flask (Webhooks)
```bash
# Instalar Flask primeiro
pip install flask

# Executar servidor
python exemplo_webhook.py
```

## Executar os Testes

```bash
# Instalar dependências de desenvolvimento
pip install -e ".[dev]"

# Executar testes
pytest

# Com cobertura
pytest --cov=pixgo --cov-report=html
```

## Publicar no PyPI (para mantenedores)

### 1. Preparar o pacote

```bash
# Limpar builds anteriores
rm -rf build dist *.egg-info

# Criar distribuições
python -m build
```

### 2. Publicar no Test PyPI (opcional)

```bash
python -m twine upload --repository testpypi dist/*
```

### 3. Publicar no PyPI

```bash
python -m twine upload dist/*
```

## Estrutura do Projeto

```
PacotePixGo/
├── pixgo/                  # Código do pacote
│   ├── __init__.py        # Exports principais
│   ├── client.py          # Cliente da API
│   ├── models.py          # Modelos de dados
│   └── exceptions.py      # Exceções personalizadas
│
├── examples/              # Exemplos de uso
│   ├── exemplo_basico.py
│   ├── exemplo_webhook.py
│   └── exemplo_ecommerce.py
│
├── tests/                 # Testes unitários
│   ├── __init__.py
│   └── test_client.py
│
├── README.md             # Documentação principal
├── CHANGELOG.md          # Histórico de mudanças
├── LICENSE               # Licença MIT
├── setup.py              # Configuração de instalação
├── pyproject.toml        # Configuração moderna
├── requirements.txt      # Dependências
├── .gitignore           # Arquivos ignorados pelo git
└── MANIFEST.in          # Arquivos incluídos na distribuição
```

## Dicas de Uso

### Use Context Manager

```python
# Fecha a conexão automaticamente
with PixGoClient(api_key="pk_...") as client:
    payment = client.create_payment(amount=10.00)
```

### Validar Pagamentos

```python
# Sempre valide pagamentos críticos
if client.check_payment(payment_id):
    # Liberar produto/serviço
    pass
```

### Webhooks em Produção

Use HTTPS e valide os dados recebidos:

```python
# Sempre revalidar com a API
payment = client.get_payment(webhook_data['payment_id'])
if payment.is_paid():
    # Processar pedido
    pass
```

## Troubleshooting

### Erro: "API key inválida"
- Verifique se a API key começa com `pk_`
- Confirme que copiou a chave completa

### Erro: "Valor mínimo é R$ 10.00"
- O valor mínimo por transação é R$ 10.00

### Erro: "Rate limit exceeded"
- Endpoint de status tem limite de 1.000 req/24h
- Reduza a frequência de consultas
- Use webhooks para notificações em tempo real

### Timeout
- Aumente o timeout: `PixGoClient(api_key="...", timeout=60)`

## Suporte

- Email: contato@pixgo.org
- Telegram: Grupo disponível no dashboard
- Documentação: https://pixgo.org/api/v1/docs
