/**
 * SC-07 · Full-Stack LLM Business Copilot
 *
 * MAIN EXECUTION FILE
 *
 * Demonstrates the full public path:
 * user question -> context -> tool selection -> validated tool call -> response.
 */
type ToolCall = { name: "pipeline_summary" | "create_follow_up"; args: Record<string, unknown> };

function retrieveContext(question: string) {
  return {
    question,
    pipelineRevenue: 418000,
    conversionRate: 0.27,
    previousConversionRate: 0.31,
    openDeals: 42,
  };
}

function chooseTool(question: string): ToolCall {
  if (question.toLowerCase().includes("follow")) {
    return { name: "create_follow_up", args: { owner: "sales", priority: "high" } };
  }
  return { name: "pipeline_summary", args: {} };
}

function runTool(call: ToolCall, context: ReturnType<typeof retrieveContext>) {
  if (call.name === "pipeline_summary") {
    return {
      revenue: context.pipelineRevenue,
      conversionRate: context.conversionRate,
      change: context.conversionRate - context.previousConversionRate,
      openDeals: context.openDeals,
    };
  }
  return { created: true, taskId: "TASK-1007", ...call.args };
}

async function main() {
  const question = "Why did pipeline conversion fall and what should I review?";
  const context = retrieveContext(question);
  const toolCall = chooseTool(question);
  const toolResult = runTool(toolCall, context);
  const response = { question, context, toolCall, toolResult };
  console.log(JSON.stringify(response, null, 2));
  return response;
}

main();
