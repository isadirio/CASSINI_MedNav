import streamlit as st
import base64

# Page config
st.set_page_config(page_title="MedNav: Smart Prevention Navigator", layout="wide")

# Title and description
st.markdown("## 🛰️ MedNav: Smart Prevention Navigator")
st.markdown("""
This demo shows how MedNav uses satellite data to anticipate health risks and suggest targeted prevention kits.
""")

# Sidebar simulated chat
st.sidebar.header("💬 AI-powered Agent")
query = st.sidebar.text_input("Ask something about the emergency kit:")

if query:
    query_lower = query.lower()
    if "where" in query_lower or "buy" in query_lower or "purchase" in query_lower:
        st.sidebar.markdown("**🤖**: You can find these items in most pharmacies or emergency supply stores online.")
    elif "mask" in query_lower:
        st.sidebar.markdown("**🤖**: FFP2 or FFP3 masks are strongly recommended in volcanic ash environments.")
    elif "kit" in query_lower:
        st.sidebar.markdown("**🤖**: The suggested kit includes masks, eye drops, burn dressings, and a bronchodilator.")
    else:
        st.sidebar.markdown("**🤖**: For volcanic risk, prioritize respiratory protection and eye care.")

# Two-column layout: video (left), suggested kit (right)
st.markdown("---")
left_col, right_col = st.columns(2)

with left_col:
    try:
        with open("lava_evolution.mp4", "rb") as video_file:
            video_bytes = video_file.read()
            st.video(video_bytes)
    except FileNotFoundError:
        st.error("⚠️ Video file 'lava_evolution.mp4' not found.")

with right_col:
    st.subheader("🧰 Suggested Kit for Volcanic Risk")
    st.markdown("""
Volcanic eruptions may cause respiratory issues due to ash and gas exposure.

**Recommended items:**
- FFP2/FFP3 masks  
- Sterile eye drops  
- Burn dressings  
- Bronchodilator (if prescribed)  
""")

    # Downloadable text file for the kit
    kit_text = """Suggested Kit for Volcanic Risk:

- FFP2/FFP3 masks
- Sterile eye drops
- Burn dressings
- Bronchodilator (if prescribed)

Always prepare this kit in volcanic-prone zones.
"""
    b64 = base64.b64encode(kit_text.encode()).decode()
    download_link = f'<a href="data:file/txt;base64,{b64}" download="volcanic_kit.txt">📥 Download Kit as TXT</a>'
    st.markdown(download_link, unsafe_allow_html=True)
