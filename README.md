<h1>Webhook raspberry pi docker</h1>

Webhook for automatisation.
When webhook called, it wil call docker-compose file to get the last image en run it.

First install Flask in raspberry pi
```
python -m pip install Flask
```

Copy main.py to raspberry pi onder /home/pi/docker

First make a service that call the script 
```
cd /lib/systemd/system/
sudo nano webhook.service
```

The service definition is as below 
```
[Unit]
Description=webhook to automat get new images by docker-compose
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/docker/main.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

Run commands bellow
```
sudo chmod 644 /lib/systemd/system/webhook.service
chmod +x /home/pi/docker/main.py
sudo systemctl daemon-reload
sudo systemctl enable webhook.service
sudo systemctl start webhook.service
```

Now add a cronjob to run service at restart
```
@reboot [sudo systemctl start webhook.service]
```

Also here have add a cronjob to run dockers when reboot it used when raspberry pi goes down
```
@reboot [sudo systemctl start docker]
```

Make webhook avalaible from outside local network by port forwarding and reverse proxy

last step is to add webhook to dockerhub onder repository.
