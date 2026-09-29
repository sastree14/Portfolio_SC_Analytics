from openai import OpenAI

def synthesize(question: str, evidence: list[str], api_key: str, model: str):
    client=OpenAI(api_key=api_key)
    prompt="Answer only from the evidence. State uncertainty.\nQuestion: "+question+"\nEvidence:\n" + "\n---\n".join(evidence)
    return client.responses.create(model=model,input=prompt).output_text
