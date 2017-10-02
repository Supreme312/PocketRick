import discord
import asyncio

pm = discord.Client()

@pm.event
async def on_ready():

	print('He is on.')


@pm.event
async def on_message(message):

	if message.content.startswith('$001'):

		with open ('./Morties/001', 'r') as m001:

			lrl = m001.read()

			await pm.send_file(message.channel, fp='./Pics/PM-001.png', filename=None, content=None, tts=False)

			await pm.send_message(message.channel, lrl)


	if message.content.startswith('$002'):

		with open ('./Morties/002', 'r') as m002:

			await pm.send_file(message.channel, fp='./Pics/PM-002.png', filename=None, content=None, tts=False)

			lrl = m002.read()

			await pm.send_message(message.channel, lrl)



	if message.content.startswith('$003'):

		with open ('./Morties/003', 'r') as m003:

			await pm.send_file(message.channel, fp='./Pics/PM-003.png', filename=None, content=None, tts=False)

			lrl = m003.read()

			await pm.send_message(message.channel, lrl)





	if message.content.startswith('$004'):

		with open ('./Morties/004', 'r') as m004:

			await pm.send_file(message.channel, fp='./Pics/PM-004.png', filename=None, content=None, tts=False)

			lrl = m004.read()

			await pm.send_message(message.channel, lrl)



	if message.content.startswith('$005'):

		with open ('./Morties/005', 'r') as m005:

			await pm.send_file(message.channel, fp='./Pics/PM-005.png', filename=None, content=None, tts=False)

			lrl = m005.read()

			await pm.send_message(message.channel, lrl)


	if message.content.startswith('$006'):

		with open ('./Morties/006', 'r') as m006:

			await pm.send_file(message.channel, fp='./Pics/PM-006.png', filename=None, content=None, tts=False)

			lrl = m006.read()

			await pm.send_message(message.channel, lrl)


	if message.content.startswith('$007'):

		with open ('./Morties/007', 'r') as m007:

			await pm.send_file(message.channel, fp='./Pics/PM-007.png', filename=None, content=None, tts=False)

			lrl = m007.read()

			await pm.send_message(message.channel, lrl)

	if message.content.startswith('$008'):

		with open ('./Morties/008', 'r') as m008:

			await pm.send_file(message.channel, fp='./Pics/PM-008.png', filename=None, content=None, tts=False)

			lrl = m008.read()

			await pm.send_message(message.channel, lrl)
   
   

pm.run('MzY0MTM5MTQ1NjI4NjE0NjU2.DLP0zQ.gv00xxN8A1IEGwg4fS2ELUvii30')

