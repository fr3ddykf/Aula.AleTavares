# Sistema de Gestão Escolar Infantil

Este projeto implementa um sistema completo de gestão para escola infantil, desenvolvido como parte das disciplinas de **Implementação de Software** e **Integração de Software** do 5º semestre.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Execução](#instalação-e-execução)
- [Documentação da API](#documentação-da-api)
- [Monitoramento](#monitoramento)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Exemplos de Uso](#exemplos-de-uso)
- [Contribuição](#contribuição)

## 🎯 Visão Geral

O Sistema de Gestão Escolar Infantil é uma aplicação web completa que permite gerenciar:

- **Alunos**: Cadastro, atualização e consulta de informações dos alunos
- **Professores**: Gestão do corpo docente
- **Turmas**: Organização das turmas por período e faixa etária
- **Disciplinas**: Cadastro das atividades pedagógicas
- **Responsáveis**: Gestão dos responsáveis pelos alunos
- **Matrículas**: Controle de matrículas e status dos alunos

## 🏗️ Arquitetura

O sistema segue uma arquitetura de microsserviços containerizada:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (Swagger UI)  │◄──►│   (Flask API)   │◄──►│  (PostgreSQL)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │     Monitoramento       │
                    │  Prometheus + Grafana   │
                    └─────────────────────────┘
```

### Componentes:

- **Backend**: API RESTful desenvolvida em Flask com SQLAlchemy
- **Banco de Dados**: PostgreSQL com estrutura relacional otimizada
- **Documentação**: Swagger/OpenAPI integrado
- **Monitoramento**: Prometheus para coleta de métricas e Grafana para visualização
- **Containerização**: Docker e Docker Compose para orquestração

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.11**
- **Flask 2.3.3** - Framework web
- **Flask-SQLAlchemy 3.0.5** - ORM
- **Flask-RESTX 1.2.0** - Extensão para APIs REST e documentação Swagger
- **Flask-CORS 4.0.0** - Suporte a CORS
- **psycopg2-binary 2.9.7** - Driver PostgreSQL

### Banco de Dados
- **PostgreSQL 15** - Sistema de gerenciamento de banco de dados

### Monitoramento
- **Prometheus** - Coleta de métricas
- **Grafana** - Visualização de dados
- **Node Exporter** - Métricas do sistema
- **Postgres Exporter** - Métricas do banco de dados

### Infraestrutura
- **Docker** - Containerização
- **Docker Compose** - Orquestração de containers

## 📋 Pré-requisitos

- **Docker** (versão 20.10 ou superior)
- **Docker Compose** (versão 2.0 ou superior)
- **Git** para clonagem do repositório

### Verificar instalação:
```bash
docker --version
docker-compose --version
```

## 🚀 Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/fr3ddykf/Aula.AleTavares.git
cd sistema-gestao-escolar
```

### 2. Executar com Docker Compose
```bash
# Construir e iniciar todos os serviços
docker-compose up --build

# Ou executar em background
docker-compose up -d --build
```

### 3. Verificar se os serviços estão rodando
```bash
docker-compose ps
```

### 4. Acessar os serviços

| Serviço | URL | Credenciais |
|---------|-----|-------------|
| **API Backend** | http://localhost:5000 | - |
| **Documentação Swagger** | http://localhost:5000/docs/ | - |
| **Grafana** | http://localhost:3000 | admin / admin123 |
| **Prometheus** | http://localhost:9090 | - |
| **PostgreSQL** | localhost:5432 | postgres / postgres |

## 📚 Documentação da API

A documentação completa da API está disponível através do Swagger UI em:
**http://localhost:5000/docs/**

### Endpoints Principais:

#### Alunos
- `GET /api/v1/alunos/` - Listar todos os alunos
- `POST /api/v1/alunos/` - Criar novo aluno
- `GET /api/v1/alunos/{id}` - Obter aluno específico
- `PUT /api/v1/alunos/{id}` - Atualizar aluno
- `DELETE /api/v1/alunos/{id}` - Deletar aluno

#### Professores
- `GET /api/v1/professores/` - Listar todos os professores
- `POST /api/v1/professores/` - Criar novo professor
- `GET /api/v1/professores/{id}` - Obter professor específico
- `PUT /api/v1/professores/{id}` - Atualizar professor
- `DELETE /api/v1/professores/{id}` - Deletar professor

#### Turmas
- `GET /api/v1/turmas/` - Listar todas as turmas
- `POST /api/v1/turmas/` - Criar nova turma
- `GET /api/v1/turmas/{id}` - Obter turma específica
- `PUT /api/v1/turmas/{id}` - Atualizar turma
- `DELETE /api/v1/turmas/{id}` - Deletar turma

#### Matrículas
- `GET /api/v1/matriculas/` - Listar todas as matrículas
- `POST /api/v1/matriculas/` - Criar nova matrícula
- `GET /api/v1/matriculas/{id}` - Obter matrícula específica
- `PUT /api/v1/matriculas/{id}` - Atualizar matrícula
- `DELETE /api/v1/matriculas/{id}` - Deletar matrícula

## 📊 Monitoramento

### Prometheus
Acesse http://localhost:9090 para visualizar:
- Métricas da aplicação Flask
- Métricas do sistema (CPU, memória, disco)
- Métricas do banco PostgreSQL

### Grafana
Acesse http://localhost:3000 (admin/admin123) para:
- Dashboards personalizados
- Visualização de métricas em tempo real
- Alertas configuráveis

## 📁 Estrutura do Projeto

```
sistema-gestao-escolar/
├── APP/                          # Código da aplicação Flask
│   ├── models/                   # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── aluno.py
│   │   ├── professor.py
│   │   ├── turma.py
│   │   ├── disciplina.py
│   │   ├── responsavel.py
│   │   └── matricula.py
│   ├── routes/                   # Rotas da API
│   │   ├── __init__.py
│   │   ├── alunos.py
│   │   ├── professores.py
│   │   ├── turmas.py
│   │   ├── disciplinas.py
│   │   ├── responsaveis.py
│   │   └── matriculas.py
│   ├── app.py                    # Aplicação principal
│   └── requirements.txt          # Dependências Python
├── monitoring/                   # Configurações de monitoramento
│   ├── prometheus/
│   │   └── prometheus.yml
│   └── grafana/
│       ├── datasources.yml
│       └── dashboards.yml
├── docker-compose.yml            # Orquestração dos serviços
├── Dockerfile.backend            # Container do backend
├── Dockerfile.db                 # Container do banco
├── init.sql                      # Script de inicialização do BD
└── README.md                     # Este arquivo
```

## 💡 Exemplos de Uso

### Criar um novo aluno
```bash
curl -X POST "http://localhost:5000/api/v1/alunos/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "data_nascimento": "2020-05-15",
    "cpf": "12345678901",
    "endereco": "Rua das Flores, 123",
    "telefone": "(11) 99999-9999",
    "email": "joao@email.com"
  }'
```

### Listar todos os alunos
```bash
curl -X GET "http://localhost:5000/api/v1/alunos/"
```

### Criar uma nova turma
```bash
curl -X POST "http://localhost:5000/api/v1/turmas/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Maternal III",
    "ano_letivo": 2024,
    "periodo": "Manhã",
    "idade_minima": 3,
    "idade_maxima": 4,
    "capacidade_maxima": 20,
    "professor_id": 1
  }'
```

### Matricular um aluno
```bash
curl -X POST "http://localhost:5000/api/v1/matriculas/" \
  -H "Content-Type: application/json" \
  -d '{
    "aluno_id": 1,
    "turma_id": 1,
    "data_inicio": "2024-02-01",
    "status": "Ativa",
    "mensalidade": 450.00
  }'
```

## 🔧 Comandos Úteis

### Docker
```bash
# Ver logs de um serviço específico
docker-compose logs backend

# Parar todos os serviços
docker-compose down

# Parar e remover volumes (CUIDADO: apaga dados do banco)
docker-compose down -v

# Reconstruir apenas um serviço
docker-compose up --build backend

# Executar comando no container
docker-compose exec backend bash
docker-compose exec db psql -U postgres -d escola_infantil
```

### Banco de Dados
```bash
# Conectar ao PostgreSQL
docker-compose exec db psql -U postgres -d escola_infantil

# Backup do banco
docker-compose exec db pg_dump -U postgres escola_infantil > backup.sql

# Restaurar backup
docker-compose exec -T db psql -U postgres escola_infantil < backup.sql
```

## 🧪 Testes

Para executar os testes da aplicação:

```bash
# Executar testes dentro do container
docker-compose exec backend python -m pytest

# Executar com coverage
docker-compose exec backend python -m pytest --cov=.
```

## 🚨 Troubleshooting

### Problemas Comuns

1. **Erro de conexão com banco de dados**
   ```bash
   # Verificar se o banco está rodando
   docker-compose ps db
   
   # Ver logs do banco
   docker-compose logs db
   ```

2. **Porta já em uso**
   ```bash
   # Verificar portas em uso
   netstat -tulpn | grep :5000
   
   # Parar serviços conflitantes ou alterar portas no docker-compose.yml
   ```

3. **Problemas de permissão**
   ```bash
   # No Linux/Mac, pode ser necessário ajustar permissões
   sudo chown -R $USER:$USER .
   ```

## 📈 Métricas Disponíveis

### Aplicação Flask
- Número de requisições por endpoint
- Tempo de resposta das requisições
- Códigos de status HTTP
- Número de usuários ativos

### Sistema
- Uso de CPU
- Uso de memória
- Uso de disco
- Tráfego de rede

### Banco de Dados
- Conexões ativas
- Queries por segundo
- Tempo de resposta das queries
- Tamanho do banco de dados

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Equipe

- **Desenvolvedor Backend**: [Seu Nome]
- **Disciplina**: Implementação de Software / Integração de Software
- **Semestre**: 5º Semestre
- **Ano**: 2024

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Entre em contato via email: [seu-email@exemplo.com]

---

**Desenvolvido com ❤️ para o curso de Sistemas de Informação**