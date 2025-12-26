# 🚀 Início Rápido - PixGo Python

## Instalação

```bash
pip install -e .
```

## Uso em 5 Minutos

### 1. Configure sua API Key

```python
from pixgo import PixGoClient

client = PixGoClient(api_key="pk_sua_chave_aqui")
```

### 2. Crie um Pagamento

```python
payment = client.create_payment(
    amount=25.50,
    description="Produto XYZ",
    customer_name="João Silva",
    customer_email="joao@exemplo.com"
)

print(f"QR Code: {payment.qr_image_url}")
```

### 3. Consulte o Status

```python
status = client.get_payment_status(payment.payment_id)

if status == PaymentStatus.COMPLETED:
    print("Pagamento confirmado! 🎉")
```

## Exemplos Prontos

Execute os exemplos incluídos:

```bash
# Exemplo básico
python examples/exemplo_basico.py

# E-commerce completo
python examples/exemplo_ecommerce.py

# Servidor Flask com webhooks
pip install flask
python examples/exemplo_webhook.py
```

## Testar Instalação

```bash
python test_install.py
```

## Documentação Completa

Veja [README.md](README.md) para documentação detalhada.

## Recursos da API

| Método | Descrição |
|--------|-----------|
| `create_payment()` | Cria novo pagamento PIX |
| `get_payment_status()` | Consulta status |
| `get_payment()` | Detalhes completos |
| `check_payment()` | Verifica se foi pago |

## Limites

- ✅ Valor mínimo: R$ 10,00
- ✅ Expiração: 20 minutos
- ✅ QR Codes ilimitados
- ⚠️ Rate limit (status): 1.000/24h

## Ajuda

- 📖 [Documentação Completa](README.md)
- 📖 [Guia de Instalação](INSTALL.md)
- 🌐 [API Docs](https://pixgo.org/api/v1/docs)
- 📧 contato@pixgo.org

---

**Pronto para começar! 🚀**
