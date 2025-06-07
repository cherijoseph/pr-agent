import aiohttp

from pr_agent.algo.ai_handlers.base_ai_handler import BaseAiHandler
from pr_agent.config_loader import get_settings
from pr_agent.log import get_logger


class SimpleAPIHandler(BaseAiHandler):
    """Minimal AI handler that posts prompts to a custom HTTP endpoint."""

    def __init__(self):
        self.endpoint = get_settings().get("CONFIG.AI_ENDPOINT", "")
        self.token = get_settings().get("CONFIG.AI_TOKEN", "")

    @property
    def deployment_id(self):
        return None

    async def chat_completion(self, model: str, system: str, user: str, temperature: float = 0.2, img_path: str | None = None):
        payload = {
            "model": model,
            "system": system,
            "user": user,
            "temperature": temperature,
        }
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.endpoint, json=payload, headers=headers, timeout=get_settings().config.ai_timeout) as resp:
                resp.raise_for_status()
                data = await resp.json()
        get_logger().debug("AI response", artifact=data)
        return data.get("content", ""), data.get("finish_reason", "stop")
