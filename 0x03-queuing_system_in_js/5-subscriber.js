import { createClient } from 'redis';

const client = createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

client.subscribe('holberton school channel');

// Event handler for received messages
client.on('message', (channel, message) => {
  console.log(`${message}`);

  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit when receiving "KILL_SERVER"
    client.unsubscribe();
    client.quit();
  }
});
