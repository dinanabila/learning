# Belajar Dictionary Nesting

travel_log = {
    "Indonesia": ["Nusa Tenggara", "Papua"], 
    "Asia" : {
        "Japan": ["Kyoto", "Tokyo"],
        "Korea": "Seoul"
    },
    "Europe": "London",
}

# Test: gimana cara manggil Indonesia?
print(list(travel_log.keys())[0])

# Task: gimana cara manggil Papua?
print(travel_log["Indonesia"][1])

# Task: gimana cara manggil Kyoto?
print(travel_log["Asia"]["Japan"][0])

# Task: gimana cara manggil Europe berdasarkan London?
for key, value in travel_log.items():
    if value == 'London':
        print(key)

nested_list = ["A", "B", ["C", "D"]]
# Task: gimana cara manggil D?
print(nested_list[2][1])