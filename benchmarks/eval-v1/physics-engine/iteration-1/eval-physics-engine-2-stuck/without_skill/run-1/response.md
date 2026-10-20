The user says their ball slowly sinks into the ground and eventually passes through it. This is a physics engine project (build-your-own-x physics engine). I need to look at the code to diagnose. Let me explore the workspace first.Empty workspace? Let me check with bash.工作目录是空的，我看不到你的代码。把物理引擎文件放进 `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-physics-engine-2`（或直接贴出来），我就能定位具体问题。

先说这个症状的典型原因，你可以对照排查：

1. **穿透修正量太小或带 slop**：每帧只修正 `penetration * 0.2` 之类的小比例，或设了较大的 `slop`（允许穿透量），重力每帧都在把球往下压，修正追不上，球就持续下沉，直到球心越过地面后碰撞检测失效，直接掉出去。

2. **碰撞检测是单侧判断**：比如平面碰撞写成 `0 < distance < radius`（只检测球心在平面上方且重叠的情况）。球心一旦沉到平面以下，检测条件不成立，重力继续拉它穿过去。改成 `distance < radius`（半空间判断）即可。

3. **法线方向反了**：修正位置时用 `pos - normal * penetration`，如果算出的 normal 朝下，每帧修正反而把球往地里推，表现就是匀速下沉直到穿透。

4. **积分顺序问题**：先做碰撞响应、后施加重力并积分位置，会导致每帧响应完又往下移一步。正确顺序是：施力/积分 → 碰撞检测 → 位置修正 → 速度修正。

把代码发我，我直接指出是哪一行。