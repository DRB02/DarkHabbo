collections = {
    "furniture": "0xec4de0a00c694cc7957fb90b9005b24a3f4f8b99",
    "clothes": "0x8c15d753c4336617890ff9e82c88aa047762b867",
    "pets": "0x792df6705032cd3ad8a6aa3b3b7b0a42c0b9759c",
    "addons": "0xacc8b12fd8b08ecea19fb586c0c744f423fc3dd2"
}

    if message.content.lower().startswith(',cheapest'):
        collection = message.content.split(' ', 1)[1]

        if collection in collections:
            collectionadd = collections[collection]

            r = requests.get('https://api.x.immutable.com/v1/orders?auxiliary_fee_percentages=1&auxiliary_fee_recipients=0x12cB8E42c7ec27d30df6Cb8f44aa6445D0e1a78C&buy_token_type=ETH&direction=asc&include_fees=true&order_by=buy_quantity_with_fees&page_size=48&sell_token_address=' +
                             collectionadd+'&sell_token_type=ERC721&status=active').json()
            productname = r['result'][0]['sell']['data']['properties']['name']
            image = r['result'][0]['sell']['data']['properties']['image_url']
            urlcode = r['result'][0]['sell']['data']['token_id']
            pricequantity = r['result'][0]['buy']['data']['quantity']
            pricedecimal = r['result'][0]['buy']['data']['decimals']
            price = int(pricequantity) / (10 ** int(pricedecimal))
            r = requests.get(
                'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()
            eth = r['USD']
            USDprice = price * eth
            embed = discord.Embed(
                title=productname, url='https://furni.app/asset/'+collectionadd+'/'+urlcode)
            embed.add_field(name="ETH:", value=price, inline=True)
            embed.add_field(name="USD:", value=round(USDprice, 2), inline=True)
            embed.set_thumbnail(url=image)
            await message.channel.send(embed=embed)
        else:
            collectionstring = ''
            for collectionitems in collections:
                collectionstring += collectionitems + ' '
            await message.channel.send('Use one of these: '+collectionstring)
