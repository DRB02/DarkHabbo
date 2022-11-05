#Gets a user unminted NFTc balance
address = message.content.split(' ',1)[1]
r = requests.get('https://nft.habbo.com/api/tokens/balance/?address='+address).json()
balance = r['balance']
await message.channel.send("Current balance: " + (str(balance)))
