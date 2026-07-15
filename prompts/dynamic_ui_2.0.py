from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGroq(model='llama-3.1-8b-instant',temperature=0)
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers",
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


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





if st.button("summarize"): 
    #fill the placeholder

    prompt = template.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input, 
            "length_input": length_input
        }
    )

    result = model.invoke(prompt)

    st.write(result.content)