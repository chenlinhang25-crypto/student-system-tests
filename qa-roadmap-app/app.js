const days = [
  {
    id: 1,
    title: "Python 脚本基础",
    goal: "能读写变量、函数、字典、文件，并写出简单测试辅助脚本。",
    tasks: ["复习 list、dict、for、if、函数", "掌握异常处理 try/except", "理解类和对象，不追求复杂继承", "写一个读取测试数据的小脚本"],
    theory: "测开不是拼算法，核心是用代码降低重复测试成本。Python 基础要服务于接口请求、数据处理、断言和报告。",
    code: `case = {"name": "login", "status": 200}
def assert_status(actual, expected):
    if actual != expected:
        raise AssertionError(f"期望 {expected}，实际 {actual}")

assert_status(case["status"], 200)`
  },
  {
    id: 2,
    title: "HTTP 与接口测试",
    goal: "能讲清楚请求、响应、状态码、Header、Cookie、Token、JSON。",
    tasks: ["用 Postman 或浏览器理解 GET/POST", "背下常见状态码 200/201/400/401/403/404/500", "理解 Header 和 Body 的区别", "知道 token 鉴权的基本流程"],
    theory: "接口测试验证的是服务端输入输出。核心关注请求参数、鉴权、业务状态、响应结构、错误码和数据落库。",
    code: `GET /users/1 HTTP/1.1
Authorization: Bearer token_value

响应重点：
1. HTTP 状态码
2. JSON 字段
3. 业务 code/message
4. 数据库或下游状态`
  },
  {
    id: 3,
    title: "requests + pytest",
    goal: "能写接口自动化用例并用 pytest 执行。",
    tasks: ["安装 requests、pytest", "写 GET/POST 请求", "使用 assert 做响应断言", "理解 test_ 开头的测试发现规则"],
    theory: "pytest 负责组织和执行用例，requests 负责发请求。断言必须验证关键业务字段，而不仅是状态码。",
    code: `import requests

def test_get_user():
    r = requests.get("https://example.com/api/users/1")
    assert r.status_code == 200
    assert "id" in r.json()`
  },
  {
    id: 4,
    title: "数据驱动与参数化",
    goal: "能把测试数据从代码里拆出去，用多组数据驱动同一个用例。",
    tasks: ["理解 YAML/JSON/Excel 用来管理测试数据", "掌握 pytest.mark.parametrize", "知道正常、异常、边界数据怎么设计", "避免复制粘贴大量相似用例"],
    theory: "数据驱动解决的是用例重复问题。测试逻辑稳定，输入和期望变化时，应该改数据而不是改代码。",
    code: `import pytest

@pytest.mark.parametrize("username, expected", [
    ("admin", 200),
    ("", 400),
])
def test_login(username, expected):
    assert isinstance(username, str)
    assert expected in [200, 400]`
  },
  {
    id: 5,
    title: "框架分层封装",
    goal: "能解释 api、data、tests、utils、reports 每层负责什么。",
    tasks: ["封装统一 request 方法", "配置 base_url", "增加日志或错误提示", "整理目录结构，形成项目感"],
    theory: "框架不是文件夹堆叠，而是让请求、数据、断言、报告职责清晰，后续接口增加时不用推倒重来。",
    code: `project/
  data/          测试数据
  tests/         测试用例
  utils/         公共方法
  reports/       测试报告
  pytest.ini     pytest 配置`
  },
  {
    id: 6,
    title: "Allure + Jenkins",
    goal: "能说清楚自动化如何生成报告、如何接入持续集成。",
    tasks: ["使用 allure-pytest 生成原始报告", "理解 Jenkins 拉代码、装依赖、跑命令、归档报告", "知道失败用例如何定位", "准备一段 CI 面试话术"],
    theory: "持续集成的价值是让自动化定时或按提交触发，尽早暴露回归问题。报告要服务于定位，而不是只服务于好看。",
    code: `pytest --alluredir=reports/allure-results
allure serve reports/allure-results`
  },
  {
    id: 7,
    title: "简历与模拟面试",
    goal: "把能力表达成项目价值，准备面试能讲的故事。",
    tasks: ["把自动化项目写进简历", "准备 8 个高频问题", "讲清楚一次接口自动化失败定位过程", "开始投自动化测试/初级测开岗位"],
    theory: "面试官不是只看你背了多少工具名，而是看你是否能用工具解决稳定性、效率、覆盖率和定位问题。",
    code: `项目价值表达：
将核心接口回归用例自动化，减少重复手工回归时间；
通过参数化和统一请求封装提升用例维护效率；
接入 Jenkins 后支持每日构建并输出测试报告。`
  }
];

const theoryCards = [
  ["测试金字塔", "单元测试多、接口测试适中、UI 测试少。接口自动化通常比 UI 更稳定，回归收益更高。"],
  ["断言策略", "至少断言状态码、业务 code、关键字段、异常提示。重要场景可结合数据库或后置查询验证。"],
  ["等价类", "把输入分成有效类和无效类，每类选代表数据，减少无意义重复。"],
  ["边界值", "重点测最小值、最大值、刚好等于、刚好超过。很多缺陷出在边界。"],
  ["幂等性", "同一个请求执行一次和多次，结果应一致或符合预期。查询、删除、支付回调常被问。"],
  ["鉴权", "常见是 Cookie、Session、Token、JWT。接口自动化要处理登录态复用和过期刷新。"],
  ["Mock", "当依赖服务不稳定或成本高时，用模拟响应隔离测试对象。"],
  ["CI/CD", "CI 是持续集成，自动拉代码、构建、测试；CD 是持续交付/部署。测试报告要能追踪失败原因。"]
];

const quiz = [
  { q: "pytest 默认会识别哪类测试函数？", options: ["test_ 开头的函数", "任意函数", "main 函数"], answer: 0, why: "pytest 默认发现 test_ 开头的函数或 Test 开头类中的测试方法。" },
  { q: "接口自动化中，只断言 HTTP 200 是否足够？", options: ["足够", "不够，还要验证业务字段和关键数据", "只要接口快就行"], answer: 1, why: "HTTP 200 只能说明请求成功到达并返回，业务可能仍然失败。" },
  { q: "401 和 403 的常见区别是什么？", options: ["401 未认证，403 无权限", "401 服务端错误，403 参数错误", "没有区别"], answer: 0, why: "401 通常表示未登录或 token 无效，403 通常表示登录了但权限不足。" },
  { q: "数据驱动主要解决什么问题？", options: ["让页面更好看", "减少重复用例代码", "替代所有手工测试"], answer: 1, why: "同一测试逻辑用多组输入和期望执行，避免复制粘贴。" },
  { q: "Jenkins 在自动化测试中的作用更接近什么？", options: ["代码编辑器", "持续集成调度器", "数据库"], answer: 1, why: "Jenkins 常用于拉代码、安装依赖、执行测试、生成报告和通知。" },
  { q: "接口测试中 token 一般放在哪里？", options: ["Header 或 Cookie", "文件名里", "截图里"], answer: 0, why: "Bearer Token 常放 Authorization Header，部分系统用 Cookie 维持登录态。" }
];

const interview = [
  ["你们接口自动化框架怎么设计？", "按 config、data、utils、tests、reports 分层。config 管理环境和 base_url，data 放测试数据，utils 封装请求和读取数据，tests 写业务用例，reports 输出 Allure 结果。"],
  ["如何处理接口依赖？", "优先通过前置 fixture 创建数据，拿到 id/token 后传给后续步骤；也可以准备稳定测试数据，或用 mock 隔离不稳定依赖。"],
  ["自动化失败怎么定位？", "先看失败断言和日志，再看请求参数、响应体、环境配置、测试数据、接口变更，最后确认是不是服务端缺陷。"],
  ["怎么设计接口测试用例？", "覆盖正常流、必填为空、参数类型错误、边界值、权限不足、重复提交、数据不存在、并发或幂等场景。"],
  ["为什么选择接口自动化而不是 UI 自动化？", "接口更接近业务逻辑，执行快、稳定性更好、维护成本更低，适合作为回归主力。UI 自动化适合覆盖关键端到端流程。"],
  ["如何让自动化更稳定？", "减少环境依赖，清理测试数据，避免强依赖执行顺序，增加合理等待和重试，断言清晰，日志足够定位。"]
];

const done = new Set(JSON.parse(localStorage.getItem("qa-sdet-done") || "[]"));

function saveProgress() {
  localStorage.setItem("qa-sdet-done", JSON.stringify([...done]));
  document.getElementById("progressText").textContent = `${done.size}/7`;
  document.getElementById("progressFill").style.width = `${(done.size / 7) * 100}%`;
}

function renderDays() {
  const list = document.getElementById("dayList");
  list.innerHTML = days.map(day => `
    <article class="dayCard">
      <div class="dayTop">
        <div>
          <span class="badge">Day ${day.id}</span>
          <h3>${day.title}</h3>
          <p class="meta">${day.goal}</p>
        </div>
        <button class="completeBtn ${done.has(day.id) ? "done" : ""}" data-day="${day.id}">
          ${done.has(day.id) ? "已完成" : "完成"}
        </button>
      </div>
      <ul class="taskList">${day.tasks.map(task => `<li>${task}</li>`).join("")}</ul>
      <p><strong>理论记忆：</strong>${day.theory}</p>
      <pre class="codeBlock"><code>${day.code}</code></pre>
    </article>
  `).join("");
}

function renderTheory() {
  document.getElementById("theoryList").innerHTML = theoryCards.map(([title, body]) => `
    <article class="theoryCard"><strong>${title}</strong><p class="meta">${body}</p></article>
  `).join("");
}

function renderQuiz() {
  document.getElementById("quizList").innerHTML = quiz.map((item, index) => `
    <article class="quizCard">
      <h3>${index + 1}. ${item.q}</h3>
      <div class="quizOptions">
        ${item.options.map((option, optionIndex) => `
          <label>
            <input type="radio" name="q${index}" value="${optionIndex}">
            <span>${option}</span>
          </label>
        `).join("")}
      </div>
    </article>
  `).join("");
}

function renderInterview() {
  document.getElementById("interviewList").innerHTML = interview.map(([q, a], index) => `
    <article class="interviewCard">
      <h3>${index + 1}. ${q}</h3>
      <p class="answer">${a}</p>
    </article>
  `).join("");
}

document.querySelectorAll(".tab").forEach(tab => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab, .view").forEach(el => el.classList.remove("active"));
    tab.classList.add("active");
    document.getElementById(tab.dataset.view).classList.add("active");
  });
});

document.addEventListener("click", event => {
  if (event.target.matches(".completeBtn")) {
    const id = Number(event.target.dataset.day);
    done.has(id) ? done.delete(id) : done.add(id);
    renderDays();
    saveProgress();
  }
});

document.getElementById("resetBtn").addEventListener("click", () => {
  done.clear();
  renderDays();
  saveProgress();
});

document.getElementById("checkQuizBtn").addEventListener("click", () => {
  let score = 0;
  const wrong = [];
  quiz.forEach((item, index) => {
    const selected = document.querySelector(`input[name="q${index}"]:checked`);
    if (selected && Number(selected.value) === item.answer) {
      score += 1;
    } else {
      wrong.push(`${index + 1}. ${item.why}`);
    }
  });
  const result = document.getElementById("quizResult");
  result.hidden = false;
  result.innerHTML = `<strong>得分：${score}/${quiz.length}</strong><br>${wrong.length ? wrong.join("<br>") : "很好，今天可以继续往下一项推进。"}`;
});

renderDays();
renderTheory();
renderQuiz();
renderInterview();
saveProgress();
