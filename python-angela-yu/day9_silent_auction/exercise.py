# Belajar Dictionary Nesting

travel_log = {
    "Indonesia": ["Nusa Tenggara", "Papua"], 
    "Asia" : {
        "Japan": ["Kyoto", "Tokyo"],
        "Korea": "Seoul"
    }
}

# Task: gimana cara manggil Papua?
print(travel_log["Indonesia"][1])

# Task: gimana cara manggil Kyoto?
print(travel_log["Asia"]["Japan"][0])

nested_list = ["A", "B", ["C", "D"]]
# Task: gimana cara manggil D?
print(nested_list[2][1])