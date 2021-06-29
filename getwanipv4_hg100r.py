import json
import requests

def get_token(api_url: str, hashed_password: str) -> str:
    payload = {
        'method': 'login',
        'id': 1,
        'jsonrpc': '2.0',
        'params': {
            'id': 'admin',
            'password': hashed_password,
        },
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    res = requests.post(api_url, headers=headers, data=json.dumps(payload))
    response = res.json()

    token = response['token']
    return token

def get_wan_ipv4(api_url: str, token: str) -> str:
    payload = {
        'method': 'QuickSetupInfo',
        'id': 90,
        'jsonrpc': '2.0',
        'token': token,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    res = requests.post(api_url, headers=headers, data=json.dumps(payload))
    response = res.json()

    result = response['result']

    ipv4_addr = result['NET_WAN_IPv4_Address']
    return ipv4_addr


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('api_url', type=str)
    parser.add_argument('hashed_password', type=str)
    args = parser.parse_args()

    api_url = args.api_url
    hashed_password = args.hashed_password

    token = get_token(api_url=api_url, hashed_password=hashed_password)
    ipv4_addr = get_wan_ipv4(api_url=api_url, token=token)

    print(ipv4_addr)
