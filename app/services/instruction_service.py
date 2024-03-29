import google.generativeai as genai
from openai import OpenAI
from typing import Optional, List
import os

from resources.prompt import prompts

class InstructionService:
    def __init__(self):
        self.openai = OpenAI(api_key=os.getenv("OPENAI_KEY"))
        self.gemini = genai.GenerativeModel('gemini-pro')
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))

    async def generate_instructions(self, query: str):
        response = self.gemini.generate_content(
            prompts.get_prompt_instruction_text(query)
        )
        return response.text

    async def generate_instruction_image(self, query: str):
        response = self.openai.images.generate(
            model="dall-e-3",
            prompt=prompts.get_prompt_instruction_image(query),
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url

    async def get_quiz_data(self, db, disaster_type: Optional[List[str]] = None, size: int = 10):
        query = f"""
        SELECT *, rand() as rand
        FROM {db.dataset_id}.quiz
        CROSS JOIN UNNEST(disaster_type) as disaster
        """

        if disaster_type is not None:
            types_str = "','".join(disaster_type)
            query += f"WHERE disaster IN ('{types_str}') "

        query += f"ORDER BY rand LIMIT {size};"
        query_job = db.client.query(query)
        results = query_job.result()

        return results