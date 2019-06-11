#!/bin/bash
echo "Current version is $(cat VERSION.txt).  What version did you want to release?"
read VERSION
echo $VERSION > VERSION.txt
python setup.py sdist
twine upload "dist/django_single_instance_model-$VERSION.tar.gz"
git add .
git commit -m "v$VERSION"
git tag -a "v$VERSION" -m "v$VERSION"
