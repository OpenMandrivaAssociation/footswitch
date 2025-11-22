name=$(cat *.spec | grep -i Name: | awk '{print $NF}')
date=$(date +%Y%m%d)
#repo_url=$(cat *.spec | grep -i URL: | awk '{print $NF}')
git clone --depth 1 https://github.com/rgerganov/footswitch $name
cd $name
git archive --format=tar --prefix $name-$(date +%Y%m%d)/ HEAD | zstd --ultra -22 > ../$name-$date.tar.zst
sed -i -E "s:%define sourcedate [0-9]+:%define sourcedate $date:g" ../$name.spec
echo "sourcedate define value: $(date +%Y%m%d)"
cd -
