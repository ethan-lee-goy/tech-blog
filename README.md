# Ethan Lee's Technical Blog

> 在线阅读：https://ethan-lee-goy.github.io/tech-blog

个人技术博客，记录和分享在人工智能、自动驾驶和算法领域的学习与研究。

## 博客主题

| 主题 | 说明 |
|------|------|
| 深度学习 | 神经网络架构、训练技巧、最新研究 |
| 强化学习 | RL算法、策略优化、应用案例 |
| 博弈算法 | 博弈论基础、纳什均衡、多智能体系统 |
| 车辆控制 | 轨迹跟踪、稳定性控制、自适应控制 |
| 规划算法 | 路径规划、运动规划、决策规划 |
| 世界模型 | 环境建模、预测模型、模型学习 |

## 技术栈

- 使用 [MkDocs](https://www.mkdocs.org/) + [Material](https://squidfunk.github.io/mkdocs-material/) 主题构建
- 通过 [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter) 原生渲染 Jupyter Notebook
- 支持 KaTeX 数学公式渲染
- GitHub Actions 自动构建部署

## 本地预览

```bash
pip install -r requirements.txt
mkdocs serve
```

## 添加文章

1. 将 `.md` 或 `.ipynb` 文件放到 `docs/` 对应目录下
2. 在 `mkdocs.yml` 的 `nav` 中添加链接
3. 提交并推送，GitHub Actions 自动部署

## 作者

Ethan Lee ([@ethan-lee-goy](https://github.com/ethan-lee-goy))
