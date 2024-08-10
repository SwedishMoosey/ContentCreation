export default async function effectClick(route: string) {
    try {
        const response = await fetch("http://localhost:8000/effect/" + route, { 
          method: 'GET',
        });
  
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
      } catch (error) {
        console.error('Error making request:', error);
      }
}