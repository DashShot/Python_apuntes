
def format_sort_records(records):
    formatted_records = []
    for record in records:
        formatted_name = f"{record[1]:<10}{record[0]:<10}"
        formatted_time = f"{record[2]:.2f}"
        formatted_records.append(f"{formatted_name} {formatted_time:>5}")

    result = '\n'.join(formatted_records)
    return result


PEOPLE = [('Donald', 'Trump', 7.85),
        ('Vladimir', 'Putin', 3.626),
        ('Jinping', 'Xi', 10.603)]

print(format_sort_records(PEOPLE))