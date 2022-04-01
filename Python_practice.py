counties={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

# for county in counties:
#     print(f'{counties.keys()} has {counties.values(county)} registered voters')

# for county in counties.keys():
#     print(county)
# for voters in counties.values():
#     print(voters)
# for county,voters in counties.items():
#     print(county+" county has "+str(voters) +" registered voters")

# voting_data = {"county":"Arapahoe", "registered_voters": 422829},"county":"Denver", "registered_voters": 463353,"county":"Jefferson", "registered_voters": 432438}

for county_dict, registered_dict in counties.items():
    print(f"{county_dict} has {registered_dict} registered voters.")