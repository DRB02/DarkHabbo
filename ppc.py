total = 0
alllisted = 0
tokenamounts = ['Habbo Credit 10', 'Habbo Credit 50', 'Habbo Credit 100', 'Habbo Credit 500', 'Habbo Credit 1000', 'Habbo Credit 10000', 'Habbo Credit 50000', 'Habbo Credit 100000']
ethprice = requests.get(
    'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()
embed = discord.Embed(title='Price Per Credit')
for tokenamount in tokenamounts:
    r = requests.get('https://api.x.immutable.com/v1/orders?auxiliary_fee_percentages=1&auxiliary_fee_recipients=0x12cB8E42c7ec27d30df6Cb8f44aa6445D0e1a78C&buy_token_type=ETH&direction=asc&include_fees=true&order_by=buy_quantity_with_fees&page_size=48&sell_token_address=0xfbf1c1c09a94fe45ea8cc981c478816963ec958c&sell_token_type=ERC721&status=active&sell_token_name='+tokenamount).json()
    for results in r['result']:
        if tokenamount == results['sell']['data']['properties']['name']:
            productname = results['sell']['data']['properties']['name']
            pricequantity = results['buy']['data']['quantity']
            pricedecimal = results['buy']['data']['decimals']
            price = int(pricequantity) / (10 ** int(pricedecimal))
            eth = ethprice['USD']
            USDprice = price * eth
            tokens = int(tokenamount.replace('Habbo Credit ', ''))
            ppc = round(USDprice/tokens, 3)
            if tokens <= 1000:
                total = total + ppc
                alllisted = alllisted + 1
            # embed.add_field(name=productname, value='$'+(str(ppc))+'\n[$'+(str(round(USDprice,2)))+'](https://market.immutable.com/collections/0xfbf1c1c09a94fe45ea8cc981c478816963ec958c?keywordSearch='+(str(tokens))+')', inline=False)
            embed.add_field(name=productname, value='$'+(str(ppc))+'\n[$'+(str(round(USDprice, 2)))+'](https://furni.app/furni/'+(tokenamount.replace(' ', '-'))+')', inline=False)
            break
# Only uses 10, 50, 100, 500 and 1000 for average ppc
total = (total/alllisted)
embed.set_footer(text="Average ppc is $" + (str(round(total, 3))))
await message.channel.send(embed=embed)
