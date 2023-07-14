workers = 5  # 定义同时开启的处理请求的进程数目
worker_class = "gevent"  # 采用gevent库，支持异步处理请求
bind = "0.0.0.0:5003"  # 监听IP放宽，以便于Docker之间，Docker和 宿主机之间通信
