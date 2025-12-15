import streamlit as st

st.set_page_config(
    page_title="Search Algorithms Playground",
    page_icon="🧠",
    layout="centered",
)


st.title("🧠 Search Algorithms Playground")
st.markdown("---")

st.markdown(
    """
This project showcases **heuristic and metaheuristic search algorithms**
through interactive demos.

Each algorithm is implemented as an independent Streamlit app,
focused on *understanding behavior*, not just code.
"""
)

st.subheader("Available algorithms")


st.link_button(
    "🧬 **Genetic Algorithm** (Siedlecki & Sklansky (1989))",
    "https://genetic-search-algorithms.streamlit.app",
    use_container_width=True,
)

st.markdown("---")

st.markdown(
    """
📚 **Goal of the project**

To provide **clear, visual, and honest implementations** of search algorithms:
- minimal math when possible  
- visual intuition when helpful  
- references for those who want to go deeper  

No magic. No buzzwords. Just algorithms doing their job.
"""
)
