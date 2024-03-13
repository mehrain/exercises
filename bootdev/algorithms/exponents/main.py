def get_estimated_spread(audiences_followers):
    avarage_followers = sum(audiences_followers) / len(audiences_followers)
    return avarage_followers * (len(audiences_followers) ** 1.2)