from src.scraper import get_reddit_data
from src.llm import build_persona
from src.utils import save_to_txt
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

if __name__ == "__main__":
    reddit_username = input("Enter Reddit username (e.g. kojied): ").strip()
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("USER_AGENT")
    openai_key = os.getenv("OPENAI_API_KEY")

    posts, comments = get_reddit_data(reddit_username, client_id, client_secret, user_agent)
    persona = build_persona(posts, comments, openai_key)
    save_to_txt(persona, reddit_username)
    print(f"✅ Persona generated and saved to {reddit_username}_persona.txt")
