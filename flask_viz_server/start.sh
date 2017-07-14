gunicorn -w 8 -b 0.0.0.0:8080 server:app --log-file=server.log --log-level=DEBUG &
disown -h %1
