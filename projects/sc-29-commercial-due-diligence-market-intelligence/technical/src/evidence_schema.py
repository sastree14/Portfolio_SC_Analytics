from dataclasses import dataclass
@dataclass
class Evidence:
    question:str
    source_url:str
    observed_at:str
    excerpt:str
    confidence:float
