# 🔑 Como Obter sua API Key do PixGo

## Passo a Passo

### 1. Criar Conta

1. Acesse [https://pixgo.org](https://pixgo.org)
2. Clique em "Criar Conta" ou "Sign Up"
3. Preencha seus dados:
   - Nome
   - Email
   - Senha
4. Confirme seu email

### 2. Validar Carteira Liquid

Antes de usar a API, você precisa validar sua carteira Liquid:

1. Faça login no [PixGo](https://pixgo.org)
2. Acesse seu perfil/configurações
3. Adicione suas informações de carteira Liquid
4. Aguarde a validação

> ⚠️ **Importante**: Sem validação da carteira Liquid, você não poderá usar a API.

### 3. Gerar API Key

1. No dashboard do PixGo, vá para:
   - **Menu** → **Checkouts** → **API**

2. Clique em "Gerar API Key" ou "Generate API Key"

3. Sua chave será gerada no formato:
   ```
   pk_1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
   ```

4. **COPIE E GUARDE EM LOCAL SEGURO**
   - Você não poderá ver a chave completa novamente
   - Se perder, terá que gerar uma nova

### 4. Configurar no Código

#### Opção 1: Diretamente no código

```python
from pixgo import PixGoClient

client = PixGoClient(api_key="pk_sua_chave_aqui")
```

#### Opção 2: Variável de ambiente

**Linux/Mac:**
```bash
export PIXGO_API_KEY=pk_sua_chave_aqui
```

**Windows (PowerShell):**
```powershell
$env:PIXGO_API_KEY="pk_sua_chave_aqui"
```

**No código:**
```python
import os
from pixgo import PixGoClient

api_key = os.getenv('PIXGO_API_KEY')
client = PixGoClient(api_key=api_key)
```

#### Opção 3: Arquivo .env

**Arquivo `.env`:**
```env
PIXGO_API_KEY=pk_sua_chave_aqui
```

**No código (com python-dotenv):**
```python
from dotenv import load_dotenv
import os
from pixgo import PixGoClient

load_dotenv()
api_key = os.getenv('PIXGO_API_KEY')
client = PixGoClient(api_key=api_key)
```

## Segurança da API Key

### ✅ FAÇA

- ✅ Guarde em variáveis de ambiente
- ✅ Use arquivo `.env` (e adicione ao `.gitignore`)
- ✅ Use gerenciadores de segredos em produção
- ✅ Regenere a chave se suspeitar de comprometimento
- ✅ Use chaves diferentes para cada ambiente

### ❌ NÃO FAÇA

- ❌ **NUNCA** comite API keys no Git
- ❌ **NUNCA** compartilhe sua chave publicamente
- ❌ **NUNCA** exponha no código front-end
- ❌ **NUNCA** inclua em logs ou mensagens de erro
- ❌ **NUNCA** envie por email ou chat não criptografado

## Validar API Key

Teste se sua API key está funcionando:

```python
from pixgo import PixGoClient, PixGoAuthenticationError

try:
    client = PixGoClient(api_key="pk_sua_chave_aqui")
    
    # Tentar criar um pagamento de teste
    payment = client.create_payment(
        amount=10.00,
        description="Teste de validação"
    )
    
    print("✓ API Key válida!")
    print(f"Pagamento teste criado: {payment.payment_id}")
    
except PixGoAuthenticationError:
    print("✗ API Key inválida ou não autorizada")
    print("Verifique se:")
    print("1. A chave está correta")
    print("2. Sua carteira Liquid está validada")
    print("3. Você está usando a chave completa")
    
except Exception as e:
    print(f"✗ Erro: {e}")
```

## Sistema de Níveis

Sua conta começa no **Nível 1** com limite de **R$ 300,00 por QR Code**.

### Progressão de Níveis

| Nível | Total Confirmado | Limite por QR Code |
|-------|------------------|-------------------|
| 1 - Iniciante | R$ 0 - R$ 299,99 | R$ 300,00 |
| 2 - Bronze | R$ 300 - R$ 499,99 | R$ 500,00 |
| 3 - Prata | R$ 500 - R$ 999,99 | R$ 1.000,00 |
| 4 - Ouro | R$ 1.000 - R$ 2.999,99 | R$ 1.500,00 |
| 5 - Platina | R$ 3.000 - R$ 4.999,99 | R$ 2.000,00 |
| 6 - Diamante | R$ 5.000 - R$ 5.999,99 | R$ 2.500,00 |
| 7 - Elite | R$ 6.000+ | R$ 3.000,00 |

> 💡 **Dica**: Os níveis evoluem automaticamente conforme você recebe pagamentos confirmados.

## Limites da API

### Rate Limits

- **Criação de pagamentos**: Ilimitado
- **Consulta de status**: 1.000 requisições / 24 horas
- **Obter detalhes**: Ilimitado

### Outros Limites

- **Valor mínimo**: R$ 10,00 por pagamento
- **Limite por CPF/CNPJ do pagador**: R$ 6.000,00 / dia
- **Expiração de QR Code**: 20 minutos
- **QR Codes por dia**: Ilimitado

## Problemas Comuns

### Erro: "API key inválida"

**Causas possíveis:**
1. Chave incompleta ou com espaços
2. Chave não começa com `pk_`
3. Chave foi revogada

**Solução:**
- Copie a chave novamente do dashboard
- Verifique se não há espaços extras
- Gere uma nova chave se necessário

### Erro: "LIMIT_EXCEEDED"

**Causa:** Valor excede seu limite atual

**Solução:**
1. Verifique seu nível atual no dashboard
2. Aguarde evolução de nível
3. Ou reduza o valor do pagamento

### Erro: "Wallet not validated"

**Causa:** Carteira Liquid não validada

**Solução:**
1. Acesse seu perfil no PixGo
2. Complete a validação da carteira
3. Aguarde aprovação

## Suporte

Precisa de ajuda?

- 📧 **Email**: contato@pixgo.org
- 💬 **Telegram**: Grupo disponível no dashboard
- 📖 **Documentação**: https://pixgo.org/api/v1/docs
- 🌐 **Site**: https://pixgo.org

## Próximos Passos

Após obter sua API key:

1. ✅ Configure no seu código
2. ✅ Execute `python test_install.py`
3. ✅ Teste com os exemplos
4. ✅ Integre no seu sistema

Veja o [QUICKSTART.md](QUICKSTART.md) para começar rapidamente!

---

**Boa sorte com sua integração! 🚀**
