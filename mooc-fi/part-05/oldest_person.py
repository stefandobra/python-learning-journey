# def oldest_person(people: list):
#     return min(people, key=lambda x: x[1])[0]

def oldest_person(people: list):
    oldest = people[0]

    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]

