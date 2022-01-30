import requests, json, time

with open("config.json", "r") as config:
    config = json.load(config)

cookie = config['cookie']
assetid = config['id']

def main():
    check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': (cookie)})
    if check.status_code == 200:
        try:
          base = requests.get(f"https://api.roblox.com/Marketplace/ProductInfo?assetId={assetid}").json()
          productid = base['ProductId']
          sellerid = base['Creator']['CreatorTargetId']
          price = base['PriceInRobux']
          name = base['Name']
          xcsrf = requests.post("https://auth.roblox.com/v2/logout", cookies={'.ROBLOSECURITY': cookie})
          token = (xcsrf.headers["x-csrf-token"])
          purchase = requests.post(f"https://economy.roblox.com/v2/user-products/{productid}/purchase", data={"expectedCurrency": 1,"expectedPrice": price,"expectedSellerId": sellerid}, cookies={'.ROBLOSECURITY': (cookie)}, headers={'x-csrf-token': token})
          if purchase.status_code == 200:
              print(f"Successfully bought {name} for {price}R$")
              time.sleep(3)
          else:
              print("Purchase failed!")
              time.sleep(3)
        except:
            print("Unexpected error!")
            time.sleep(3)
    else:
        print("Invalid Cookie!")
        time.sleep(3)

main()
