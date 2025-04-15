from transformers import pipeline

class TitleGenerator:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.model = pipeline(
                "text-generation", 
                model="gpt2",
                device=-1  # Use CPU if no GPU
            )
        return cls._instance
        
    def generate_titles(self, content, num_titles=3):
        prompt = f"Generate {num_titles} blog titles for:\n{content}\nTitles:"
        results = self.model(
            prompt,
            max_length=50,
            num_return_sequences=num_titles,
            temperature=0.7,
            truncation=True
        )
        return [r['generated_text'].replace(prompt, '').split('\n')[0].strip() for r in results]