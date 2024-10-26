#a program that checks whether a given person is a good influencer, 
# that is, whether the person has at least two of the following accounts: 
# Facebook, Twitter or Instagram.

facebook = True
twitter = False
instagram = True

if (facebook and twitter) or (facebook and instagram) or (instagram and twitter):
    print("You are a good influencer")
else:
    print("You need more social media accounts to be a good influencer")