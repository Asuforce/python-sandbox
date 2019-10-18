import os
import slack
import json
import csv


def get_channels(client):
    channels = client.conversations_list(limit=1000)
    if channels["ok"]:
        return channels["channels"]
    else:
        assert channels["ok"]
        return None


def main():
    cli = slack.WebClient(token=os.environ["SLACK_API_TOKEN"])
    channels = get_channels(cli)

    with open("channel_list.json", "w") as f:
        json.dump(channels, f)

    with open("channel_list.csv", "w") as f:

        w = csv.writer(f)
        w.writerow(channels)


if __name__ == "__main__":
    main()
