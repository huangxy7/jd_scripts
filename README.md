

# AI线报采集

##  TG频道:  [https://t.me/yangmao_ai](https://t.me/yangmao_ai)
##  TG群:  [https://t.me/+llx5c1gg5kBkYzY1](https://t.me/+llx5c1gg5kBkYzY1)

一个功能强大的线报采集、清洗、分析和推送框架，支持从Telegram群组采集线报，自动过滤和分析，然后推送到指定的Telegram频道。

## 功能特点

### 核心功能
- **多渠道采集**：支持从多个Telegram群组同时采集线报
- **智能过滤**：基于规则和AI的双重过滤，确保只推送高价值线报
- **自动分析**：使用AI分析线报内容，提取关键信息
- **链接转换**：自动转换京东、淘宝等平台的链接为推广链接
- **去重处理**：基于内容哈希的去重，避免重复推送
- **多平台支持**：支持京东、淘宝、拼多多等多个电商平台
- **图片处理**：自动提取和推送商品图片
- **消息格式化**：美观的Markdown格式消息，提升用户体验

### 技术特点
- **异步处理**：使用asyncio实现高效的异步处理
- **可配置性**：通过YAML配置文件灵活配置各种参数
- **可扩展性**：模块化设计，易于添加新的处理器和数据源
- **容错处理**：完善的错误处理和重试机制
- **实时监控**：详细的日志记录，便于问题排查



## 项目结构

```
xianbao/
├── app.py              # 应用入口
├── config.py           # 配置管理
├── pipeline.py         # 处理管道
├── models.py           # 数据模型
├── processors/         # 处理器
│   ├── affiliate.py    # 推广链接转换
│   ├── ai.py           # AI分析
│   ├── dedupe.py       # 去重处理
│   ├── extract_product.py # 产品信息提取
│   ├── normalize.py    # 文本标准化
│   ├── rules.py        # 规则过滤
│   └── value_filter.py # 价值过滤
├── sinks/              # 输出
│   ├── telegram_bot.py # Telegram推送
│   └── webhook.py      # Webhook推送
└── sources/            # 数据源
    └── telegram.py     # Telegram采集
```

## 常见问题

### 1. 应用无法连接到Telegram
- 检查API ID和API Hash是否正确
- 检查网络连接是否正常
- 尝试使用代理

### 2. 线报没有被推送
- 检查过滤规则是否过于严格
- 检查AI分析是否正常
- 检查Telegram机器人是否有发送消息的权限

### 3. 链接转换失败
- 检查推广平台的配置是否正确
- 检查网络连接是否正常
- 检查推广平台的API是否可用

## 贡献

欢迎提交Issue和Pull Request，共同改进这个项目。

## 许可证

MIT License

## GitHub热门搜索关键词

以下是GitHub上搜索量较高的关键词，按类别分类：

### 前端开发
javascript, react, vue, angular, typescript, html, css, tailwindcss, bootstrap, svelte, nextjs, nuxtjs, gatsby, vite, webpack, babel, eslint, prettier, jest, cypress

### 后端开发
python, django, flask, fastapi, nodejs, express, nestjs, spring, java, golang, rust, php, laravel, symfony, ruby, rails, c#, asp.net, postgresql, mysql, mongodb, redis

### 移动开发
react-native, flutter, swift, kotlin, android, ios, capacitor, ionic, expo

### 数据科学
python, numpy, pandas, tensorflow, pytorch, scikit-learn, jupyter, matplotlib, seaborn, keras, scipy, statsmodels, nltk, spacy, transformers, openai

###  DevOps & 工具
docker, kubernetes, git, github, gitlab, ci/cd, jenkins, github-actions, aws, azure, gcp, terraform, ansible, vagrant, docker-compose, nginx, linux, bash, powershell

### 人工智能
machine-learning, deep-learning, artificial-intelligence, ai, nlp, computer-vision, reinforcement-learning, neural-network, chatbot, openai, gpt, llm, transformers

### 区块链
blockchain, ethereum, bitcoin, solidity, web3, smart-contracts, nft, defi, cryptocurrency, solana, polkadot, avalanche, cosmos

### 游戏开发
unity, unreal-engine, godot, game-development, pygame, phaser, threejs, webgl, cocos2d, spritekit

### 安全
security, cybersecurity, ethical-hacking, penetration-testing, cryptography, owasp, vulnerability, ssl, authentication, authorization

### 物联网
iot, raspberry-pi, arduino, esp32, embedded-systems, sensors, microcontroller, home-automation, smart-home

### 羊毛党相关
羊毛, 线报, 优惠, 折扣, 秒杀, 抢购, 免单, 0元购, 漏洞价, 神价, 优惠券, 返利, 推广, 导购, 薅羊毛, 优惠信息, 特价, 促销, 活动, 福利, 红包, 满减, 满赠, 限时, 限量, 独家, 内部, 渠道, 捡漏, 白菜价, 性价比, 省钱, 购物, 电商, 京东, 淘宝, 拼多多, 苏宁, 天猫, 唯品会, 考拉, 聚划算, 双十一, 双十二, 618, 黑五, 年中大促, 年终大促, 会员日, 品牌日, 新品, 首发, 预售, 抢购, 秒杀, 闪购, 团购, 拼团, 砍价, 助力, 抽奖, 免费, 试用, 体验, 样品, 小样, 优惠券, 折扣券, 满减券, 立减券, 代金券, 礼品卡, 储值卡, 积分, 会员, VIP, 等级, 特权, 返利, 返现, 返券, 返积分, 推广, 代理, 分销, 佣金, 提成, 分成, 渠道, 资源, 信息, 情报, 线报群, 羊毛群, 优惠群, 福利群, 购物群, 比价, 价格监控, 降价提醒, 库存监控, 自动下单, 脚本, 工具, 软件, 平台, 网站, 小程序, APP, 应用, 服务, 系统, 框架, 解决方案, 技术, 教程, 指南, 攻略, 经验, 分享, 交流, 社区, 论坛, 博客, 公众号, 微博, 抖音, 快手, 视频, 直播, 带货, 推荐, 种草, 测评, 开箱, 体验, 反馈, 维权, 售后, 投诉, 建议, 改进, 优化, 创新, 趋势, 预测, 分析, 报告, 数据, 统计, 排行, 榜单, 热门, 精选, 优质, 高价值, 低价格, 性价比, 划算, 值得买, 必买, 推荐, 爆款, 热销, 新品, 限量版, 联名款, 定制款, 独家款, 首发款, 限定款, 纪念款, 收藏款, 稀有款, 绝版, 断货, 补货, 预售, 预约, 抢购, 秒杀, 闪购, 限时, 限量, 独家, 内部, 渠道, 捡漏, 白菜价, 神价, 漏洞价, 0元购, 免单, 白嫖, 福利, 红包, 现金, 奖励, 补贴, 扶持, 政策, 活动, 促销, 优惠, 折扣, 满减, 满赠, 买一送一, 第二件半价, 全场包邮, 会员专享, 新客专享, 老客专享, 限时特惠, 年度大促, 季度大促, 月度大促, 周周特惠, 日日特惠, 整点秒杀, 午夜场, 早场, 晚场, 专场, 主题活动, 节日活动, 庆典活动, 周年庆, 店庆, 开业, 促销, 清仓, 甩卖, 换季, 新品上市, 旧品下架, 尾货, 库存, 积压, 处理, 特价, 折扣, 优惠, 福利, 红包, 现金, 奖励, 补贴, 扶持, 政策, 活动, 促销, 优惠, 折扣, 满减, 满赠, 买一送一, 第二件半价, 全场包邮, 会员专享, 新客专享, 老客专享, 限时特惠, 年度大促, 季度大促, 月度大促, 周周特惠, 日日特惠, 整点秒杀, 午夜场, 早场, 晚场, 专场, 主题活动, 节日活动, 庆典活动, 周年庆, 店庆, 开业, 促销, 清仓, 甩卖, 换季, 新品上市, 旧品下架, 尾货, 库存, 积压, 处理, 特价, 折扣, 优惠, 福利, 红包, 现金, 奖励, 补贴, 扶持, 政策, 活动, 促销, 优惠, 折扣, 满减, 满赠, 买一送一, 第二件半价, 全场包邮, 会员专享, 新客专享, 老客专享, 限时特惠, 年度大促, 季度大促, 月度大促, 周周特惠, 日日特惠, 整点秒杀, 午夜场, 早场, 晚场, 专场, 主题活动, 节日活动, 庆典活动, 周年庆, 店庆, 开业, JD, 京东自营, 京东超市, 京东到家, 京东物流, 京东金融, 京东plus, 京东会员, 京东优惠券, 京东活动, 京东秒杀, 京东抢购, 京东好价, 京东神价, 京东漏洞, 京东白嫖, 脚本抢购, 自动抢购, 秒杀脚本, 抢购脚本, 优惠脚本, 羊毛脚本, 自动下单脚本, 价格监控脚本, 库存监控脚本, 优惠券脚本, 返利脚本, 推广脚本, 引流脚本, 白嫖教程, 白嫖方法, 白嫖技巧, 白嫖攻略, 0元购教程, 免单教程, 漏洞价教程, 神价教程, 优惠券教程, 返利教程, 推广教程, 导购教程, 薅羊毛教程, 优惠信息教程, 特价教程, 促销教程, 活动教程, 福利教程, 红包教程, 满减教程, 满赠教程, 限时教程, 限量教程, 独家教程, 内部教程, 渠道教程, 捡漏教程, 白菜价教程, 性价比教程, 省钱教程, 购物教程, 电商教程, 京东教程, 淘宝教程, 拼多多教程, 苏宁教程, 天猫教程, 唯品会教程, 考拉教程, 聚划算教程, 双十一教程, 双十二教程, 618教程, 黑五教程, 年中大促教程, 年终大促教程, 会员日教程, 品牌日教程, 新品教程, 首发教程, 预售教程, 抢购教程, 秒杀教程, 闪购教程, 团购教程, 拼团教程, 砍价教程, 助力教程, 抽奖教程, 免费教程, 试用教程, 体验教程, 样品教程, 小样教程, 优惠券教程, 折扣券教程, 满减券教程, 立减券教程, 代金券教程, 礼品卡教程, 储值卡教程, 积分教程, 会员教程, VIP教程, 等级教程, 特权教程, 返利教程, 返现教程, 返券教程, 返积分教程, 推广教程, 代理教程, 分销教程, 佣金教程, 提成教程, 分成教程, 渠道教程, 资源教程, 信息教程, 情报教程, 线报群教程, 羊毛群教程, 优惠群教程, 福利群教程, 购物群教程, 比价教程, 价格监控教程, 降价提醒教程, 库存监控教程, 自动下单教程, 脚本教程, 工具教程, 软件教程, 平台教程, 网站教程, 小程序教程, APP教程, 应用教程, 服务教程, 系统教程, 框架教程, 解决方案教程, 技术教程, 教程教程, 指南教程, 攻略教程, 经验教程, 分享教程, 交流教程, 社区教程, 论坛教程, 博客教程, 公众号教程, 微博教程, 抖音教程, 快手教程, 视频教程, 直播教程, 带货教程, 推荐教程, 种草教程, 测评教程, 开箱教程, 体验教程, 反馈教程, 维权教程, 售后教程, 投诉教程, 建议教程, 改进教程, 优化教程, 创新教程, 趋势教程, 预测教程, 分析教程, 报告教程, 数据教程, 统计教程, 排行教程, 榜单教程, 热门教程, 精选教程, 优质教程, 高价值教程, 低价格教程, 性价比教程, 划算教程, 值得买教程, 必买教程, 推荐教程, 爆款教程, 热销教程, 新品教程, 限量版教程, 联名款教程, 定制款教程, 独家款教程, 首发款教程, 限定款教程, 纪念款教程, 收藏款教程, 稀有款教程, 绝版教程, 断货教程, 补货教程, 预售教程, 预约教程, 抢购教程, 秒杀教程, 闪购教程, 限时教程, 限量教程, 独家教程, 内部教程, 渠道教程, 捡漏教程, 白菜价教程, 神价教程, 漏洞价教程, 0元购教程, 免单教程, 白嫖教程, 福利教程, 红包教程, 现金教程, 奖励教程, 补贴教程, 扶持教程, 政策教程, 活动教程, 促销教程, 优惠教程, 折扣教程, 满减教程, 满赠教程, 买一送一教程, 第二件半价教程, 全场包邮教程, 会员专享教程, 新客专享教程, 老客专享教程, 限时特惠教程, 年度大促教程, 季度大促教程, 月度大促教程, 周周特惠教程, 日日特惠教程, 整点秒杀教程, 午夜场教程, 早场教程, 晚场教程, 专场教程, 主题活动教程, 节日活动教程, 庆典活动教程, 周年庆教程, 店庆教程, 开业教程

### 其他热门
opensource, free, tutorial, beginner-friendly, boilerplate, template, starter, example, demo, showcase, portfolio, dashboard, admin-panel, api, rest-api, graphql, microservices, monorepo, serverless, edge-computing, progressive-web-app, pwa, single-page-application, spa, static-site-generator, ssg, jamstack, headless-cms, content-management-system, cms, e-commerce, shopping-cart, payment-gateway, stripe, paypal, social-media, chat, messaging, real-time, websocket, video, audio, streaming, file-upload, image-processing, pdf, excel, csv, data-visualization, chart, graph, map, geolocation, localization, i18n, l10n, accessibility, a11y, performance, optimization, seo, search-engine-optimization, pagination, sorting, filtering, authentication, oauth, jwt, session, cookies, cors, middleware, routing, state-management, redux, context-api, hooks, components, styled-components, css-in-js, responsive-design, mobile-first, accessibility, dark-mode, theme, animation, transitions, drag-and-drop, file-upload, form-validation, error-handling, logging, testing, unit-testing, integration-testing, end-to-end-testing, mock, stub, fixture, coverage, performance-testing, load-testing, security-testing, continuous-integration, continuous-deployment, ci/cd, deployment, hosting, cloud, server, database, sql, nosql, graphql, rest, api-design, swagger, openapi, documentation, markdown, readme, contributing, license, changelog, release, versioning, branching, merging, rebasing, cherry-picking, tagging, issues, pull-requests, code-review, code-quality, linting, formatting, refactoring, debugging, profiling, monitoring, logging, alerting, observability, tracing, metrics, dashboard, analytics, user-experience, ux, user-interface, ui, design, wireframe, mockup, prototype, usability, accessibility, user-research, user-testing, a/b-testing, conversion-rate-optimization, cro, seo, search-engine-optimization, content-marketing, social-media-marketing, email-marketing, paid-marketing, digital-marketing

### 中文引流关键词

#### 羊毛党核心词汇
羊毛, 薅羊毛, 线报, 优惠, 折扣, 秒杀, 抢购, 免单, 0元购, 漏洞价, 神价, 优惠券, 返利, 推广, 导购, 优惠信息, 特价, 促销, 活动, 福利, 红包, 满减, 满赠, 限时, 限量, 独家, 内部, 渠道, 捡漏, 白菜价, 性价比, 省钱, 购物, 电商

#### 电商平台
京东, 淘宝, 拼多多, 苏宁, 天猫, 唯品会, 考拉, 聚划算, 京东自营, 京东超市, 京东到家, 京东物流, 京东金融, 京东plus, 京东会员, 淘宝特价版, 天猫超市, 拼多多百亿补贴, 苏宁易购, 唯品会特卖, 考拉海购

#### 促销活动
双十一, 双十二, 618, 黑五, 年中大促, 年终大促, 会员日, 品牌日, 新品, 首发, 预售, 闪购, 团购, 拼团, 砍价, 助力, 抽奖, 免费, 试用, 体验, 样品, 小样

#### 优惠券类型
优惠券, 折扣券, 满减券, 立减券, 代金券, 礼品卡, 储值卡, 积分, 会员, VIP, 等级, 特权, 返利, 返现, 返券, 返积分

#### 推广模式
推广, 代理, 分销, 佣金, 提成, 分成, 渠道, 资源, 信息, 情报, 线报群, 羊毛群, 优惠群, 福利群, 购物群

#### 工具脚本
比价, 价格监控, 降价提醒, 库存监控, 自动下单, 脚本, 工具, 软件, 平台, 网站, 小程序, APP, 应用, 服务, 系统, 框架, 解决方案, 技术

#### 内容形式
教程, 指南, 攻略, 经验, 分享, 交流, 社区, 论坛, 博客, 公众号, 微博, 抖音, 快手, 视频, 直播, 带货, 推荐, 种草, 测评, 开箱, 体验, 反馈

#### 商品类型
爆款, 热销, 新品, 限量版, 联名款, 定制款, 独家款, 首发款, 限定款, 纪念款, 收藏款, 稀有款, 绝版, 断货, 补货

#### 活动类型
限时, 限量, 独家, 内部, 渠道, 捡漏, 白菜价, 神价, 漏洞价, 0元购, 免单, 白嫖, 福利, 红包, 现金, 奖励, 补贴, 扶持, 政策

#### 促销方式
买一送一, 第二件半价, 全场包邮, 会员专享, 新客专享, 老客专享, 限时特惠, 年度大促, 季度大促, 月度大促, 周周特惠, 日日特惠, 整点秒杀, 午夜场, 早场, 晚场, 专场, 主题活动, 节日活动, 庆典活动, 周年庆, 店庆, 开业

#### 清仓甩卖
清仓, 甩卖, 换季, 新品上市, 旧品下架, 尾货, 库存, 积压, 处理

#### 京东专属
JD, 京东自营, 京东超市, 京东到家, 京东物流, 京东金融, 京东plus, 京东会员, 京东优惠券, 京东活动, 京东秒杀, 京东抢购, 京东好价, 京东神价, 京东漏洞, 京东白嫖

#### 脚本工具
脚本抢购, 自动抢购, 秒杀脚本, 抢购脚本, 优惠脚本, 羊毛脚本, 自动下单脚本, 价格监控脚本, 库存监控脚本, 优惠券脚本, 返利脚本, 推广脚本, 引流脚本

#### 教程攻略
白嫖教程, 白嫖方法, 白嫖技巧, 白嫖攻略, 0元购教程, 免单教程, 漏洞价教程, 神价教程, 优惠券教程, 返利教程, 推广教程, 导购教程, 薅羊毛教程, 优惠信息教程, 特价教程, 促销教程, 活动教程, 福利教程, 红包教程, 满减教程, 满赠教程, 限时教程, 限量教程, 独家教程, 内部教程, 渠道教程, 捡漏教程, 白菜价教程, 性价比教程, 省钱教程, 购物教程, 电商教程, 京东教程, 淘宝教程, 拼多多教程, 苏宁教程, 天猫教程, 唯品会教程, 考拉教程, 聚划算教程, 双十一教程, 双十二教程, 618教程, 黑五教程, 年中大促教程, 年终大促教程, 会员日教程, 品牌日教程, 新品教程, 首发教程, 预售教程, 抢购教程, 秒杀教程, 闪购教程, 团购教程, 拼团教程, 砍价教程, 助力教程, 抽奖教程, 免费教程, 试用教程, 体验教程, 样品教程, 小样教程, 优惠券教程, 折扣券教程, 满减券教程, 立减券教程, 代金券教程, 礼品卡教程, 储值卡教程, 积分教程, 会员教程, VIP教程, 等级教程, 特权教程, 返利教程, 返现教程, 返券教程, 返积分教程, 推广教程, 代理教程, 分销教程, 佣金教程, 提成教程, 分成教程, 渠道教程, 资源教程, 信息教程, 情报教程, 线报群教程, 羊毛群教程, 优惠群教程, 福利群教程, 购物群教程, 比价教程, 价格监控教程, 降价提醒教程, 库存监控教程, 自动下单教程, 脚本教程, 工具教程, 软件教程, 平台教程, 网站教程, 小程序教程, APP教程, 应用教程, 服务教程, 系统教程, 框架教程, 解决方案教程, 技术教程

#### 其他热门词汇
值得买, 必买, 推荐, 爆款, 热销, 新品, 限量版, 联名款, 定制款, 独家款, 首发款, 限定款, 纪念款, 收藏款, 稀有款, 绝版, 断货, 补货, 预售, 预约, 抢购, 秒杀, 闪购, 限时, 限量, 独家, 内部, 渠道, 捡漏, 白菜价, 神价, 漏洞价, 0元购, 免单, 白嫖, 福利, 红包, 现金, 奖励, 补贴, 扶持, 政策, 活动, 促销, 优惠, 折扣, 满减, 满赠, 买一送一, 第二件半价, 全场包邮, 会员专享, 新客专享, 老客专享, 限时特惠, 年度大促, 季度大促, 月度大促, 周周特惠, 日日特惠, 整点秒杀, 午夜场, 早场, 晚场, 专场, 主题活动, 节日活动, 庆典活动, 周年庆, 店庆, 开业, 清仓, 甩卖, 换季, 新品上市, 旧品下架, 尾货, 库存, 积压, 处理, 特价, 折扣, 优惠, 福利, 红包, 现金, 奖励, 补贴, 扶持, 政策, 活动, 促销, 优惠, 折扣, 满减, 满赠, 买一送一, 第二件半价, 全场包邮, 会员专享, 新客专享, 老客专享, 限时特惠, 年度大促, 季度大促, 月度大促, 周周特惠, 日日特惠, 整点秒杀, 午夜场, 早场, 晚场, 专场, 主题活动, 节日活动, 庆典活动, 周年庆, 店庆, 开业gg, growth-hacking, startup, entrepreneurship, business, product-management, project-management, agile, scrum, kanban, waterfall, lean, devops, sre, it-operations, system-administration, network-administration, database-administration, cloud-administration, security-administration, it-support, help-desk, technical-support, customer-support, sales-engineering, solutions-engineering, pre-sales, post-sales, consulting, training, education, teaching, learning, online-learning, e-learning, MOOC, bootcamp, workshop, conference, meetup, hackathon, competition, challenge, prize, award, recognition, certification, badge, credential, portfolio, resume, cv, cover-letter, interview, job, career, salary, negotiation, remote-work, work-from-home, hybrid-work, flexible-work, work-life-balance, diversity, equity, inclusion, dei, mental-health, wellness, burnout, productivity, time-management, organization, goal-setting, habit-forming, motivation, leadership, management, team-building, collaboration, communication, conflict-resolution, feedback, mentoring, coaching, training, development, growth, promotion, advancement, networking, community, open-source, contribution, volunteering, philanthropy, social-good, impact, sustainability, environmental, climate-change, renewable-energy, carbon-footprint, zero-waste, circular-economy, social-justice, equality, human-rights, accessibility, inclusion, diversity, equity, lgbtq+, women-in-tech, underrepresented-groups, education, literacy, numeracy, stem, steam, stem-education, computer-science-education, coding-education, programming-education, online-education, e-learning, MOOC, bootcamp, workshop, conference, meetup, hackathon, competition, challenge, prize, award, recognition, certification, badge, credential, portfolio, resume, cv, cover-letter, interview, job, career, salary, negotiation, remote-work, work-from-home, hybrid-work, flexible-work, work-life-balance, diversity, equity, inclusion, dei, mental-health, wellness, burnout, productivity, time-management, organization, goal-setting, habit-forming, motivation, leadership, management, team-building, collaboration, communication, conflict-resolution, feedback, mentoring, coaching, training, development, growth, promotion, advancement, networking, community, open-source, contribution, volunteering, philanthropy, social-good, impact, sustainability, environmental, climate-change, renewable-energy, carbon-footprint, zero-waste, circular-economy, social-justice, equality, human-rights, accessibility, inclusion, diversity, equity, lgbtq+, women-in-tech, underrepresented-groups, education, literacy, numeracy, stem, steam, stem-education, computer-science-education, coding-education, programming-education, online-education, e-learning, MOOC, bootcamp,
