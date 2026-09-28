def get_next_id(items):
    if len(items) == 0:
        return 1

    largest_id = 0

    for item in items:
        if item["id"] > largest_id:
            largest_id = item["id"]

    return largest_id + 1
