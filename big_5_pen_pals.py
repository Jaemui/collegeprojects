import json
import pandas as pd

def loadFile(filename):
    f = open(filename)
    data = json.load(f)
    return data

def sort_school(schoolName):
    students = []
    for i in data:
        if data[i][0]["School"] == schoolName:
            students.append(i)
    return students

# def sort_year(Year):
#     students = []
#     for i in data:
#         if data[i][0]["Year?"] == Year:
#             students.append(i)
#     return students
#
# def sort_phone(Phone):
#     students = []
#     for i in data:
#         if data[i][0]["Do you have an iPhone or Android?"] == Phone:
#             students.append(i)
#     return students

def group_pref(pref):
    students = []
    for i in data:
        if data[i][0]["Would you like to be paired with one person or with a group?"] == pref:
            students.append(i)
    return students

def hobbies(hobbies):
    students = []
    for i in data:
        if data[i][0]["Type of Person"] == hobbies:
            students.append(i)
    return students

def createGroupYearHobby(phone_type,year,group_pref,hobby):
    group = []
    same_year_leftovers = []
    ucla_count = 0
    usc_count = 0
    uci_count = 0
    ucsd_count = 0
    ucr_count = 0
    for person in ucla_students:
        if data[person][0]["School"] == "UCLA" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (ucla_count<2):
            if data[person][0]["Type of Person"] == hobby:
                group.append(person)
                ucla_count += 1
                #print(person)
                ucla_students.pop(ucla_students.index(person))
    for person in usc_students:
        if data[person][0]["School"] == "USC" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (usc_count<1):
            if data[person][0]["Type of Person"] == hobby:
                group.append(person)
                usc_count += 1
                #print(person)
                usc_students.pop(usc_students.index(person))
    for person in uci_students:
        if data[person][0]["School"] == "UCI" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (uci_count<1):
            if data[person][0]["Type of Person"] == hobby:
                group.append(person)
                uci_count+= 1
                uci_students.pop(uci_students.index(person))
            else:
                break

    for person in ucsd_students:
        if data[person][0]["School"] == "UCSD" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (ucsd_count<1):
            if data[person][0]["Type of Person"] == hobby:
                group.append(person)
                ucsd_count += 1
                #print(person)
                ucsd_students.pop(ucsd_students.index(person))
    return group

# def createHobby(phone_type,hobby):

def createGroup(phone_type,year,group_pref):
    group = []
    same_year_leftovers = []
    ucla_count = 0
    usc_count = 0
    uci_count = 0
    ucsd_count = 0
    ucr_count = 0
    for person in ucla_students:
        if data[person][0]["School"] == "UCLA" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (ucla_count<2):
            group.append(person)
            ucla_count += 1
                #print(person)
            ucla_students.pop(ucla_students.index(person))
    for person in usc_students:
        if data[person][0]["School"] == "USC" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (usc_count<1):
            group.append(person)
            usc_count += 1
            usc_students.pop(usc_students.index(person))
    for person in uci_students:
        if data[person][0]["School"] == "UCI" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (uci_count<1):
            group.append(person)
            uci_count+= 1
            uci_students.pop(uci_students.index(person))
    for person in ucsd_students:
        if data[person][0]["School"] == "UCSD" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and data[person][0]["Would you like to be paired with one person or with a group?"] == group_pref and (ucsd_count<1):
            group.append(person)
            ucsd_count += 1
            ucsd_students.pop(ucsd_students.index(person))
    return group
def createDuo(phone_type,year):
    pair = []
    ucla_count = 0
    usc_count = 0
    uci_count = 0
    ucsd_count = 0
    ucr_count = 0
    for person in duos:
        if len(pair) == 2:
            break
        elif data[person][0]["School"] == "UCLA" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and ucla_count <1:
            pair.append(person)
            ucla_count += 1
            ucla_students.pop(ucla_students.index(person))
            duos.pop(duos.index(person))
        elif data[person][0]["School"] == "USC" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and usc_count <1:
            pair.append(person)
            usc_count += 1
            usc_students.pop(usc_students.index(person))
            duos.pop(duos.index(person))
        elif data[person][0]["School"] == "UCI" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and uci_count <1:
            pair.append(person)
            uci_count += 1
            uci_students.pop(uci_students.index(person))
            duos.pop(duos.index(person))
        elif data[person][0]["School"] == "UCSD" and data[person][0]["Do you have an iPhone or Android?"] == phone_type and data[person][0]["Year?"] == year and ucsd_count <1:
            pair.append(person)
            ucsd_count+= 1
            ucsd_students.pop(ucsd_students.index(person))
            duos.pop(duos.index(person))
    return pair

def compile_info(group):
    all_info = []
    for person in group:
        person_info = dict({"Name": person, "School": data[person][0]["School"], "Phone Number": data[person][0]["Phone Number"], "Socials": data[person][0]["Social Media (FB"]["Instagram Handle)"]})
        all_info.append(person_info)
    return all_info

if __name__ == '__main__':
    data = loadFile("big_5.json")
    ucla_students = sort_school("UCLA")
    usc_students = sort_school("USC")
    ucsd_students = sort_school("UCSD")
    uci_students = sort_school("UCI")
    ucr_students = sort_school("UCR")
    duos = group_pref("One individual")
    # groupies = group_pref("Group chat")
    # gamers = hobbies("Gamer")
    # athletes = hobbies("Sports")
    #
    # while gamers:
    #     first_year_group_gamers = createGroupYearHobby("IPHONE", "First Year", "Group chat", "Gamer")
    #     for name in first_year_group_gamers:
    #         gamers.remove(name)
    #     second_year_group_gamers = createGroupYearHobby("IPHONE", "Second Year", "Group chat", "Gamer")
    #     for name in second_year_group_gamers:
    #         gamers.remove(name)
    #     third_year_group_gamers = createGroupYearHobby("IPHONE", "Third Year", "Group chat", "Gamer")
    #     for name in third_year_group_gamers:
    #         gamers.remove(name)
    #     fourth_year_group_gamers = createGroupYearHobby("IPHONE", "Fourth Year", "Groupchat", "Gamer")
    #     for name in fourth_year_group_gamers:
    #         gamers.remove(name)
    #     print(first_year_group_gamers)
    #     print(second_year_group_gamers)
    #     print(third_year_group_gamers)
    #     print(fourth_year_group_gamers)
    #
    # while athletes:
    #     first_year_group_athletes = createGroupYearHobby("IPHONE", "First Year", "Group chat", "Sports")
    #     for name in first_year_group_athletes:
    #         athletes.remove(name)
    #     second_year_group_athletes = createGroupYearHobby("IPHONE", "Second Year", "Group chat", "Sports")
    #     for name in second_year_group_athletes:
    #         athletes.remove(name)
    #     third_year_group_athletes = createGroupYearHobby("IPHONE", "Third Year", "Group chat", "Sports")
    #     for name in third_year_group_athletes:
    #         athletes.remove(name)
    #     fourth_year_group_athletes = createGroupYearHobby("IPHONE", "Fourth Year", "Groupchat", "Sports")
    #     for name in fourth_year_group_athletes:
    #         athletes.remove(name)
    #     print(first_year_group_athletes)
    #     print(second_year_group_athletes)
    #     print(third_year_group_athletes)
    #     print(fourth_year_group_athletes)


    while ucla_students and usc_students and ucsd_students and uci_students:

        first_year_group_iphone = compile_info(createGroup("IPHONE","First Year","Group chat"))
        second_year_group_iphone = compile_info(createGroup("IPHONE","Second Year","Group chat"))
        third_year_group_iphone = compile_info(createGroup("IPHONE","Third Year","Group chat"))
        fourth_year_group_iphone = compile_info(createGroup("IPHONE","Fourth Year","Group chat"))

        first_year_group_android = compile_info(createGroup("ANDROID", "First Year", "Group chat"))
        second_year_group_android = compile_info(createGroup("ANDROID", "Second Year", "Group chat"))
        third_year_group_android = compile_info(createGroup("ANDROID", "Third Year", "Group chat"))
        fourth_year_group_android = compile_info(createGroup("ANDROID", "Fourth Year", "Group chat"))

        first_year_solo_iphone = compile_info(createDuo("IPHONE","First Year"))
        second_year_solo_iphone = compile_info(createDuo("IPHONE","Second Year"))
        third_year_solo_iphone = compile_info(createDuo("IPHONE", "Third Year"))
        fourth_year_solo_iphone = compile_info(createDuo("IPHONE", "Fourth Year"))

        first_year_solo_android = compile_info(createDuo("ANDROID", "First Year"))
        second_year_solo_android = compile_info(createDuo("ANDROID", "Second Year"))
        third_year_solo_android = compile_info(createDuo("ANDROID", "Third Year"))
        fourth_year_solo_android = compile_info(createDuo("ANDROID", "Fourth Year"))

        df = pd.DataFrame(fourth_year_group_iphone) #Run the code multiple times while changing this to each group to append to matches.csv
        df.to_csv('matches.csv', mode = "a", index=False)





