#!/bin/bash

# 将项目根目录的 skills 目录软链到各 AI 工具目录
# 目标目录: .claude/skills, .gemini/skills, .trae/skills, .codebuddy/skills

set -e

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 源目录
SOURCE_DIR="skills"

# 目标目录列表（父目录）
TARGET_PARENTS=(
    ".claude"
    ".gemini"
    ".trae"
    ".codebuddy"
)

# 检查源目录是否存在
if [ ! -d "$SOURCE_DIR" ]; then
    echo "❌ 源目录不存在: $SOURCE_DIR"
    echo "请先创建 skills 目录并添加技能"
    exit 1
fi

echo "📦 源目录: $SOURCE_DIR"
echo ""

# 错误标志
HAS_ERROR=0

# 第一步：检查所有目标目录
echo "🔍 检查目标目录..."
for PARENT in "${TARGET_PARENTS[@]}"; do
    TARGET_PATH="$PARENT/skills"
    
    if [ -e "$TARGET_PATH" ] && [ ! -L "$TARGET_PATH" ]; then
        echo "  ❌ $TARGET_PATH 已存在且不是软链"
        echo "     请手动移动或删除: rm -rf $TARGET_PATH"
        HAS_ERROR=1
    elif [ -L "$TARGET_PATH" ]; then
        echo "  ✓ $TARGET_PATH (已是软链)"
    else
        echo "  ○ $TARGET_PATH (待创建)"
    fi
done
echo ""

# 如果有错误，退出
if [ $HAS_ERROR -eq 1 ]; then
    echo "❌ 存在冲突，请先手动处理上述目录后重新运行"
    exit 1
fi

# 第二步：创建软链
echo "🔗 创建软链..."
for PARENT in "${TARGET_PARENTS[@]}"; do
    TARGET_PATH="$PARENT/skills"
    RELATIVE_SOURCE="../$SOURCE_DIR"
    
    # 创建父目录（如果不存在）
    mkdir -p "$PARENT"
    
    if [ -L "$TARGET_PATH" ]; then
        # 检查软链是否指向正确
        CURRENT_TARGET=$(readlink "$TARGET_PATH")
        if [ "$CURRENT_TARGET" = "$RELATIVE_SOURCE" ]; then
            echo "  ✓ $TARGET_PATH (已存在，无需更新)"
        else
            # 更新软链
            rm "$TARGET_PATH"
            ln -s "$RELATIVE_SOURCE" "$TARGET_PATH"
            echo "  ↻ $TARGET_PATH (已更新)"
        fi
    else
        # 创建新的软链
        ln -s "$RELATIVE_SOURCE" "$TARGET_PATH"
        echo "  + $TARGET_PATH (已创建)"
    fi
done
echo ""

echo "✅ 完成!"
echo ""
echo "📁 目录结构:"
echo "   skills/               <- 源目录 (存放所有技能)"
echo "   .claude/skills        -> ../skills"
echo "   .gemini/skills        -> ../skills"
echo "   .trae/skills          -> ../skills"
echo "   .codebuddy/skills     -> ../skills"
