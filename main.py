import streamlit as st

# Define the pages
pages = {
    "Home": "Welcome to the home page!",
    "About Me": "This is where you share your story.",
    "Projects": "Here are some of my projects.",
    "Contact": "Feel free to reach out via email."
}

# Get the current page from query parameters
current_page = st.query_params.get("page", ["Home"])[0]

# Ensure current_page is a valid key
if current_page not in pages:
    current_page = "Home"  # Default to Home if invalid

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page:", list(pages.keys()), index=list(pages.keys()).index(current_page))

# Update the URL when the page is changed
if page != current_page:
    st.experimental_set_query_params(page=page)  # Only update URL when page changes

# Display the selected page content
st.title(page)
st.write(pages[page])
