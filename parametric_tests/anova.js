// Load the anova-pairs library.
const anova = require("anova-pairs");

// The data for the ANOVA test.
const data = [
  // Group 1.
  [1, 2, 3],
  // Group 2.
  [2, 3, 4],
  // Group 3.
  [3, 4, 5],
];

// Perform the ANOVA test and calculate the F-value and p-value.
const result = anova.oneway(data);
const fValue = result.fValue;
const pValue = result.pValue;

// Print the F-value and p-value.
console.log(`F-value: ${fValue}`);
console.log(`p-value: ${pValue}`);