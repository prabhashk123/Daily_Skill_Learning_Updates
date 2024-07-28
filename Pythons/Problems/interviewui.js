const a=[{id:1, name: "p"}, {id:2, name: "s"},{id:3, name: "s"}]
// find() method print one first object in in jaavascripts.

const p=a.find(a =>a.name=="s");
console.log(p)

// find all object in javascript use filter.
const ans = a.filter(obj => obj.name == "s");
console.log(ans)