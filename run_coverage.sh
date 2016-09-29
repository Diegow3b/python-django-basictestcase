#!/bin/bash
coverage run --source="." manage.py test
if [ $? -eq 0 ]; then
    coverage html
    coverage report
else
    echo FAIL
fi
