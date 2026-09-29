import Fastify from "fastify";
const app=Fastify();
app.post("/twilio/inbound",async(req,reply)=>{
  const body=req.body as Record<string,string>;
  return reply.type("application/xml").send(`<Response><Message>Thanks. We received: ${body.Body ?? ""}</Message></Response>`);
});
app.post("/qualification",async(req)=>({status:"qualified",next_action:"offer_calendly"}));
app.listen({port:3000,host:"0.0.0.0"});
