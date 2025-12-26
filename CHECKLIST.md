# ✅ Checklist de Uso - PixGo Python Client

Use este checklist para garantir que você configurou e está usando o pacote corretamente.

## 📦 Instalação

- [ ] Python 3.7+ instalado
  ```bash
  python --version
  ```

- [ ] Pacote instalado
  ```bash
  pip install -e .
  ```

- [ ] Teste de instalação executado
  ```bash
  python test_install.py
  ```

- [ ] Dependências instaladas corretamente
  ```bash
  pip list | grep requests
  ```

## 🔑 Configuração

- [ ] Conta criada no [PixGo.org](https://pixgo.org)

- [ ] Email confirmado

- [ ] Carteira Liquid validada

- [ ] API Key gerada (formato: `pk_...`)

- [ ] API Key guardada em local seguro

- [ ] Variável de ambiente configurada (opcional)
  ```bash
  # Linux/Mac
  export PIXGO_API_KEY=pk_sua_chave
  
  # Windows PowerShell
  $env:PIXGO_API_KEY="pk_sua_chave"
  ```

- [ ] Arquivo `.env` configurado (opcional)
  ```bash
  cp .env.example .env
  # Edite .env com sua API key
  ```

## 🧪 Testes Básicos

- [ ] Importação funciona
  ```python
  from pixgo import PixGoClient
  ```

- [ ] Cliente inicializa
  ```python
  client = PixGoClient(api_key="pk_sua_chave")
  ```

- [ ] Pagamento de teste criado
  ```python
  payment = client.create_payment(amount=10.00, description="Teste")
  print(payment.payment_id)
  ```

- [ ] Status consultado
  ```python
  status = client.get_payment_status(payment.payment_id)
  print(status)
  ```

## 📚 Documentação

- [ ] Li o [QUICKSTART.md](QUICKSTART.md)

- [ ] Li o [API_KEY.md](API_KEY.md)

- [ ] Consultei o [README.md](README.md)

- [ ] Vi o [INDICE.md](INDICE.md) para referência

## 💡 Exemplos

- [ ] Executei `exemplo_basico.py`
  ```bash
  python examples/exemplo_basico.py
  ```

- [ ] Entendi os conceitos básicos

- [ ] Testei criar pagamento próprio

- [ ] Testei consultar status

## 🎯 Uso Básico

### Criar Pagamento

- [ ] Sei criar pagamento simples
  ```python
  payment = client.create_payment(amount=25.50)
  ```

- [ ] Sei adicionar dados do cliente
  ```python
  payment = client.create_payment(
      amount=25.50,
      customer_name="João Silva",
      customer_cpf="12345678901",
      customer_email="joao@exemplo.com"
  )
  ```

- [ ] Sei adicionar external_id
  ```python
  payment = client.create_payment(
      amount=25.50,
      external_id="meu_pedido_123"
  )
  ```

### Consultar Pagamento

- [ ] Sei consultar apenas status
  ```python
  status = client.get_payment_status(payment_id)
  ```

- [ ] Sei obter detalhes completos
  ```python
  payment = client.get_payment(payment_id)
  ```

- [ ] Sei verificar se foi pago
  ```python
  if client.check_payment(payment_id):
      print("Pago!")
  ```

### Tratar Erros

- [ ] Sei capturar erros de validação
  ```python
  try:
      payment = client.create_payment(amount=5.00)
  except PixGoValidationError as e:
      print(f"Erro: {e}")
  ```

- [ ] Sei tratar erro de autenticação
  ```python
  except PixGoAuthenticationError:
      print("API key inválida")
  ```

- [ ] Sei tratar erro de API
  ```python
  except PixGoAPIError as e:
      print(f"Erro da API: {e.error_code}")
  ```

## 🔔 Webhooks (Opcional)

- [ ] Entendo o conceito de webhooks

- [ ] Vi o exemplo `exemplo_webhook.py`

- [ ] Sei configurar webhook_url
  ```python
  payment = client.create_payment(
      amount=25.50,
      webhook_url="https://meusite.com/webhook"
  )
  ```

- [ ] Tenho endpoint para receber webhooks

- [ ] Endpoint responde com HTTP 200

- [ ] Valido webhooks recebidos com a API

## 🚀 Produção

### Segurança

- [ ] API key em variável de ambiente

- [ ] API key NÃO está no código

- [ ] API key NÃO está no Git

- [ ] Uso HTTPS para webhooks

### Validação

- [ ] Valido valores antes de criar pagamento

- [ ] Valido CPF/CNPJ se necessário

- [ ] Trato todos os erros possíveis

- [ ] Revalido webhooks com a API

### Monitoramento

- [ ] Tenho logs de pagamentos criados

- [ ] Tenho logs de webhooks recebidos

- [ ] Monitoro erros de API

- [ ] Respeito rate limits

### Boas Práticas

- [ ] Uso context manager quando possível
  ```python
  with PixGoClient(api_key="...") as client:
      payment = client.create_payment(...)
  ```

- [ ] Fecho conexões manualmente se não usar context manager
  ```python
  client.close()
  ```

- [ ] Uso external_id para rastrear pedidos

- [ ] Aguardo confirmação antes de liberar produto

## 📊 Limites e Restrições

- [ ] Sei que valor mínimo é R$ 10.00

- [ ] Sei que QR Code expira em 20 minutos

- [ ] Sei meu nível atual e limite por pagamento

- [ ] Sei que consulta de status tem rate limit (1000/24h)

- [ ] Sei usar webhooks para evitar consultas excessivas

## 🎓 Conhecimento Avançado (Opcional)

- [ ] Li o código fonte em `pixgo/`

- [ ] Entendo os modelos de dados

- [ ] Sei criar testes para minha aplicação

- [ ] Executei os testes unitários
  ```bash
  pytest
  ```

- [ ] Li o [CONTRIBUTING.md](CONTRIBUTING.md)

- [ ] Li o [ESTRUTURA.md](ESTRUTURA.md)

## 💼 Casos de Uso

Marque os casos de uso que você implementou:

- [ ] **E-commerce**: Sistema de vendas online

- [ ] **Doações**: Sistema de doações

- [ ] **Assinaturas**: Sistema de recorrência (manual)

- [ ] **Eventos**: Venda de ingressos

- [ ] **Serviços**: Pagamento de serviços

- [ ] **Marketplace**: Plataforma com múltiplos vendedores

- [ ] **SaaS**: Software as a Service

- [ ] **Outros**: ___________________________

## 🐛 Troubleshooting

Se tiver problemas, verifique:

- [ ] API key está correta e completa

- [ ] Carteira Liquid está validada

- [ ] Valor é >= R$ 10.00

- [ ] Não excedi meu limite atual

- [ ] Conexão com internet está OK

- [ ] Consultei os logs de erro

- [ ] Li a seção de erros no README

## 📞 Quando Buscar Ajuda

Busque suporte se:

- [ ] Seguiu todos os passos e ainda tem erro

- [ ] Erro persiste após verificar documentação

- [ ] Encontrou um bug

- [ ] Tem sugestão de melhoria

### Canais de Suporte

- 📖 Documentação: [README.md](README.md)
- 📧 Email: contato@pixgo.org
- 💬 Telegram: Grupo no dashboard
- 🌐 Docs API: https://pixgo.org/api/v1/docs

## ✅ Conclusão

Quando completar todos os itens relevantes deste checklist, você estará pronto para usar o PixGo Python Client em produção! 🎉

---

**Data de Conclusão**: ___/___/______

**Ambiente**: [ ] Desenvolvimento  [ ] Homologação  [ ] Produção

**Notas**: 
_____________________________________________
_____________________________________________
_____________________________________________
