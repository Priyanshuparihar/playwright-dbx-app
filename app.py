import streamlit as st
# from scraper import scrape_quotes

st.title("Playwright Scraper App 🚀")

if st.button("Run Scraper"):
    st.write("Running scraper...")

    # quotes = scrape_quotes()

    st.success("Done!")

    # for i, q in enumerate(quotes, 1):
    #     st.write(f"{i}. {q}")