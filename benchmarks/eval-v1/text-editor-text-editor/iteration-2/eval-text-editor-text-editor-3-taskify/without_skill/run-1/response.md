The user wants me to convert the "Build Your Own Text Editor" tutorial (kilo editor tutorial from viewsourcecode.org) into a Claude Code executable learning task list. Let me first fetch the tutorial to understand its structure, then create a task list.

Let me fetch the tutorial's table of contents first.工作区是空的。教程共 8 章、184 个步骤。我先抓取各章节内容，了解每章的步骤结构，再生成任务清单。继续抓取剩余章节，提取每章的步骤范围和关键内容。各章步骤边界已确认（第1章: 1-2, 第2章: 3-19, 第3章: 20-54, 第4章: 55-100, 第5章: 101-130, 第6章: 131-141, 第7章: 142-?）。教程声称共 184 步，我验证一下最后一步的编号。184 个 tag 确认了 184 步。现在按拓扑顺序导出完整步骤名列表，用于精确划分章节任务。There's a commit "open-file c-unknown" that doesn't match the pattern. Let me check: 185 commits total, 183 with " cN" suffix, plus "open-file c-unknown" and "-" (the empty last commit). So 183 + 1 + 1 = 185. But there are 184 tags. So "open-file" is a step too (step with unknown chapter). Let me rebuild including open-file.

Actually wait — the "-" commit is the last one (empty message, probably the final commit). Let me check: 184 tags = 184 steps. Commits: 185. The "-" commit at the end is probably not a step. So steps = 184 = 183 (cN commits) + open-file (c-unknown).

Let me verify open-file's position and rebuild the list properly.Hmm, "open-file c-unknown" still has the suffix because my sed pattern `s/ c[0-9-]+$/` — wait, I used `sed -E 's/ c[0-9-]+$//'` which should match " c-unknown". Let me check — the output shows "58: open-file c-unknown" still. The issue: `[0-9-]+` matches "-unknown"? No — "unknown" contains letters. " c-unknown" = space + "c-unknown". My regex ` c[0-9-]+$` requires the string after " c" to be only digits/hyphens until end. "c-unknown" has letters, so no match. Fix: `s/ c-unknown$//` separately or use ` c[a-z0-9-]+$`.184 步的完整清单和章节边界已全部确认（tag 名 = step 名，与教程页面的 Step 编号逐一吻合）。现在生成任务清单文件。修正一处笔误后做最终核对。552 说明有重复匹配，列出实际匹配项核对。核对完成：里程碑行恰好覆盖 184 步，章节边界连续无缝隙、无重叠。任务清单已生成。

## 完成：`TASKS.md`

**来源核实**（全部基于实际证据，非推测）：
- 从 `kilo-src` 仓库导出 184 个 tag 的拓扑顺序，得到完整 step 名列表（`main` → `propagate-highlight`），与教程页面上的 Step 编号逐一吻合（如 step 130 = `basic-search`、step 142 = `syntax-digits`）
- 章节边界：Ch1: 1–2 / Ch2: 3–19 / Ch3: 20–54 / Ch4: 55–100 / Ch5: 101–130 / Ch6: 131–141 / Ch7: 142–184，已验证连续覆盖 184 步无缺口

**清单结构**：
- **执行协议**：每 step 固定 7 步流程 —— 定位当前 step → 取参考 diff → 手写改动 → `make` → 验证 → commit（message = step 名）→ 卡住时与参考 tag 逐字符 diff
- **交互测试**：用 macOS 自带 `expect` 驱动 pty（kilo 是全屏 TUI，无法用管道测试），附按键字节表
- **7 章 × 里程碑表**：每个里程碑 3–9 个 step，含内容摘要和可观察的验收点（区分 "compiles" / "无观察效果" 两类）
- **每章验收 + 最终验收**：8 条可执行检查项
- **断点续做**：`git log` 即进度表，新会话可从任意 step 恢复

关键设计决策：以 git tag 名（= step 名）作为唯一进度锚点，commit message 与 tag 名一一对应，使 `git -C .kilo-src diff <prev> <cur>` 永远可得，无需解析教程 HTML。