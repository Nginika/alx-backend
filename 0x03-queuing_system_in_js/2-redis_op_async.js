import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(`${value}`);
  } catch (error) {
    console.error(`Error getting value for ${schoolName}: ${err.message}`);
  }
}


async function main() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  client.quit();
}

main();
