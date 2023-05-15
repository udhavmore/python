def online_stat(statuses: dict):
    online_users = []
    for k,v in statuses.items():
        if statuses[k] == 'online':
            online_users.append(k)
    return len(online_users)

status_dict = {
    "udhav": "online",
    "suraj": "offline",
    "bharat": "offline",
    "kiran": "online",
    "puneet": "online"
}

print(online_stat(status_dict))
