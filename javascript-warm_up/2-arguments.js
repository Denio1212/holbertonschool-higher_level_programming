#!/usr/bin/node

/* The message is as large as your imagination */
const Countargs = process.argv.length - 2;
/* The reason its -2 is beacuse it skips the script ending */
if (Countargs == 0) {
	console.log('No argument');
} else if (Countargs == 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found')
}
