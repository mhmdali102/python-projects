import requests


def main():
    username = "pythonapi123"
    password = "thisistest124"

    auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
    if auth_res.status_code == 200:
        access_token = auth_res.content.decode()

    headers = {"Authorization": f"Bearer {access_token}"}

    groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
    if groups_res.status_code == 200:
        groups_data = groups_res.json()['groups'][0]
        guid = groups_data['guid']

    url = input("Enter url: ")
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)

    if shorten_res.status_code == 200:
        link = shorten_res.json().get("link")
        print("Shortened URL:", link)


if __name__ == '__main__':
    main()