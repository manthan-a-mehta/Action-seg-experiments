VERSION=sv_allwt
DS=breakfast #breakfast 50salads gtea
SP=1
ID=1
LOGFILE=logs/eval_${VERSION}_${SP}_${DS}.log

CUDA_VISIBLE_DEVICES=${ID} python3 evaluate.py ./result/${DS}/dataset-${DS}_split-${SP}/config.yaml> "$LOGFILE" 2>&1 &