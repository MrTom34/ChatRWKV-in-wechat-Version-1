# ChatRWKV-in-wechat-Version-1


原文详见[一个基于RWKV的](https://github.com/shengxia/RWKV_Role_Playing)

## 配置要求

- 方案一：内存4G，显存7.4G，本地部署方案，推理相对较快
- 方案二：内存要求12G，cuda无要求，推理慢
- 方案三：与方案一相同，使用colab进行部署

## 文件描述：

1. RWKV_Role_Playing:语言模型，用于生成回答,并投射到一个网页上
2. wechat.py:实现网页与wechat之间的交互

另外，`亚托莉`的初始化文件已经保存在chars文件夹下

## 使用方法

在`命令行`powershell中运行以下命令：

```powershell
pip install torch==1.13.1 --extra-index-url https://download.pytorch.org/whl/cu117 --upgrade
pip install -r ./RWKV_Role_Playing/requirements.txt
```

接下来下载预训练模型参数

### 方案一

```powershell
Invoke-WebRequest -Uri "https://huggingface.co/wdmz/rwkv_mybackup/resolve/main/fp16i8-RWKV-4-World-CHNtuned-7B-v1-20230709-ctx4096.pth" -OutFile "model/RWKV-4-World-CHNtuned-7B-v1.pth"
```

运行webui.py打开网页

```powershell
python ./RWKV_Role_Playing/webui.py --model model/RWKV-4-World-CHNtuned-7B-v1 --cuda_on 1 --share --strategy 'cuda fp16i8'
```

**请务必使用edge浏览器，并保持在聊天界面**

#### 配置人物

- 右上角选择待选人物，有亚托莉和小雪
- 当ai与你打招呼时转到`操作微信`步操作$\int_a^bf(x)  \,dx$

### 方案二

```powershell
Invoke-WebRequest -Uri "https://huggingface.co/wdmz/rwkv_mybackup/resolve/main/fp32i8-RWKV-4-World-CHNtuned-7B-v1-20230709-ctx4096.pth" -OutFile "model/RWKV-4-World-CHNtuned-7B-v1.pth"
```

运行webui.py打开网页

```powershell
python ./RWKV_Role_Playing/webui.py --model model/RWKV-4-World-CHNtuned-7B-v1 --cuda_on 0 --share --strategy 'cpu fp32i8'
```

**请务必使用edge浏览器，并保持在聊天界面**

#### 配置人物

- 右上角选择待选人物，有亚托莉和小雪
- 当ai与你打招呼时转到`操作微信`步操作

## 操作微信

- 请打开微信，保持电脑下边栏可以看到微信，不要关掉edge，同样保证电脑下边栏可以看到edge
- 在wechat.py中修改按需求修改参数 ：`friend_list `修改为你希望对话的好友；`print('发送成功，正在生成回答，30s') time.sleep(30)`是为ai生成答案所需要的时间设定的
- 安装wechat.py所需要的环境：`pip install -r requirements.txt`
- 最后在命令行中运行wechat.py(也可以直接打开运行)

```powershell
python wechat.py
```


