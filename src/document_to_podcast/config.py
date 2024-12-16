from pathlib import Path
from typing import Literal
from typing_extensions import Annotated

from pydantic import BaseModel, FilePath
from pydantic.functional_validators import AfterValidator

from document_to_podcast.preprocessing import DATA_LOADERS


DEFAULT_PROMPT = """
You are a podcast scriptwriter generating engaging and natural-sounding conversations about GitHub repositories in JSON format.
The script features the following speakers:
{SPEAKERS}

Instructions:
- Break down the README content into an engaging discussion that helps listeners understand:
  * The purpose and main features of the project
  * How to get started with the project
  * Key use cases and examples
  * Any important technical requirements or dependencies
- Write dynamic, easy-to-follow dialogue that makes technical concepts accessible
- Include natural interruptions and clarifying questions
- Use analogies and real-world examples to explain complex ideas
- Format output as a JSON conversation

Example:
{
  "Speaker 1": "Welcome to our tech breakdown! Today we're exploring an interesting GitHub project called...",
  "Speaker 2": "Oh nice! What caught your attention about this one?",
  "Speaker 1": "Well, it solves a really common problem that developers face...",
  "Speaker 2": "Could you break that down with an example?",
  "Speaker 1": "Sure! Think of it like..."
}
"""

DEFAULT_SPEAKERS = [
    {
        "id": 1,
        "name": "Laura",
        "description": "The technical expert. She breaks down complex technical concepts clearly, explains code architecture and features, and provides practical insights about implementation.",
        "voice_profile": "female_1",
    },
    {
        "id": 2,
        "name": "Jon",
        "description": "The curious developer. He asks insightful questions about real-world applications, implementation details, and potential challenges, helping surface important details for listeners.",
        "voice_profile": "male_1",
    },
]

SUPPORTED_TTS_MODELS = Literal[
    "OuteAI/OuteTTS-0.1-350M-GGUF/OuteTTS-0.1-350M-FP16.gguf",
    "OuteAI/OuteTTS-0.2-500M-GGUF/OuteTTS-0.2-500M-FP16.gguf",
    "parler-tts/parler-tts-large-v1",
    "parler-tts/parler-tts-mini-v1",
    "parler-tts/parler-tts-mini-v1.1",
]


def validate_input_file(value):
    if Path(value).suffix not in DATA_LOADERS:
        raise ValueError(
            f"input_file extension must be one of {list(DATA_LOADERS.keys())}"
        )
    return value


def validate_text_to_text_model(value):
    parts = value.split("/")
    if len(parts) != 3:
        raise ValueError("text_to_text_model must be formatted as `owner/repo/file`")
    if not value.endswith(".gguf"):
        raise ValueError("text_to_text_model must be a gguf file")
    return value


def validate_text_to_text_prompt(value):
    if "{SPEAKERS}" not in value:
        raise ValueError("text_to_text_prompt must contain `{SPEAKERS}` placeholder")
    return value


class Speaker(BaseModel):
    id: int
    name: str
    description: str
    voice_profile: str

    def __str__(self):
        return f"Speaker {self.id}. Named {self.name}. {self.description}"


class Config(BaseModel):
    input_file: Annotated[FilePath, AfterValidator(validate_input_file)]
    output_folder: str
    text_to_text_model: Annotated[str, AfterValidator(validate_text_to_text_model)]
    text_to_text_prompt: Annotated[str, AfterValidator(validate_text_to_text_prompt)]
    text_to_speech_model: SUPPORTED_TTS_MODELS
    speakers: list[Speaker]
