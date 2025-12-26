"""
Script de teste rápido para verificar se o pacote está funcionando
Execute: python test_install.py
"""

def test_imports():
    """Testa se todos os imports funcionam"""
    print("Testando imports...")
    
    try:
        from pixgo import PixGoClient
        print("✓ PixGoClient importado")
        
        from pixgo import Payment, PaymentStatus
        print("✓ Payment e PaymentStatus importados")
        
        from pixgo import (
            PixGoException,
            PixGoAPIError,
            PixGoValidationError,
            PixGoAuthenticationError,
            PixGoRateLimitError
        )
        print("✓ Exceções importadas")
        
        return True
    except ImportError as e:
        print(f"✗ Erro de importação: {e}")
        return False


def test_client_initialization():
    """Testa inicialização do cliente"""
    print("\nTestando inicialização do cliente...")
    
    try:
        from pixgo import PixGoClient, PixGoValidationError
        
        # Teste com API key válida
        client = PixGoClient(api_key="pk_test_key")
        print("✓ Cliente inicializado com API key válida")
        
        # Teste com API key inválida
        try:
            client = PixGoClient(api_key="invalid_key")
            print("✗ Deveria ter levantado erro para API key inválida")
            return False
        except PixGoValidationError:
            print("✓ Validação de API key funcionando")
        
        # Teste sem API key
        try:
            client = PixGoClient(api_key="")
            print("✗ Deveria ter levantado erro para API key vazia")
            return False
        except PixGoValidationError:
            print("✓ Validação de API key vazia funcionando")
        
        return True
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False


def test_models():
    """Testa os modelos de dados"""
    print("\nTestando modelos de dados...")
    
    try:
        from pixgo import Payment, PaymentStatus
        
        # Criar payment a partir de dict
        data = {
            "payment_id": "dep_test123",
            "amount": 25.50,
            "status": "pending",
            "qr_code": "test_qr",
            "qr_image_url": "http://test.com/qr.png",
            "created_at": "2025-01-01",
            "expires_at": "2025-01-01",
        }
        
        payment = Payment.from_dict(data)
        print("✓ Payment criado a partir de dict")
        
        # Testar métodos
        assert payment.is_pending() == True
        print("✓ Método is_pending() funcionando")
        
        assert payment.is_paid() == False
        print("✓ Método is_paid() funcionando")
        
        # Testar conversão para dict
        payment_dict = payment.to_dict()
        assert payment_dict["payment_id"] == "dep_test123"
        print("✓ Conversão para dict funcionando")
        
        # Testar enum
        assert PaymentStatus.PENDING.value == "pending"
        assert PaymentStatus.COMPLETED.value == "completed"
        print("✓ PaymentStatus enum funcionando")
        
        return True
    except Exception as e:
        print(f"✗ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_version():
    """Testa se a versão está acessível"""
    print("\nTestando versão do pacote...")
    
    try:
        import pixgo
        version = pixgo.__version__
        print(f"✓ Versão: {version}")
        return True
    except Exception as e:
        print(f"✗ Erro ao obter versão: {e}")
        return False


def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("TESTE DE INSTALAÇÃO - PIXGO PYTHON CLIENT")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Inicialização do Cliente", test_client_initialization),
        ("Modelos de Dados", test_models),
        ("Versão", test_version),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        results[test_name] = test_func()
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    passed = sum(1 for result in results.values() if result)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASSOU" if result else "✗ FALHOU"
        print(f"{test_name}: {status}")
    
    print("-" * 60)
    print(f"Total: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\n✓ Instalação OK! O pacote está pronto para uso.")
        print("\nPróximos passos:")
        print("1. Obtenha sua API key em https://pixgo.org")
        print("2. Veja os exemplos na pasta 'examples/'")
        print("3. Leia a documentação no README.md")
    else:
        print("\n✗ Alguns testes falharam. Verifique a instalação.")
    
    print("=" * 60)
    
    return passed == total


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
