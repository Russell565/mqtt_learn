# mqtt_learn
学习一下mqtt。

根据路径：https://www.emqx.io/docs/zh/v4.4/getting-started/getting-started.html#%E5%AE%89%E8%A3%85-emqx
通过Docker容器运行emqx
docker pull emqx/emqx:latest
docker run -d --name emqx -p 1883:1883 -p 8081:8081 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx:latest
运行成功后， 打开http://localhost:18083/  ；用户名admin，密码public。进入databoard控制台

安装：pip install paho-mqtt
运行订阅消息，接受发布的消息：python mqtt_subscribe.py
运行发布消息：python mqtt_publish.py
