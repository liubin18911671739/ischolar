---
title: "第_4_课C__GPU_云端技术本地Ollama与国内算力云_实战_Obsidian_Hermes版"
workflow: "Obsidian + Hermes (OpenCode / DeepSeek Harness) + iScholar"
software_policy: "国产软件 + 开源软件（零翻墙）"
---

# 第_4_课C__GPU_云端技术本地Ollama与国内算力云_实战_Obsidian_Hermes版

> **工具栈说明**：本讲义将传统云端知识库工作流全面重构为 **Obsidian Vault + Hermes（OpenCode 或 DeepSeek Harness）+ 本地 iScholar 应用（Streamlit + FastAPI）**，配套软件全部采用国产软件与开源软件。

         ☁️
         ☁️ 第 4 课C — GPU 云端技术
         ·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战
           ☁️    课程目标： 掌握 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 云端 GPU 平台，完成模型微调（Axolotl + 魔塔
                 ModelScope）、vLLM Serverless 部署、Jupyter 云端训练与 ComfyUI
                 多模态生成




         📍 模块一：校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 平台入门（15 分钟）
         ☁️ 为什么需要云端 GPU？
           💡     文科老师也能用 GPU！ 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 让你按需租用高性能显卡，无需购买昂贵
                 硬件。就像"云端超级计算机"——用多少付多少，用完即停。


         云端 GPU 适用场景

                                 本地电脑能做
          任务类型                             为什么需要 GPU                 课题应用
                                 吗？

          大模型微调（Fine-
          Tuning）
                                 ❌ 显存不够    LoRA 微调 7B 模型需要
                                           ≥16GB 显存
                                                                     训练课题专用的多语种
                                                                     翻译/问答模型

          大模型推理部署                ❌ 速度太慢    GPU 并行计算加速推理
                                           10-100 倍
                                                                     部署私有化大模型处理
                                                                     敏感数据

          图像/视频生成
                                 ⚠️ 勉强可以   Stable Diffusion / Flux
                                                                     生成文化遗产宣传素材
                                 （慢）       需要 GPU 加速

          大规模文本处理                ⚠️ 非常慢    批量 Embedding / NER
                                           需要 GPU
                                                                     处理万级旅游评论语料



         校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 注册与充值
         操作步骤：




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                                    1


---

          1. 访问 runpod.io → 注册账号
          2. 进入 Billing → 充值（最低 $5，支持信用卡/PayPal）
          3. 了解计费模式：


           💰     GPU Pods（按时计费）
                      租用整台 GPU 服务器
                                                        ⚡   Serverless（按请求计费）
                                                              按 GPU 秒计费

                      适合长时间训练/开发                              空闲时不收费

                      RTX 4090: ~$0.39/hr                     适合 API 服务部署

                      A100 80GB: ~$1.64/hr                    自动扩缩容

                      A40 48: 0.4/hr



         校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama GPU 选择指南
          GPU 型号            显存              参考价格        适合任务

                                                        LoRA 微调 7B 模型、ComfyUI 图像
          RTX 5090          24 GB           ~$0.89/hr
                                                        生成

          A40               48 GB           ~$0.4/hr    微调 13B 模型、中等规模推理

          A100 80GB         80 GB           ~$1.64/hr   微调 70B 模型、大规模批处理

          H100              80 GB           ~$3.49/hr   最高性能训练、多模型并行



           ⚠️    省钱技巧： ① 用完立即停止 Pod ② 选择 Community Cloud（比 Secure
                 Cloud 便宜 30-50%） ③ 微调用 Spot Instance（更便宜但可能被中断）
                 ④ 不用时切换为 Stop（只收存储费）而非 Terminate（数据丢失）




         📍 模块二：Axolotl + 魔塔（ModelScope）模型微调
         （20 分钟）




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                                     2


---

           🦎     Axolotl 是目前最流行的开源 LLM 微调框架，支持 LoRA / QLoRA / 全量
                 微调，配置简单、一个 YAML 文件搞定。配合 魔塔（ModelScope） 模型
                 库，可以快速微调任意开源模型。


         什么是模型微调（Fine-Tuning）？

            graph
              A["     🧠
                    通用大模型<br>Qwen2.5-7B"] --> B["     📚你的课题数据<br
           >多语种旅游语料"]
              B --> C["          🔧
                          微调训练<br>Axolotl + LoRA"]
              C --> D["          🎯
                          课题专用模型<br>精通旅游+多语种"]
              style A fill:#E3F2FD,stroke:#1565C0
              style C fill:#FFF3E0,stroke:#E65100
              style D fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px


                                     🧠 通用大模型
                                      Qwen2.5-7B




                                     📚 你的课题数据
                                     多语种旅游语料




                                      🔧 微调训练
                                     Axolotl + LoRA




                                     🎯 课题专用模型
                                     精通旅游+多语种




         LoRA 微调原理（简化版）



☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                       3


---

           💡     LoRA（Low-Rank Adaptation）： 不修改原模型的全部参数（动辄数十
                 亿），只训练一小组"适配器"参数（通常 < 1% 的模型大小）。就像给大模型
                 戴上一副"专业眼镜"——模型本身不变，但看问题的方式变了。


          对比维度                   全量微调           LoRA 微调            QLoRA（量化+LoRA）
          训练参数量                  100%（数十亿）      ~0.1-1%            ~0.1-1%
          显存需求（7B模型）             ≥ 80GB（A100）   ≥ 16GB（RTX 4090）   ≥ 12GB（RTX 4090）

          训练时间                   数天             数小时                数小时

          效果                     最好             接近全量               略低于 LoRA

          推荐场景                   企业级、资源充足       科研首选               显存有限时


         Axolotl 微调实战
         Step 1：在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 创建 GPU Pod

          1. 登录 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama → Pods → + Deploy
          2. 选择模板：校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama Pytorch 2.x
          3. 选择 GPU：RTX 4090（24GB，LoRA 微调 7B 足够）
          4. 设置存储：50GB（模型 + 数据 + 输出）
          5. 点击 Deploy → 等待 Pod 启动

         Step 2：安装 Axolotl

           # SSH 连接到 Pod（校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 提供 Web Terminal）
           # 安装 Axolotl
           pip install axolotl
           # 或从源码安装（获取最新功能）
           git clone https://github.com/axolotl-ai-cloud/axolotl.git
           cd axolotl
           pip install -e .


         Step 3：准备训练数据




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                                        4


---

           // training_data.jsonl — 每行一条训练样本
           {"instruction": "请将以下中文旅游介绍翻译成英文", "input": "故宫
           博物院位于北京市中心，是中国明清两代的皇家宫殿。", "output": "The P
           alace Museum, located in the center of Beijing, was the imp
           erial palace of the Ming and Qing dynasties of China."}
           {"instruction": "分析以下旅游评论的情感倾向", "input": "长城太壮
           观了！但是人太多，排队很久。", "output": "情感倾向：混合（正面+负
           面）。正面因素：对长城景观的赞叹（'太壮观了'）。负面因素：游客过多导致体
           验下降（'人太多，排队很久'）。总体偏正面，但存在明显的旅游体验痛点。"}
           {"instruction": "请用法语介绍天坛的历史背景", "input": "", "out
           put": "Le Temple du Ciel, situé dans le sud-est de Pékin, e
           st un complexe de bâtiments religieux construit entre 1406
           et 1420 sous le règne de l'empereur Yongle de la dynastie M
           ing..."}


         Step 4：编写 Axolotl 配置文件

           # config.yml — Axolotl 微调配置
           base_model: Qwen/Qwen2.5-7B-Instruct
           model_type: AutoModelForCausalLM
           tokenizer_type: AutoTokenizer

           # 数据集配置
           datasets:
             - path: ./training_data.jsonl
                 type: alpaca    # instruction/input/output 格式

           # LoRA 配置
           adapter: lora
           lora_r: 16             # LoRA 秩（越大学习能力越强，显存越多）
           lora_alpha: 32         # 缩放因子
           lora_dropout: 0.05     # 防过拟合
           lora_target_modules:     # 微调哪些层
             - q_proj
              - v_proj
              - k_proj
              - o_proj


☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                           5


---

           # 训练参数
           num_epochs: 3
           micro_batch_size: 4
           gradient_accumulation_steps: 4
           learning_rate: 2e-4
           optimizer: adamw_torch
           lr_scheduler: cosine
           warmup_steps: 100

           # 输出
           output_dir: ./output/qwen-tourism-lora
           logging_steps: 10
           save_steps: 500


         Step 5：启动训练

           # 使用 tmux 保持长时间训练（断开 SSH 也不中断）
           tmux new -s training

           # 启动 Axolotl 微调
           accelerate launch -m axolotl.cli.train config.yml

           # 训练完成后，模型保存在 ./output/qwen-tourism-lora/


         Step 6：上传模型到魔塔（ModelScope）

           # 安装 modelscope
           pip install modelscope

           # 登录魔塔
           modelscope login


           # 上传模型
           python -c "
           from modelscope.hub.api import HubApi



☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                 6


---

           api = HubApi()
           api.upload_folder(
               repo_id='your-username/qwen-tourism-lora',
                 folder_path='./output/qwen-tourism-lora',
                 repo_type='model'
           )
           print('    ✅ 模型上传成功！')
           "


         魔塔（ModelScope）模型库使用
          功能                操作                                        用途

                                                                      找到适合课题的基座模
          浏览模型              modelscope.cn/models → 按任务/语言筛选
                                                                      型
                             modelscope download Qwen/Qwen2.5-7B-     获取模型权重到本
          下载模型              Instruct                                  地/Pod

          上传模型               modelscope upload 或 Python API           分享你微调后的模型

                            README.md 描述模型信息、训练配置、评测结                 学术论文引用、可复现
          模型卡片
                            果                                         性



           🎓     课题价值： 微调后的模型可以：① 作为论文实验的核心组件 ② 上传魔塔
                 （ModelScope）获得学术引用 ③ 作为课题「程序原型」的后端引擎




         📍 模块三：vLLM Serverless 部署（10 分钟）
          ⚡      vLLM 是高性能大模型推理引擎，支持在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 上 Serverless 部署——
                 按需调用、按量计费、空闲零成本。


         为什么用 vLLM Serverless？
          对比维度              商业 API（DeepSeek/OpenAI）        vLLM Serverless（校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama）
          成本                按 token 计费，大量调用费用高             按 GPU 秒计费，批量处理更划算

          模型选择              仅限平台提供的模型                      可部署任意开源模型（含你微调的模型）

          数据隐私              数据发送到第三方服务器                    数据在你的 Pod 中处理




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                                       7


---

          对比维度              商业 API（DeepSeek/OpenAI）   vLLM Serverless（校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama）
                                                      大规模文本处理、敏感数据、自定义模
          适用场景              日常使用、小规模分析
                                                      型


         部署步骤
          1. 登录 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama → Serverless → + New Endpoint
          2. 选择模板：vLLM Inference
          3. 配置模型：

           {
               "MODEL_NAME": "Qwen/Qwen2.5-7B-Instruct",
               "MAX_MODEL_LEN": 8192,
               "GPU_MEMORY_UTILIZATION": 0.9
           }


          1. 选择 GPU 和并发设置：
                  Min Workers: 0（空闲时不收费）
                  Max Workers: 3（最大并发数）
                  GPU: RTX 4090 或 A40
          2. 部署 → 获取 Endpoint URL 和 API Key

         调用示例

           import requests

           # 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama vLLM Serverless API 调用
           ENDPOINT = "https://api.runpod.ai/v2/YOUR_ENDPOINT_ID/runsy
           nc"
           API_KEY = "YOUR_RUNPOD_API_KEY"


           def query_model(prompt):
               response = requests.post(
                   ENDPOINT,
                   headers={"Authorization": f"Bearer {API_KEY}"},
                       json={




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                                  8


---

                             "input": {
                                 "prompt": prompt,
                                 "max_tokens": 512,
                                 "temperature": 0.7
                             }
                       }
                 )
                 return response.json()["output"]

           # 批量处理课题数据
           reviews = ["长城太壮观了！", "故宫人太多了", "天坛很安静很美"]
           for review in reviews:
               result = query_model(f"分析以下旅游评论的情感和文化感知维度：
           {review}")
                 print(f"    📝 {review}\n🤖 {result}\n")

           💡     进阶用法： 部署你用 Axolotl 微调的模型 → 在 MODEL_NAME 中填入你的魔塔
                 模型 ID（如 your-username/qwen-tourism-lora ），即可将微调模型变成 API 服
                 务。




         📍 模块四：Jupyter 云端训练大模型（10 分钟）
          📓      在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 上直接使用 Jupyter Notebook 交互式训练和实验大模型——
                 无需命令行，所见即所得。


         为什么在云端用 Jupyter？




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                               9


---

           ✅     云端 Jupyter 优势                📓   适合的任务

                      GPU 加速，训练速度提                   模型微调实验（参数调
                      升 10-100 倍                     优）

                      显存充足（24-80GB）                  Embedding 生成与向量
                                                     检索
                      交互式调试，逐步验证
                                                     批量文本分析与 NLP
                      可视化训练曲线
                                                     模型效果评估




         在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 中启动 Jupyter
          1. 创建 GPU Pod（选择 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama Pytorch 模板）
          2. Pod 启动后 → 点击 Connect → Jupyter Lab
          3. 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 自动打开浏览器中的 Jupyter Lab 界面
          4. 新建 Notebook → 开始编程

         训练实战：在 Jupyter 中微调模型

           # Cell 1: 检查 GPU 环境
           import torch
           print(f"    🖥️
                      GPU: {torch.cuda.get_device_name(0)}")
           print(f"    💾
                      显存: {torch.cuda.get_device_properties(0).total
           _mem / 1e9:.1f} GB")


           # Cell 2: 加载模型和 LoRA 配置
           from transformers import AutoModelForCausalLM, AutoTokenize
           r
           from peft import LoraConfig, get_peft_model


           model_name = "Qwen/Qwen2.5-7B-Instruct"
           tokenizer = AutoTokenizer.from_pretrained(model_name)
           model = AutoModelForCausalLM.from_pretrained(
                 model_name, torch_dtype=torch.float16, device_map="aut




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                            10


---

           o"
           )


           # LoRA 配置
           lora_config = LoraConfig(
               r=16, lora_alpha=32, lora_dropout=0.05,
               target_modules=["q_proj", "v_proj", "k_proj", "o_pro
           j"],
               task_type="CAUSAL_LM"
           )
           model = get_peft_model(model, lora_config)
           print(f"    🔧
                      可训练参数: {model.print_trainable_parameters
           ()}")



           # Cell 3: 加载训练数据
           from datasets import load_dataset
           dataset = load_dataset("json", data_files="training_data.js
           onl")
           print(f"    📚
                      训练样本数: {len(dataset['train'])}")



           # Cell 4: 配置训练参数并启动
           from transformers import TrainingArguments, Trainer


           training_args = TrainingArguments(
               output_dir="./output",
               num_train_epochs=3,
                 per_device_train_batch_size=4,
                 gradient_accumulation_steps=4,
                 learning_rate=2e-4,
                 logging_steps=10,
                 save_steps=500,
                 fp16=True,
           )


           trainer = Trainer(
               model=model, args=training_args,
               train_dataset=dataset["train"],



☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                           11


---

           )
           trainer.train()       #   🚀 开始训练！
           # Cell 5: 测试微调后的模型
           prompt = "请分析故宫的文化遗产价值及其对入境旅游的影响"
           inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
           outputs = model.generate(**inputs, max_new_tokens=256)
           print(tokenizer.decode(outputs[0], skip_special_tokens=Tru
           e))




           ⚠️    重要提醒： 在 Jupyter 中训练时，使用 tmux 或确保浏览器标签页不关
                 闭。如果需要长时间训练，建议使用 Axolotl 命令行方式（模块二）更稳
                 定。




         📍 模块五：ComfyUI 多模态内容生成（10 分钟）
          🎨      ComfyUI 是基于节点的 AI 图像/视频生成工作流引擎。通过可视化拖拽连
                 接，无需编程即可构建复杂的生成管道。


         ComfyUI 核心概念
            graph
               A["📥 输入节点<br>文本提示词/图像"] --> B["🧠 模型节点<br>SD
           XL / Flux / SD3"]
               B --> C["🎛️ 采样节点<br>步数/CFG/采样器"]
               C --> D["🖼️ 输出节点<br>预览/保存图像"]
                 style A fill:#E3F2FD,stroke:#1565C0
                 style B fill:#F3E5F5,stroke:#7B1FA2
                 style C fill:#FFF3E0,stroke:#E65100
                 style D fill:#E8F5E9,stroke:#2E7D32




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                          12


---

                                     📥 输入节点
                                   文本提示词/图像




                                     🧠 模型节点
                                   SDXL / Flux / SD3




                                     🎛️ 采样节点
                                   步数/CFG/采样器




                                     🖼️ 输出节点
                                    预览/保存图像




         在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 上部署 ComfyUI
         操作步骤：

          1. 登录 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama → Pods → + Deploy
          2. 搜索模板：ComfyUI → 选择官方模板
          3. 选择 GPU：RTX 4090（24GB，图像生成足够）
          4. 部署后点击 Connect → 打开 ComfyUI Web UI
          5. 加载默认工作流 → 修改提示词 → 点击 Queue Prompt 生成

         使用 tmux 保持 ComfyUI 长期运行

           # 创建 tmux 会话
           tmux new -s comfyui


           # 启动 ComfyUI
           cd /workspace/ComfyUI
           python main.py --listen 0.0.0.0 --port 8188



☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                           13


---

           # 按 Ctrl+B 然后按 D 分离会话
           # 重新连接：tmux attach -t comfyui


         课题应用场景
          应用场景                   工作流设计                           对应课题

                                 文本提示 → SDXL/Flux → 风格化处理
          文化遗产宣传图                                                论文 1：目的地形象研究素材
                                 → 多语种文字叠加

          AI vs 真实 UGC 对         同一场景分别用 AI 生成和真实照片 →            论文 1：AI 生成 vs UGC 的形
          比                      做感知实验                           象感知差异

                                 图谱节点 → 文本描述 → AI 生成节点配          论文 2：为知识图谱添加多模
          知识图谱可视化
                                 图                               态展示

          教学素材生成                 课题内容 → 信息图/图解 → 教学演示            专著：教学辅助素材


         提示词示例（课题相关）


           💬     Prompt 1 — 故宫宣传图（中国风）
                 The Forbidden City in Beijing, aerial view, golden rooftops, traditional
                 Chinese architecture, morning light, cinematic, 8k, masterpiece,
                 chinese watercolor style
                 Prompt 2 — 多语种旅游海报
                 A modern tourism poster for the Great Wall of China, multilingual text
                 overlay in Chinese English French Japanese, minimalist design,
                 vibrant colors, professional layout



         📝 课后作业
            A. 在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 创建一个 GPU Pod，完成 Axolotl 安装并使用示例数据运行一次
         LoRA 微调
            B. 在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama Serverless 上部署一个 vLLM Endpoint，用 Python 脚本调用
         API 完成 3 条旅游评论分析
              C. 在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 的 Jupyter Lab 中运行模型推理代码，测试 GPU 加速效果
              D. 部署 ComfyUI 并生成两张北京文化遗产相关的宣传素材图

         📐
☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                                              14


---

         📐 练习试题
         选择题
         Q1. LoRA 微调的核心优势是什么？
             A. 修改模型的全部参数以获得最佳效果
             B. 只训练少量适配器参数，大幅降低显存需求
             C. 不需要任何 GPU 即可完成
             D. 自动生成训练数据
            答案：B — LoRA 只训练约 0.1-1% 的参数，让 RTX 4090（24GB）就能微调 7B
            模型。

         Q2. vLLM Serverless 相比商业 API 的最大优势是？
             A. 永远免费
             B. 不需要 GPU
             C. 可部署任意开源模型，数据隐私可控
             D. 速度一定更快
            答案：C — vLLM Serverless 允许你部署自定义/微调模型，且数据在自己的环境
            中处理。

         Q3. ComfyUI 的工作方式是？
             A. 命令行输入代码生成图像
             B. 通过可视化节点连接构建生成工作流
             C. 只能使用预设模板
             D. 需要编写 Python 脚本
            答案：B — ComfyUI 采用基于节点的可视化界面，拖拽连接即可构建复杂工作
            流。

         Q4. 在 校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 中使用 tmux 的目的是？
             A. 加速 GPU 计算
             B. 防止 SSH 断开后训练中断
             C. 管理 Python 虚拟环境


☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                                    15


---

             D. 自动安装依赖包
            答案：B — tmux 创建持久会话，即使 SSH 断开，训练任务仍在后台运行。

         Q5. Axolotl 配置文件中 lora_r: 16 参数的含义是？
             A. 学习率为 16
             B. LoRA 秩（rank）为 16，控制适配器的学习能力
             C. 训练 16 个 epoch
             D. 使用 16 块 GPU
            答案：B — lora_r 是 LoRA 的秩参数，越大学习能力越强但需要更多显存。



         🔮 下节预告
          ✍️     第 5 课 — 论文不再难产·AI 模块化写作与三级润色

                      中英文论文结构详解

                      模块化写作法 + AI 提示词模板

                      三级润色管道




☁️ 第 4 课C — GPU 云端技术·校内 L20 共享算力 / AutoDL（国内算力云）+ 本地 Ollama 实战                           16


---

