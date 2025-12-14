import os
from dotenv import load_dotenv
from openai import OpenAI

from app.agent import ReactAgent
from app.prompts import SYSTEM_PROMPT

load_dotenv()

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    agent = ReactAgent(client)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "Používatelia odchádzajú z checkoutu na kroku doručenia. "
                "Nevidia cenu dopravy a po kliknutí sa niekedy nič nedeje. "
                "CTA je 'Pokračovať'. Navrhni UX riešenie."
            ),
        },
    ]

    result = agent.run(messages)
    print("\nFINAL OUTPUT:\n")
    print(result)

if __name__ == "__main__":
    main()
