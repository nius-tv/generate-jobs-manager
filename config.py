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
		'next-job': 'calculate-transitions'
	},
	{
		'subscription': 'completed-speech-to-landmarks-2',
		'next-job': 'captions-generator'
	},
	{
		'subscription': 'completed-captions-generator',
		'next-job': 'html-capture'
	},
	{
		'subscription': 'completed-calculate-transitions',
		'next-job': 'pix-to-pix'
	},
	{
		'subscription': 'completed-pix-to-pix',
		'next-job': 'rotate-images'
	},
	{
		'subscription': 'completed-rotate-images',
		'next-job': 'images-to-video'
	},
	{
		'subscription': 'completed-images-to-video',
		'next-job': 'adjust-anchor'
	},
	{
		'subscription': 'completed-adjust-anchor',
		'next-job': 'add-mask'
	},
	{
		'subscription': 'completed-add-mask',
		'next-job': 'animate-anchor'
	},
	{
		'subscription': 'completed-animate-anchor',
		'next-job': 'add-audio-to-story'
	},
	{
		'subscription': 'completed-add-audio-to-story',
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
		'subscription': 'add-category-logo-to-story',
		'next-job': 'images-to-dynamic-overlay'
	},
	{
		'subscription': 'completed-images-to-dynamic-overlay',
		'next-job': 'add-dynamic-overlay-to-story'
	},
	{
		'subscription': 'completed-add-dynamic-overlay-to-story',
		'next-job': 'normalize-audio'
	},
	{
		'subscription': 'completed-normalize-audio',
		'next-job': 'export-story'
	},
	{
		'subscription': 'completed-export-story',
		'next-job': 'end-story'
	},
	{
		'subscription': 'completed-end-story'
	}
]
COMPUTE_PROJECT_NAME = os.environ.get('COMPUTE_PROJECT_NAME')
TMP_STORY_DIR = '/tmp'
