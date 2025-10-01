# portfolio

Still very much under construction.

My portfolio/website. Originally for applications to internships, grad school, etc, I think now it'll become more of a blog. It uses Pelican to generate the site and is based on the [pelican-boostrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) theme, with some minor changes.

## Usage

### First-time setup

- Create the Python virtual environment (venv): `py -3.13 -m venv venv`
- Activate the venv: varies by OS
  - Windows: `venv\Scripts\activate.bat`
  - Linux and MacOS: `source venv/bin/activate`
- Install requirements to the venv: `pip install -r requirements.txt`

### Building the site

This is done automatically by a Github worker on push, but can be done locally to test it out.

- Build the output: `pelican content`
- Run the local server: `pelican --listen`

### Changing the virtual environment

If there doesn't currently exist a requirements.txt, make a venv and install pip-tools to it.

- Make desired modifications to "requirements.in"
- With the venv still activated, compile "requirements.in": `pip-compile requirements.in`
- Deactivate the venv: `deactivate`
- Delete the "venv" folder
- Perform the "First-Time Setup" instructions above.
