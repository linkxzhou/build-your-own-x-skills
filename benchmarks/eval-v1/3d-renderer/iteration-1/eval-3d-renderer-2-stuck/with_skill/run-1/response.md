The user is asking about shadow acne in ray tracing - their sphere renders as black speckled noise. This is a classic ray tracing problem. Let me think about whether I need to look at their code.

The user says "我的光线追踪球体渲染出来全是黑色的点状噪声（shadow acne）。怎么回事？" - "My ray-traced sphere renders as all black speckled noise (shadow acne). What's going on?"

This is a question, likely they have code in the workspace. Let me check if there's code in the workspace first. The instructions say to explore before proposing edits. Let me glob for files to see if there's a ray tracer project.

Actually, the question might be answerable directly - shadow acne is a well-known issue caused by self-intersection due to floating point precision: the shadow ray origin is exactly on the surface, and due to floating point error, the ray intersects the surface itself at t≈0, so the point is considered in shadow.

The standard fixes:
1. Offset the shadow ray origin along the surface normal (epsilon bias): `shadow_origin = hit_point + normal * 1e-4` (or 1e-3).
2. Use a minimum t value (t_min) when checking intersections, e.g., ignore intersections with t < epsilon.
3. For spheres, compute the hit point by re-deriving from t and center, or use the "double float" trick.

But wait - the user says the whole sphere is black speckled noise, not just shadowed areas. Shadow acne typically manifests as black speckles/mottling on lit surfaces where shadow rays self-intersect. If the entire sphere is black noise, it could also be:
- Normal flipping issue (normal pointing inward, so dot(N, L) < 0 everywhere)
- The hit point used for shading is wrong
- Actually shadow acne does look like black speckled noise across the lit surface.

Let me check the workspace for their code first. The developer instructions say to explore before modifying code, and to use parallel read-only tools. Let me glob for source files.

I should look for the code. Let me do a glob for common patterns like **/*.py, **/*.cpp, **/*.c, **/*.rs, **/*.js etc. Or just glob **/* to see what's there.

Let me start with a broad glob and grep for shadow-related terms.

Plan:
1. Glob for source files in workspace.
2. If found, read the relevant intersection/shadow code.
3. Diagnose and propose fix.

If no code found, answer the general question with the classic explanation and fixes.

Let me do parallel calls: glob **/* and maybe grep for "shadow" or "intersect".

Actually glob pattern "**/*" might return a lot. Let me try "**/*.py", "**/*.cpp", "**/*.c", "**/*.cc", "**/*.rs", "**/*.js", "**/*.ts" — that's many calls. Better: bash `ls -la` or `find . -type f | head -50`. The bash tool is available. Let me use `find . -maxdepth 3 -type f -not -path '*/node_modules/*' | head -100`.

Let me do that first, then read the relevant files.工作区里没有你的代码，我按典型成因讲。黑色点状噪声是自遮挡（self-intersection）：阴影射线从表面点出发，浮点舍入让求交函数在 t≈0 处命中球体自身，这个"自交"被当成遮挡物，于是亮面上撒满黑点。球面曲率使误差随位置变化，所以呈噪点而非均匀变暗。

修复按优先级：

1. **沿法线偏移阴影射线起点**（最常用）：
```cpp
vec3 shadow_orig = hit_p + N * 1e-4;   // N 为朝外的几何法线
// shadow_orig = hit_p - N * 1e-4;     // 若光线从背面来则反向
```

2. **求交时忽略过近的命中**（Ray Tracing in One Weekend 的做法）：
```cpp
// 判断遮挡时
if (t > 1e-4 && t < dist_to_light) occluded = true;
```
两条一起用最稳。epsilon 取场景尺度的 1e-4 ~ 1e-3：太大产生 peter-panning（阴影脱离物体、接缝漏光），太小 acne 复发。

3. **反射/折射射线同样处理**。二次射线起点也要 `hit_p + N * eps`，否则镜面反射里会出现同样的噪点。

4. **提高求交精度**（可选）：球面交点用 `center + t * unit_dir` 相对球心重算，减少大坐标下的精度损失；单精度场景可换 `double` 验证是否是精度问题。

另外排查一点：如果整球连亮面都均匀发黑，检查法线朝向——`dot(N, L)` 为负会被 clamp 成 0，表现也是全黑，但那是法线翻转，和 acne 的修复方式不同（翻转法线或用 `faceforward`）。

把求交/阴影代码贴出来（或放进工作区），我可以直接指出具体行。