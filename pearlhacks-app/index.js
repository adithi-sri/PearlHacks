// index.js
import express from 'express';
import { Server } from 'socket.io';
import { createServer } from 'http';
import cors from 'cors';

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: '*',  
  },
});

app.use(cors());

// When a new client connects
io.on('connection', (socket) => {
  console.log(`A user connected with ID: ${socket.id}`);

  // Listen for messages from the client
  socket.on('message', (msg) => {
    console.log(`Message from ${socket.id}:`, msg);
    io.emit('message', msg);  // Broadcast the message to all connected clients
  });

  // Handle disconnection
  socket.on('disconnect', () => {
    console.log(`User with ID ${socket.id} disconnected`);
  });
});

// Start the server
httpServer.listen(3000, () => {
  console.log('Server Running on http://localhost:3000 <3!');
});