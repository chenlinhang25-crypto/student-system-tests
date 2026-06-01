# 测试转测开 7 天冲刺包

这个目录里有两部分：

- `qa-roadmap-app/`：本地学习打卡应用，包含每日学习步骤、理论速记、考试练习、面试题和简历项目写法。
- `api_automation_demo/`：Python 接口自动化示例项目，用来练 pytest、requests、YAML 数据驱动和 Allure 报告。

## 启动学习应用

```powershell
cd C:\Users\陈林航\Documents\Codex\2026-05-28\new-chat\qa-roadmap-app
python -m http.server 4173
```

浏览器打开：

```text
http://localhost:4173
```

## 运行接口自动化示例

```powershell
cd C:\Users\陈林航\Documents\Codex\2026-05-28\new-chat
.\.venv\Scripts\Activate.ps1
cd .\api_automation_demo
pytest
pytest --alluredir=reports/allure-results
```

如果已经安装 Allure 命令行，可运行：

```powershell
allure serve reports/allure-results
```
