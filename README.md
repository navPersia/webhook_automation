<h1>Webhook raspberry pi docker container repull and buled</h1>

webhook for automatisation when a new docker get a new image it wil call  web hook on raspberry and that webhook run docker-compose to refresh all images.

we need to install Flask
```
python -m pip install Flask
```

copy main.py to raspberry pi onder /home/pi/docker

first make a service that call the script
```
cd /lib/systemd/system/
sudo nano webhook.service
```

the service definition is as below 
```
Unit]
Description=webhook to automat get new images by docker-compose
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/docker/main.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

run commands bellow
```
sudo chmod 644 /lib/systemd/system/webhook.service
chmod +x /home/pi/docker/main.py
sudo systemctl daemon-reload
sudo systemctl enable webhook.service
sudo systemctl start webhook.service
```

now add a cronjob to run service at restart
```
@reboot [sudo systemctl start webhook.service]
```

we also here have cronjob to run dockers when reboot
```
@reboot [sudo systemctl start docker]
```

last step is to make your webhook avalaible from outside 

and add webhook to dockerhub