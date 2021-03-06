# -*- coding: utf-8 -*-

# Scrapy settings for XiaocaiCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'XiaocaiCrawler'

SPIDER_MODULES = ['XiaocaiCrawler.spiders']
NEWSPIDER_MODULE = 'XiaocaiCrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'XiaocaiCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'XiaocaiCrawler.middlewares.XiaocaicrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'XiaocaiCrawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'XiaocaiCrawler.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOADER_MIDDLEWARES = {
   'XiaocaiCrawler.contrib.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware': 543, # 设置userAgent
}


#------------scrapy-redis 分布式爬虫相关设置-----------------
# 修改scrapy默认的调度器为scrapy重写的调度器 启动从reids缓存读取队列调度爬虫
SCHEDULER = "XiaocaiCrawler.scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "XiaocaiCrawler.scrapy_redis.dupefilter.RFPDupeFilter"
# 调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True

# 请求调度使用优先队列（默认)
SCHEDULER_QUEUE_CLASS = 'XiaocaiCrawler.scrapy_redis.queue.SpiderPriorityQueue'

# 请求调度使用FIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# 请求调度使用LIFO队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# 最大的空闲时间，避免分布式爬取得情况下爬虫被关闭
# 此设置只适用于SpiderQueue和SpiderStack
# 也是爬虫第一次启动时的等待时间（应为队列是空的）
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 存储爬取到的item，一定要在所有的pipeline最后，即设定对应的数字大于其他pipeline
ITEM_PIPELINES = {
    'XiaocaiCrawler.pipelines.BaseSpiderPipeline': 256,
    'XiaocaiCrawler.scrapy_redis.pipelines.RedisPipeline': 300
}

# 指定redis的地址和端口(可选，程序将使用默认的地址localhost:6379)
REDIS_HOST = '127.0.0.1'
#REDIS_PORT = 6378
REDIS_PORT = 6379

# 声明redis的url地址（可选）
# 如果设置了这一项，则程序会有限采用此项设置，忽略REDIS_HOST 和 REDIS_PORT的设置
#REDIS_URL = 'redis://user:pass@hostname:9001'
#------------end scrapy-redis----------------------------


#------------graphite setting ---------------------------
#STATS_CLASS = 'XiaocaiCrawler.statscol.graphite.RedisGraphiteStatsCollector'
GRAPHITE_HOST = '143.89.156.62'
#GRAPHITE_HOST = '127.0.0.1'
GRAPHITE_PORT = 2003
