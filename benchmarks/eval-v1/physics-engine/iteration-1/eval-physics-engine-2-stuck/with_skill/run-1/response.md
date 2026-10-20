The user says: "我的小球掉到地面上会慢慢陷进去，最后穿过地面。" (My ball falls onto the ground and slowly sinks into it, eventually passing through the ground.)

This is a physics simulation bug report. But I have no context about their project. Let me look at the workspace to see what files exist.

Let me explore the workspace first.The workspace only contains skill files, no user project files. Let me check for any project files outside .agents.工作区里只有技能文件，没有你的项目代码，先按症状给诊断。

“缓慢下陷 → 最终穿过”是接触求解的典型症状，手写物理循环里常见原因按可能性排：

1. **穿透只做比例修正**：每帧只把重叠深度推回一部分（如 `y += penetration * 0.2`），重力每帧又压下去一点，净效果是蠕沉，直到完全穿过。修法：位置一步投影回表面。
2. **位置和速度只处理了一个**：碰撞时把球拉回地面但速度仍向下（或只翻速度、位置留在地面下），每帧净下移。
3. **弹簧接触刚度不足**：`F = k·penetration` 的平衡深度是 `mg/k`，k 太小球停在地面以下；力有上限或加了阻尼时会继续下沉。
4. **检测点用错**：用球心 `y < 0` 判地，球先陷进一个半径才触发，应为 `y - r < 0`。
5. **dt 过大 + 显式欧拉**：接触弹簧较硬时每帧注入能量或直接跳过检测（隧穿）。

标准修法（半隐式欧拉 + 硬投影 + 速度反射）：

```python
vy += g * dt          # 先更新速度
y  += vy * dt         # 再用新速度更新位置
if y - r < 0:         # 球底触地
    y = r             # 位置硬投影回表面
    vy = -vy * e      # 速度反射，e 为恢复系数（0~1）
    if abs(vy) < 20:  # 低速贴地，防无限微弹跳
        vy = 0
```

顺序是关键：先积分速度再积分位置；碰撞后位置一步归位、速度同步处理，缺一个都会蠕沉。

用现成引擎（Unity / Godot / Matter.js / Cannon.js）的话，对应检查：地面碰撞体是否被设成 Trigger、刚体是否误设为 Kinematic、Fixed Timestep 是否过大、高速球是否需要开 CCD。

把物理步进那段代码贴出来（或告诉我文件路径），我帮你定位到具体行。