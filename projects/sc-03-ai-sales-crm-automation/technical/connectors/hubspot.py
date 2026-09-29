import httpx

class HubSpotConnector:
    def __init__(self, token: str):
        self.client=httpx.Client(base_url="https://api.hubapi.com",headers={"Authorization":f"Bearer {token}"},timeout=20)
    def get_contact(self, contact_id: str):
        r=self.client.get(f"/crm/v3/objects/contacts/{contact_id}"); r.raise_for_status(); return r.json()
