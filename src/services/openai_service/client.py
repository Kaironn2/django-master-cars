import openai
from decouple import config


class OpenAIClient:
    def __init__(self):
        self.client = openai.OpenAI(api_key=config('OPENAI_API_KEY'))

    def get_bio(self, car_model: str, car_brand: str, car_year: str) -> str:
        prompt = f"""
            Write a short bio for {car_year} {car_brand} {car_model} in pt-BR.
            Max length: 250 characters.
        """
        response = self.client.responses.create(
            model='gpt-4o-mini',
            input=prompt,
            max_output_tokens=350,
        )
        return response.output_text
