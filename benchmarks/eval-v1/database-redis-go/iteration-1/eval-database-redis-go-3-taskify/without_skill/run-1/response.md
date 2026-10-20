The user wants me to convert the tutorial at https://www.build-redis-from-scratch.dev/ into a Claude Code executable learning task list. Let me first fetch the tutorial content to understand what it covers.

Let me fetch the website first.页面返回为空。让我尝试其他方法来获取教程内容。The homepage redirects to `/en/introduction`. This looks like a Nextra documentation site. Let me fetch that page.The hgetall implementation seems to be missing from the extracted text (probably it was in a code block that got truncated in my extraction). Let me check the raw HTML for hgetall.The hgetall function code seems to be missing from the article (it's referenced in the Handlers map but the implementation isn't shown in the extracted blocks — it may have been skipped in the article itself, or it's in the GitHub repo). The tutorial's GitHub repo is github.com/ahmedash95/redis-clone (mentioned "You can find all the code for our project on Github"). The hgetall implementation is known from the repo:

```go
func hgetall(args []Value) Value {
	if len(args) != 1 {
		return Value{typ: "error", str: "ERR wrong number of arguments for 'hgetall' command"}
	}

	hash := args[0].bulk

	HSETsMu.RLock()
	hashMap := HSETs[hash]
	HSETsMu.RUnlock()

	array := []Value{}
	for key, value := range hashMap {
		array = append(array, Value{typ: "bulk", bulk: key})
		array = append(array, Value{typ: "bulk", bulk: value})
	}

	return Value{typ: "array", array: array}
}
```

Now let me read the AOF chapter.I now have all the tutorial content. Let me also check the resp-writer's Writer code (NewWriter) which I saw partially. Let me extract the writer code blocks.I have the full tutorial content. Let me verify the final code against the author's GitHub repo (the AOF `Read` loop in the article looks like it lost a line in extraction).我已经有了参考仓库。让我获取它的 `aof.go` 以确认正确的 `Read` 循环（文章中的版本看起来有格式错误的代码块）。我已经获取了完整的教程（共 8 页）以及作者的参考实现（`ahmedash95/build-redis-from-scratch`）。在编写任务列表之前，我先记录一下探索结果并制定计划。已生成 `TASKS.md`，把教程全部 8 个章节转成了 8 个顺序执行的 Claude Code 任务（Task 0–7），每个任务包含：可直接粘贴的 Prompt、可执行的验收命令、学习点。

结构：

| Task | 内容 | 对应章节 |
|------|------|----------|
| 0 | Go module 初始化 + redis-cli 环境验证 | introduction / first-steps |
| 1 | TCP 服务器骨架（:6379，回 `+OK\r\n`） | writing-server |
| 2 | RESP 读取器（Value struct、递归解析 array/bulk） | resp-reader |
| 3 | RESP 写入器（Marshal 五种类型 + Writer） | resp-writer |
| 4 | 6 个命令：PING/SET/GET/HSET/HGET/HGETALL | implementing-commands |
| 5 | AOF 持久化（everysec 刷盘 + 启动重放） | aof |
| 6 | 多连接并发（goroutine per connection，教程承诺但正文缺失，已补） | 教程补充 |
| 7 | 扩展练习（DEL/KEYS、HSET 返回整数、优雅关闭、AOF 重写、Pub/Sub） | next |

转换时修正了教程的三处问题（已在任务中标注）：

1. **AOF `Read` 代码块有误**：教程页面缺少 `Seek(0, 0)` 且 EOF 分支写法错误，重放会漏读数据。已按作者参考仓库 `ahmedash95/build-redis-from-scratch` 的正确版本描述。
2. **hgetall 实现缺失**：教程正文只注册了函数名没给代码，已从参考仓库恢复（扁平化为 `[k1,v1,k2,v2...]` bulk 数组）。
3. **单连接 vs 并发矛盾**：Introduction 承诺 goroutine 并发但正文只 Accept 一次，Task 6 补齐，这也是理解 `sync.RWMutex` 的关键。

末尾附总验收清单（编译、全部命令行为、持久化重启、并发互阻），全部通过即教程完成。