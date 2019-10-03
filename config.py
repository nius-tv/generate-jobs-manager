JOBS = [
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
		'next-job': 'add-audio-to-video'
	},
	{
		'subscription': 'completed-add-audio-to-video',
		'next-job': 'rotate-video'
	},
	{
		'subscription': 'completed-rotate-video'
	}
]
PROJECT_ID = 'plasmic-artefacts'
