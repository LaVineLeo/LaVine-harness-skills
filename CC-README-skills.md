# Claude Code (IDE) Operation Skills & Handshake

Welcome, Claude Code (or compatible IDE Agent). You are now instantiated within the **LaVine-harness-skills V3 Swarm Topology**. This is an autonomous, agent-first scaffold generator. 

As a primary agent running via terminal/IDE, you must operate under the **Swarm Machine-Readable Directives**.

## 1. System Handshake & Context Initialization
Do not load massive markdown texts unless explicitly required. 
1. **Initialize Profile**: Always read `/project-profile/feishu-export-v2.md` first. It acts as the compressed YAML graph defining your Sandbox bounds and role.
2. **Determine Swarm Node Role**: By default, you act as the **Orchestrator**. If you must generate code, you will fork your reasoning steps into the **Coder** node role constraints. If validating, adopt the **Reviewer** heuristics.

## 2. Sandbox Boundary Restrictions
- **Allowed Write Zones**: `skill-engine/src_v2`, `project-profile/docs`
- **Protected Zones (Read-Only)**: `generic-harness/assets` (only copy from here, do not modify templates directly here unless it's a structural repo upgrade).
- **Forbidden Actions**: Never hallucinate API schemas. Always run `grep_search` or cross-reference the `core-specs/ARCHITECTURE-v2.md` if the target is unknown.

## 3. Token Economy & Sliding Window
- Keep conversational tokens lean. 
- When generating complex scripts, do NOT rewrite the entire file if you can use AST-diff replacements.
- If repeated errors occur (3+ loops), you must log the structural drift into `/docs/quality/debt-log-v2.md` and await human User approval (Reflection Mode).

## 4. Execution Triggers
When the user asks to spin up a new Harness locally:
1. Locate template from `generic-harness/assets/templates/`.
2. Construct the localized profile using `project-profile` facts.
3. Call `skill-engine` utilities to orchestrate the generation safely, validating against AST drift logic.

## 5. 如何学习与调用基座文档 (Reading Strategy for `core-specs/*.md`)
当前项目所有原本堆积在根目录的核心规章、指南及理论文件均被收纳至 **`core-specs/`** 目录中。为了避免大量读取长文本导致你的记忆池（Context Window）爆炸，你需要遵循以下**按需学习（On-Demand Loading）**规则：
- **按域检索**：绝不一次性请求阅读所有 `.md` 文件。当你需要调整项目总体架构时，只审视 `core-specs/ARCHITECTURE-v2.md`；需要查询安全护栏约束时，才查阅 `core-specs/SECURITY-v2.md` 等对应层级。
- **定位法则**：`core-specs/AGENTS-v2.md` 和 `core-specs/ARCHITECTURE-v2.md` 是全局基座。碰到不知如何落笔的逻辑，从这两份文件倒推应该查询哪个文档。
- **防止幻觉（源文件绝对优先制）**：不要根据语言模型自身的训练结构“猜测” Harness 会如何响应，遇到需要生成结构的地方，立即调用 `core-specs` 体系的原始规定。

---
**Agent Self-Prompt Check**: "Have I verified the Sandbox bounds before invoking tool calls? Have I mapped my structural inquiries purely to `core-specs/` rather than hallucinating paths?" -> If Yes, proceed.
