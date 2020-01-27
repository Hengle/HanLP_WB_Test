from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class HttpProxy(HttpProxyMiddleware):

    @staticmethod
    def proxy_shadowsocks():
        proxy = "http://127.0.0.1:50420"
        return proxy