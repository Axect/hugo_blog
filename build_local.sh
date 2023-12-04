rm -rf ../axect.github.io/*
rm -rf public/
hugo -t hello-friend-ng
cp -r public/* ../axect.github.io/
