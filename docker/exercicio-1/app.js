const express = require('express');
const os = require('os');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware para JSON
app.use(express.json());

// Rota principal
app.get('/', (req, res) => {
  res.send('Hello from Docker!');
});

// Rota de health check
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    uptime: process.uptime(),
    timestamp: new Date().toISOString()
  });
});

// Rota about
app.get('/about', (req, res) => {
  res.json({
    exercise: 'Exercício 1',
    description: 'Hello World com Docker e Node.js',
    author: 'Gabriel CH',
    technologies: ['Docker', 'Node.js', 'Express']
  });
});

// Iniciar servidor
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 Servidor rodando na porta ${PORT}`);
  console.log(`🐳 Container ID: ${os.hostname()}`);
  console.log(`📅 Iniciado em: ${new Date().toISOString()}`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('🛑 SIGTERM recebido, encerrando...');
  process.exit(0);
});

process.on('SIGINT', () => {
  console.log('🛑 SIGINT recebido, encerrando...');
  process.exit(0);
});
