/**

Staqlt Dual-Entry Comparator

Runs on submission to check for 'Blind Match' */

function compareEntries(entryA, entryB) { const fieldsToCompare = ['tonnes', 'grade', 'contained_metal', 'category', 'metal_type'];

let match = true; let differences = [];

fieldsToCompare.forEach(field => { if (entryA[field] !== entryB[field]) { match = false; differences.push(field); } });

return { isMatch: match, flaggedFields: differences, status: match ? 'Human Matched' : 'Conflict Flagged' }; }

module.exports = { compareEntries };