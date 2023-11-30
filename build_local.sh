rm -rf ../blog/*
rm -rf public/
hugo -t hello-friend-ng
cp -r public/* ../blog/
