from random import randrange

teams = {}

def main():
    with open("topics.txt") as file:
        txt = file.read()
        topics = txt.split(", ")
    num_teams = len(topics)
    for i in range(num_teams):
        teams[f"team{i + 1}"] = []
    with open("expierenced_members.txt") as file:
        txt = file.read()
        expierenced = txt.split(", ")
    with open("unexpierenced_members.txt") as file:
        txt = file.read()
        unexpierenced = txt.split(", ")
    shuffle(expierenced)
    shuffle(unexpierenced)
    exp_per_team = int(len(expierenced) / num_teams)
    unexp_per_team = int(len(unexpierenced) / num_teams)
    exp_rem = len(expierenced) % num_teams
    unexp_rem = len(unexpierenced) % num_teams
    organize(expierenced, len(expierenced) - exp_rem, exp_per_team)
    organize(unexpierenced, len(unexpierenced) - unexp_rem, unexp_per_team)
    if exp_rem != 0:
        organize_rem(expierenced, exp_per_team * num_teams)
    if unexp_rem != 0:
        organize_rem(unexpierenced, unexp_per_team * num_teams)
    with open("teams.txt", "w") as file:
        file.write("")
    with open("teams.txt", "a") as file:
        topic_index = 0
        for value in teams.values():
            add_comma(value)
            members =  "".join(value)
            members = members.replace(",", ", ")
            file.write(f"{topics[topic_index]}: {members}")
            topic_index += 1
            if topic_index < num_teams:
                file.write("\n")


def organize(members, mem_count, count):
    team = 1
    prev_i = 0
    for i in range(count, mem_count + 1, count):
        for j in range(prev_i, i):
            teams[f"team{team}"].append(members[j])
        prev_i = i
        team += 1


def organize_rem(members, start):
    sorted_teams = sorted(teams, key=lambda key: len(teams[key]))
    team_index = 0
    for i in range(start, len(members)):
        teams[sorted_teams[team_index]].append(members[i])
        team_index += 1


def add_comma(members):
    for i in range(len(members) - 1):
        members[i] = members[i] + ","

    
def shuffle(arr):
    last_index = len(arr) - 1
    while last_index > 0:
        rand_index = randrange(last_index)
        temp = arr[last_index]
        arr[last_index] = arr[rand_index]
        arr[rand_index] = temp
        last_index -= 1
    

if __name__ == "__main__":
    main()