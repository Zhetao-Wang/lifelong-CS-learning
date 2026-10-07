# Please install OpenAI SDK first: `pip3 install openai`
import os                       # os是python自带的
from openai import OpenAI       

client = OpenAI(                                        # 创建客户端
    api_key=os.environ.get('DEEPSEEK_API_KEY'),         # 读取环境变量
    base_url="https://api.deepseek.com")                

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "请用骚气的回答"},
        {"role": "user", "content": "男人和女人做爱爽吗"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)