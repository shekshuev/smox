#!/bin/bash
cd smox-app
npm run build
cd ../smox-auth
npm run build_no_clean
cd ..