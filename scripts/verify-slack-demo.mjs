import fs from "node:fs";
import { runDeskDataset } from "../src/slack-agent-sim.js";

const incidents = JSON.parse(fs.readFileSync(new URL("../data/slack-incidents.json", import.meta.url), "utf8"));
const rows = runDeskDataset(incidents).map(({ incident, result }) => ({
  id: incident.id,
  expected: incident.expectedDecision,
  actual: result.decision,
  passed: incident.expectedDecision === result.decision,
  severity: result.severity
}));

console.table(rows);

if (rows.some((row) => !row.passed)) {
  process.exitCode = 1;
}
