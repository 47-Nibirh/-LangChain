from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    
    """
You are an expert AI researcher and teacher.

Explain the research paper "{paper_input}".

Explanation Style: {style_input}
Explanation Length: {length_input}

Please include:
1. Introduction
2. Problem Statement
3. Proposed Solution
4. Key Contributions
5. Advantages
6. Limitations
7. Applications
8. Final Summary

Format the response using Markdown.
""",
)

template.save('template.json')