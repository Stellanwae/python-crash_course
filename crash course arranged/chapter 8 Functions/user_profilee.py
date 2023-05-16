def build_profile(first, last, **user_profile):
    user_profile['First_name'] = first
    user_profile['Last_name'] = last
    print(user_profile)
build_profile("Stella", "Nicole", location = "kenya", field = "software development")
