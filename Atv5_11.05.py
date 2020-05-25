def ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    interest.append("interessado em")

def interests_with_people(peoles):
    if peoles == "M" and peoles == "F":
        return peoles

def interest_friends():
    for peoles, user_id in interests:
        peoples[user_id].append(interests)
        if interests[user_id] != peoples:
            return interests[user_id]
            
def interest_common_with_friends():
    if interest_friends != interest:
        for friend in interests:
            friend.append(interests_with_people(friend))
        return friend

print (interest_common_with_friends)
