import effectPayload from "./effectInterface";

export default async function effectClick(data: effectPayload) {
    try {
        const response = await fetch("http://localhost:8000/effect/", { 
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        });
  
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
      } catch (error) {
        console.error('Error making request:', error);
      }
}