import os
import time
import warnings
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Suppress duckduckgo_search renaming RuntimeWarning globally
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*duckduckgo_search.*")
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*ddgs.*")

load_dotenv()

class RateLimitedChatGroq(ChatGroq):
    def invoke(self, *args, **kwargs):
        # Default sleep to pace requests
        time.sleep(2)
        
        max_attempts = 5
        delay = 12
        for attempt in range(max_attempts):
            try:
                return super().invoke(*args, **kwargs)
            except Exception as e:
                err_msg = str(e)
                # Catch rate limits (429 status code or rate_limit string)
                is_rate_limit = any(x in err_msg.lower() for x in ["rate_limit", "429", "rate limit"])
                if is_rate_limit and attempt < max_attempts - 1:
                    time.sleep(delay)
                    delay += 8
                    continue
                raise e


llm = RateLimitedChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.1
)