#!/bin/bash
cd smox-app
npm install
npm run build
cd ../smox-auth
npm install
npm run build_no_clean
cd ..