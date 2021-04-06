left_join = lambda phrases:",".join([el.replace("right", "left") for el in phrases])

print(left_join(("left", "wright", "left", "stop")))

