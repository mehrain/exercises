def get_avg_brand_followers(all_handles=None, brand_name=None):
    brand_counted = 0
    influencer_quantity = 0
    
    if all_handles == None or brand_name == None:
        raise ValueError("Handles or brandname is empty")

    for lists in all_handles:
        influencer_quantity += 1
        for handles in lists:
            if brand_name in handles:
                brand_counted += 1
    return brand_counted / influencer_quantity
