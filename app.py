import streamlit as st
import requests

st.set_page_config(page_title="দেশীটিউব - গ্যালারি", layout="wide")
st.title("🇧🇩 দেশীটিউব (DeshiTube)")

# ভিডিও তালিকা (এখানে আপনার পছন্দের বাংলাদেশের ভিডিওর লিংক দিন)
videos = [
    {"title": "বাংলাদেশের সংস্কৃতি", "url": "https://www.youtube.com/watch?v=উদাহরণ১"},
    {"title": "শিক্ষামূলক ক্লাস", "url": "https://www.youtube.com/watch?v=উদাহরণ২"}
]

# গ্রিড আকারে ভিডিও প্রদর্শন
cols = st.columns(2)
for i, video in enumerate(videos):
    with cols[i % 2]:
        st.subheader(video['title'])
        st.video(video['url'])
        
        # ডাউনলোড বাটন (এটি ব্রাউজারে ফাইল ডাউনলোড করবে)
        st.info("দ্রষ্টব্য: ইউটিউব ভিডিওর স্বত্বাধিকারের কারণে সরাসরি ডাউনলোড বাটন দেওয়া সীমাবদ্ধ।")
        st.write("ভিডিওটি দেখতে এখানে ক্লিক করুন। অফলাইনে দেখার জন্য ইউটিউব অ্যাপের অফলাইন ফিচার ব্যবহার করুন।")

st.sidebar.header("আপনার প্রোফাইল")
st.sidebar.write("এটি আপনার পার্সোনাল লার্নিং হাব।")
