import requests

IPFS_GATEWAY = "https://ipfs.io/ipns/"
IPNS_KEY = "k51qzi5uqu5djvfmh4cfgegvdeypgkiv5bm8u9djljncvo2kgxvxglgpbnpuil"

def fetch_latest_dataset():
    url = f"{IPFS_GATEWAY}{IPNS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch dataset:", response.status_code)
        return None
