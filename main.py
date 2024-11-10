# streamlit user interface to interact with llm.
# Selenium allows to activate web browser.
import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)

#from parse import parse_with_ollama

# give a title
st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

# if button is clicked then do this
if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    # expander text box
    # next part is take this dom content and pass it to LLM for it to parse.
    with st.expander("View DOM Content"):
        st.text_area("DOM content", cleaned_content, height=300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
            # pass this into LLM
            # we are taking this chunks and passing them into LLM.
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # what information we want from this data
            #result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
            