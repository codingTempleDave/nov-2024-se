"""
Rules:
-Possible values for size: "small", "medium", "large"
-Possible values for clatters: "no", "a bit", "yes"
-Possible values for weight: "light", "medium", "heavy"
-Don't add any item more than once to the result - USE SET??
-The order of names in the output doesn't matter - USE SET??
-It's possible, that multiple items from your wish list have the same attribute values. 
If they match the attributes of one of the presents, add all of them.
"""


def guess_gifts(wishlist, presents): 
    # return a list of the names of all wishlisted presents that you might have gotten.
    matched_gifts = []    

    # Loop through each item in the wishlist
    for item in wishlist:
        #Loop through each present
        for present in presents:
            #Check if the present matches the wishlist attributes
            if (item['size'] == present['size'] and
                item['clatters'] == present['clatters'] and
                item['weight'] == present['weight']):  
                matched_gifts.append(item['name'])
            
    return set(matched_gifts)

wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
        {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
        {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
        {'size': "small", 'clatters': "yes", 'weight': "light"}]

gifts = guess_gifts(wishlist, presents)

print(gifts)