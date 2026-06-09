import streamlit as st
import time

# অ্যাপের শিরোনাম
st.title("🏡 আমাদের এলাকা - কমিউনিটি")

# ১. পোস্ট করার সেকশন
st.subheader("আপনার কথা শেয়ার করুন")
with st.form("post_form", clear_on_submit=True):
    user_name = st.text_input("আপনার নাম")
    user_post = st.text_area("কী ঘটছে আপনার এলাকায়?")
    uploaded_file = st.file_uploader("ছবি বা ভিডিও আপলোড করুন", type=["jpg", "png", "mp4"])
    submit_button = st.form_submit_button("পোস্ট করুন")

    if submit_button:
        if user_name and user_post:
            st.success("আপনার পোস্টটি সফলভাবে পাবলিশ হয়েছে!")
            # এখানে ফায়ারবেস ডাটাবেজে ডাটা পাঠানোর কোড বসবে
        else:
            st.warning("নাম এবং কিছু কথা লিখুন!")

# ২. পোস্ট ফিড (ফেসবুকের মতো)
st.divider()
st.subheader("সাম্প্রতিক পোস্টসমূহ")

# উদাহরণ হিসেবে একটি পোস্ট
st.write("---")
st.markdown(f"**আকাশ আহমেদ:** আমাদের এলাকায় আজ নতুন রাস্তা তৈরির কাজ শুরু হয়েছে।")
st.image("https://via.placeholder.com/600x300", caption="রাস্তার কাজের দৃশ্য")
st.button("লাইক 👍", key="like1")
st.button("কমেন্ট 💬", key="comment1")
