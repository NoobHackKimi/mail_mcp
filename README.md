📧 邮件发送服务

一个基于 FastMCP 框架的轻量级邮件发送服务，通过简单的 API 接口即可发送电子邮件。服务使用 SMTP 协议发送邮件，所有配置通过 .env 文件集中管理。

!https://via.placeholder.com/800x400.png?text=邮件服务架构图 <!-- 实际使用时可替换为真实架构图 -->

✨ 功能特性
🚀 一键发送：只需提供标题和内容即可发送邮件

⚙️ 集中配置：通过 .env 文件管理所有设置

🔒 安全连接：支持 SSL/TLS 加密传输

📧 自定义发件人：可设置发件人名称和邮箱

📊 详细日志：完整的运行日志和错误记录

🌐 RESTful API：标准化的接口设计

🔄 跨平台：支持 Windows/Linux/macOS

🚀 快速开始

安装依赖

pip install fastmcp python-dotenv

配置服务
创建 .env.example 配置文件：

==

SMTP 配置

==

SMTP_HOST=smtp.qq.com
SMTP_PORT=587
SMTP_SECURE=false
SMTP_USER=your_email@qq.com
SMTP_PASS=your_auth_code

==

发件人配置

==

DEFAULT_FROM_NAME=邮件服务
DEFAULT_FROM_EMAIL=your_email@qq.com

==

收件人配置

==

DEFAULT_RECEIVER_EMAIL=recipient@example.com

==

服务配置

==

SERVICE_PORT=2224

替换为您的实际配置：

SMTP_USER：您的邮箱账号

SMTP_PASS：邮箱密码或授权码

DEFAULT_FROM_NAME：发件人显示名称

DEFAULT_FROM_EMAIL：发件人邮箱地址

DEFAULT_RECEIVER_EMAIL：默认收件人邮箱

启动服务

python email_sender.py

服务启动后将显示配置信息：

邮件发送服务配置

发件人: 邮件服务 <your_email@qq.com>
收件人: recipient@example.com
SMTP服务器: smtp.qq.com:587 (安全连接: 否)
服务端口: 2224

服务已启动，等待请求...

📡 API 接口

基本信息
URL: http://localhost:2224/tool/send_email

方法: POST

Content-Type: application/json

请求参数

"subject": "邮件主题",

  "message": "邮件正文内容"

调用示例

使用 curl

curl -X POST http://localhost:2224/tool/send_email \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "测试邮件",
    "message": "这是一封来自邮件服务的测试邮件"
  }'

使用 Python

import requests

url = "http://localhost:2224/tool/send_email"
headers = {"Content-Type": "application/json"}
data = {
    "subject": "Python测试邮件",
    "message": "这是一封通过Python脚本发送的测试邮件"
response = requests.post(url, json=data, headers=headers)

print(response.text)

响应示例

成功响应:
"邮件成功发送至 recipient@example.com"

失败响应:
"邮箱认证失败，请检查用户名和密码/授权码是否正确"

⚙️ 配置说明

.env 文件配置项
配置项 说明 默认值 必填

SMTP_HOST SMTP服务器地址 无 ✅
SMTP_PORT SMTP端口号 无 ✅
SMTP_SECURE 是否使用SSL/TLS加密 false ❌
SMTP_USER SMTP用户名/邮箱 无 ✅
SMTP_PASS SMTP密码/授权码 无 ✅
DEFAULT_FROM_NAME 默认发件人名称 "邮件服务" ❌
DEFAULT_FROM_EMAIL 默认发件人邮箱 SMTP_USER 的值 ❌
DEFAULT_RECEIVER_EMAIL 默认收件人邮箱 无 ✅
SERVICE_PORT 服务监听端口 2224 ❌

常见邮箱服务商配置参考
邮箱服务商 SMTP_HOST SMTP_PORT SMTP_SECURE

QQ邮箱 smtp.qq.com 465 true

smtp.qq.com 587 false
163邮箱 smtp.163.com 465 true
Gmail smtp.gmail.com 587 false
Outlook smtp.office365.com 587 false

❓ 常见问题
邮箱认证失败怎么办？

检查 SMTP_USER 和 SMTP_PASS 是否正确

对于QQ邮箱，请使用授权码而非密码

确保邮箱已开启SMTP服务（通常在邮箱设置中）
如何发送给不同的收件人？

修改 .env 文件中的 DEFAULT_RECEIVER_EMAIL 配置项，或者修改代码支持动态收件人。
服务启动时报错 "KeyError" 怎么办？

确保 .env 文件中包含了所有必需的配置项，特别是：
SMTP_HOST

SMTP_PORT

SMTP_USER

SMTP_PASS

DEFAULT_RECEIVER_EMAIL
如何修改服务端口？

在 .env 文件中设置 SERVICE_PORT 为所需端口号：
SERVICE_PORT=8080

🔒 安全建议
保护敏感信息：

不要将 .env 文件提交到版本控制系统

将 .env 添加到 .gitignore 文件中
使用专用邮箱：

创建专门用于发送邮件的邮箱账户

启用应用专用密码（如QQ邮箱的授权码）
限制访问：

仅在安全网络环境下运行服务

考虑添加API密钥验证机制
定期更新：

定期更换邮箱授权码

关注服务的安全更新

📂 项目结构

email-service/
├── .env.example            # 配置文件模板
├── mail.py                 # 主程序
└── README.md               # 说明文档

📜 许可证

本项目采用 LICENSE。

🤝 贡献指南

欢迎提交 issue 和 pull request：
Fork 项目仓库

创建特性分支 (git checkout -b feature/AmazingFeature)

提交更改 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

打开 Pull Request

开始使用邮件发送服务，让您的应用轻松集成邮件功能！ 📨✨
