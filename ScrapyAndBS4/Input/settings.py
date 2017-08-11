# -*- coding: utf-8 -*-

BOT_NAME = 'ip_proxy_pool'

SPIDER_MODULES = ['ip_proxy_pool.spiders']
NEWSPIDER_MODULE = 'ip_proxy_pool.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'ip_proxy_pool.pipelines.IpProxyPoolPipeline': 300,
}

#爬取间隔
DOWNLOAD_DELAY = 1

# 禁用cookie
COOKIES_ENABLED = False


# 重写默认请求头
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html, application/xhtml+xml, application/xml',
  'Accept-Language': 'zh-CN,zh;q=0.8',
  'Host':'ip84.com',
  'Referer':'http://ip84.com/',
  'X-XHR-Referer':'http://ip84.com/'
}

#激活自定义UserAgent和代理IP
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'ip_proxy_pool.useragent.UserAgent': 1,
   'ip_proxy_pool.proxymiddlewares.ProxyMiddleware':100,
   'scrapy.downloadermiddleware.useragent.UserAgentMiddleware' : None,
}
