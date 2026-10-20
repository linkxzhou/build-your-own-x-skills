The user is asking about shadow acne in their ray tracer - black speckled noise on rendered spheres. This is a classic ray tracing problem. Let me first look at their code to understand their implementation before answering.

Let me explore the workspace to find the ray tracer code.工作区里没有代码文件，我直接讲原理和修法。

## 原因

Shadow ray 从命中点 `P` 出发时，浮点舍入让 `P` 实际上略微落在球面**内侧**（或正好在球面上）。这条 shadow ray 会以 `t ≈ 0` 再次击中球体自己，于是球体"遮挡了自己"——每个像素是否中招取决于舍入的随机性，所以表现为黑色点状噪声，集中在被照亮的面和阴影 terminator 附近。

## 修复（任选其一，通常两个都做）

**1. 沿法线偏移 shadow ray 起点**（最常用）：

```cpp
Vec3 shadowOrig = hitPos + N * 1e-3f;   // N 是表面法线，朝外
if (inShadow(shadowOrig, lightDir)) ...
```

注意偏移方向是**法线方向**，不是光线方向。沿法线推对球体在几何上是严格安全的（法线必然指向球外）。

**2. 求交时忽略过近的 t**：

```cpp
// ray-sphere 求交后
if (t > 1e-4f) return t;   // 丢弃 t ≈ 0 的自交
```

对 shadow ray 传一个 `t_min = 1e-4` 的下界即可，主光线仍用 `t_min = 0`。

**3. 二次光线同样处理**：反射、折射光线的起点也要 `hitPos + N * eps`（反射沿 `N`，折射沿 `-N`），否则镜面上会出现同样的黑斑或暗环。

## 参数选择

- `eps` 取 `1e-3` ~ `1e-4`（float 精度下别小于 `1e-5`，double 可以更小）。
- 太大会导致阴影"漂移"（peter-panning：物体底部和它的影子脱开），场景尺度大（坐标上千）时按比例放大 `eps`。
- 如果用 float 且场景坐标很大，优先考虑改 double，比调 eps 更治本。

改完后黑点应完全消失，阴影边缘干净。如果还有残留噪声，把求交代码贴出来，我帮你看具体是哪一步舍入引入的。