import streamlit as st

# অ্যাপের শিরোনাম (আপনার বোনের নাম এখানে বসিয়ে দিন)
st.title("🇧🇩 [বোনের নাম]-এর দেশীটিউব (DeshiTube)")
st.write("এটি আপনার বোনের জন্য তৈরি একটি স্পেশাল ভিডিও গ্যালারি।")

# ইউটিউব ভিডিওর লিংকগুলো এখানে যোগ করুন
# এখানে লিংকগুলো পরিবর্তন করলেই আপনার অ্যাপে নতুন ভিডিও যোগ হবে
video_list = {
    "ভিডিও শিরোনাম ১": "https://www.youtube.com/watch?v=ভিডিওর_আইডি_১",
    "ভিডিও শিরোনাম ২": "https://www.youtube.com/watch?v=ভিডিওর_আইডি_২",
    "ভিডিও শিরোনাম ৩": "https://www.youtube.com/watch?v=ভিডিওর_আইডি_৩"
}

# ভিডিওগুলো সাজিয়ে দেখানোর কোড
st.subheader("আপনার প্রিয় ভিডিওসমূহ:")
for title, url in video_list.items():
    st.markdown(f"### {title}")
    st.video(url)

# নতুন কিছু শেয়ার করার জন্য আপলোডার (যদি প্রয়োজন হয়)
st.divider()
st.subheader("আপনার ব্যক্তিগত ভিডিও আপলোড করুন:")
uploaded_file = st.file_uploader("নিজের ফাইল থেকে ভিডিও শেয়ার করুন", type=['mp4', 'mov'])
if uploaded_file is not None:
    st.video(uploaded_file)
