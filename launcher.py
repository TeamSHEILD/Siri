from siri import Siri
import config
import asyncio

def run_bot():
	loop = asyncio.get_event_loop() 
	bot = Siri()
	bot.run(config.token)
	
if __name__ == '__main__':
	run_bot()
