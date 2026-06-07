import streamlit as st

st.set_page_config(page_title="দেশীটিউব (DeshiTube)", page_icon="🇧🇩")
st.title("🇧🇩 দেশীটিউব (DeshiTube)")
st.subheader("আপনার ও আপনার বোনের প্রথম মিউজিক প্ল্যাটফর্ম!")

name = st.text_input("এখানে আপনার নাম লিখুন:")
if name:
    st.success(f"অভিনন্দন! {name} এর দেশীটিউব প্রোফাইল এখন সম্পূর্ণ রেডি।")

video_file = st.file_uploader("আপনার গান বা ভিডিও এখানে আপলোড করুন", type=["mp4", "mp3", "mov"])
if video_file is not None:
    st.video(video_file)
    st.balloons()
  
