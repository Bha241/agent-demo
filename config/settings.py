from dotenv import load_dotenv
import os
import warnings

# Suppress duckduckgo_search renaming warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*duckduckgo_search.*")

load_dotenv()


class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")

    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")


settings = Settings()