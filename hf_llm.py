from langchain.llms.base import LLM
from huggingface_hub import InferenceClient
from typing import Optional, List
import os


class HuggingFaceRouterLLM(LLM):
    def __init__(
        self,
        model: str = "meta-llama/Meta-Llama-3-8B-Instruct",
        temperature: float = 0.0,
    ):
        super().__init__()
        self.model = model
        self.temperature = temperature

        self.client = InferenceClient(
            model=self.model,
            token=os.getenv("HF_TOKEN")
        )

    @property
    def _llm_type(self) -> str:
        return "huggingface-router"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
    ) -> str:
        response = self.client.text_generation(
            prompt,
            max_new_tokens=300,
            temperature=self.temperature,
        )
        return response
