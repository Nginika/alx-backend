import { createClient, print } from 'redis';

const client = createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);
}

// Function to display the hash
function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error getting hash: ${err.message}`);
    } else {
      console.log('Hash stored in Redis:');
      console.log(reply);
    }
    // Close the Redis connection when done
    client.quit();
  });
}

// Create and display the hash
createHash();
displayHash();
