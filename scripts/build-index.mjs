#!/usr/bin/env node
// Validate apps/*.json, then write index.json (what the Studio fetches) and the README catalogue.
//   node scripts/build-index.mjs          # exits 1 on any invalid entry
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const categories = JSON.parse(fs.readFileSync(path.join(root, "categories.json"), "utf8"));
const catIds = new Set(categories.map(([id]) => id));
const KINDS = new Set(["open-source", "service", "desktop", "skill", "mcp", "cli"]);
const PRICING = new Set(["free", "freemium", "paid"]);
// The Studio applies these without running any code. Commands are never accepted from a registry.
const INTEGRATIONS = new Set(["link", "keys", "folder", "skills-repo", "mcp"]);

const errors = [];
const apps = [];
const ids = new Set();
for (const file of fs.readdirSync(path.join(root, "apps")).filter((f) => f.endsWith(".json")).sort()) {
  const where = `apps/${file}`;
  let a;
  try {
    a = JSON.parse(fs.readFileSync(path.join(root, "apps", file), "utf8"));
  } catch (e) {
    errors.push(`${where}: invalid JSON (${e.message})`);
    continue;
  }
  const bad = (m) => errors.push(`${where}: ${m}`);
  if (!/^[a-z0-9][a-z0-9-]*$/.test(a.id || "")) bad("id must be lowercase-kebab");
  if (`${a.id}.json` !== file) bad("file name must be <id>.json");
  if (ids.has(a.id)) bad("duplicate id");
  ids.add(a.id);
  for (const k of ["name", "tagline", "description"]) if (typeof a[k] !== "string" || !a[k].trim()) bad(`missing ${k}`);
  if (!catIds.has(a.category)) bad(`unknown category ${a.category}`);
  if (!KINDS.has(a.kind)) bad(`unknown kind ${a.kind}`);
  if (!PRICING.has(a.pricing)) bad(`unknown pricing ${a.pricing}`);
  if (!a.links || !Object.values(a.links).length || Object.values(a.links).some((u) => !/^https:\/\//.test(u))) bad("links must be https URLs");
  const i = a.integration || {};
  if (!INTEGRATIONS.has(i.type)) bad(`integration.type must be one of ${[...INTEGRATIONS].join(", ")}`);
  if (i.type === "skills-repo" && !/^[\w.-]+\/[\w.-]+$/.test(i.repo || "")) bad("skills-repo needs repo: owner/name");
  if (i.type === "keys" && (!Array.isArray(i.keys) || !i.keys.every((k) => /^[A-Z0-9_]+$/.test(k)))) bad("keys must be ENV_NAMES");
  if (i.type === "mcp") {
    const c = i.config || {};
    if (!/^[a-z0-9-]+$/.test(i.name || "")) bad("mcp.name must be lowercase-kebab");
    if (c.url ? !/^https:\/\//.test(c.url) : !["npx", "uvx"].includes(c.command)) bad("mcp.config needs an https url, or command npx/uvx");
  }
  if (a.color && !/^#[0-9A-Fa-f]{6}$/.test(a.color)) bad("color must be #RRGGBB");
  apps.push(a);
}
if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

apps.sort((x, y) => x.name.localeCompare(y.name));
fs.writeFileSync(path.join(root, "index.json"), JSON.stringify({ version: 1, generatedAt: new Date().toISOString(), categories, apps }, null, 1) + "\n");

// README catalogue
const count = (t) => apps.filter((a) => a.integration.type === t).length;
let md = fs.readFileSync(path.join(root, "README.header.md"), "utf8").replace("{{COUNT}}", apps.length);
md += `\n## Catalogue (${apps.length} apps)\n\n${count("mcp")} with an MCP connector · ${count("skills-repo")} skill packs · ${count("keys")} API-key integrations · ${count("folder")} export-folder apps\n`;
for (const [id, label] of categories) {
  const list = apps.filter((a) => a.category === id);
  if (!list.length) continue;
  md += `\n### ${label}\n\n| App | What it does | Type | Price | Studio integration |\n|---|---|---|---|---|\n`;
  for (const a of list) {
    const url = a.links.Website || a.links.GitHub || Object.values(a.links)[0];
    md += `| [${a.name}](${url}) | ${a.tagline} | ${a.kind}${a.license ? ` (${a.license})` : ""} | ${a.pricing} | ${a.integration.type} |\n`;
  }
}
fs.writeFileSync(path.join(root, "README.md"), md);
console.log(`✔ ${apps.length} apps valid → index.json, README.md`);
