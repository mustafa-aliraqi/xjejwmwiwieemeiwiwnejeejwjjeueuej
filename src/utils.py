from time import time
import samino
from json import load
from time import sleep
from threading import Thread
from tabulate import tabulate
from src.library import amino
import random
from concurrent.futures import ThreadPoolExecutor


accounts = []
with open("accounts.json") as database:
	data = load(database)
	for account in data:
		accounts.append(account)


def login(client: amino.Client, email: str, password: str):
	try:
		print(f"[deviceID]::: {account['device']}")
		client.login(
			email=email, password=password, socket=False)
		print(f"[Logged in]::: {email}")
	except Exception as e:
		print(f"[Error in login]::: {e}")
        
        
def get_timers():
	return {"start": int(time()), "end": int(time()) + 300}


def coin_generator(client: amino.Client, ndc_id: int, email: str, delay: int):
	timers = [get_timers() for _ in range(50)]
	client.send_active_object(ndc_id=ndc_id, timers=timers)
	print(f"[Generating coins in]::: {email}")


def generate_coins(client: amino.Client, ndc_id: int, email: str, delay: int):
	Thread(target=coin_generator, args=(client, ndc_id, email, delay)).start()
	
	
def play_lottery(client: amino.Client, ndc_id: int):
	try:
		lottery = client.lottery(ndc_id=ndc_id)["api:message"]
		print(f"[Lottery]::: {lottery}")
	except Exception as e:
		print(f"[Error in play lottery]::: {e}")
		
		
def watch_ad(client: amino.Client):
	try:
		watch_ad = client.watch_ad()["api:message"]
		print(f"[Watch ad]::: {watch_ad}")
	except Exception as e:
		print(f"[Error in watch ad]::: {e}")
	
def blog_spam():
	comu9 = amino.Client().get_from_code(
	input("[Community link]::: "))["linkInfoV2"]["extensions"]["community"]["ndcId"]
	title=input("[Title]::: ")	
	content=input("[Content]::: ")
	for account in accounts:
		c = samino.Client(deviceId=account["device"])
		email = account["email"]
		password = account["password"]
		c.login(email,password)
		local = samino.Local(comu9)
		try:
			c.join_community(comu9)			
			local.post_blog(title=title,content=content)
			local.post_blog(title=title,content=content)
			local.post_blog(title=title,content=content)
		except Exception as e:
			print("[Error in blog spam]::: "+str(e))
		
def spam():
	msg99=input("[Msg]::: ").split()
	link99 = amino.Client().get_from_code(
	input("[Chat link]::: "))["linkInfoV2"]["extensions"]["linkInfo"]
	for account in accounts:
		c=samino.Client(deviceId=account["device"])
		email = account["email"]
		password = account["password"]
		c.login(email,password)
		local = samino.Local(link99["ndcId"])
		try:
			c.join_community(link99["ndcId"])
			local.join_chat(chatId=link99["objectId"])
		except:
			pass
		def lol98():
			try:
				while True:
					local.send_message(link99["objectId"],random.choice(msg99),messageType=0)
			except Exception as e:
				print(f"[Error in spam]::: {e}")
		Thread(target=lol98(),daemon=True).start()
							
def transfer_coins():
	link_info = amino.Client().get_from_code(
		input("[Blog link]::: "))["linkInfoV2"]["extensions"]["linkInfo"]
	ndc_id = link_info["ndcId"]
	blog_id = str(link_info["objectId"])
	delay = int(input("[Transfer delay in seconds]::: "))
	for account in accounts:
		client = amino.Client(device_id=account["device"])
		c = samino.Client(deviceId=account["device"])
		email = account["email"]
		password = account["password"]
		try:
			login(client=client, email=email, password=password)
			c.login(email,password)
			local = samino.Local(ndc_id)
			c.join_community(ndc_id)
			total_coins = client.get_wallet_info()["wallet"]["totalCoins"]
			print(f"[{email} total coins]::: {total_coins}")
			if total_coins != 0:
				local.tip_coins(coins=total_coins,blogId=blog_id)
				print(f"[{email} sent]::: {total_coins}")
			elif total_coins > 500:
				total_coins = 500
				local.tip_coins(coins=total_coins,blogId=blog_id)
				print(f"[{email} sent]::: {total_coins}")
			sleep(delay)
		except Exception as e:
			print(f"[Error in transfer coins]::: {e}")


def main_process():
	ndc_id = amino.Client().get_from_code(
		input("[Community link]::: "))["linkInfoV2"]["extensions"]["community"]["ndcId"]
	delay = int(input("[Generation delay in seconds]::: "))
	for account in accounts:
		client = amino.Client(device_id=account["device"])
		c = samino.Client(deviceId=account["device"])
		email = account["email"]
		password = account["password"]
		try:
			c.login(email,password)
			c.join_community(ndc_id)
			login(client=client, email=email, password=password)
			play_lottery(client=client, ndc_id=ndc_id)
			watch_ad(client=client)
			with ThreadPoolExecutor(max_workers=100) as executor: 
				[executor.submit(generate_coins(client, ndc_id, email, delay)) for _ in range(25)]
			sleep(delay)
		except Exception as e:
			print(f"[Error in main process]::: {e}")
