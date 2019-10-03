import os
import subprocess
import threading
import time

from config import *
from envsubst import envsubst
from google.cloud import pubsub_v1


def create_story_dir(story_id):
	dir_path = '{}/{}'.format(TMP_STORY_DIR, story_id)
	if not os.path.isfile(dir_path):
		os.mkdir(dir_path)
	return dir_path


def launch_job(story_id, job_name):
	story_dir_path = create_story_dir(story_id)
	job_file_path = prepare_job(story_dir_path, job_name)
	cmd = 'kubectl apply -f {}'.format(job_file_path)
	print('exec:', cmd)
	cmd = ['bash', '-c', cmd]
	subprocess.call(cmd)


def prepare_job(output_dir_path, job_name):
	filename = '{}.yaml'.format(job_name)
	with open(filename) as f:
		data = f.read()

	data = envsubst(data)

	output_file_path = '{}/{}.yaml'.format(output_dir_path, job_name)
	with open(output_file_path, 'w') as f:
		f.write(data)

	return output_file_path


def subscribe(job):
	def callback(message):
		story_id = message.data.decode('utf-8') # binary to utf-8 string
		print('story id:', story_id)

		if next_job:
			launch_job(story_id, next_job)
		else:
			print('finished!')

		message.ack()

	subscription = job['subscription']
	next_job = job.get('next-job')
	print('subscribed to:', subscription)

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
