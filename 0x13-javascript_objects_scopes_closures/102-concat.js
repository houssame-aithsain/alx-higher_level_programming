#!/usr/bin/node
// Write a script that concats 2 files.

const fs = require('fs');

const concatFiles = (sourceFile1, sourceFile2, destinationFile) => {
  try {
    const content1 = fs.readFileSync(sourceFile1, 'utf8');
    const content2 = fs.readFileSync(sourceFile2, 'utf8');
    const concatenatedContent = content1 + '\n' + content2;
    fs.writeFileSync(destinationFile, concatenatedContent);
    console.log('Files concatenated successfully!');
  } catch (error) {
    console.error('An error occurred:', error);
  }
};

const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);
concatFiles(sourceFile1, sourceFile2, destinationFile);
