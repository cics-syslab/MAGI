/*** convert.js
 * simple script to convert the test files in the autograder
 * into a test_list.toml for easier modification. usage:
 * 
 * node convert.js path/to/*test.ts
 */
const fs = require("fs")
const file = fs.readFileSync(process.argv[2]).toString()

let toml = ""
const matches = file.matchAll(/describe\("(.*)?"[\s\S]*?(?=describe|\z)/g)
for (const match of matches) {
  const tests = [...match[0].matchAll(/it\("(.*?)"/g)]
  for (const test of tests) {
    const public = test[0].match(/\[PUBLIC\]/)
    const visibility = public ? "public" : "after_published"
    const name = public ? `name = "${test[1].replace(/\s*\[PUBLIC\]$/, "")}"\n` : ""
    toml += `[${match[1]}."${test[1]}"]\n${name}max_score = 1\nvisibility = "${visibility}"\n`
  }
  toml += "\n"
}

fs.writeFileSync("test_list.toml", toml)
