from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from llm.llm_provider import LLMProvider

load_dotenv()

class GeminiLLM(LLMProvider):
    def get_llm(self):
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0
        )