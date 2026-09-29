from openai import OpenAI

def extract_terms(text: str, api_key: str, model: str):
    client=OpenAI(api_key=api_key)
    r=client.responses.create(model=model,input=f"Extract acquisition, planning and cost assumptions as JSON:\n{text}")
    return r.output_text
