# portfolio

My portfolio for applications to internships, grad school, etc.

## Setup

1. Install submodules: `git submodule init && git submodule update`
2. Create the python virtual environment: `python -m venv venv`
3. Activate the venv: varies by OS
   - Windows: `venv\Scripts\Activate.bat`
4. Install requirements: `pip install -r requirements.txt`

## Building the site

1. Build the output: `pelican content`
2. Run the local server: `pelican --listen`
