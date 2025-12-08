from .gemini_node import IFGeminiAdvanced
from .task_prompt_manager import IFTaskPromptManager, IFPromptCombiner
from .api_routes import *  # Import API routes

NODE_CLASS_MAPPINGS = {
    "CustomGeminiNode": IFGeminiAdvanced,
    "IFTaskPromptManager": IFTaskPromptManager,
    "IFPromptCombiner": IFPromptCombiner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CustomGeminiNode": "Custom Gemini",
    "IFTaskPromptManager": "IF Task Prompt Manager",
    "IFPromptCombiner": "IF Prompt Combiner"
}

# Path to web directory relative to this file
WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]