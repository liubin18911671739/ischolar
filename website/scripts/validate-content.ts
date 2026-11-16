import assert from "node:assert/strict";
import { courses, totalHours, topicHours, moduleHours, topics } from "../src/content/courses";
import { resources } from "../src/content/resources";
import { guides } from "../src/content/guides";
import { platformInformation, siteConfig } from "../src/content/site";

assert.equal(courses.length, 16, "必须恰好有16次课程");
assert.equal(new Set(courses.map((course) => course.id)).size, 16, "课程ID不能重复");
assert.equal(totalHours, 32, "总课时必须为32小时");
assert.deepEqual(Object.keys(topics).map((id) => topicHours(id as keyof typeof topics)), [12, 6, 8, 4, 2], "专题课时须与日历一致");
assert.deepEqual([moduleHours("research"), moduleHours("teaching"), moduleHours("office")], [18, 12, 2]);
const resourceIds = new Set(resources.map((resource) => resource.id));
assert.equal(resourceIds.size, resources.length, "模板ID不能重复");
for (const [index, course] of courses.entries()) {
  assert.equal(course.id, String(index + 1).padStart(2, "0"));
  assert.equal(course.number, index + 1);
  assert.equal(course.hours, 2);
  assert.equal(course.week, Math.floor(index / 2) + 1);
  assert.equal(course.module, index < 9 ? "research" : index < 15 ? "teaching" : "office");
  for (const key of ["goals", "tasks", "outputs", "tools", "review", "resourceIds"] as const) assert.ok(course[key].length > 0, `${course.id}缺少${key}`);
  for (const id of course.resourceIds) assert.ok(resourceIds.has(id), `${course.id}关联了不存在的资源${id}`);
}
for (let week = 1; week <= 8; week++) assert.equal(courses.filter((course) => course.week === week).length, 2);
for (const resource of resources) {
  assert.ok(resource.title && resource.description && resource.body.trim() && resource.tags.length);
  assert.ok(courses.some((course) => course.resourceIds.includes(resource.id)), `资源${resource.id}未关联任何课程`);
  if (resource.format === "csv") {
    const [header, ...rows] = resource.body.trimEnd().split("\n");
    assert.ok(header.split(",").length >= 5);
    for (const row of rows) assert.equal(row.split(",").length, header.split(",").length, `${resource.id} CSV列数不一致`);
  }
}
for (const [topic, guide] of Object.entries(guides)) {
  assert.ok(topic in topics);
  assert.equal(guide.steps.length, 6);
  for (const ref of guide.references) assert.equal(new URL(ref.url).protocol, "https:");
}
for (const info of platformInformation) {
  if (info.status.kind === "confirmed" || info.status.kind === "tested") {
    assert.ok(info.status.evidence.trim() && info.status.date && info.status.responsible.trim());
  }
}
for (const [id, date] of Object.entries(siteConfig.courseDates)) {
  assert.ok(courses.some((course) => course.id === id));
  assert.match(date!, /^\d{4}-\d{2}-\d{2}$/);
  assert.equal(new Date(`${date}T00:00:00Z`).toISOString().slice(0, 10), date, "日期必须真实有效");
}
assert.ok(!siteConfig.contact.email || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(siteConfig.contact.email));
console.log(`内容检查通过：${courses.length}次课，${totalHours}小时，${resources.length}份模板，5个专题。`);
