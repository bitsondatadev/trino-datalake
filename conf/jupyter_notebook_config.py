# This is needed to launch the jupyter notebooks to connect to 0.0.0.0 and expose the
# ip properly to docker.

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
