/**
 * SC-04 · AI Receptionist & Lead Qualification
 *
 * MAIN EXECUTION FILE
 *
 * This is the clearest end-to-end public execution path:
 * inbound enquiry -> structured qualification -> routing -> scheduling hand-off.
 */
type Enquiry = {
  name: string;
  company: string;
  message: string;
  urgency: "low" | "medium" | "high";
  budgetBand: "unknown" | "small" | "medium" | "large";
};

type Qualification = {
  qualified: boolean;
  score: number;
  route: "self-service" | "human-review" | "priority-call";
  missingFields: string[];
};

function extractQualification(enquiry: Enquiry): Qualification {
  let score = 0;
  if (enquiry.company.trim().length > 1) score += 25;
  if (enquiry.message.length > 40) score += 25;
  if (enquiry.urgency === "high") score += 25;
  if (["medium", "large"].includes(enquiry.budgetBand)) score += 25;

  const missingFields: string[] = [];
  if (enquiry.budgetBand === "unknown") missingFields.push("budget");

  return {
    qualified: score >= 50,
    score,
    route: score >= 75 ? "priority-call" : score >= 50 ? "human-review" : "self-service",
    missingFields,
  };
}

function schedulingHandOff(result: Qualification) {
  return result.route === "priority-call"
    ? { provider: "Calendly", action: "offer-priority-event-type" }
    : { provider: "none", action: "do-not-book-yet" };
}

async function main() {
  const enquiry: Enquiry = {
    name: "Alex",
    company: "Example Services",
    message: "We want to automate inbound qualification and appointment routing for our sales team.",
    urgency: "high",
    budgetBand: "medium",
  };

  const qualification = extractQualification(enquiry);
  const scheduling = schedulingHandOff(qualification);
  const output = { enquiry, qualification, scheduling };
  console.log(JSON.stringify(output, null, 2));
  return output;
}

main();
