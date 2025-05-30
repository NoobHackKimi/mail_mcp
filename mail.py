import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from fastmcp import FastMCP
import logging
from dotenv import dotenv_values

# 创建MCP实例
mcp = FastMCP("email_sender", debug=True, log_level="DEBUG")

# 直接从 .env 文件读取配置
config = dotenv_values(".env.example")

# 获取配置值
SMTP_HOST = config["SMTP_HOST"]
SMTP_PORT = int(config["SMTP_PORT"])
SMTP_SECURE = config["SMTP_SECURE"].lower() == "true"
SMTP_USER = config["SMTP_USER"]
SMTP_PASS = config["SMTP_PASS"]
DEFAULT_FROM_NAME = config["DEFAULT_FROM_NAME"]
DEFAULT_FROM_EMAIL = config["DEFAULT_FROM_EMAIL"]
DEFAULT_RECEIVER_EMAIL = config["DEFAULT_RECEIVER_EMAIL"]
SERVICE_PORT = int(config["SERVICE_PORT"])

@mcp.tool()
def send_email(subject: str, message: str) -> str:
    """
    发送电子邮件到指定邮箱

    :param subject: 邮件主题
    :param message: 邮件正文内容
    :return: 发送结果消息
    """
    try:
        # 创建邮件对象
        msg = MIMEMultipart()

        # 设置发件人（包含名称）
        from_address = f"{Header(DEFAULT_FROM_NAME, 'utf-8').encode()} <{DEFAULT_FROM_EMAIL}>"
        msg['From'] = from_address
        msg['To'] = DEFAULT_RECEIVER_EMAIL
        msg['Subject'] = Header(subject, 'utf-8')

        # 添加邮件正文
        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        # 连接SMTP服务器
        if SMTP_SECURE:
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        else:
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
            if SMTP_PORT == 587:  # 587端口通常需要STARTTLS
                server.starttls()

        # 登录并发送邮件
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(DEFAULT_FROM_EMAIL, DEFAULT_RECEIVER_EMAIL, msg.as_string())
        server.quit()

        return f"邮件成功发送至 {DEFAULT_RECEIVER_EMAIL}"

    except smtplib.SMTPAuthenticationError:
        error_msg = "邮箱认证失败，请检查用户名和密码/授权码是否正确"
        logging.error(error_msg)
        return error_msg
    except smtplib.SMTPException as e:
        error_msg = f"SMTP服务器错误: {str(e)}"
        logging.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"邮件发送失败: {str(e)}"
        logging.error(error_msg)
        return error_msg

# 运行MCP服务
if __name__ == "__main__":
    # 打印配置信息
    print("=" * 60)
    print("邮件发送服务配置")
    print("=" * 60)
    print(f"发件人: {DEFAULT_FROM_NAME} <{DEFAULT_FROM_EMAIL}>")
    print(f"收件人: {DEFAULT_RECEIVER_EMAIL}")
    print(f"SMTP服务器: {SMTP_HOST}:{SMTP_PORT} (安全连接: {'是' if SMTP_SECURE else '否'})")
    print(f"服务端口: {SERVICE_PORT}")
    print("=" * 60)
    print("服务已启动，等待请求...")

    mcp.run(transport="sse", port=SERVICE_PORT)