from abc import ABC, abstractmethod

class GoogleSearchAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def execute(self, query: str) -> dict:
        # Mocking the search result for now as I don't have a real Google API key
        # In a real scenario, this would use the google-api-python-client
        print(f"Searching for: {query}")
        
        # Example mock results
        if "machine learning" in query.lower():
            return {
                "results": [
                    {"title": "What is Machine Learning?", "description": "Machine learning is a field of AI focused on building systems that learn from data."},
                    {"title": "Types of ML", "description": "Supervised, Unsupervised, and Reinforcement Learning."},
                    {"title": "MLing Project", "description": "Examples of ML projects include image recognition and NLP."}
                ],
                "images": ["https://example.com/ml_image1.jpg"],
                "videos": []
            }
        
        return {
            "results": [{"title": "Generic Result", "description": "Found some info."}],
            "images": [],
            "videos": []
        }
