# Contribuindo para o PixGo Python Client

Obrigado por considerar contribuir para o PixGo Python Client! 

## Como Contribuir

### Reportar Bugs

Se você encontrou um bug, por favor:

1. Verifique se o bug já não foi reportado nas [Issues](https://github.com/DevWand/pixgo-python/issues)
2. Se não encontrou, crie uma nova issue com:
   - Título claro e descritivo
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Comportamento esperado vs comportamento atual
   - Versão do Python e do pacote
   - Código de exemplo (se possível)

### Sugerir Melhorias

Para sugerir uma nova funcionalidade ou melhoria:

1. Verifique se já não existe uma issue sobre isso
2. Crie uma nova issue descrevendo:
   - O que você gostaria de ver
   - Por que isso seria útil
   - Como você imagina que funcionaria

### Contribuir com Código

#### Setup do Ambiente

1. Fork o repositório
2. Clone seu fork:
```bash
git clone https://github.com/seu-usuario/pixgo-python.git
cd pixgo-python
```

3. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

4. Instale o pacote em modo de desenvolvimento:
```bash
pip install -e ".[dev]"
```

#### Fluxo de Trabalho

1. Crie uma branch para sua feature:
```bash
git checkout -b feature/minha-feature
```

2. Faça suas alterações seguindo as diretrizes de código

3. Adicione testes para suas alterações:
```bash
pytest tests/
```

4. Formate o código:
```bash
black pixgo/
```

5. Verifique o linting:
```bash
flake8 pixgo/
```

6. Commit suas alterações:
```bash
git commit -m "Adiciona funcionalidade X"
```

7. Push para seu fork:
```bash
git push origin feature/minha-feature
```

8. Abra um Pull Request

#### Diretrizes de Código

- **Python**: Siga a PEP 8
- **Docstrings**: Use docstrings em Google style
- **Type Hints**: Use type hints quando possível
- **Testes**: Adicione testes para novas funcionalidades
- **Commits**: Mensagens claras e descritivas em português

#### Estrutura de Docstring

```python
def funcao_exemplo(param1: str, param2: int) -> bool:
    """
    Breve descrição da função
    
    Descrição mais detalhada se necessário.
    
    Args:
        param1: Descrição do parâmetro 1
        param2: Descrição do parâmetro 2
    
    Returns:
        Descrição do retorno
    
    Raises:
        TipoDeErro: Quando o erro ocorre
    
    Example:
        >>> funcao_exemplo("test", 42)
        True
    """
    pass
```

#### Testes

- Todos os testes devem passar antes do PR
- Novos recursos precisam de testes
- Mantenha cobertura de teste alta (>80%)

```bash
# Executar todos os testes
pytest

# Com cobertura
pytest --cov=pixgo --cov-report=html

# Ver relatório
open htmlcov/index.html  # Mac/Linux
start htmlcov/index.html  # Windows
```

### Documentação

Se você modificar a API ou adicionar funcionalidades:

1. Atualize o README.md
2. Atualize docstrings relevantes
3. Adicione exemplos se apropriado
4. Atualize CHANGELOG.md

### Processo de Review

1. Mantenedor revisará seu PR
2. Pode haver pedidos de alterações
3. Após aprovação, será feito merge
4. Seu nome será adicionado aos contribuidores!

## Código de Conduta

### Nosso Compromisso

Estamos comprometidos em tornar a participação neste projeto uma experiência livre de assédio para todos.

### Comportamento Esperado

- Use linguagem acolhedora e inclusiva
- Respeite pontos de vista diferentes
- Aceite críticas construtivas graciosamente
- Foque no que é melhor para a comunidade

### Comportamento Inaceitável

- Linguagem ou imagens sexualizadas
- Comentários insultuosos ou depreciativos
- Assédio público ou privado
- Publicar informações privadas de outros

## Dúvidas?

- Abra uma issue com a tag [question]
- Entre em contato via email: contato@pixgo.org

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a Licença MIT.

---

**Obrigado por contribuir! 🎉**
