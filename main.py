import time
import os
from agents_project.google_search_agent.search_agent import GoogleSearchAgent
from agents_project.llm_agent.llm_agent import LLAMgent
from agents_project.combine_result_agent.combine_result_agent import CombineResultAgent
from agents_project.video_generation_agent.video_generation_agent import VideoGenerationAgent

class Pipeline:
    def __init__(self):
        self.search_agent = GoogleSearchAgent()
        self.llm_agent = LLAMgent()
        self.combine_agent = CombineResultAgent()
        self.video_agent = VideoGenerationAgent()

    def run(self, query: str):
        print(f"\n--- Starting Pipeline ---")
        print(f"Query: {query}")
        
        # 1. Search & LLM (Simulated parallel/concurrent)
        print("Step 1: Searching...")
        search_results = self.search_agent.execute(query)
        print("Step 1: LLM Processing...")
        llm_response = self.llm_agent.execute(query)
        
        # 2. Combine Results
        print("Step 2: Combining results...")
        combined_data = self.combine_agent.execute(search_results, llm_response)
        
        # 3. Generate Video
        print("Step 3: Generating video...")
        video_path = self.video_agent.execute(combined_data)
        
        print(f"--- Pipeline Complete ---")
        print(f"Resulting video file: {video_path}")
        return video_path

if __name__ == "__main__":
    pipeline = Pipeline()
    user_query = input("Enter your query: ")
    video_path = pipeline.run(user_query)
    print(f"Final Path: {video_path}")
