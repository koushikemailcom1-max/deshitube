import streamlit as st

# আপনার বোনের নাম এখানে লিখুন
st.title("🇧🇩 [আপনার বোনের নাম]-এর দেশীটিউব (DeshiTube)")

# ভিডিওর লিংকগুলো এখানে দিন (আপনি যত খুশি যোগ করতে পারেন)
video_urls = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2"
]

st.subheader("পছন্দের ভিডিওর তালিকা:")

# ইউটিউবের মতো করে ভিডিওগুলো দেখাবে
for url in video_urls:
    st.video(url)
