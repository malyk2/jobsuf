# export REPO_SSH='git@github.com:malyk2/jobsuf.git' 
# export REPO_FOLDER='back' 
# export REPO_BRANCH='develop'
# echo 'REPO_BRANCH'
# echo ${REPO_BRANCH}

git init \
    && git remote add -f origin ${REPO_SSH} \
    && git config core.sparseCheckout true \
    && echo ${REPO_FOLDER} >> .git/info/sparse-checkout \
    && git pull origin ${REPO_BRANCH} \
    && mv ${REPO_FOLDER}/* . && mv ${REPO_FOLDER}/.[!.]* . 
