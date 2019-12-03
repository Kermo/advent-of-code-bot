import requests
import json
import datetime
from datetime import timezone


def load_json_data():
    url = "https://adventofcode.com/2019/leaderboard/private/view/21796.json"
    session_id = ""
    cookie = {"session": session_id}

    post_response = requests.post(url, cookies=cookie)
    json_data = json.loads(post_response.text)

    return json_data


def send_slack_msg(name, challenge, part, stars, points):
    real_webhook_url = ""
    own_webhook_url = ""
    msg = "{} solved day {} part {} and has now {} :star: and {} points. Congratulations!".format(name, challenge, part, stars, points)
    payload = '{"text" : "' + msg + '"}'
    req = requests.post(own_webhook_url, headers={"Content-Type":"application/x-www-form-urlencoded"}, data=payload.encode('utf-8'))



def find_newest_completion():
    json = load_json_data()

    for id in json["members"]:
        member_object = json["members"][id]
        name_st = member_object["name"]
        stars_st = member_object["stars"]
        points_st = member_object["local_score"]

        dt = datetime.datetime.now()
        last_star_ts = member_object["last_star_ts"]

        if dt.timestamp() - int(last_star_ts) < 61:

            for challenges in member_object["completion_day_level"]:
                challenge_days = member_object["completion_day_level"][challenges]

                for day in challenge_days:
                    part_times = challenge_days[day]
                    for star_time in part_times:
                        if int(part_times[star_time]) == int(last_star_ts):
                            day_ts = challenges
                            part_ts = day

                            send_slack_msg(name_st, day_ts, part_ts, stars_st, points_st)


find_newest_completion()
