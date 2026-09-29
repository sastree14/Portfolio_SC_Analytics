export async function getEventTypes(token:string){
  const r=await fetch("https://api.calendly.com/event_types",{headers:{Authorization:`Bearer ${token}`}});
  if(!r.ok) throw new Error("Calendly request failed");
  return r.json();
}
