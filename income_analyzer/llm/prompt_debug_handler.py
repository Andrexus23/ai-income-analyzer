from langchain.callbacks.base import BaseCallbackHandler

class PromptDebugHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print("MODEL INPUT PROMPTS:")
        for i, prompt in enumerate(prompts):
            print(f"Prompt {i+1}:")
            print(prompt)
            print("-" * 50)
    
    def on_llm_end(self, response, **kwargs):
        print("MODEL OUTPUT:")
        print(response.generations[0][0].text)
        print("=" * 50)
