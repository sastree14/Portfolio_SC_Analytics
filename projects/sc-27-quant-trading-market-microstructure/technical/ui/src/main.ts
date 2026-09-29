const wsUrl = import.meta.env.VITE_WS_URL || "ws://localhost:8000/stream";
const socket = new WebSocket(wsUrl);
socket.onmessage = (event) => {
  const payload = JSON.parse(event.data);
  console.log("market update", payload);
};
