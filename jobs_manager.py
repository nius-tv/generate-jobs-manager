import subprocess
import threading
import time

from config import *
from google.cloud import pubsub_v1


def launch_job(name):
	cmd = 'kubectl apply -f {}.yaml'.format(name)
	print('exec:', cmd)
	cmd = ['bash', '-c', cmd]
	subprocess.call(cmd)


def subscribe(job):
	subscription = job['subscription']
	print('subscribed to:', subscription)

	def callback(message):
		data = message.data.decode('utf-8') # binary to utf-8 string
		print('message received:', data)

		if 'next-job' in job:
			launch_job(job['next-job'])
		else:
			print('finished!')

		message.ack()

	subscriber = pubsub_v1.SubscriberClient()
	subscription_path = subscriber.subscription_path(PROJECT_ID, subscription)
	subscriber.subscribe(subscription_path, callback=callback)


if __name__ == '__main__':
	for job in JOBS:
		thread = threading.Thread(target=subscribe, args=(job,))
		thread.start()

	# Prevents app from exiting
	while True:
		time.sleep(60)
