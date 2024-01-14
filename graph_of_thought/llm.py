from abc import ABC, abstractmethod

class LLM(ABC):
    # Placeholder for running and executing LLM powered evaluation prompts
    @abstractmethod
    def evaluate(self, prompt, node, path):
        pass

class HumanDrivenLLM(LLM):
    def evaluate(self, prompt, node, path):
        print(f"Evaluating path from {node} to {path}:")
        return input("Is this path valid? (yes/no): ").strip().lower() == 'yes'