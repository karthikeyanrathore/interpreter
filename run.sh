#!/bin/bash
cd build
printf "testing AST \n"
./test_ast.py 
printf "testing Syntax-directed interpreters \n"
./test_sdi.py
cd ../
