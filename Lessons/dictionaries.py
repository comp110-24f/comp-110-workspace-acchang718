ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["pbj"] = 1  # adds pbj into the dictionary and gives it a value of 1
ice_cream["pbj"] += 10  # adds 10 to pbj's current value
ice_cream["mint"] = 4

print(ice_cream["mint"])  # prints the value of mint

ice_cream.pop(
    "strawberry"
)  # will return the value of strawberry while removing it from the dictionary

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}:{tally}")
