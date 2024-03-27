import instaloader
import requests

about = """\n Welcome to InstaSurface! \n InstaSurface is your go-to tool for quickly fetching essential \n information from Instagram profiles without the \n need to log in. It provides you with surface-level details, \n ensuring a seamless experience while respecting privacy. \n Explore usernames effortlessly and uncover key profile insights \n with ease. Get started with InstaSurface today! 😊📷"""
print(about)

def search_instagram_profile(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    # Print various profile information
    print("\n👤 Username:", profile.username)
    print("👨‍🦰 Full Name:", profile.full_name)
    print("📝 Biography:", profile.biography)
    print("🔗 External URL:", profile.external_url)
    print("🖼️ Profile Pic URL:", profile.profile_pic_url)
    print("📅 Number of Posts:", profile.mediacount)
    print("👥 Number of Followers:", profile.followers)
    print("👣 Number of Following:", profile.followees)
    print("🆔 Profile ID:", profile.userid)
    print("📺 IGTV count:", profile.igtvcount)
    print("🔒 Is Private Account:", profile.is_private)
    print("✅ Is Verified Account:", profile.is_verified)
    print("💼 Is Business Account:", profile.is_business_account)
    print("🏢 Business Category Name:", profile.business_category_name)
    print("🌟 Has Highlight Reels:", profile.has_highlight_reels)

    # Business Information
    if profile.is_business_account:
        print("💼 Business Category:", profile.business_category_name)

# Example usage:
search_username = input("\n   Enter Username: ")
search_instagram_profile(search_username)

