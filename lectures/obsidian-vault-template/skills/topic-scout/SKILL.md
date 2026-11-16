---
name: topic-scout
description: "Use when user wants to discover research topics, evaluate a candidate topic, find a research gap, or run FINER feasibility checks. Outputs candidate topics with novelty/value/feasibility scores."
version: 1.0.0
author: AI4S Course
license: MIT
created: 2026-09-19
updated: 2026-11-15
type: 笔记
---

# Topic Scout Agent

围绕高校文科教师（外语 / 翻译 / 文学 / 旅游 / 国关 / 经济）的科研实际，完成从研究兴趣到可执行研究问题的收敛：**发散候选选题 → 核验学术空白 → FINER 体检 → 输出选题评估报告**。

## Models

### 选题三角（Topic Triangle）

```
        Gap（学术空白）
           /\
          /  \
         /    \
        /  选题  \
       /________\
Feasibility      Venue
（可行性）      （发表去向）
```

| 情况 | 问题 | 建议 |
| :-- | :-- | :-- |
| 有 Gap + 可行，无 Venue | 题目太偏 | 调整研究角度或更换目标期刊层级 |
| 有 Gap + 有 Venue，不可行 | 理想化 | 缩小研究范围、限定对象与时间 |
| 可行 + 有 Venue，无 Gap | 重复研究 | 换语境、换方法或换理论视角 |
| 三者兼备 | 理想选题 | 推进研究设计 |

### FINER 五维体检

| 维度 | 含义 | 检查问题 |
| :-- | :-- | :-- |
| **F**easible | 可行性 | 时间、资源、能力是否匹配？ |
| **I**nteresting | 趣味性 | 研究者是否真正愿意长期投入？ |
| **N**ovel | 创新性 | 相对已有文献的新贡献是什么？ |
| **E**thical | 伦理性 | 是否符合学术伦理与数据合规？ |
| **R**elevant | 相关性 | 对学科与实践是否有明确价值？ |

### RQ 锤炼四步法

1. **一句话兴趣**：`我对[领域]中的[具体问题]感兴趣，因为[原因]。`
2. **5W1H 边界锁定**：Who / What / Where / When / Why / How。
3. **RQ 三大句式**：
   - 描述型（What）：`……的现状如何？`
   - 关系型（How/Why）：`哪些因素影响……？`
   - 比较型（Difference）：`不同……之间存在什么差异？`
4. **FINER 体检**：逐维打勾并写下结论。

## Prompt Templates

### Candidate Topic Generation

````
我是[学科领域]的高校教师，研究兴趣包括[兴趣1]、[兴趣2]，
可支配时间约[时长]，可获取的材料为[公开语料/问卷/访谈/档案]，
目标发表去向为[CSSCI 核心 / 北核 / SSCI / 校级课题]。

请帮我完成选题发散：
1. 提供 3 个候选研究选题，避免宏大而空泛的表述
2. 每个选题包含：一句话描述、核心研究问题、研究空白（Gap）、潜在创新点
3. 按选题三角给出打分（1-10）：
   - novelty（创新性）
   - value（学术与实践价值）
   - feasibility（数据、时间、能力可行性）
4. 说明每个选题最适合的发表去向与理由
5. 在末尾附上如下 JSON 代码块：

```json
{
  "topics": [
    {
      "title": "候选选题名称",
      "gap": "研究空白描述",
      "novelty": 8,
      "value": 8,
      "feasibility": 7,
      "rationale": "选题依据与可行性说明"
    }
  ]
}
```

注意：
- 只使用真实存在、可回源核验的文献方向，不得虚构具体文献条目
- 同时给出“不建议做”的理由，帮助我排除伪需求选题
````

### Gap Verification

```
我正在考虑研究「[候选选题]」。

请基于以下已读文献信息，帮我核验研究空白：
1. 方法论空白：哪些方法尚未被用于该问题？
2. 语境空白：哪些语种、地区、机构类型或人群尚未被覆盖？
3. 理论空白：哪些理论关系尚未被检验或整合？
4. 时间空白：近 2 年的新现象是否已被跟进？

已读文献信息（题名 / 作者 / 年份 / 核心发现）：
- [文献1]
- [文献2]
- [文献3]

请输出：
- 每个维度的空白判断及支撑理由
- 需要我到知网（CNKI）或 OpenAlex 补充检索的检索式
- 该空白是否足以支撑一篇 CSSCI / SSCI 论文的判断
```

### FINER Check & RQ Refinement

```
请用 FINER 框架评估以下选题，并帮我锤炼研究问题。

选题：[选题描述]
研究者背景：[学科 / 职称 / 可用时间与资源]
初步研究问题：[RQ 草稿]

请输出：
1. FINER 五维逐项评估（Feasible / Interesting / Novel / Ethical / Relevant），每项给出 1-5 分与理由
2. 用 5W1H 锁定研究边界，指出当前表述中过宽或过窄的部分
3. 改写为 2-3 条可检验的 RQ（标注描述型 / 关系型 / 比较型）
4. 给出结论：推进 / 调整后推进 / 放弃，并说明关键风险
5. 提醒需要回源核验的文献、数据与政策依据
```

## Workflow

1. **发散**：用「Candidate Topic Generation」生成 3 个候选选题。
2. **核验**：用「Gap Verification」在知网 / OpenAlex / WOS 实检文献分布，剔除伪空白。
3. **收敛**：用「FINER Check & RQ Refinement」锁定 1 个主攻选题与 2 条备选 RQ。
4. **落盘**：套用 `templates/选题评估模板.md` 写入 Vault，并把结构化 JSON 结果同步到 iScholar `TopicScout` 运行记录。
5. **留痕**：在《证据与来源台账》登记关键文献与政策依据，标注许可状态与复核人。

## Output Location

- 选题评估报告：`01-选题池/` 或项目的 `00_项目卡/`，建议命名 `YYYY-MM-DD_选题评估_<关键词>.md`
- 结构化结果：随 iScholar 运行记录导出至 `03_已复核成果/`
- 统一标签：`#选题评估` `#选题三角` `#FINER`

## Quality Checklist

- [ ] 每个候选选题都写清了 Gap，而不是只描述现象
- [ ] 三维评分有理由，不是无依据的数字
- [ ] RQ 已完成 5W1H 边界锁定，对象、语境、时间明确
- [ ] FINER 五维均有结论，伦理与数据合规未被跳过
- [ ] 引用的文献、政策与统计数字均已回源核验，未把模型生成条目当作真实文献
- [ ] 已记录放弃的选题及放弃理由，便于后期复盘
