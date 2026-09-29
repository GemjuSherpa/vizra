class CombineResultAgent:
    def execute(self, search_results: dict, llm_response: dict) -> dict:
        results = search_results.get("results", [])
        llm_response_text = llm_response.get("response", "")
        
        combined_content = f"Summary: {llm_response_text}\n\nDetails found: "
        for r in results:
            combined_content += f"{r.get('title')}: {r.get('description')} "
            
        return {
            "content": combined_content,
            "images": search_results.get("images", []),
            "videos": search_results.get("videos", [])
        }
