import streamlit as st

st.set_page_config(page_title="দেশীটিউব (DeshiTube)", layout="wide")

st.title("🇧🇩 দেশীটিউব (DeshiTube) - আপনার অল-ইন-ওয়ান গ্যালারি")
st.subheader("এখানে ইউটিউব এবং ফেসবুকের প্রিয় ভিডিওগুলো দেখুন")

# ট্যাব তৈরি করা
tab1, tab2, tab3 = st.tabs(["📺 ইউটিউব ভিডিও", "📘 ফেসবুক ভিডিও", "📤 নিজের ফাইল আপলোড"])

with tab1:
    st.header("ইউটিউব গ্যালারি")
    youtube_url = st.text_input("ইউটিউব ভিডিওর লিংক দিন:")
    if youtube_url:
        st.video(youtube_url)

with tab2:
    st.header("ফেসবুক গ্যালারি")
    st.write("ফেসবুকের ভিডিও দেখার জন্য নিচের বক্সে লিংক পেস্ট করুন:")
    fb_url = st.text_input("ফেসবুক ভিডিওর লিংক দিন:")
    if fb_url:
        st.info("দ্রষ্টব্য: ফেসবুক ভিডিওর নিরাপত্তার জন্য এটি সরাসরি প্লে না-ও হতে পারে।")
        st.video(fb_url)

with tab3:
    st.header("নিজের ভিডিও বা ছবি")
    uploaded_file = st.file_uploader("আপনার ডিভাইস থেকে ফাইল সিলেক্ট করুন", type=['mp4', 'mov', 'jpg', 'png'])
    if uploaded_file is not None:
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file)
        else:
            st.video(uploaded_file)
