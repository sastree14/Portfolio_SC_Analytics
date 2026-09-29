from abc import ABC, abstractmethod

from app.settings import get_settings


SYSTEM_PROMPT = """You are planning one controlled business operation.
Return a concise action plan in plain text.
Do not claim that an external action has happened.
The execution layer, not the model, performs external actions.
"""


class Provider(ABC):
    @abstractmethod
    def plan(self, goal: str) -> str:
        raise NotImplementedError


class MockProvider(Provider):
    def plan(self, goal: str) -> str:
        return (
            "1. Validate the requested objective and required inputs.\n"
            "2. Prepare the external action without executing it.\n"
            "3. Request approval if the workflow requires it.\n"
            f"4. Execute the approved action for: {goal}\n"
            "5. Persist the result and any exception."
        )


class OpenAIProvider(Provider):
    def __init__(self) -> None:
        settings = get_settings()
        if not settings.openai_api_key or not settings.openai_model:
            raise ValueError(
                "OPENAI_API_KEY and OPENAI_MODEL are required when provider=openai"
            )

        from openai import OpenAI

        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def plan(self, goal: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            instructions=SYSTEM_PROMPT,
            input=goal,
        )
        return response.output_text


class AnthropicProvider(Provider):
    def __init__(self) -> None:
        settings = get_settings()
        if not settings.anthropic_api_key or not settings.anthropic_model:
            raise ValueError(
                "ANTHROPIC_API_KEY and ANTHROPIC_MODEL are required when provider=anthropic"
            )

        from anthropic import Anthropic

        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.model = settings.anthropic_model

    def plan(self, goal: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=700,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": goal}],
        )
        return "".join(
            block.text for block in message.content if getattr(block, "type", None) == "text"
        )


def get_provider(name: str) -> Provider:
    providers = {
        "mock": MockProvider,
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
    }

    try:
        return providers[name]()
    except KeyError as exc:
        raise ValueError(f"Unsupported provider: {name}") from exc
