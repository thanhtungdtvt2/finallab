import requests
import json
base_url = "https://api.meraki.com/api/v1"
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

# cau a,b
def get_orgs():
    url = f"{base_url}/organizations"
    headers = {
        "Content-type": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.get(url=url, headers=headers)
    data = response.json()
    print(json.dumps(data, indent=4))
    


def get_org_inv_devices():
    org_id = 681155
    url = f"{base_url}/organizations/{org_id}/inventory/devices"
    headers = {
        "Content-type": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    
    response = requests.get(url=url, headers=headers)
    data = response.json()
    # print(json.dumps(data, indent=4))
    return data



def find_devices():
    devices = get_org_inv_devices()
    
    for i in range (len(devices)):
        if devices[i]['networkId'] == None:
            print(devices[i])

if __name__ == '__main__':
    #get_orgs()
    # get_org_inv_devices()
    find_devices()