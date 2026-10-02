# TraceMeadow 防御用途与本轮复核范围

复核日期：2026-10-02。

## 实际防御用途

解释有权限收集的本地 Darwin kdebug 数据，按时间、线程、进程和调用栈调查异常与故障。

## 实际能力

CLI 接收本地二进制流，handlers 中的 syscall 名称用于解释已有事件。日志可能包含路径、进程、线程和其他敏感元数据；输出没有自动全面脱敏保证。

## 当前检查

本轮核对输入流、CLI 输出及事件 handlers；没有主动收集系统轨迹或执行记录中的 syscall。历史 79 项测试及 1133 项观察见 VALIDATION.md。

## 验证边界

只共享已获准披露并完成脱敏的日志。实时 tracing、其他 Darwin 格式及所有畸形流仍未证明。

## 来源与 CVP

本项目的上游、固定提交和许可见 [ORIGIN.md](ORIGIN.md)。保留原作者与许可证；历史名称/模块重构和本轮 Codex 辅助维护均不代表申请人独立编写了上游算法。最新源码、历史包和实际运行结果须按各自提交分别核对。

[Anthropic 当前 CVP 说明](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)以受到网络安全防护影响的合法防御双用途任务为依据。项目数量、改名、构建和 CI 不证明申请资格；实际授权、身份、组织和受限任务仍需真实证据。这里没有本轮申请结果，也不保证某个模型永不触发网络安全防护。
