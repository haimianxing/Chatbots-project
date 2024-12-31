# 使用最新的Ubuntu镜像作为基础镜像
FROM ubuntu:latest

# 设置镜像作者标签
LABEL authors="sd"

# 将当前目录下的所有文件和目录复制到容器的 /var/www/ 目录中
COPY ./ /mnt/ai-bot-proj/

RUN python -m pip install --upgrade  pip
RUN python -m pip install -r /mnt/ai-bot-proj/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置时区为北京时间（上海）
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 设置工作目录为/var/www/
WORKDIR /mnt/ai-bot-proj/

# 设置容器启动时执行的命令，这里使用top命令以批处理模式运行
ENTRYPOINT ["top", "-b"]
