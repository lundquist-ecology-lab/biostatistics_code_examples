import { oneWay } from 'ml-anova';

// The data for the ANOVA test.
const data = [6, 8, 4, 5, 3, 4, 8, 12, 9, 11, 6, 8, 13, 9, 11, 8, 7, 12];
const classes = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2];

const result = oneWay(data, classes, { alpha: 0.05 });

console.log(result);