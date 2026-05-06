#!/bin/bash
# 深度学习简明指南 - 批量渲染并合并脚本
# 用法: ./render_all.sh [quality]
#   quality: l (低质量/快速), m (中等), h (高质量), k (4K)
#   默认: l (低质量预览)

QUALITY="${1:-l}"
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# 输出目录
OUTPUT_DIR="media/videos/combined"
mkdir -p "$OUTPUT_DIR"

# 场景列表
declare -a SCENES=(
    "scene_01_intro.py:IntroScene"
    "scene_02_learning_paradigms.py:LearningParadigmsScene"
    "scene_03_gpu_tensor.py:GPUTensorScene"
    "scene_04_forward_backward.py:ForwardBackwardScene"
    "scene_05_loss_optimization.py:LossOptimizationScene"
    "scene_06_depth_value.py:DepthValueScene"
    "scene_07_building_blocks.py:BuildingBlocksScene"
    "scene_08_architectures.py:ArchitecturesScene"
    "scene_09_perception.py:PerceptionScene"
    "scene_10_generation.py:GenerationScene"
    "scene_11_large_models.py:LargeModelsScene"
    "scene_12_future.py:FutureScene"
)

echo "=================================="
echo "深度学习简明指南 - 批量渲染"
echo "质量: -q${QUALITY}"
echo "=================================="

# 创建文件列表
FILE_LIST="$OUTPUT_DIR/file_list.txt"
> "$FILE_LIST"

# 渲染每个场景
for i in "${!SCENES[@]}"; do
    IFS=':' read -r file class <<< "${SCENES[$i]}"
    num=$(printf "%02d" $((i + 1)))
    
    echo ""
    echo "[$num/12] 渲染 $class ..."
    
    # 渲染场景
    manim -q${QUALITY} --disable_caching "$file" "$class"
    
    if [ $? -eq 0 ]; then
        # 查找生成的视频文件
        case $QUALITY in
            l) res_dir="480p15" ;;
            m) res_dir="720p30" ;;
            h) res_dir="1080p60" ;;
            k) res_dir="2160p60" ;;
            *) res_dir="480p15" ;;
        esac
        
        video_file=$(find "media/videos/${file%.py}/$res_dir" -name "*.mp4" -type f 2>/dev/null | head -1)
        
        if [ -n "$video_file" ]; then
            echo "  ✓ 完成: $video_file"
            echo "file '$DIR/$video_file'" >> "$FILE_LIST"
        else
            echo "  ✗ 未找到输出文件"
        fi
    else
        echo "  ✗ 渲染失败"
    fi
done

echo ""
echo "=================================="
echo "合并视频..."
echo "=================================="

# 检查 ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "错误: 未安装 ffmpeg"
    echo "请运行: brew install ffmpeg"
    exit 1
fi

# 合并视频
OUTPUT_FILE="$OUTPUT_DIR/deep_learning_intro_complete.mp4"

if [ -s "$FILE_LIST" ]; then
    ffmpeg -y -f concat -safe 0 -i "$FILE_LIST" -c copy "$OUTPUT_FILE"
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "=================================="
        echo "✓ 完成！"
        echo "输出文件: $OUTPUT_FILE"
        echo "=================================="
        
        # 显示文件信息
        ls -lh "$OUTPUT_FILE"
    else
        echo "合并失败"
        exit 1
    fi
else
    echo "错误: 没有成功渲染的视频"
    exit 1
fi
