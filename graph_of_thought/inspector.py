from abc import ABC, abstractmethod
class Inspector(ABC):
    """
    Checker function is chain of
    Inspector instances, so we ask the user to
    define them. For qualitative types of assessment an LLM is made available
    """
    def __init__(self, LLM=None):
        self.LLM = LLM

    @abstractmethod
    def evaluate(self, node, path, n):
        pass