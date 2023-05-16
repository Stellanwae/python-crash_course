'''Using arbitrary keyword arguments'''
def build_profile(first, last, **user_profile):
    '''Making first and last part of the user
    profile'''
    user_profile['first_name'] = first
    user_profile['last_name'] = last
    print(user_profile)
build_profile('albert', 'einstein', location='princeton', field='physics')
