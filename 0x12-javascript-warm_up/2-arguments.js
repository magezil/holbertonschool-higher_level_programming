#!/usr/bin/node
//console.log(process.argv.length);
//process.argv.forEach((val, index) => {
//	  console.log(`${index}: ${val}`);
//});
if (process.argv.length == 2) {
	console.log('No argument');
} else if (process.argv.length == 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
