#Gets a user unminted NFTc balance
address = message.content.split(' ',1)[1]
if ".eth" in address:
    r = requests.get('https://ensdata.net/'+address).json()
    try:
        address = r['address']
        r = requests.get('https://nft.habbo.com/api/tokens/balance/?address='+address).json()
        balance = r['balance']
        await message.channel.send("Current balance: " + (str(balance)))
    except:
        await message.channel.send("You tried an invalid ENS")

else:    
    r = requests.get(
        'https://nft.habbo.com/api/tokens/balance/?address='+address).json()
    balance = r['balance']
    await message.channel.send("Current balance: " + (str(balance)))
