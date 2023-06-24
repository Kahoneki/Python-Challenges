def online_count(statuses):
    return sum([statuses[i] == "online" for i in statuses])