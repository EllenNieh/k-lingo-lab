"""Validate lessons.js without external packages using installed Node.js.
Run: python scripts/validate_lessons.py
"""
from pathlib import Path
import subprocess, sys
root=Path(__file__).resolve().parents[1]
script=r'''
import { categories, lessons } from './data/lessons.js';
let errors=[]; const ids=new Set(), cats=new Set(categories.map(c=>c.id));
for(const [i,l] of lessons.entries()){
const p=`lesson[${i}] (${l.id||'no id'})`;
if(typeof l.id!=='string'||!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(l.id))errors.push(`${p}: invalid id`);
if(ids.has(l.id))errors.push(`${p}: duplicate id`);ids.add(l.id);
if(!cats.has(l.category))errors.push(`${p}: unknown category`);
if(!['入門','初級','中級'].includes(l.level))errors.push(`${p}: invalid level`);
if(!Number.isInteger(l.minutes)||l.minutes<=0)errors.push(`${p}: invalid minutes`);
for(const k of ['emoji','title','subtitle','description'])if(typeof l[k]!=='string'||!l[k].trim())errors.push(`${p}: missing ${k}`);
if(!Array.isArray(l.objectives)||l.objectives.length<2||l.objectives.some(s=>typeof s!=='string'||!s.trim()))errors.push(`${p}: objectives invalid`);
if(!Array.isArray(l.sections)||l.sections.length<2||l.sections.some(s=>!s.heading?.trim()||!s.body?.trim()))errors.push(`${p}: sections invalid`);
if(!Array.isArray(l.examples)||l.examples.length<3||l.examples.some(e=>!e.ko?.trim()||!e.zh?.trim()||!e.roman?.trim()))errors.push(`${p}: examples invalid`);
if(!Array.isArray(l.quiz)||l.quiz.length<2||l.quiz.some(q=>!q.question?.trim()||!Array.isArray(q.options)||q.options.length!==4||q.options.some(o=>typeof o!=='string'||!o.trim())||!Number.isInteger(q.answer)||q.answer<0||q.answer>3||!q.explanation?.trim()))errors.push(`${p}: quiz invalid`);
}
if(errors.length){console.error(errors.join('\n'));process.exit(1)}
console.log(`PASS: ${lessons.length} lessons, ${categories.length} categories validated.`);
'''
result=subprocess.run(['node','--input-type=module','-e',script],cwd=root,check=False)
sys.exit(result.returncode)
