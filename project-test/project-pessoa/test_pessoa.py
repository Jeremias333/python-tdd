from unittest import TestCase, main, mock
from pessoa import Pessoa

class TestePessoa(TestCase):
    def setUp(self):
        self.pessoa = Pessoa('Jeremias', 'Oliveira')
    
    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.pessoa.nome, "Jeremias")

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.pessoa.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.pessoa.sobrenome, "Oliveira")

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.pessoa.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.pessoa.dados_obtidos)

    def test_pessoa_attr_dados_obtidos_e_bool(self):
        self.assertIsInstance(self.pessoa.dados_obtidos, bool)
    
    def test_obter_todo_os_dados_sucesso_OK(self):
        with mock.patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.pessoa.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.pessoa.dados_obtidos)
    
    def test_obter_todo_os_dados_falha_404(self):
        with mock.patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            
            self.assertEqual(self.pessoa.obter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.pessoa.dados_obtidos)

if __name__ == '__main__':
    main(verbosity=2)