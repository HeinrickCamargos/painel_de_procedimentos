# 📂 Sistema Interno de Procedimentos (POP Digital)

Este repositório contém o código-fonte de um **Sistema Interno de Procedimentos (POP Digital)**, uma plataforma robusta desenvolvida para a organização e gestão eficiente de Procedimentos Operacionais Padrão (POP) e bases de conhecimento em ambientes corporativos. O sistema permite estruturar o conhecimento técnico e operacional em "Blocos" lógicos, facilitando o acesso e a manutenção das informações.

## ✨ Principais Funcionalidades

O POP Digital oferece um conjunto abrangente de recursos para otimizar a gestão de procedimentos:

*   **Organização por Blocos**: Agrupamento intuitivo de tarefas e conhecimentos por categorias ou departamentos específicos (ex: TI, Financeiro, FAQ), promovendo uma estrutura clara e de fácil navegação.
*   **Editor Rich Text (Quill.js)**: Um editor de texto avançado que permite o registro de procedimentos detalhados com suporte completo a formatação de texto, inclusão de links e a capacidade de colar imagens diretamente (prints de tela), enriquecendo a documentação.
*   **Gestão de Setores**: Atribuição de setores responsáveis para cada procedimento individual, garantindo clareza sobre as responsabilidades e facilitando a coordenação.
*   **Anexos**: Funcionalidade para upload e vinculação de documentos auxiliares em diversos formatos (PDF, Word, Imagens), centralizando todas as informações relevantes em um único local.
*   **Busca Inteligente**: Um sistema de busca global eficiente que permite a localização rápida de procedimentos ou blocos específicos, otimizando o tempo de pesquisa.
*   **Interface Moderna e Responsiva**: Design focado na experiência do usuário (UX) com um layout responsivo, garantindo acessibilidade e clareza das informações em diferentes dispositivos.

## 🚀 Tecnologias Utilizadas

O projeto foi construído com uma pilha de tecnologias modernas e eficientes:

*   **Backend**: Python com o framework **Flask**, conhecido por sua leveza e flexibilidade, para a lógica de servidor e manipulação de dados.
*   **Banco de Dados**: **SQLAlchemy** como ORM (Object-Relational Mapper) para interação com um banco de dados **SQLite**, proporcionando uma solução de armazenamento de dados simples e eficaz para pequenas e médias aplicações.
*   **Frontend**: 
    *   **Jinja2**: Motor de templates para renderização dinâmica das páginas HTML.
    *   **Bootstrap 5**: Framework CSS para um design responsivo e moderno.
    *   **Quill.js**: Editor Rich Text para a criação e edição de conteúdo detalhado dos procedimentos.

## ⚙️ Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

### Pré-requisitos

Certifique-se de ter o Python 3.x e o `pip` (gerenciador de pacotes do Python) instalados em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/HeinrickCamargos/painel_de_procedimentos.git
cd painel_de_procedimentos
```

### 2. Criar e Ativar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3. Instalar as Dependências

Instale todas as bibliotecas Python necessárias listadas no arquivo `requirements.txt` (se existir, caso contrário, instale manualmente):

```bash
pip install Flask Flask-SQLAlchemy Werkzeug
```

### 4. Inicializar o Banco de Dados

O banco de dados SQLite (`database.db`) será criado automaticamente na primeira execução do aplicativo, juntamente com as tabelas `bloco` e `procedimento` definidas em `models.py`.

### 5. Executar a Aplicação

```bash
python app.py
```

Após a execução, o aplicativo estará disponível em `http://127.0.0.1:5000/` (ou outra porta, dependendo da configuração do Flask).

## 💡 Como Usar

1.  **Navegação**: Ao acessar a aplicação, você verá a tela inicial com os blocos de procedimentos existentes.
2.  **Criar Novo Bloco**: Utilize a opção para criar novos blocos e organizar seus procedimentos por categorias.
3.  **Adicionar Procedimento**: Dentro de cada bloco, você pode adicionar novos procedimentos, preenchendo o título, setor responsável, descrição detalhada (com o editor Rich Text) e anexando documentos, se necessário.
4.  **Visualizar e Editar**: Clique em um bloco ou procedimento para visualizar seus detalhes. Procedimentos podem ser editados para atualizar informações ou anexos.
5.  **Busca**: Use a barra de pesquisa para encontrar rapidamente blocos ou procedimentos por título.

## 📸 Telas do Sistema

A seguir, algumas capturas de tela da aplicação em funcionamento:

### TELA INICIAL

<img width="1391" height="669" alt="image" src="https://github.com/user-attachments/assets/03aa80ba-14f6-4ab8-9d10-e5f4dbff289b"/>

### CRIANDO O BLOCO

<img width="1382" height="736" alt="WhatsApp Image 2026-05-06 at 18 45 28 (2)" src="https://github.com/user-attachments/assets/f6f5ea01-fab8-46cd-b7c5-cf855e942388" />

### BLOCOS CRIADOS

<img width="1350" height="642" alt="WhatsApp Image 2026-05-06 at 18 45 28 (4)" src="https://github.com/user-attachments/assets/c79db54a-41b6-4496-882f-b194d2ccf308" />

### PROCEDIMENTOS

<img width="1378" height="644" alt="WhatsApp Image 2026-05-06 at 18 45 28 (5)" src="https://github.com/user-attachments/assets/99d39656-bbc5-441d-bfc4-61e54907ade1" />

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, relatórios de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Para dúvidas ou informações adicionais, entre em contato com Heinrick Camargos. 
