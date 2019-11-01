import os

JOBS = [
	{
		'subscription': 'init-generate',
		'next-job': 'init-story'
	},
	{
		'subscription': 'completed-init-story',
		'next-job': 'text-to-spec'
	},
	{
		'subscription': 'completed-text-to-spec',
		'next-job': 'speech-to-landmarks'
	},
	{
		'subscription': 'completed-speech-to-landmarks',
		'next-job': 'prepare-for-inference'
	},
	{
		'subscription': 'completed-prepare-for-inference',
		'next-job': 'pix-to-pix'
	},
	{
		'subscription': 'completed-pix-to-pix',
		'next-job': 'images-to-video'
	},
	{
		'subscription': 'completed-images-to-video',
		'next-job': 'add-audio-to-story'
	},
	{
		'subscription': 'completed-add-audio-to-story',
		'next-job': 'rotate-video'
	},
	{
		'subscription': 'completed-rotate-video',
		'next-job': 'add-presenter-bg'
	},
	{
		'subscription': 'completed-add-presenter-bg',
		'next-job': 'add-bg-to-story'
	},
	{
		'subscription': 'completed-add-bg-to-story',
		'next-job': 'add-images-to-story'
	},
	{
		'subscription': 'completed-add-images-to-story',
		'next-job': 'add-category-logo-to-story'
	},
	{
		'subscription': 'completed-add-category-logo-to-story',
		'next-job': 'html-capture'
	},
	{
		'subscription': 'completed-html-capture',
		'next-job': 'normalize-audio'
	},
	{
		'subscription': 'completed-normalize-audio',
		'next-job': 'end-story'
	},
	{
		'subscription': 'completed-end-story'
	}
]
COMPUTE_PROJECT_NAME = os.environ.get('COMPUTE_PROJECT_NAME')
TMP_STORY_DIR = '/tmp'
