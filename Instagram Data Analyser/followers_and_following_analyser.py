""" This is a Simple python Script that will analyse the Instagram account data provided in the data folder """
"""
Data Stricture in Dictionary generated is :
Key : Type 
value : [{"insta_id": "...(str)", "insta_link": "...(str)", "java_timestamp": "...(int)"}, ...]
"""
import json
import os
import pickle
import main_vars


def saveAnalysedData(data_dict, fileName):
    with open(fileName, "wb") as pklObj: pickle.dump(data_dict, pklObj)


def check_follow_back(followers, followings):
    followers_id = []
    following_id = []
    for follower in followers: followers_id.append(follower["insta_id"])
    for following in followings: following_id.append(following["insta_id"])

    not_following_back = []
    for following in following_id:
        if following not in followers_id:
            not_following_back.append(following)

    return not_following_back


def accounts_not_followed_back(followers, followings):
    followers_id = []
    following_id = []
    for follower in followers: followers_id.append(follower["insta_id"])
    for following in followings: following_id.append(following["insta_id"])

    accounts_not_followed_back_list = []
    for follower in followers_id:
        if follower not in following_id:
            accounts_not_followed_back_list.append(follower)

    return accounts_not_followed_back_list


if __name__ == '__main__':
    os.chdir(main_vars.latest_data_dir)

    # Finding follower_and_following information
    json_files = []
    for path, dirs, files in os.walk(f"{os.getcwd()}\\followers_and_following"):
        for file in files:
            if file.endswith(".json"):
                json_files.append(f"{path}\\{file}")

    data_collected = {}

    for json_file in json_files:
        with open(json_file) as file_data:
            data = json.load(file_data)
            file_data = []
            for key, val in data.items():
                for item in data[key]:
                    file_data.append({"insta_id": item["string_list_data"][0]["value"], "insta_link": item["string_list_data"][0]["href"], "java_timestamp": item["string_list_data"][0]["timestamp"]})

                data_collected[key] = file_data

    # for key, val in data_collected.items():
    #     print(key)
    #     print("Items in this category are : ")
    #     for item in val:
    #         print(item)
    #     print(end="\n\n\n\n")

    print(f"Accounts that do not follow you back are {check_follow_back(data_collected['relationships_followers'], data_collected['relationships_following'])}")
    print(f"Accounts that you do not follow back are {accounts_not_followed_back(data_collected['relationships_followers'], data_collected['relationships_following'])}")

    print("Analysed Data Saved!")
    saveAnalysedData(data_collected, "D:\\Python\\Playground\\Instagram Data Analyser\\data\\analysed\\_saini_gurnoor_at_02-10-2022.pkl")

