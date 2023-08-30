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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}: ${err.message}`);
    } else {
      console.log(`${reply}`);
    }
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
